"""
Rotation:
  R(t) = [ [cos(t), -sin(t)],
           [sin(t), cos(t)] ]
  v = [ x,
        y ]

  v' = R(t) * v

  so basically, to rotate the quad, the new positions are as follows:
  x' = x*cos(t) - y*sin(t)
  y' = x*sin(t) + y*sin(t)

"""



vertex = """
  uniform float theta;
	uniform float scale;
	attribute vec2 position;
	attribute vec4 color;
	varying vec4 v_color;
	void main()
	{
  float c_t = cos(theta);
  float s_t = sin(theta);


  float x = position.x*c_t - p.y*s_t;
  float y = position.x*s_t + position.y*c_t;
  

	gl_Position = vec4(scale*x, scale*y, 0.0, 1.0);
	v_color = color;
	} """


