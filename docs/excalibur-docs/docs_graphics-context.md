Skip to main content
On this page
## Why Graphics?​
ExcaliburGraphicsContext is the abstraction over the underlying drawing mechanism used to displaying images and graphics to the screen. It is recommended to use ex.Graphics objects with Actors/Entities but the ExcaliburGraphicsContext can be directly drawn to.
The default implementation in Excalibur uses WebGL, however Excalibur can fallback to the 2D Canvas implementation if WebGL isn't supported or there isn't browser hardware acceleration. Read more
### Canvas support​
If you have need to switch to 2D canvas based rendering turn on the flag before engine construction.
warning
Some features like
custom renderers
and
post processors
do not work with the Canvas 2D implementation!
```

typescript
ex.Flags.useCanvasGraphicsContext();
constgame=new ex.Engine(...);
Copy
```
```

typescript
ex.Flags.useCanvasGraphicsContext();
constgame=new ex.Engine(...);
Copy
```

## Drawing to the Context​
The graphics context automatically batches draw calls and flushes them to the screen at the end of every frame. It is therefore recommended you draw in one of the supported drawing lifecycle events.
Either directly by extending the Excalibur Scene
```

typescript
constgame=new ex.Engine({...});
classMySceneextendsex.Scene {
onPreDraw(ctx:ExcaliburGraphicsContext) {
    ctx.save();
    ctx.drawRectangle(...);
    ctx.restore();
  }
onPostDraw(ctx:ExcaliburGraphicsContext) {
    ctx.save();
    ctx.drawRectangle(...);
    ctx.restore();
  }
}
game.addScene('myscene', newMyScene());
game.goToScene('myscene');
game.start();
Copy
```
```

typescript
constgame=new ex.Engine({...});
classMySceneextendsex.Scene {
onPreDraw(ctx:ExcaliburGraphicsContext) {
    ctx.save();
    ctx.drawRectangle(...);
    ctx.restore();
  }
onPostDraw(ctx:ExcaliburGraphicsContext) {
    ctx.save();
    ctx.drawRectangle(...);
    ctx.restore();
  }
}
game.addScene('myscene', newMyScene());
game.goToScene('myscene');
game.start();
Copy
```

Or as an event on the the Excalibur Scene
```

typescript
constgame=new ex.Engine({...});
game.currentScene.on('predraw', (ctx:ExcaliburGraphicsContext) => {
  ctx.save();
  ctx.drawRectangle(...);
  ctx.restore();
});
Copy
```
```

typescript
constgame=new ex.Engine({...});
game.currentScene.on('predraw', (ctx:ExcaliburGraphicsContext) => {
  ctx.save();
  ctx.drawRectangle(...);
  ctx.restore();
});
Copy
```

Or as part of an Actor/Entity graphics component
```

typescript
constgame=new ex.Engine({...});
constactor=new ex.Actor({pos: ex.vec(100, 100)});
game.currentScene.add(actor);
game.start();
// Draw before graphics component but after the transform for actor pos/rotation/scale
actor.graphics.onPreDraw= (ctx:ExcaliburGraphicsContext) => {
  ctx.save();
  ctx.drawRectangle(...);
  ctx.restore();
}
// Draw after graphics component but after the transform for actor pos/rotation/scale
actor.graphics.onPostDraw= (ctx:ExcaliburGraphicsContext) => {
  ctx.save();
  ctx.drawRectangle(...);
  ctx.restore();
}
Copy
```
```

typescript
constgame=new ex.Engine({...});
constactor=new ex.Actor({pos: ex.vec(100, 100)});
game.currentScene.add(actor);
game.start();
// Draw before graphics component but after the transform for actor pos/rotation/scale
actor.graphics.onPreDraw= (ctx:ExcaliburGraphicsContext) => {
  ctx.save();
  ctx.drawRectangle(...);
  ctx.restore();
}
// Draw after graphics component but after the transform for actor pos/rotation/scale
actor.graphics.onPostDraw= (ctx:ExcaliburGraphicsContext) => {
  ctx.save();
  ctx.drawRectangle(...);
  ctx.restore();
}
Copy
```

## Save and Restore​
The ExcaliburGraphicsContext emulates other graphics context APIs by providing a save/restore feature. These are used to save the state of the context before you modify its global state, and then restore it back after you are finished drawing. If you do not, modifications to ExcaliburGraphicsContext will affect other draw calls.
```

typescript
onPostDraw(ctx: ExcaliburGraphicsContext) {
  ctx.save();
  ctx.translate(50, 50);
  ctx.rotate(Math.PI/2);
  ctx.drawRectangle(...);
  ctx.restore();
}
Copy
```
```

typescript
onPostDraw(ctx: ExcaliburGraphicsContext) {
  ctx.save();
  ctx.translate(50, 50);
  ctx.rotate(Math.PI/2);
  ctx.drawRectangle(...);
  ctx.restore();
}
Copy
```

## Setting z-index​
Excalibur allows you to set the z-index of any draw call by setting the ExcaliburGraphicsContext.z property on the context.
```

typescript
onPostDraw(ctx: ExcaliburGraphicsContext) {
  ctx.save();
  ctx.z =-1;
  ctx.drawRectangle(...);
  ctx.restore();
}
Copy
```
```

typescript
onPostDraw(ctx: ExcaliburGraphicsContext) {
  ctx.save();
  ctx.z =-1;
  ctx.drawRectangle(...);
  ctx.restore();
}
Copy
```

## Snap To pixel​
Excalibur has built in snap to pixel support, this can be useful if you are building a game with a pixel aesthetic.
To enable snap to pixel, enable `snapToPixel` in the engine constructor parameter. By default `snapToPixel` is not enabled.
```

typescript
constgame=new ex.Engine({
...
  snapToPixel: true
});
Copy
```
```

typescript
constgame=new ex.Engine({
...
  snapToPixel: true
});
Copy
```

## Custom Renderer​
Custom renderers are a way to extend what the ExcaliburGraphicsContextWebGL can draw by default. In fact all of the things that the graphics context can draw are implemented this way internally.
```

typescript
constMyRenderer implements ex.RendererPlugin {
...
}
constgraphicsContextWebGL= game.graphicsContext asExcaliburGraphicsContextWebGL;
graphicsContextWebGL.register(newMyRenderer());
graphicsContextWebGL.draw<MyRenderer>(...);
Copy
```
```

typescript
constMyRenderer implements ex.RendererPlugin {
...
}
constgraphicsContextWebGL= game.graphicsContext asExcaliburGraphicsContextWebGL;
graphicsContextWebGL.register(newMyRenderer());
graphicsContextWebGL.draw<MyRenderer>(...);
Copy
```

Read a more in-depth example here
## Performance​
Excalibur's performance fallback behavior can be configured by developers to help players experiencing poor performance in non-standard browser configurations
This will fallback to the Canvas2D rendering graphics context which usually performs better on non hardware accelerated browsers, currently postprocessing effects are unavailable in this fallback.
By default if a game is running at 20fps or lower for 100 frames or more after the game has started it will be triggered, the developer can optionally show a player message that is off by default.
```

typescript
var game =new ex.Engine({
...
  configurePerformanceCanvas2DFallback: {
// opt-out of the fallback
    allow: true,
// opt-in to a player pop-up message
    showPlayerMessage: true,
// configure the threshold to trigger the fallback
    threshold: { fps: 20, numberOfFrames: 100 }
  }
});
Copy
```
```

typescript
var game =new ex.Engine({
...
  configurePerformanceCanvas2DFallback: {
// opt-out of the fallback
    allow: true,
// opt-in to a player pop-up message
    showPlayerMessage: true,
// configure the threshold to trigger the fallback
    threshold: { fps: 20, numberOfFrames: 100 }
  }
});
Copy
```

  * Why Graphics?
    * Canvas support
  * Drawing to the Context
  * Save and Restore
  * Setting z-index
  * Snap To pixel
  * Custom Renderer
  * Performance


