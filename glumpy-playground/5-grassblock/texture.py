from glumpy import app, gloo, gl, glm, data
import numpy as np
import cv2

from vertex import vertex
from fragment import fragment

def cube():
  vertex_type = [ ("a_position", np.float32, 3),
                  ("a_texcoord", np.float32, 2),
                  ("a_normal", np.float32, 3),
                  ("a_color", np.float32, 4)]
  int_type = np.uint32
 

  # vertex positions
  v_pos = np.array([[1, 1, 1],
                    [-1, 1, 1],
                    [-1, -1, 1], 
                    [1, -1, 1],
                    [1, -1, -1], 
                    [1, 1, -1],
                    [-1, 1, -1],
                    [-1, -1, -1]], dtype=float)

  # face normal vectors
  f_norm = np.array([[0, 0, 1], 
                    [1, 0, 0], 
                    [0, 1, 0],
                    [-1, 0, 1],
                    [0, -1, 0],
                    [0, 0, -1]])

  v_color = np.array([[0, 1, 1, 1],
                      [0, 0, 1, 1], 
                      [0, 0, 0, 1],
                      [0, 1, 0, 1],
                      [1, 1, 0, 1], 
                      [1, 1, 1, 1], 
                      [1, 0, 1, 1], 
                      [1, 0, 0, 1]])

  # texture coords
  t_coords = np.array([ [0.5,0.5],
                        [0.5,1.0],
                        [1.0,1.0],
                        [1.0,0.5] ])
  
  #indices corresponding to faces
  f_pos_idx = [0, 1, 2, 3,  0, 3, 4, 5,   0, 5, 6, 1,
             1, 6, 7, 2,  7, 4, 3, 2,   4, 7, 6, 5]
  
  f_norm_idx = [0, 0, 0, 0,  1, 1, 1, 1,   2, 2, 2, 2,
             3, 3, 3, 3,  4, 4, 4, 4,   5, 5, 5, 5]
  f_color_idx = [0, 1, 2, 3,  0, 3, 4, 5,   0, 5, 6, 1,
               1, 6, 7, 2,  7, 4, 3, 2,   4, 7, 6, 5]


  f_t_idx = [0, 1, 2, 3,  0, 1, 2, 3,   0, 1, 2, 3,
             3, 2, 1, 0,  0, 1, 2, 3,   0, 1, 2, 3]

  vertices = np.zeros(24, vertex_type)

  vertices["a_position"] = v_pos[f_pos_idx]
  vertices["a_texcoord"] = t_coords[f_t_idx]
  vertices["a_color"] = v_color[f_color_idx]
  vertices["a_normal"] = f_norm[f_norm_idx]
  
  filled = np.resize(np.array([0,1,2,0,2,3], dtype=int_type), 6*2*3)
  filled += np.repeat(4*np.arange(6, dtype=int_type), 6)

  outline = np.resize(np.array([0, 1, 1, 2, 2, 3, 3, 0], dtype=int_type), 6 * (2 * 4))
  outline += np.repeat(4 * np.arange(6, dtype=int_type), 8)
  
  vertices = vertices.view(gloo.VertexBuffer)
  filled =filled.view(gloo.IndexBuffer)
  outline = outline.view(gloo.IndexBuffer)

  return vertices, filled, outline

window = app.Window(width=500, height=500,
                    color=(0.50, 0.50, 0.50, 1.00))
@window.event
def on_draw(dt):
  global phi, theta, duration

  window.clear()

  gl.glDisable(gl.GL_BLEND)
  gl.glEnable(gl.GL_DEPTH_TEST)
  gl.glEnable(gl.GL_POLYGON_OFFSET_FILL)
  cube["u_color"] = 1,1,1,1
  cube.draw(gl.GL_TRIANGLES, indices)
  
  # Outlined cube
  gl.glDisable(gl.GL_POLYGON_OFFSET_FILL)
  gl.glEnable(gl.GL_BLEND)
  gl.glDepthMask(gl.GL_FALSE)
  cube['u_color'] = 0, 0, 0, 1
  cube.draw(gl.GL_LINES, outline)
  gl.glDepthMask(gl.GL_TRUE)
  
  #rotate cube
  theta += 0.5 # deg
  phi += 0.5 # deg
  model = np.eye(4, dtype=np.float32)
  glm.rotate(model, theta, 0,0,1)
  glm.rotate(model, phi, 0,1,0)
  cube['u_model'] = model

@window.event
def on_resize(width, height):
  cube['u_projection'] = glm.perspective(45.0, width / float(height), 2.0, 100.0)

@window.event
def on_init():
  gl.glEnable(gl.GL_DEPTH_TEST)
  gl.glPolygonOffset(1,1)
  gl.glEnable(gl.GL_LINE_SMOOTH)

vertices, indices,outline = cube()
cube = gloo.Program(vertex, fragment)
cube.bind(vertices)
cube['u_texture'] = np.array(cv2.imread('data.png'))/255.0
cube['u_model'] = np.eye(4, dtype=np.float32)
cube['u_view'] = glm.translation(0, 0, -5)
phi, theta = 40, 30

app.run()
