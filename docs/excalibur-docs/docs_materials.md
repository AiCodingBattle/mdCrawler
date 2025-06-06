Skip to main content
On this page
Sometimes you need even more control about how your graphics render in your game! For example you might want a custom blend, a reflection effect, or a warping effect. With this api you can provide custom shaders to graphics.
If you want to apply a shader to the whole screen check out PostProcessors
warning
Materials are only supported in WebGL mode, this is the default mode for Excalibur but if you switch or fallback to 2D Canvas materials will not have an effect.
warning
If you are using the `ex.Engine({pixelArt: true})` setting, you'll need to re-include the pixelArt sampler in your custom shader in order to preserve the pixel art effect.
```

#version 300 es
precision mediump float;
in vec2 v_uv;
out vec4 fragColor;
uniform vec2 u_graphic_resolution;
uniform sampler2D u_graphic;

// Inigo Quilez pixel art filter https://jorenjoestar.github.io/post/pixel_art_filtering/
vec2 uv_iq(in vec2 uv, in vec2 texture_size) {
 vec2 pixel = uv * texture_size;
 
 vec2 seam=floor(pixel+.5);
 vec2 dudv=fwidth(pixel);
 pixel=seam+clamp((pixel-seam)/dudv,-.5,.5);
 
 return pixel/texture_size;
}
void main(void) {
  // Use the new UV from uv_iq to sample your pixel art texture
  vec2 newUv = uv_iq(v_uv, u_graphic_resolution);
  vec4 sourceColor = texture(u_graphic, newUv);
  fragColor = sourceColor;
  fragColor.rgb = fragColor.rgb * fragColor.a; // premultiply alpha
}
Copy
```
```

#version 300 es
precision mediump float;
in vec2 v_uv;
out vec4 fragColor;
uniform vec2 u_graphic_resolution;
uniform sampler2D u_graphic;

// Inigo Quilez pixel art filter https://jorenjoestar.github.io/post/pixel_art_filtering/
vec2 uv_iq(in vec2 uv, in vec2 texture_size) {
 vec2 pixel = uv * texture_size;
 
 vec2 seam=floor(pixel+.5);
 vec2 dudv=fwidth(pixel);
 pixel=seam+clamp((pixel-seam)/dudv,-.5,.5);
 
 return pixel/texture_size;
}
void main(void) {
  // Use the new UV from uv_iq to sample your pixel art texture
  vec2 newUv = uv_iq(v_uv, u_graphic_resolution);
  vec4 sourceColor = texture(u_graphic, newUv);
  fragColor = sourceColor;
  fragColor.rgb = fragColor.rgb * fragColor.a; // premultiply alpha
}
Copy
```

## Creating Material Shaders​
We recommend using the ExcaliburGraphicsContext.createMaterial method to create materials.
```

ts
constactor=new ex.Actor({
 pos: ex.vec(200, 200),
 width: 100,
 height: 100,
 color: ex.Color.Blue // Default graphic will be modified by the material
});
// Simple material that colors every pixel red
constmaterial= game.graphicsContext.createMaterial({
 name: 'custom-material',
 fragmentSource: `#version 300 es
 precision mediump float;
 out vec4 color;
 void main() {
  color = vec4(1.0, 0.0, 0.0, 1.0);
 }`
});
// Material applied to the actor's graphics
actor.graphics.material = material;
Copy
```
```

ts
constactor=new ex.Actor({
 pos: ex.vec(200, 200),
 width: 100,
 height: 100,
 color: ex.Color.Blue // Default graphic will be modified by the material
});
// Simple material that colors every pixel red
constmaterial= game.graphicsContext.createMaterial({
 name: 'custom-material',
 fragmentSource: `#version 300 es
 precision mediump float;
 out vec4 color;
 void main() {
  color = vec4(1.0, 0.0, 0.0, 1.0);
 }`
});
// Material applied to the actor's graphics
actor.graphics.material = material;
Copy
```

note
Excalibur only supports GLSL ES 300 shaders `#version 300 es`, this version declaration must be the very first thing. No spaces or newlines before it or WebGL will not compile it.
warning
Excalibur deals in pre-multiplied alphas! This means your shader transparency might not be what you expect.
Generally this can be solved by adding `fragColor.rgb = fragColor.rgb * fragColor.a;` or similar to your code.
Check out this great post about premultiplied alphas
Once a material is created it can be added/removed from the actor's graphics component by accessing the GraphicsComponent.material property.
## Passing parameters to Materials​
To pass data to materials we use a concept called "uniforms", you can think of these as global variables that are the same for each pixel during a draw.
To update a materials uniform we recommend using Material.update, this will automatically set up the shader context for you so it is ready for you to use. You get passed the excalibur Shader instance and you can set uniforms from there! There are a number of `trySet*` prefixed methods we recommend you use, these methods will attempt to set a uniform if it exists.
```

ts
constactor=new ex.Actor({
 pos: ex.vec(200, 200),
 width: 100,
 height: 100,
 color: ex.Color.Blue // Default graphic will be modified by the material
});
constmaterial= actor.graphics.material = game.graphicsContext.createMaterial({
 name: 'custom-material',
 fragmentSource: `#version 300 es
 precision mediump float;
 uniform vec2 iMouse;
 out vec4 color;
 void main() {
  // Change the color based on mouse position
  vec2 mouseColor = iMouse / 800.0;
  color = vec4(mouseColor, 0.0, 1.0);
 }`
});
game.input.pointers.primary.on('move', evt=> {
 actor.pos = evt.worldPos;
 material.update(shader=> {
  shader.trySetUniformFloatVector('iMouse', evt.worldPos);
 });
});
Copy
```
```

ts
constactor=new ex.Actor({
 pos: ex.vec(200, 200),
 width: 100,
 height: 100,
 color: ex.Color.Blue // Default graphic will be modified by the material
});
constmaterial= actor.graphics.material = game.graphicsContext.createMaterial({
 name: 'custom-material',
 fragmentSource: `#version 300 es
 precision mediump float;
 uniform vec2 iMouse;
 out vec4 color;
 void main() {
  // Change the color based on mouse position
  vec2 mouseColor = iMouse / 800.0;
  color = vec4(mouseColor, 0.0, 1.0);
 }`
});
game.input.pointers.primary.on('move', evt=> {
 actor.pos = evt.worldPos;
 material.update(shader=> {
  shader.trySetUniformFloatVector('iMouse', evt.worldPos);
 });
});
Copy
```

## Additional Textures in Materials​
You can now specify as many additional textures into your Material as your GPU has texture slots! You may provide a dictionary of uniform names to excalibur ImageSource and it will be loaded into the material.
```

typescript
constnoise=new ex.ImageSource('./noise.avif', false, ex.ImageFiltering.Pixel);
loader.addResource(noise);
var waterMaterial = game.graphicsContext.createMaterial({
 name: 'water',
 fragmentSource: waterFrag,
 color: ex.Color.fromRGB(55, 0, 200, .6),
 images: {
  u_noise: noise
 }
});
Copy
```
```

typescript
constnoise=new ex.ImageSource('./noise.avif', false, ex.ImageFiltering.Pixel);
loader.addResource(noise);
var waterMaterial = game.graphicsContext.createMaterial({
 name: 'water',
 fragmentSource: waterFrag,
 color: ex.Color.fromRGB(55, 0, 200, .6),
 images: {
  u_noise: noise
 }
});
Copy
```

## Material Built In Uniforms​
Materials come with a lot of built in uniforms you can use!
  * `vec4 u_color` - This is the current color of the material
  * `float u_time_ms` - This is `performance.now()` a ms timestamp that starts from initial navigation to the page
  * `float u_opacity` - Current opacity of your graphic, Graphic.opacity
  * `vec2 u_resolution` - Current screen resolution
  * `vec2 u_graphic_resolution` - Current graphic's resolution
  * `vec2 u_size` - Current destination draw size
  * `mat4 u_matrix` - Excalibur's current orthographic projection matrix
  * `mat4 u_transform` - Excalibur's current world transform
  * `sampler2D u_graphic` - Current graphic's texture
  * `sampler2D u_screen_texture` - Current excalibur screen texture just before rendering the material


## Material Built In attributes​
  * `v_uv` - Current UV coordinate of the graphic
  * `v_screenuv` - Current Screen UV coordinate behind the graphic


## Outline Material Example​
One common use case for materials is to apply an effect to your actors, a not uncommon ask is to create an outline. This can be useful for selections, attacks, etc.
Here is the shader code for a rainbow outline. Change `outlineColorHSL` to a constant if you don't want a rainbow effect 🌈
The theory behind this shader is we sample up, down, left, and right of the current pixel in the graphic and color it.
```

shader
#version 300 es
precision mediump float;
uniform float u_time_ms;
uniform sampler2D u_graphic;
in vec2 v_uv;
in vec2 v_screenuv;
out vec4 fragColor;
vec3 hsv2rgb(vec3 c){
 vec4 K=vec4(1.,2./3.,1./3.,3.);
 return c.z*mix(K.xxx,clamp(abs(fract(c.x+K.xyz)*6.-K.w)-K.x, 0., 1.),c.y);
}
void main() {
 const float TAU = 6.28318530;
 const float steps = 4.0; // up/down/left/right pixels
float radius = 2.0;
float time_sec = u_time_ms / 1000.;
 vec3 outlineColorHSL = vec3(sin(time_sec/2.0) * 1., 1., 1.);
 vec2 aspect = 1.0 / vec2(textureSize(u_graphic, 0));
for (float i = 0.0; i < TAU; i += TAU / steps) {
// Sample image in a circular pattern
  vec2 offset = vec2(sin(i), cos(i)) * aspect * radius;
  vec4 col = texture(u_graphic, v_uv + offset);
// Mix outline with background
floatalpha = smoothstep(0.5, 0.7, col.a);
  fragColor = mix(fragColor, vec4(hsv2rgb(outlineColorHSL), 1.0), alpha); // apply outline
 }
// Overlay original texture
 vec4 mat = texture(u_graphic, v_uv);
float factor = smoothstep(0.5, 0.7, mat.a);
 fragColor = mix(fragColor, mat, factor);
}
Copy
```
```

shader
#version 300 es
precision mediump float;
uniform float u_time_ms;
uniform sampler2D u_graphic;
in vec2 v_uv;
in vec2 v_screenuv;
out vec4 fragColor;
vec3 hsv2rgb(vec3 c){
 vec4 K=vec4(1.,2./3.,1./3.,3.);
 return c.z*mix(K.xxx,clamp(abs(fract(c.x+K.xyz)*6.-K.w)-K.x, 0., 1.),c.y);
}
void main() {
 const float TAU = 6.28318530;
 const float steps = 4.0; // up/down/left/right pixels
float radius = 2.0;
float time_sec = u_time_ms / 1000.;
 vec3 outlineColorHSL = vec3(sin(time_sec/2.0) * 1., 1., 1.);
 vec2 aspect = 1.0 / vec2(textureSize(u_graphic, 0));
for (float i = 0.0; i < TAU; i += TAU / steps) {
// Sample image in a circular pattern
  vec2 offset = vec2(sin(i), cos(i)) * aspect * radius;
  vec4 col = texture(u_graphic, v_uv + offset);
// Mix outline with background
floatalpha = smoothstep(0.5, 0.7, col.a);
  fragColor = mix(fragColor, vec4(hsv2rgb(outlineColorHSL), 1.0), alpha); // apply outline
 }
// Overlay original texture
 vec4 mat = texture(u_graphic, v_uv);
float factor = smoothstep(0.5, 0.7, mat.a);
 fragColor = mix(fragColor, mat, factor);
}
Copy
```

Here is the code in action!
## Using the Screen Texture Example​
The screen texture gives you access to the texture right before the material is drawn, this allows you to do some cool compositing effects like creating a reflected water material!
This shader is adapted from this tutorial in Godot https://www.youtube.com/watch?v=32jdNLTJ3zY
The theory is sample the screen texture with a reflected coordinate, apply noise distortion to make the wobble, and some sin/cos sdf magic to create the crest at the top.
```

shader
#version 300 es
precision mediump float;
#define NUM_NOISE_OCTAVES 20
// Precision-adjusted variations of https://www.shadertoy.com/view/4djSRW
floathash(float p) { p = fract(p * 0.011); p *= p + 7.5; p *= p + p; return fract(p); }
floathash(vec2 p) {vec3 p3 = fract(vec3(p.xyx) * 0.13); p3 += dot(p3, p3.yzx + 3.333); return fract((p3.x + p3.y) * p3.z); }
floatnoise(float x) {
float i = floor(x);
float f = fract(x);
float u = f * f * (3.0 - 2.0 * f);
  return mix(hash(i), hash(i + 1.0), u);
}
floatnoise(vec2 x) {
  vec2 i = floor(x);
  vec2 f = fract(x);
// Four corners in 2D of a tile
floata = hash(i);
floatb = hash(i + vec2(1.0, 0.0));
float c = hash(i + vec2(0.0, 1.0));
float d = hash(i + vec2(1.0, 1.0));
// Simple 2D lerp using smoothstep envelope between the values.
// return vec3(mix(mix(a, b, smoothstep(0.0, 1.0, f.x)),
//			mix(c, d, smoothstep(0.0, 1.0, f.x)),
//			smoothstep(0.0, 1.0, f.y)));
// Same code, with the clamps in smoothstep and common subexpressions
// optimized away.
  vec2 u = f * f * (3.0 - 2.0 * f);
	return mix(a, b, u.x) + (c - a) * u.y * (1.0 - u.x) + (d - b) * u.x * u.y;
}
floatfbm(float x) {
float v = 0.0;
floata = 0.5;
float shift = float(100);
for (int i = 0; i < NUM_NOISE_OCTAVES; ++i) {
		v += a * noise(x);
		x = x * 2.0 + shift;
a *= 0.5;
	}
	return v;
}
floatfbm(vec2 x) {
float v = 0.0;
floata = 0.5;
	vec2 shift = vec2(100);
// Rotate to reduce axial bias
  mat2 rot = mat2(cos(0.5), sin(0.5), -sin(0.5), cos(0.50));
for (int i = 0; i < NUM_NOISE_OCTAVES; ++i) {
		v += a * noise(x);
		x = rot * x * 2.0 + shift;
a *= 0.5;
	}
	return v;
}
uniform float u_time_ms;
uniform vec4 u_color;
uniform sampler2D u_graphic;
uniform sampler2D u_screen_texture;
uniform vec2 u_resolution; // screen resolution
uniform vec2 u_graphic_resolution; // graphic resolution
in vec2 v_uv;
in vec2 v_screenuv;
out vec4 fragColor;
void main() {
float time_sec = u_time_ms / 1000.;
float wave_amplitude = .525;
float wave_speed = 1.8;
float wave_period = .175;
 vec2 scale = vec2(2.5, 8.5);
float waves = v_uv.y * scale.y + 
sin(v_uv.x * scale.x / wave_period - time_sec * wave_speed) *
cos(0.2 * v_uv.x * scale.x /wave_period + time_sec * wave_speed) *
    wave_amplitude - wave_amplitude;
float distortion = noise(v_uv*scale*vec2(2.1, 1.05) + time_sec * 0.12) * .25 - .125;
 vec2 reflected_screenuv = vec2(v_screenuv.x - distortion, v_screenuv.y);
 vec4 screen_color = texture(u_screen_texture, reflected_screenuv);
 vec4 wave_crest_color = vec4(1);
float wave_crest = clamp(smoothstep(0.1, 0.14, waves) - smoothstep(0.018, 0.99, waves), 0., 1.);
 fragColor.a = smoothstep(0.1, 0.12, waves);
 vec3 mixColor = (u_color.rgb * u_color.a); // pre-multiplied alpha
 fragColor.rgb = mix(screen_color.rgb, mixColor, u_color.a)*fragColor.a + (wave_crest_color.rgb * wave_crest);
}
Copy
```
```

shader
#version 300 es
precision mediump float;
#define NUM_NOISE_OCTAVES 20
// Precision-adjusted variations of https://www.shadertoy.com/view/4djSRW
floathash(float p) { p = fract(p * 0.011); p *= p + 7.5; p *= p + p; return fract(p); }
floathash(vec2 p) {vec3 p3 = fract(vec3(p.xyx) * 0.13); p3 += dot(p3, p3.yzx + 3.333); return fract((p3.x + p3.y) * p3.z); }
floatnoise(float x) {
float i = floor(x);
float f = fract(x);
float u = f * f * (3.0 - 2.0 * f);
  return mix(hash(i), hash(i + 1.0), u);
}
floatnoise(vec2 x) {
  vec2 i = floor(x);
  vec2 f = fract(x);
// Four corners in 2D of a tile
floata = hash(i);
floatb = hash(i + vec2(1.0, 0.0));
float c = hash(i + vec2(0.0, 1.0));
float d = hash(i + vec2(1.0, 1.0));
// Simple 2D lerp using smoothstep envelope between the values.
// return vec3(mix(mix(a, b, smoothstep(0.0, 1.0, f.x)),
//			mix(c, d, smoothstep(0.0, 1.0, f.x)),
//			smoothstep(0.0, 1.0, f.y)));
// Same code, with the clamps in smoothstep and common subexpressions
// optimized away.
  vec2 u = f * f * (3.0 - 2.0 * f);
	return mix(a, b, u.x) + (c - a) * u.y * (1.0 - u.x) + (d - b) * u.x * u.y;
}
floatfbm(float x) {
float v = 0.0;
floata = 0.5;
float shift = float(100);
for (int i = 0; i < NUM_NOISE_OCTAVES; ++i) {
		v += a * noise(x);
		x = x * 2.0 + shift;
a *= 0.5;
	}
	return v;
}
floatfbm(vec2 x) {
float v = 0.0;
floata = 0.5;
	vec2 shift = vec2(100);
// Rotate to reduce axial bias
  mat2 rot = mat2(cos(0.5), sin(0.5), -sin(0.5), cos(0.50));
for (int i = 0; i < NUM_NOISE_OCTAVES; ++i) {
		v += a * noise(x);
		x = rot * x * 2.0 + shift;
a *= 0.5;
	}
	return v;
}
uniform float u_time_ms;
uniform vec4 u_color;
uniform sampler2D u_graphic;
uniform sampler2D u_screen_texture;
uniform vec2 u_resolution; // screen resolution
uniform vec2 u_graphic_resolution; // graphic resolution
in vec2 v_uv;
in vec2 v_screenuv;
out vec4 fragColor;
void main() {
float time_sec = u_time_ms / 1000.;
float wave_amplitude = .525;
float wave_speed = 1.8;
float wave_period = .175;
 vec2 scale = vec2(2.5, 8.5);
float waves = v_uv.y * scale.y + 
sin(v_uv.x * scale.x / wave_period - time_sec * wave_speed) *
cos(0.2 * v_uv.x * scale.x /wave_period + time_sec * wave_speed) *
    wave_amplitude - wave_amplitude;
float distortion = noise(v_uv*scale*vec2(2.1, 1.05) + time_sec * 0.12) * .25 - .125;
 vec2 reflected_screenuv = vec2(v_screenuv.x - distortion, v_screenuv.y);
 vec4 screen_color = texture(u_screen_texture, reflected_screenuv);
 vec4 wave_crest_color = vec4(1);
float wave_crest = clamp(smoothstep(0.1, 0.14, waves) - smoothstep(0.018, 0.99, waves), 0., 1.);
 fragColor.a = smoothstep(0.1, 0.12, waves);
 vec3 mixColor = (u_color.rgb * u_color.a); // pre-multiplied alpha
 fragColor.rgb = mix(screen_color.rgb, mixColor, u_color.a)*fragColor.a + (wave_crest_color.rgb * wave_crest);
}
Copy
```

  * Creating Material Shaders
  * Passing parameters to Materials
  * Additional Textures in Materials
  * Material Built In Uniforms
  * Material Built In attributes
  * Outline Material Example
  * Using the Screen Texture Example


