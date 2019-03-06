"""
Chaos Game
---
1. Start with an equilateral triangle with vertices A,B,C
2. Pick a random (non-vertex) point P_1 that lies within the triangle. Plot it.
3. Roll an imaginary 3 sided die labelled with the triangle vertices
4. Your next point, P_2, will be the midpoint between P_1 and the vertex chosen by the die. Plot P_2
5. Repeat Step 4 forever. (P_n is the midpoint between a vertex and P_(n-1) ). Plot it.
"""


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np
import random

width = 400
height = 500

dom = np.pi


A = [dom/2, np.sqrt(3)*dom/2]
B = (-dom/2, dom/2)

def plotTriangle():
  """ Plots triangle ABC """
  glColor3f(1.0,1.0,1.0)

  glLineWidth(10.0)
  glBegin(GL_LINES)
  
  glVertex2f(0, np.sqrt(3)*dom/2)
  glVertex2f(-dom, -dom)
  glVertex2f(-dom, -dom)
  glVertex2f(dom, -dom)
  glVertex2f(dom, -dom)
  glVertex2f(0, np.sqrt(3)*dom/2)
  glEnd()

def plotfunc():
  # clears color buffer bit
  glClear(GL_COLOR_BUFFER_BIT)
  # sets next color
  glColor3f(1.0, 0.0, 1.0)
  
  plotTriangle() 

  glFlush()

def init():
  
  glClearColor(0.2, 0.2, 0.2, 1.0) # (r, g, b, a) tells OpenGL what color we use to clear
  gluOrtho2D(-dom, dom, -dom, dom) # sets coord system ranges (x_min, x_max, y_min, y_max)
  # center is 0,0 

def reshape(w, h):
  """ preserves aspect ratio of window """
  
  if h==0:
    h==1
  if w==0:
    w==1
  # fill entire window
  glViewport(0,0,w,h)
  
  # set projection matrix
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()

  # set aspect ratio of plot
  if w <= h:
    gluOrtho2D(-dom, dom, -dom*h/w, dom*h/w)
  else:
    gluOrtho2D(-dom*w/h, dom*w/h, -dom, dom)

  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()

def keyboard(key, x, y):
  # quit by pressing 'esc' or 'q'
  if key == b'q' or key == b'\x1b':
    sys.exit()

if __name__ == "__main__":
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(500, 500)
  #glutInitWindowPosition(1080,100)
  glutCreateWindow("Plot Polar Equation")
  glutReshapeFunc(reshape)
  glutDisplayFunc(plotfunc)
  glutKeyboardFunc(keyboard)
  init()
  glutMainLoop()
