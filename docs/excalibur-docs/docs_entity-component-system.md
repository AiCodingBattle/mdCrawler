Skip to main content
On this page
Excalibur has a built in Entity Component System (ECS for short), which is a popular software technique in the video game industry for managing behavior in a game in a composable and reusable way. Many ECS implementations also focus on memory cache optimization techniques, that is not a goal of the current Excalibur implementation.
## What is an Entity-Component-System​
The wikipedia article does a pretty good job of explaining the design pattern, but here is the gist:
  * Entity - Any "thing" in the game that has behavior, it has an `id` place to to put components.
  * Component - Any state for a particular entity, generally these are state only, but can contain small amounts of logic
  * System - Implementation of behavior given a set of components on an entity


Many of the features built in Excalibur are built using this, and users of Excalibur can make their own systems and/or replace existing excalibur systems.
## Excalibur ECS Implementation​
In addition to the familiar Entity, Component, and System, Excalibur also implements an ECS World where all of these pieces live and can interact together. Each Scene in Excalibur contains an ECS world, they are not shared between scenes.
Inside an ECS World there is an EntityManager, QueryManager, and SystemManager that handle all the details.
  * EntityManager - Manages all the entities known by the world, it is an Observer of entity component changes over time.
  * QueryManager - Manages all the entity queries, a Query allows a search of all known entities by a set of component types.
  * SystemManager - Manages all the systems known by the world, it updates a System in priority order (low to high) and gives them a set of entities that match types.


Excalibur Actor's are in fact Entity's in this ECS implementation. Actors come "pre-installed" with a set of components and features.
  * What is an Entity-Component-System
  * Excalibur ECS Implementation


