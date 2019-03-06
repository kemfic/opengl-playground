attribute vec2 position;
attribute vec3 color;

void main() {
  gl_Position = vec3(position, 0.0, 1.0);
}
