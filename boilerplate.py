"""
Boilerplate Skeleton Code for 2D Plotting
"""


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np

width = 400
height = 500

dom = np.pi
interval = 1000.0

t_min = -np.pi
t_max = np.pi

def fx(x):
  return x

def drawaxes():
  """ draws axis lines """
  glColor3f(1.0,1.0,1.0)
  glLineWidth(1.0)

  glBegin(GL_LINES)

  glVertex2f(-dom, 0.0)
  glVertex2f(dom, 0.0)
  glVertex2f(0.0, dom)
  glVertex2f(0.0, -dom)
  glEnd()

def plotfunc():
  # clears color buffer bit
  glClear(GL_COLOR_BUFFER_BIT)
  drawaxes()
  # sets next color
  glColor3f(1.0, 0.0, 1.0)
  
  # draws points
  glPointSize(3.0)
  glBegin(GL_POINTS)

  for x in np.arange(x_min, x_max, 1.0/interval):
    y=fx(x)
    glVertex2f(x,y)
  

  glEnd()
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
  glutCreateWindow("Plot 2D function")
  glutReshapeFunc(reshape)
  glutDisplayFunc(plotfunc)
  glutKeyboardFunc(keyboard)
  init()
  glutMainLoop()
