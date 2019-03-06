"""
First PyOpenGL Program
0-teapot.py
"""


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys



def draw():
  glClear(GL_COLOR_BUFFER_BIT) # clears GL color buffers
  glutWireTeapot(0.5)
  glFlush() # forces execution of GL commands in finite time

if __name__ == "__main__":
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(250, 250)
  glutInitWindowPosition(100,100)
  glutCreateWindow("Hello World")
  glutDisplayFunc(draw)
  glutMainLoop()
