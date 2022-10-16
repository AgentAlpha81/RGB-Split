# RGB-Split
![screenshot0001](https://user-images.githubusercontent.com/23055740/128658333-8ad6c0a4-50ed-49fe-a05c-af4c43ccce4a.png)

Custom Ren'Py RGB Split shader that has the same effect as chromatic aberration or anaglyph images.
It shifts the red and blue channels each one in different directions and rotates them around the green channel.

Video: https://vk.com/video-201215195_456239021

# Instruction:
Minimum Ren'Py version - 7.4.0

* Drop rgb_split_shader.rpy inside your project.
* Add "config.gl2 = True" line to enable shaders in your game.
* Create transform with "rgb_split" shader and set values to u_intensity and u_angle.
* Apply created transform to your image.

# Usage Example:

![2021-08-09_085415](https://user-images.githubusercontent.com/23055740/128658974-97f348dd-5560-4b49-89eb-70e6a7d6a519.png)

u_intensity - distance between channels, in pixels

u_angle - rotation degrees. 
