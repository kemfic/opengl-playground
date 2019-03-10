"""
Texture blending in GLSL

http://distrustsimplicity.net/articles/texture-blending-in-glsl/
"""

fragment = """
uniform float alpha_thresh = 0.1;
uniform vec4      u_color;    // Global color
uniform sampler2D u_texture;  // Texture 
varying vec4      v_color;    // Interpolated fragment color (in)
varying vec2      v_texcoord; // Interpolated fragment texture coordinates (in)
varying vec2      v_texcoord2; // used for stacking textures
void main()
{
    // Get texture color
    vec4 t0 = texture2D(u_texture, v_texcoord);
    vec4 t1 = texture2D(u_texture, v_texcoord);

    gl_FragColor = mix(t0, t1, t1.a);
    if (gl_FragColor.a < alpha_thresh){
    discard;
    }
}
"""
