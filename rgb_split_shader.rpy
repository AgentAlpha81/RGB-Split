python early hide:

    ############################################################################
    ## RGB Split

    """
    'rgb_split'     - shader name.
    'u_intensity'   - channels separation length.
    'u_angle'       - angle degrees.
    """

    renpy.register_shader(
        "rgb_split",
        variables="""
            uniform float u_intensity;
            uniform float u_angle;
            uniform vec2 u_model_size;
            uniform sampler2D tex0;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
            varying vec2 v_pix_size;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
            v_pix_size = 1.0 / u_model_size;
        """,
        fragment_300="""
            #define PI 3.14159265359

            float rad = u_intensity / 2.0;
            float fi = u_angle * PI / 180.0;

            vec2 angle = vec2(cos(fi), sin(fi));

            vec2 pos_r = v_tex_coord + rad * v_pix_size * angle;
            vec2 pos_g = v_tex_coord;
            vec2 pos_b = v_tex_coord - rad * v_pix_size * angle;

            vec4 res;
            res.r = texture2D(tex0, pos_r).r;
            res.g = texture2D(tex0, pos_g).g;
            res.b = texture2D(tex0, pos_b).b;
            res.a = (texture2D(tex0, pos_r).a + texture2D(tex0, pos_g).a + texture2D(tex0, pos_b).a) / 3.0;

            gl_FragColor = res;
        """
    )

init -1000:

    transform tr_rgb_split(time=30.0, intensity=5.0):
        animation
        shader 'rgb_split'
        u_intensity intensity
        block:
            linear time u_angle 360.0
            u_angle 0.0
            repeat
