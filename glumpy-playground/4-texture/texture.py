from glumpy import app, gloo, gl, glm
import numpy as np

from vertex import vertex
from fragment import fragment

def block():
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
  t_coords = np.array([ [0,0],
                        [0,1],
                        [1,1],
                        [1,0] ])
  
  #indices corresponding to faces
  f_pos_idx = [0, 1, 2, 3,  0, 3, 4, 5,   0, 5, 6, 1,
             1, 6, 7, 2,  7, 4, 3, 2,   4, 7, 6, 5]
  
  f_coord_idx = [0, 1, 2, 3,  0, 3, 4, 5,   0, 5, 6, 1,
             1, 6, 7, 2,  7, 4, 3, 2,   4, 7, 6, 5]
  
  f_norm_idx = [0, 0, 0, 0,  1, 1, 1, 1,   2, 2, 2, 2,
             3, 3, 3, 3,  4, 4, 4, 4,   5, 5, 5, 5]
  
  f_t_color_idx = [0, 1, 2, 3,  0, 1, 2, 3,   0, 1, 2, 3,
             3, 2, 1, 0,  0, 1, 2, 3,   0, 1, 2, 3]

  vertices = np.zeros(24, vertex_type)

  vertices["a_position"] = v_pos[f_pos_idx]
  vertices["a_texcoord"] = v_pos[f_pos_idx]
  vertices["a_normal"] = v_pos[f_pos_idx]
  vertices["a_color"] = v_pos[f_pos_idx]
  
  filled = np.resize(np.array[0,1,2,0,2,3], dype=int_type), 6*2*3)
  filled += np.repeat(4*np.arange(6, dtype=int_type), 6)

  outline = np.resize(np.array([0, 1, 1, 2, 2, 3, 3, 0], dtype=int_type), 6 * (2 * 4))
  outline += np.repeat(4 * np.arange(6, dtype=int_type), 8)
  
  vertices = vertices.view(gloo.VertexBuffer)
  filled =filled.view(gloo.IndexBuffer)
  outline = outline.view(gloo.IndexBuffer)

  return vertices, filled, outline

window = app.Window(width=1024, height=1024,
                    color=(0.10, 0.10, 0.10, 1.00))

# run the app
app.run()
