Skip to main content
On this page
The Screen is useful for for controlling the shape and behavior of you screen.
## Basic Screen​
For many games specifying a static width and height is all you need. This example is the default DisplayMode, fixed.
```

typescript
constgame=new ex.Engine({
 width: 800,
 height: 600
});
Copy
```
```

typescript
constgame=new ex.Engine({
 width: 800,
 height: 600
});
Copy
```

The above snippet has the affect of setting the logical resolution to 800x600 and the viewport css pixels to 800x600.
## Understanding Viewport & Resolution​
Excalibur has a screen abstraction for dealing with Screen.viewport size, and Screen.resolution. It also handles HiDPI scaling, the browser fullscreen API, and translation of screen coordinates into game world coordinates.
The Screen.viewport represents the size of the window into the game work in CSS pixels on the screen. Another way to think about viewport is it represents the actual size of the "window" into the game on the computer screen.
The Screen.resolution represents the number of logical pixels stretched across the viewport.
For example, a screen with resolution 100x100 and a resolution of 1000x1000 stretches, 100 logical game pixels across 1000 pixels of the screen.
The screen resolution and viewport can be set and accessed of the engine constructor.
```

typescript
constgame=new ex.Engine({
// set the viewport dimensions
 viewport: { width: 800, height: 600 },
// sets the resolution
 resolution: ex.Resolution.GameBoy
});
constscreen= game.screen;
Copy
```
```

typescript
constgame=new ex.Engine({
// set the viewport dimensions
 viewport: { width: 800, height: 600 },
// sets the resolution
 resolution: ex.Resolution.GameBoy
});
constscreen= game.screen;
Copy
```

## HiDPI scaling​
Excalibur will automatically detect HiDPI devices and scale the internal canvas resolution. This prevents an issue that causes graphics to look blurry because images are spread across at least twice as many physical pixels. Read more about this on MDN.
This automatic scaling can be disabled with the `suppressHiDPIScaling: true` in the Engine constructor.
You may wish to disable this scaling for a few reasons:
  1. Large resolutions in addition to the scaling can cause games to break on mobile (4k pixels in width or height will cause mobile devices to fail loading to the GPU).
  2. Performance, a smaller resolution means the game does not need to drive as many pixels.


note
Large resolutions (Commonly in the range 4000x4000) can cause problems on HiDPI screens (aka Retina), the underlying WebGL technology will limit the size.
If you need large resolutions you may need to suppress HiDPI
```

typescript
constgame=new ex.Engine({
// set the viewport dimensions
 viewport: { width: 800, height: 600 },
// sets the resolution
 resolution: { width: 3000, height: 3000 },
 suppressHiDPIScaling: true
});
Copy
```
```

typescript
constgame=new ex.Engine({
// set the viewport dimensions
 viewport: { width: 800, height: 600 },
// sets the resolution
 resolution: { width: 3000, height: 3000 },
 suppressHiDPIScaling: true
});
Copy
```

## Coordinate systems​
In Excalibur, due to HTML canvas native and scaled resolution, there are essentially _two_ kinds of coordinates: a **screen** coordinate and a **world** coordinate.
### Screen coordinates​
A screen coordinate is a point on a user's physical screen. `(0, 0)` in screen coordinates is the top-left of the canvas. Excalibur translates mouse event positions into screen coordinates for you. Screen coordinates ignore the game camera, think of it like where the user is physically pointing on top of your game.
### World coordinates​
A world coordinate is a point _in the game world_ relative to a scene's camera. The world space is the default place where actors operate. By default the camera is centered such that the origin is in the top left. If the camera is not moved `(0, 0)` in the game world will be the top left of your game, but if you move the camera to `(0, 0)` the actor will now be center screen.
### Converting between coordinates​
Usually, your game logic should only deal in terms of world coordinates because this is the coordinate system you're positioning actors in or drawing in. Sometimes though, you need to convert between systems when interfacing with input.
Excalibur provides two methods to convert between systems, Engine.screenToWorldCoordinates and Engine.worldToScreenCoordinates. Use these methods to convert between coordinate systems as they take into account all the information Excalibur collects to appropriately do the math for you including scaling, device pixel ratio, and more.
## Game resolution​
An HTML canvas element has a "native" resolution which is specified using the `width` and `height` HTML attributes. In Excalibur, these can be set using canvasWidth and canvasHeight respectively.
### Native Resolution​
If you don't explicitly set `canvasWidth` or `canvasHeight` Excalibur will manage the values for you, meaning that the "native" resolution will be the physical screen width/height so there is no "scaling" happening. This means your game logic must be responsive if the resolution of the game changes and you cannot depend on a "fixed" width/height coordinate system. Games which can be played on mobile devices _and_ desktop will work, since your game logic can detect what screen size the game is being played on and respond accordingly.
### Scaled Resolution​
Alternatively, if a native resolution is set and then CSS is used to change the _styled_ `width` and `height`, this makes your game _scale_ to whatever the CSS dimensions are. You would want to explicitly set a native resolution if your game depends on having a specific width/height of the "draw area". For example, you may want to design a game that depends on a fixed size of 1280x720 but you want to allow the user to view it at higher resolutions on their browser, so you may scale the canvas to a 16:9 ratio. Your game logic and positioning logic will still work since the game world is still 720px wide even though it may be displaying at 1080px wide on a high-res screen.
### HiDPI Displays​
HiDPI displays scale device pixels. For example, on a normal monitor, a 1280x720 game canvas will return `1280` and `720` for the `width` and `height` respectively. However, on a 2X HiDPI display _what's actually drawn_ is multiplied by a device pixel ratio of `2` so, `2560` and `1440`. Any time you need to get this "actual" width and height of what's being drawn to the canvas, the engine exposes Engine.drawWidth and Engine.drawHeight that takes into account the device pixel ratio. In this HiDPI scenario, Engine.canvasWidth and Engine.canvasHeight would still return the native `1280x720` resolution.
## Advanced Viewport and Resolution Manipulation​
The best way to change the viewport and resolution is in the Engine constructor arguments. If the viewport or resolution is changed after constructor time, Screen.applyResolutionAndViewport must be called to have the changes take effect.
```

typescript
// get or set the viewport
constviewport= game.screen.viewport;
game.screen.viewport = { width: 400, height: 300 };
// get or set the resolution
constresolution= game.screen.resolution;
game.screen.resolution = { width: 100, height: 100 };
// Apply changes to viewport and resolution to the canvas and graphics context
game.screen.applyResolutionAndViewport();
Copy
```
```

typescript
// get or set the viewport
constviewport= game.screen.viewport;
game.screen.viewport = { width: 400, height: 300 };
// get or set the resolution
constresolution= game.screen.resolution;
game.screen.resolution = { width: 100, height: 100 };
// Apply changes to viewport and resolution to the canvas and graphics context
game.screen.applyResolutionAndViewport();
Copy
```

Sometimes you might want to switch between 2 different resolutions and viewports, perhaps for different scenes, or for some in game animation. This can be done with Screen.pushResolutionAndViewport and Screen.popResolutionAndViewport.
```

typescript
// Save the current resolution and viewport
game.screen.pushResolutionAndViewport();
// Change and apply
game.screen.resolution = ex.Resolution.NES;
game.screen.applyResolutionAndViewport();
// Show some animation or do something at NES resolution
// Restore the old resolution and viewport, then apply
game.screen.popResolutionAndViewport();
game.screen.applyResolutionAndViewport();
Copy
```
```

typescript
// Save the current resolution and viewport
game.screen.pushResolutionAndViewport();
// Change and apply
game.screen.resolution = ex.Resolution.NES;
game.screen.applyResolutionAndViewport();
// Show some animation or do something at NES resolution
// Restore the old resolution and viewport, then apply
game.screen.popResolutionAndViewport();
game.screen.applyResolutionAndViewport();
Copy
```

  * Basic Screen
  * Understanding Viewport & Resolution
  * HiDPI scaling
  * Coordinate systems
    * Screen coordinates
    * World coordinates
    * Converting between coordinates
  * Game resolution
    * Native Resolution
    * Scaled Resolution
    * HiDPI Displays
  * Advanced Viewport and Resolution Manipulation


