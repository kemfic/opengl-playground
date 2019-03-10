
vertex = """
uniform mat4   u_model;         // Model matrix
uniform mat4   u_view;          // View matrix
uniform mat4   u_projection;    // Projection matrix
attribute vec4 a_color;         // Vertex color
attribute vec3 position;      // Vertex position
attribute vec2 a_texcoord0;      // Vertex texture coordinates
attribute vec2 a_texcoord1;      // Vertex texture coordinates (alpha)
varying vec4   v_color;         // Interpolated fragment color (out)
varying vec2   v_texcoord0;      // Interpolated fragment texture coordinates (out)
varying vec2   v_texcoord1;      // texture with alpha, goes on top
void main()
{
    // Assign varying variables
    v_color     = a_color;      
    v_texcoord0  = a_texcoord0;
    v_texcoord1  = a_texcoord1;
    // Final position
    gl_Position = <transform>;
}
"""
