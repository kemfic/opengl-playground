import sys
import OpenGl.GL as gl
import OpenGL.GLUT as glut

def display():
  glut.glutSwapBuffers()

def reshape(w, h):
  gl.glViewPort(0,0,w,h)

def keyboard(key, x, y):
  if key == b'\x1b' or key == b'q':
    sys.exit()

if __name__ == "__main__":
  glut.glutInit()
  glut.glutInitDisplayMode(glut.GLUT_DOUBLE | GLUT_RGB)
  glut.glutCreateWindow("Hello World!")
  glut.glutReshapeWindow(500, 500)
  glut.glutReshapeFunc(reshape)
  glut.glutDisplayFunc(display)
  glut.glutKeyboardFund(keyboard)
  glut.glutMainLoop()