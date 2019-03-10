vertex = """
uniform mat4    u_model;      // object space -> world space
uniform mat4    u_view;       // world space -> camera space
uniform mat4    u_projection; // camera space -> screen space
uniform vec4    u_color;       // Global Color

attribute vec4 a_color;       // vertex color
attribute vec3 a_position;    // vertex position
varying vec4 v_color;         // interpolated fragment color (out)


void main(){
  v_color = u_color * a_color;
  gl_Position = u_projection * u_view * u_model * vec4(a_position, 1.0);
} """
