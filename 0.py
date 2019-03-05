# First Python OpenGL Program
# 0.py

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def draw():
  glutWireTeapot(0.5)
  glFlush()

if __name__ == "__main__":
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutCreateWindow("Hello World")
  glutDisplayFunc(draw)
  glutMainLoop()