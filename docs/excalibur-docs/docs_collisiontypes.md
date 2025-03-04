Skip to main content
On this page
Colliders have the default collision type of CollisionType.Passive, this is so colliders don't accidentally opt into something computationally expensive. **In order for colliders to participate in collisions** and the global physics system, colliders **must** have a collision type of CollisionType.Active or CollisionType.Fixed.
### Prevent​
Actors with the CollisionType.PreventCollision setting do not participate in any collisions and do not raise collision events.
### Passive​
Actors with the CollisionType.Passive setting only raise collision events, but are not influenced or moved by other actors and do not influence or move other actors.
### Active​
Actors with the CollisionType.Active setting raise collision events and participate in collisions with other actors and will be push or moved by actors sharing the CollisionType.Active or CollisionType.Fixed setting.
### Fixed​
Actors with the CollisionType.Fixed setting raise collision events and participate in collisions with other actors. Actors with the CollisionType.Fixed setting will not be pushed or moved by other actors sharing the CollisionType.Fixed.
Think of `Fixed` actors as "immovable/unstoppable" objects. If two CollisionType.Fixed actors meet they will not be pushed or moved by each other, they will not interact except to throw collision events.
### Collision Type Behavior Matrix​
This matrix shows what will happen with 2 actors of any collision type.
Collision Type| Prevent| Passive| Active| Fixed  
---|---|---|---|---  
Prevent| None| None| None| None  
Passive| None| Events Only| Events Only| Events Only  
Active| None| Events Only| Resolution & Events| Resolution & Events  
Fixed| None| Events Only| Resolution & Events| None  
  * None = No collision resolution and no collision events
  * Events Only = No resolution is performed, only collision events are fired on colliders, except for `postcollision` which only fires if resolution was performed.
  * Resolution & Events = Collider positions are resolved according to their collision type and collision events are fired on both colliders


  * Prevent
  * Passive
  * Active
  * Fixed
  * Collision Type Behavior Matrix


