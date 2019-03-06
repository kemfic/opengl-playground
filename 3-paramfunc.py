"""
Function Plotting
"""


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np


dom = np.pi #domain

def init():
  
  glClearColor(0.2, 0.2, 0.2, 1.0) # (r, g, b, a) tells OpenGL what color we use to clear
  gluOrtho2D(-dom, dom, -dom, dom) # sets coord system ranges (x_min, x_max, y_min, y_max)
  # center is 0,0 

def plotfunc():
  # clears color buffer bit
  glClear(GL_COLOR_BUFFER_BIT)

  glColor3f(1.0, 1.0, 1.0)
  glLineWidth(1.0)
  glBegin(GL_LINES)
  glVertex2f(-dom, 0.0)
  glVertex2f(dom, 0.0)
  glVertex2f(0.0, dom)
  glVertex2f(0.0, -dom)
  glEnd()
  # sets next color
  glColor3f(1.0, 0.0, 1.0)
  
  # draws points
  glPointSize(3.0)
  glBegin(GL_POINTS)

  for x in np.arange(-dom, dom, dom/50.0):
    y=np.pi*np.tanh(x)
    glVertex2f(x,y)
  

  glEnd()
  glFlush()

if __name__ == "__main__":
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(500, 500)
  #glutInitWindowPosition(1080,100)
  glutCreateWindow("Plot Function")
  glutDisplayFunc(plotfunc)
  init()
  glutMainLoop()
