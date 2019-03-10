fragment = """
uniform float alpha_thresh = 0.1;
uniform vec4      u_color;    // Global color
uniform sampler2D u_texture;  // Texture 
varying vec4      v_color;    // Interpolated fragment color (in)
varying vec2      v_texcoord; // Interpolated fragment texture coordinates (in)
void main()
{
    // Get texture color
    gl_FragColor = texture2D(u_texture, v_texcoord);
    if (gl_FragColor.a < alpha_thresh){
    discard;
    }
}
"""
