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
            uniform sampler2D tex0;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            #define PI 3.14159265359
            vec2 pos_r = v_tex_coord.xy;
            vec2 pos_g = v_tex_coord.xy;
            vec2 pos_b = v_tex_coord.xy;

            float r = u_intensity * .01 / 2.0;
            float fi = u_angle * PI / 180.0;

            pos_r += vec2(r * cos(fi), r * sin(fi));
            pos_b -= vec2(r * cos(fi), r * sin(fi));

            vec4 res;
            res.r = texture2D(tex0, pos_r).r;
            res.g = texture2D(tex0, pos_g).g;
            res.b = texture2D(tex0, pos_b).b;
            res.a = (texture2D(tex0, pos_r).a+texture2D(tex0, pos_g).a+texture2D(tex0, pos_b).a)/3.0;
            gl_FragColor = res;
        """
    )

init -1000:

    transform tr_rgb_split(time=30.0, intensity=1.0):
        animation
        shader 'rgb_split'
        u_intensity intensity
        block:
            linear time u_angle 360
            u_angle 0
            repeat
