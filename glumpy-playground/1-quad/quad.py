from glumpy import app, gloo, gl
import numpy as np

from vertex import vertex
from fragment import fragment

# build program with corresponding buffers
quad = gloo.Program(vertex, fragment, count=4)

# load data to GPU
quad['color'] = [ (1,0,0,1), (0,1,0,1), (0,0,1,1), (1,1,0,1) ]
quad['position'] = [ (-1,-1),   (-1,+1),   (+1,-1),   (+1,+1)   ]
quad['scale'] = 1.0

# create window
window = app.Window()

@window.event
def on_draw(dt):
  window.clear()
  quad.draw(gl.GL_TRIANGLE_STRIP)

# run the app
app.run()
