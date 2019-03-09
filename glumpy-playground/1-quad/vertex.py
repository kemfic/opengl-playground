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
  float cos_theta = cos(theta);
  float sin_theta = sin(theta);


  float x = position.x*cos_theta - position.y*sin_theta;
  float y = position.x*cos_theta + position.y*sin_theta;
  
  position.x = x;
  position.y = y;

	gl_Position = vec4(scale*position, 0.0, 1.0);
	v_color = color;
	} """


