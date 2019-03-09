vertex = """
uniform mat4    u_model; // object space -> world space
uniform mat4    u_view; // world space -> camera space
uniform mat4    u_projection; // camera space -> screen space
attribute vec3 a_position;

void main(){
  gl_Position = u_projection * u_view * u_model * vec4(a_position, 1.0);
} """
