from glumpy import app, gloo, gl, glm
import numpy as np

from vertex import vertex
from fragment import fragment

window = app.Window(width=1024, height=1024,
                    color=(0.10, 0.10, 0.10, 1.00))

vertices = np.zeros(8, [("a_position", np.float32, 3),
                        ("a_color", np.float32, 4)])

vertices["a_position"]  = [[ 1, 1, 1], [-1, 1, 1], [-1,-1, 1], [ 1,-1, 1],
                   [ 1,-1,-1], [ 1, 1,-1], [-1, 1,-1], [-1,-1,-1]]
vertices["a_color"] = [[0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 1, 0, 1],
                   [1, 1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 1]]
indices = np.array([0,1,2, 0,2,3,  0,3,4, 0,4,5,  0,5,6, 0,6,1,
              1,6,7, 1,7,2,  7,4,3, 7,3,2,  4,7,6, 4,6,5], dtype=np.uint32)
outlines = np.array([0,1, 1,2, 2,3, 3,0, 4,7, 7,6,
              6,5, 5,4, 0,5, 1,6, 2,7, 3,4], dtype=np.uint32)

# send to GPU
vertices = vertices.view(gloo.VertexBuffer)
indices = indices.view(gloo.IndexBuffer)
outlines = outlines.view(gloo.IndexBuffer)

cube = gloo.Program(vertex, fragment)
cube.bind(vertices)
cube["a_position"] = vertices

view = np.eye(4,dtype=np.float32)
model = np.eye(4,dtype=np.float32)
projection = np.eye(4,dtype=np.float32)
glm.translate(view, 0,0,-5)

cube['u_model'] = model
cube['u_view'] = view
cube['u_projection'] = projection
cube['scale'] = 1.0
phi, theta, time = 0,0, 0
@window.event
def on_draw(dt):  
  global phi, theta, time
  
  window.clear()
  time += dt
  # fill cube
  gl.glLineWidth(2)
  cube['u_color'] = 1, 1, 1, 1
  cube.draw(gl.GL_TRIANGLES, indices)
  cube['u_color'] = 0, 0, 0, 1
  cube.draw(gl.GL_LINES, outlines)
  # rotation animation
  theta += 0.25 # deg
  phi += 0.25 # deg
  
  model = np.eye(4, dtype=np.float32)
  glm.rotate(model, theta, 0, 0, 1)
  glm.rotate(model, phi, 0, 1, 0)
  cube["u_model"] = model

@window.event
def on_resize(w, h):
  ratio = w /float(h)
  cube["u_projection"] = glm.perspective(45.0, ratio, 2.0, 100.0)

@window.event
def on_init():
  gl.glEnable(gl.GL_DEPTH_TEST)



# run the app
app.run()
