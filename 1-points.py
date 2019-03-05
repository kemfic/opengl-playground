"""
First PyOpenGL Program
0-teapot.py
"""


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys



def init():
  
  glClearColor(0.0, 0.0, 0.0, 1.0) # (r, g, b, a) tells OpenGL what color we use to clear
  gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # sets coord system ranges (x_min, x_max, y_min, y_max)
  # center is 0,0 

def plotpoints():
  # clears color buffer bit
  glClear(GL_COLOR_BUFFER_BIT)
  # sets next color
  glColor3f(1.0, 0.0, 0.0)
  
  # draws points
  glPointSize(10.0)
  glBegin(GL_POINTS)
  glVertex2f(0.0, 0.0)
  glVertex2f(0.5, 0.5)
  glVertex2f(-0.5, 0.5)
  glVertex2f(0.5, -0.5)
  glVertex2f(-0.5, -0.5)

  glEnd()
  glFlush()

if __name__ == "__main__":
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(500, 500)
  glutInitWindowPosition(1080,100)
  glutCreateWindow("Plot Points")
  glutDisplayFunc(plotpoints)
  init()
  glutMainLoop()
