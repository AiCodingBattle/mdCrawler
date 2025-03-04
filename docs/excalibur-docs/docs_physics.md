Skip to main content
On this page
Excalibur comes built in with two physics simulations.
  * "Arcade" style physics which is good for basic collision detection for non-rotated rectangular areas. 
    * Example: platformers, tile based games, top down, etc
  * "Realistic" style physics which is good for rigid body games where realistic collisions are desired 
    * Example: block stacking, angry bird's style games, etc


**Limitations**
> **_Note:_** The `SolverStrategy.Arcade` does not support `body.friction`.
## Arcade​
Arcade physics simulation is on by default, but can be enabled explicitly in the `Engine` constructor.
```

typescript
constgame=newEngine({
 physics: {
  solver: SolverStrategy.Arcade
 },
...
});
Copy
```
```

typescript
constgame=newEngine({
 physics: {
  solver: SolverStrategy.Arcade
 },
...
});
Copy
```

## Realistic​
Realistic physics are not on by default, but can be enabled explicitly in the `Engine` constructor.
```

typescript
constgame=newEngine({
 physics: {
  solver: SolverStrategy.Realistic
 },
...
});
Copy
```
```

typescript
constgame=newEngine({
 physics: {
  solver: SolverStrategy.Realistic
 },
...
});
Copy
```

### Example​
## Other Physics Settings​
See PhysicsConfig documentation for more
  * Turn off excalibur physics PhysicsConfig.enabled
  * Global acceleration applied to active objects with PhysicsConfig.gravity
  * Configure Fast moving object detection (continuous collision) PhysicsConfig.continuous
  * Physics realistic passes, more passes mean higher quality simulation at the expense of cpu 
    * Realistic solver position iterations, improves overlap resolution PhysicsConfig.realistic.positionIterations
    * Realistic solver velocity iterations, improves response and stability PhysicsConfig.realistic.velocityIterations


## Using Physics with Actors or Entities​
The physics simulation has 2 major pieces for actors
  1. BodyComponent - Controls the motion and qualities of the physics simulation
  2. ColliderComponent - Stores the geometry of any collider and performs overlap testing


### Actors​
Actors come out of the box with both of these components, an implicitly created BodyComponent and a ColliderComponent of a box that matches the specified `width` and `height`, or a circle
```

typescript
constactor=new ex.Actor({
 pos: ex.vec(200, 200),
 width: 100,
 height: 100,
 collisionType: ex.CollisionType.Active,
})
constbuiltInBox= actor.collider.get()
Copy
```
```

typescript
constactor=new ex.Actor({
 pos: ex.vec(200, 200),
 width: 100,
 height: 100,
 collisionType: ex.CollisionType.Active,
})
constbuiltInBox= actor.collider.get()
Copy
```

### Entities​
Reminder entities don't have anything pre-built, all Actors are Entities, but with the common built in features included.
```

typescript
constentity=new ex.Entity([
newTransformComponent(),
newBodyComponent(),
newColliderComponent(),
])
consttx= entity.get(TransformComponent)
constbody= entity.get(BodyComponent)
constcollider= entity.get(ColliderComponent)
Copy
```
```

typescript
constentity=new ex.Entity([
newTransformComponent(),
newBodyComponent(),
newColliderComponent(),
])
consttx= entity.get(TransformComponent)
constbody= entity.get(BodyComponent)
constcollider= entity.get(ColliderComponent)
Copy
```

## Collision System Under the Hood​
Under the hood excalibur does a broadphase/narrowphase approach to locating and resolving collisions.
  1. Broadphase is run against a dynamic tree spatial data structure to locate potential collision pairs
  2. Narrowphase is run to find any actual overlapping colliders
  3. The collision solver is run (Arcade or Realistic). Collisions are resolved according to the configured solver, either Arcade which does axis aligned resolution, or realistic which attempts to do a force based resolution.
a. `precollision` events are fired on Entities just before collision resolution, you have an opportunity to call CollisionContact.cancel and stop the collision at this time.
b. `postcollision`events are fire after resolution.
c. `collisionstart` events fire when two colliders first touch, and does not fire in subsequent frames until they separate.
d. `collisionend` events fire when two colliders separate, and does not fire in subsequent frames until they touch again.


## Example Active-Active/Active-Fixed scenario​
```

ts
// setup game
constgame=new ex.Engine({
 width: 600,
 height: 400,
 physics: {
// use rigid body realistic
  solver: ex.SolverStrategy.Realistic,
// set global acceleration simulating gravity pointing down
  gravity: ex.vec(0, 700)
 }
});
constblock=new ex.Actor({
 pos: new ex.Vector(300, 0),
 width: 20,
 height: 20,
 color: ex.Color.Blue
});
block.body.useBoxCollider(); // useBoxCollision is the default, technically optional
block.body.collider.type = ex.CollisionType.Active;
game.add(block);
constcircle=new ex.Actor({
 x: 301,
 y: 100,
 width: 20,
 height: 20,
 color: ex.Color.Red
});
circle.body.useCircleCollider(10);
circle.body.collider.type = ex.CollisionType.Active;
game.add(circle);
constground=new ex.Actor({
 x: 300,
 y: 380,
 width: 600,
 height: 10,
 color: ex.Color.Black;
});
ground.body.useBoxCollider(); // optional
ground.body.collider.type = ex.CollisionType.Fixed;
game.add(ground);
// start the game
game.start();
Copy
```
```

ts
// setup game
constgame=new ex.Engine({
 width: 600,
 height: 400,
 physics: {
// use rigid body realistic
  solver: ex.SolverStrategy.Realistic,
// set global acceleration simulating gravity pointing down
  gravity: ex.vec(0, 700)
 }
});
constblock=new ex.Actor({
 pos: new ex.Vector(300, 0),
 width: 20,
 height: 20,
 color: ex.Color.Blue
});
block.body.useBoxCollider(); // useBoxCollision is the default, technically optional
block.body.collider.type = ex.CollisionType.Active;
game.add(block);
constcircle=new ex.Actor({
 x: 301,
 y: 100,
 width: 20,
 height: 20,
 color: ex.Color.Red
});
circle.body.useCircleCollider(10);
circle.body.collider.type = ex.CollisionType.Active;
game.add(circle);
constground=new ex.Actor({
 x: 300,
 y: 380,
 width: 600,
 height: 10,
 color: ex.Color.Black;
});
ground.body.useBoxCollider(); // optional
ground.body.collider.type = ex.CollisionType.Fixed;
game.add(ground);
// start the game
game.start();
Copy
```

  * Arcade
  * Realistic
    * Example
  * Other Physics Settings
  * Using Physics with Actors or Entities
    * Actors
    * Entities
  * Collision System Under the Hood
  * Example Active-Active/Active-Fixed scenario


