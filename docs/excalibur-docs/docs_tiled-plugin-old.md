Skip to main content
On this page
This extension adds support for tile maps from all Tiled map editor files in Excalibur. Use the `TiledMapResource` to load and interact with Tiled based maps!
## Features​
  * Parse default Tiled tmx files 
    * Supports all Tiled compressions zlib, gzip, and zstd
  * Parse Tiled exported json files
  * Supports external tilesets `.tsx` and `json`
  * New TypeScript based object model for working with Tiled data 
    * Query for layers by property
    * Query for objects by property
    * Easy helpers to locate Polygons, PolyLines, and Text
  * Automatic Excalibur wiring for certain Tiled properties and objects: 
    * Camera
    * Colliders
    * Solid TileMap Layers
    * Tiled Text
    * Inserted Tiled Tiles


## Quickstart​
Install using npm:
```

> npm install @excaliburjs/plugin-tiled
Copy
```
```

> npm install @excaliburjs/plugin-tiled
Copy
```

## ES2015 (TS/JS)​
The ES2015 `import` syntax is the recommended way to use Excalibur with Excalibur Tiled and is supported through a module loader like webpack or Parcel with TypeScript or Babel:
```

ts
import*as ex from'excalibur'
import { TiledMapResource } from'@excaliburjs/plugin-tiled'
// Create tiled map resource, pointing to static asset path
consttiledMap=newTiledMapResource('/assets/map.tmx')
// Create a loader and reference the map
constloader=new ex.Loader([tiledMap])
// Start the game (starts the loader)
game.start(loader).then(function () {
 console.log('Game loaded')
 tiledMap.addTiledMapToScene(game.currentScene)
})
Copy
```
```

ts
import*as ex from'excalibur'
import { TiledMapResource } from'@excaliburjs/plugin-tiled'
// Create tiled map resource, pointing to static asset path
consttiledMap=newTiledMapResource('/assets/map.tmx')
// Create a loader and reference the map
constloader=new ex.Loader([tiledMap])
// Start the game (starts the loader)
game.start(loader).then(function () {
 console.log('Game loaded')
 tiledMap.addTiledMapToScene(game.currentScene)
})
Copy
```

### Excalibur Wiring​
You may opt-in to the Excalibur wiring by calling `addTiledMapToScene(someScene)`
```

typescript
// After loading tiledMapResource
tiledMapResource.addTiledMapToScene(game.currentScene)
Copy
```
```

typescript
// After loading tiledMapResource
tiledMapResource.addTiledMapToScene(game.currentScene)
Copy
```

  * **Only object layers with`"excalibur"=true` are parsed for objects**. These object layers can be retrieved with
```

typescript
constobjects:TiledObjectGroup[] = tiledMapResource.getExcaliburObjects()
Copy
```
```

typescript
constobjects:TiledObjectGroup[] = tiledMapResource.getExcaliburObjects()
Copy
```

![object layer property menu in Tiled](https://github.com/excaliburjs/excalibur-tiled/raw/main/readme/excalibur-object.png)
  * **Camera Position & Zoom** - You may set the starting camera position and zoom
![Tiled Position Object as Camera](https://github.com/excaliburjs/excalibur-tiled/raw/main/readme/camera.png)
    * In an object layer with a custom property "excalibur"=true
    * **Note** Only the first Camera in the first "excalibur"=true layer will be used
    * Create a Tiled "Point" with the Tiled Type "Camera"
    * Optionally, to set zoom other than the default of 1.0, create a custom property named "Zoom" with a numeric value
  * **Solid layers** - You can mark a particular layers tiles as solid in Tiled
![Tiled Layer Marked Solid](https://github.com/excaliburjs/excalibur-tiled/blob/main/readme/solid.png)
    * In the Tiled layer properties, add a custom property named "Solid" with a boolean value `true`
    * The presence of a tile in this layer indicates that space is solid, the absence of a tile means it is not solid
  * **Colliders** - You may position Excalibur colliders within Tiled ![Tiled Object as BoxCollider](https://github.com/excaliburjs/excalibur-tiled/raw/main/readme/collider.png)
    * In an object layer with a custom property "excalibur"=true
    * Create a "Circle" (ellipses are not supported) or "Rectangle" 
      * Set the Tiled type to "BoxCollider" or "CircleCollider"
      * Optionally, to set an Excalibur collision type specify a custom property named "CollisionType" with the value 
        * "Fixed" (default for colliders) - non-movable object
        * "Passive" - triggers events, does not participate in collision
        * "Active" - participates in collision and can be pushed around
        * "PreventCollision" - all collisions are ignored
  * **Text** - You may insert excalibur labels within Tiled ![Tiled Text](https://github.com/excaliburjs/excalibur-tiled/raw/main/readme/text.png)
    * In an object layer with a custom property "excalibur"=true
    * Create a Tiled Text object
    * Optionally, you can set the "ZIndex" as a float custom tiled property
    * **⚠ A word of caution around fonts ⚠** - fonts are different on every operating system (some may not be available to your user unless you explicitly load them into the page with a font loader). See here for some detail
  * **Inserted Tile Objects** - You may insert tiles on or off grid in Tiled with inserted tiles ![Tiled inserted tiles](https://github.com/excaliburjs/excalibur-tiled/raw/main/readme/insertedtile.png)
    * In an object layer with a custom property "excalibur"=true
    * Create a Tiled inserted Tile
    * Optionally, you can set the "ZIndex" as a float custom tiled property
    * Optionally, to set an Excalibur collision type specify a custom property named "CollisionType" with the value 
      * "Fixed" non-movable object
      * "Passive" (default for inserted tiles) - triggers events, does not participate in collision
      * "Active" - participates in collision and can be pushed around
      * "PreventCollision" - all collisions are ignored


## Not Yet Supported Out of the Box​
  * Currently Isometric and Hexagonal maps are not directly supported by Excalibur TileMaps, however the data is still parsed by this plugin and can be used manually by accessing the `RawTiledMap` in `TiledMapResource.data.rawMap` after loading.
  * Excalibur Text is limited at the moment and doesn't support Tiled word wrapping or Tiled text alignment other than the default "Left" horizontal, "Top" vertical alignments.
  * Layer offsets are yet not supported.
  * Layer tinting is not yet supported
  * Parallax factor is not yet supported.
  * Image Layers - Tiled image layers are not yet fully supported, but do show up in the `RawTiledMap` so can be used that way. Using inserted Tile Objects is a way to achieve the same effect in a fully supported way.
  * Group Layers - Tiled group layers are not yet supported at all, currently layers in a group do not load. Maps with group layers will load all other layers fine.
  * Infinite maps - Tiled infinite maps are not yet supported, but do show up in the `RawTiledMap`.
  * `RawTiledMap` fully types the Tiled 1.4.3 api, this can be used to write custom code for anything this plugin doesn't yet support.

```

typescript
import*as ex from'excalibur'
import { TiledMapResource } from'@excaliburjs/plugin-tiled'
// Create tiled map resource, pointing to static asset path
consttiledMap=newTiledMapResource('/assets/map.tmx')
// Create a loader and reference the map
constloader=new ex.Loader([tiledMap])
game.start(loader).then(function () {
// Access raw data
constrawMap= tiledMap.data.rawMap
})
Copy
```
```

typescript
import*as ex from'excalibur'
import { TiledMapResource } from'@excaliburjs/plugin-tiled'
// Create tiled map resource, pointing to static asset path
consttiledMap=newTiledMapResource('/assets/map.tmx')
// Create a loader and reference the map
constloader=new ex.Loader([tiledMap])
game.start(loader).then(function () {
// Access raw data
constrawMap= tiledMap.data.rawMap
})
Copy
```

## Webpack Configuration​
You will need to modify your webpack configuration to load Tiled JSON files using `file-loader` and then ensure any TileMap images are copied to the same output directory as your bundle, see this example-ts-webpack branch for an example.
## Standalone Script File (JS)​
In your HTML file, add a reference **dist/excalibur-tiled.min.js** in your page:
```

html
<script
type="text/javascript"
src="node_modules/excalibur/dist/excalibur.min.js"
></script>
<script
type="text/javascript"
src="node_modules/@excaliburjs/excalibur-tiled/dist/excalibur-tiled.min.js"
></script>
Copy
```
```

html
<script
type="text/javascript"
src="node_modules/excalibur/dist/excalibur.min.js"
></script>
<script
type="text/javascript"
src="node_modules/@excaliburjs/excalibur-tiled/dist/excalibur-tiled.min.js"
></script>
Copy
```

and then you can use it like this:
```

js
// New game
constgame=new ex.Engine({ width: 500, height: 400, canvasElementId: 'game' })
// Create a new TiledMapResource loadable
consttiledMap=new ex.Plugin.Tiled.TiledMapResource('test.tmx')
// Create a loader and reference the map
constloader=new ex.Loader([tiledMap])
// Start the game (starts the loader)
game.start(loader).then(function () {
 console.log('Game loaded')
 tiledMap.addTiledMapToScene(game.currentScene)
})
Copy
```
```

js
// New game
constgame=new ex.Engine({ width: 500, height: 400, canvasElementId: 'game' })
// Create a new TiledMapResource loadable
consttiledMap=new ex.Plugin.Tiled.TiledMapResource('test.tmx')
// Create a loader and reference the map
constloader=new ex.Loader([tiledMap])
// Start the game (starts the loader)
game.start(loader).then(function () {
 console.log('Game loaded')
 tiledMap.addTiledMapToScene(game.currentScene)
})
Copy
```

The dist uses a UMD build and will attach itself to the `ex.Plugin.Tiled` global if running in the browser standalone.
  * Features
  * Quickstart
  * ES2015 (TS/JS)
    * Excalibur Wiring
  * Not Yet Supported Out of the Box
  * Webpack Configuration
  * Standalone Script File (JS)


