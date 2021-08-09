init -2 python:
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
            
            vec3 res;
            res.r = texture2D(tex0, pos_r).r;
            res.g = texture2D(tex0, pos_g).g;
            res.b = texture2D(tex0, pos_b).b;
            
            gl_FragColor = vec4(res, 1.0);
        """
    )
