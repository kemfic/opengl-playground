fragment = """
uniform vec4      u_color;    // Global color
uniform sampler2D u_texture;  // Texture 
varying vec4      v_color;    // Interpolated fragment color (in)
varying vec2      v_texcoord; // Interpolated fragment texture coordinates (in)
void main()
{
    // Get texture color
    vec4 t_color = vec4(vec3(texture2D(u_texture, v_texcoord).r), 1.0);
    // Final color
    gl_FragColor = u_color * t_color * mix(v_color, t_color, 0.25);
}
"""
