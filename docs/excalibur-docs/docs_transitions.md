Skip to main content
On this page
Many times in your game you'll want to smoothly go from one scene to the next, or provide a custom effect when transitioning!
## Using Pre-Defined Scene Transitions​
It is generally recommended that you define you scenes up front, when you do you have the opportunity to also specify the in/out transitions for a scene.
  * `in` transitions play when the target scene has started, and will play the effect until the `duration` in milliseconds is complete
  * `out` transitions play before the current scene is deactivated, the transition must complete before deactivation.


If no `in/out` transition is specified for a scene it will hard cut from one to the other.
```

ts
constgame=new ex.Engine({
 scenes: {
  scene1: {
   scene: MyScene,
   transitions: {
    in: new ex.FadeInOut({duration: 500, direction: 'in', color: ex.Color.Black}),
    out: new ex.FadeInOut({duration: 500, direction: 'out', color: ex.Color.Black})
   }
  },
  scene2: {
   scene: MyOtherScene,
   transitions: {
    in: new ex.FadeInOut({duration: 500, direction: 'in', color: ex.Color.Black}),
    out: new ex.FadeInOut({duration: 500, direction: 'out', color: ex.Color.Black})
   }
  }
 }
});
game.goToScene('scene1');
Copy
```
```

ts
constgame=new ex.Engine({
 scenes: {
  scene1: {
   scene: MyScene,
   transitions: {
    in: new ex.FadeInOut({duration: 500, direction: 'in', color: ex.Color.Black}),
    out: new ex.FadeInOut({duration: 500, direction: 'out', color: ex.Color.Black})
   }
  },
  scene2: {
   scene: MyOtherScene,
   transitions: {
    in: new ex.FadeInOut({duration: 500, direction: 'in', color: ex.Color.Black}),
    out: new ex.FadeInOut({duration: 500, direction: 'out', color: ex.Color.Black})
   }
  }
 }
});
game.goToScene('scene1');
Copy
```

or using the add scene api
```

ts
constgame=new ex.Engine();
game.add('scene1', {
 scene: MyScene,
 transitions: {
  in: new ex.FadeInOut({duration: 500, direction: 'in', color: ex.Color.Black}),
  out: new ex.FadeInOut({duration: 500, direction: 'out', color: ex.Color.Black})
 }
});
Copy
```
```

ts
constgame=new ex.Engine();
game.add('scene1', {
 scene: MyScene,
 transitions: {
  in: new ex.FadeInOut({duration: 500, direction: 'in', color: ex.Color.Black}),
  out: new ex.FadeInOut({duration: 500, direction: 'out', color: ex.Color.Black})
 }
});
Copy
```

Click canvas to transition!
## Transition Options​
Transitions have a few tricks up their sleeves, you can control duration, direction, easing function, whether to hide any loaders, or block user input during the transition
```

ts
consttransition=new ex.Transition({
/**
  * Transition duration in milliseconds
  */
 duration: 1000,
/**
  * Optionally hides the loader during the transition
  *
  * If either the out or in transition have this set to true, then the loader will be hidden.
  *
  * Default false
  */
 hideLoader: false,
/**
  * Optionally blocks user input during a transition
  *
  * Default false
  */
 blockInput: false,
/**
  * Optionally specify a easing function, by default linear
  */
 easing: ex.EasingFunctions.Linear,
/**
  * Optionally specify a transition direction, by default 'out'
  *
  * * For 'in' direction transitions start at 1 and complete is at 0
  * * For 'out' direction transitions start at 0 and complete is at 1
  */
 direction: 'out',
})
Copy
```
```

ts
consttransition=new ex.Transition({
/**
  * Transition duration in milliseconds
  */
 duration: 1000,
/**
  * Optionally hides the loader during the transition
  *
  * If either the out or in transition have this set to true, then the loader will be hidden.
  *
  * Default false
  */
 hideLoader: false,
/**
  * Optionally blocks user input during a transition
  *
  * Default false
  */
 blockInput: false,
/**
  * Optionally specify a easing function, by default linear
  */
 easing: ex.EasingFunctions.Linear,
/**
  * Optionally specify a transition direction, by default 'out'
  *
  * * For 'in' direction transitions start at 1 and complete is at 0
  * * For 'out' direction transitions start at 0 and complete is at 1
  */
 direction: 'out',
})
Copy
```

## Overriding Transitions​
There are 2 ways to override pre-defined transitions
  * `goToScene('myscene', { destinationIn: ..., sourceOut: ... })` takes the highest precedence and will override any transition
  * Extending Scene.onTransition you can provide dynamic transitions depending on your scene's state

```

typescript
classMyCustomSceneextendsex.Scene {
onTransition(direction:"in"|"out") {
returnnew ex.FadeInOut({
   direction,
   color: ex.Color.Violet,
   duration: 2000
  });
 }
}
Copy
```
```

typescript
classMyCustomSceneextendsex.Scene {
onTransition(direction:"in"|"out") {
returnnew ex.FadeInOut({
   direction,
   color: ex.Color.Violet,
   duration: 2000
  });
 }
}
Copy
```

## FadeInOut​
This transition does exactly as it sounds, you can specific a duration in milliseconds and it will fade in the specified `direction`. FadeInOut uses the color Color.Black by default.
  * The `direction: 'in'` direction means the transition will start fully opaque (non-transparent), then transition to fully transparent.
  * The `direction: 'out'` direction means the transition will start fully transparent, then transition to fully opaque (non-transparent).


## CrossFade​
warning
CrossFade can only be used on the `in`` transition for a scene, this is because it needs to screenshot the previous scene in order to cross fade it.
You can specific a duration in milliseconds and it will fade in the specified `direction`. CrossFade takes a screen shot of the previous scene and blends that into the current scene.
  * The `direction: 'in'` direction means the transition will start fully opaque (non-transparent), then transition to fully transparent.
  * The `direction: 'out'` direction means the transition will start fully transparent, then transition to fully opaque (non-transparent).


Click canvas to transition!
## Starting Scene Transition​
Sometimes you want a special start transition for the beginning of your game after loading. You may want to match the color, do something special, etc.
This can be done on the Engine.start by providing a start transition
```

typescript
game.start('scene1',
{
 inTransition: startTransition
});
Copy
```
```

typescript
game.start('scene1',
{
 inTransition: startTransition
});
Copy
```

## Custom built Transitions​
Transitions are really an Entity with a TransformComponent and GraphicsComponent that take up the entire screen and draw on top of everything by default `z = Infinity`.
To build your own custom transition, extend Transition and implement the stubbed methods
For example this is CrossFade's implementation
```

typescript
exportclassCrossFadeextendsTransition {
engine:Engine;
image:HTMLImageElement;
screenCover:Sprite;
constructor(options:TransitionOptions&CrossFadeOptions) {
super(options);
this.name =`CrossFade#${this.id}`;
 }
overrideasynconPreviousSceneDeactivate(scene:Scene<unknown>) {
this.image =await scene.engine.screenshot(true);
 }
overrideonInitialize(engine:Engine):void {
this.engine = engine;
constbounds= engine.screen.getWorldBounds();
this.transform.pos =vec(bounds.left, bounds.top);
this.screenCover = ImageSource.fromHtmlImageElement(this.image).toSprite();
this.graphics.add(this.screenCover);
this.transform.scale =vec(1/ engine.screen.pixelRatio, 1/ engine.screen.pixelRatio);
this.graphics.opacity =this.progress;
 }
overrideonStart(_progress:number):void {
this.graphics.opacity =this.progress;
 }
overrideonReset() {
this.graphics.opacity =this.progress;
 }
overrideonEnd(progress:number):void {
this.graphics.opacity = progress;
 }
overrideonUpdate(progress:number):void {
this.graphics.opacity = progress;
 }
}
Copy
```
```

typescript
exportclassCrossFadeextendsTransition {
engine:Engine;
image:HTMLImageElement;
screenCover:Sprite;
constructor(options:TransitionOptions&CrossFadeOptions) {
super(options);
this.name =`CrossFade#${this.id}`;
 }
overrideasynconPreviousSceneDeactivate(scene:Scene<unknown>) {
this.image =await scene.engine.screenshot(true);
 }
overrideonInitialize(engine:Engine):void {
this.engine = engine;
constbounds= engine.screen.getWorldBounds();
this.transform.pos =vec(bounds.left, bounds.top);
this.screenCover = ImageSource.fromHtmlImageElement(this.image).toSprite();
this.graphics.add(this.screenCover);
this.transform.scale =vec(1/ engine.screen.pixelRatio, 1/ engine.screen.pixelRatio);
this.graphics.opacity =this.progress;
 }
overrideonStart(_progress:number):void {
this.graphics.opacity =this.progress;
 }
overrideonReset() {
this.graphics.opacity =this.progress;
 }
overrideonEnd(progress:number):void {
this.graphics.opacity = progress;
 }
overrideonUpdate(progress:number):void {
this.graphics.opacity = progress;
 }
}
Copy
```

  * Using Pre-Defined Scene Transitions
  * Transition Options
  * Overriding Transitions
  * FadeInOut
  * CrossFade
  * Starting Scene Transition
  * Custom built Transitions


