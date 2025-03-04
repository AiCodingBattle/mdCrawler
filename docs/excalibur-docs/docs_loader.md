Skip to main content
On this page
## Why Resources​
When building games you may have assets you want to load from an external file, like sound, art, etc.
Resources, like ImageSource or Sound, must be loaded by calling `.load()` or by using a Loader before they can be used in your game.
## Creating Loader for Resources​
When calling Engine.start, you can optionally pass an asset Loader. This loader will contain a reference to any "loadables" you want to load.
```

ts
constloader=new ex.Loader([
/* add Loadables here */
]);
Copy
```
```

ts
constloader=new ex.Loader([
/* add Loadables here */
]);
Copy
```

Loadables are different kinds of assets such as image, sounds, and generic resources.
note
**Anytime** you call `game.start(loader)`, the game will pause and the engine will load assets. This means that you _do not have to load every asset at once_! Instead you may want to call `game.start(loader)` initially with core assets and then again when initializing a Scene.
## Generic Resources​
Sometimes you may have some other type of file you'd like to load, perhaps some data stored in a text file, json, or perhaps some binary data.
Excalibur supports a generic Resource to load arbitrary data.
```

const game = new Engine({...});
const text = new Resource<string>('./path/to/my/data.txt', 'text');
const json = new Resource<MyJsonShapeType>('./path/to/my/json.json', 'json');
const loader = new Loader([text, json]);
await game.start(loader);
console.log(text.data);
console.log(json.data);
Copy
```
```

const game = new Engine({...});
const text = new Resource<string>('./path/to/my/data.txt', 'text');
const json = new Resource<MyJsonShapeType>('./path/to/my/json.json', 'json');
const loader = new Loader([text, json]);
await game.start(loader);
console.log(text.data);
console.log(json.data);
Copy
```

## Other Resources​
  * Gif resource supports loading Gif's as animation, spritesheets, or sprites!
  * The Tiled plugin adds support for Tiled map type resources


## Using a web server​
The asset loader **only works with a web server** since it loads assets with XHR. That means you cannot use the loader when running an HTML file locally from the file-system (e.g. a `file://` protocol URL will not work). The browser throws errors that will prevent you from loading assets.
The fastest way to serve a folder of files is by using the serve NPM package.
```

bash
# Serve the current directory
npx serve .
# Serve a folder
npx serve ./dist
Copy
```
```

bash
# Serve the current directory
npx serve .
# Serve a folder
npx serve ./dist
Copy
```

If you are developing a game using Excalibur with Webpack, Parcel, or another bundler, these typically already come with dev servers for running your game. See Excalibur project templates for templates you can start from that use these tools.
### Relative vs. absolute paths​
Given this directory structure:
```

/root
 src/
  game.js
 assets/
  textures/
   map.png
 index.html
Copy
```
```

/root
 src/
  game.js
 assets/
  textures/
   map.png
 index.html
Copy
```

And you serve from the `root` directory like this:
```

> cd root
> npx serve .
Now serving on http://localhost:3000/
Copy
```
```

> cd root
> npx serve .
Now serving on http://localhost:3000/
Copy
```

The path to your assets doesn't matter as much because both absolute and relative paths will work:
  * `/assets/textures/map.png => HTTP 200 OK`
  * `assets/textures/map.png => HTTP 200 OK`


But if you are serving under a sub-directory, like `http://localhost:3000/root/index.html` then the format of your paths matter:
  * `/assets/textures/map.png => HTTP 404 Not Found`
  * `assets/textures/map.png => HTTP 200 OK`


The first path will fail to load as the absolute asset path would now be `/root/assets` and not `/assets`. Use a relative path to load assets _relative_ to the HTML file serving your game.
### Setting the base for a page​
In your HTML file(s), to set the base for any absolute paths like the example above, you can use the base tag:
```

html
<!DOCTYPEhtml>
<html>
 <head>
<!-- Set the base for all absolute URLs -->
  <basehref="/root" />
 </head>
 <body>
<!-- The browser will now properly resolve /root/game.js -->
  <scriptsrc="/game.js"></script>
 </body>
</html>
Copy
```
```

html
<!DOCTYPEhtml>
<html>
 <head>
<!-- Set the base for all absolute URLs -->
  <basehref="/root" />
 </head>
 <body>
<!-- The browser will now properly resolve /root/game.js -->
  <scriptsrc="/game.js"></script>
 </body>
</html>
Copy
```

This can be accessed programmatically using document.baseUri to resolve absolute paths in JavaScript.
This is a good approach to use when hosting your game at a sub-directory, such as publishing to GitHub Pages.
  * Why Resources
  * Creating Loader for Resources
  * Generic [[Resource|Resources]]
  * Other Resources
  * Using a web server
    * Relative vs. absolute paths
    * Setting the base for a page


