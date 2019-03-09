from glumpy import app, gloo, gl
import numpy as np

from vertex import vertex
from fragment import fragment

time = 0
# build program with corresponding buffers
quad = gloo.Program(vertex, fragment, count=4)

# load data to GPU
quad['color'] = [ (1,0,0,1), (0,1,0,1), (0,0,1,1), (1,1,0,1) ]
quad['position'] = [ (-1,-1),   (-1,+1),   (+1,-1),   (+1,+1)   ]
quad['scale'] = 0.75
quad['theta'] = 0.75
# create window
window = app.Window()


@window.event
def on_draw(dt):
  global time
  time += dt
  quad['theta'] += dt 
  quad['scale'] = np.abs(np.sin(time))


  window.clear()
  quad.draw(gl.GL_TRIANGLE_STRIP)

@window.event
def on_resize(w, h):
  if w > h:
    x = (w - h)/2
    y = 0
    w = h
  else:
    x = 0
    y = (h-w)/2
    h = w
  gl.glViewport(int(x), int(y), int(w), int(h))
  window.dispatch_event('on_draw', 0.0)
  window.swap()
  return True

# run the app
app.run()
