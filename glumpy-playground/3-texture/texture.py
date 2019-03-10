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

vertices = vertices.view(gloo.VertexBuffer)
indices = indices.view(gloo.IndexBuffer)

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

phi, theta = 0,0
test = 0
@window.event
def on_draw(dt):  
  global phi, theta, test
  n = app.clock.tick()
  window.clear()
  cube.draw(gl.GL_TRIANGLES, indices)
  
  # rotation animation
  theta += 100*dt # deg
  phi += 100*dt # deg
  
  model = np.eye(4, dtype=np.float32)
  print(app.clock.get_fps())  
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
