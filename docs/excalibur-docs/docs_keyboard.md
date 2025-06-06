Skip to main content
On this page
## Keyboard​
Keyboard input is accessible through engine.input.keyboard. You can inspect whether a button was just pressed or released this frame, or if the key is currently being held down. Common keys are held in the Keys enumeration but you can pass any character code to the methods.
Excalibur subscribes to the browser events and keeps track of what keys are currently held, released, or pressed. A key can be held for multiple frames, but a key cannot be pressed or released for more than one subsequent update frame.
### Inspecting the keyboard​
You can inspect engine.input.keyboard to see what the state of the keyboard is during an update.
It is recommended that keyboard actions that directly effect actors be queried, instead of subscribed to:
```

ts
classPlayerextendsex.Actor {
publicupdate(engine, delta) {
if (
   engine.input.keyboard.isHeld(ex.Keys.W) ||
   engine.input.keyboard.isHeld(ex.Keys.Up)
  ) {
   player._moveForward()
  }
if (engine.input.keyboard.wasPressed(ex.Keys.Right)) {
   player._fire()
  }
 }
}
Copy
```
```

ts
classPlayerextendsex.Actor {
publicupdate(engine, delta) {
if (
   engine.input.keyboard.isHeld(ex.Keys.W) ||
   engine.input.keyboard.isHeld(ex.Keys.Up)
  ) {
   player._moveForward()
  }
if (engine.input.keyboard.wasPressed(ex.Keys.Right)) {
   player._fire()
  }
 }
}
Copy
```

Checking whether keys are pressed or released during the update frame makes your game logic easier to follow and is less prone to tracking bugs since Excalibur tracks keyboard input on your behalf.
### Keyboard Events​
If you need more complex logic or if you need to be notified when input was processed, you can subscribe to keyboard events through `engine.input.keyboard.on`. A KeyEvent object is passed to your handler which offers information about the key that was part of the event.
  * `press` - When a key was just pressed this frame
  * `release` - When a key was just released this frame
  * `hold` - Whenever a key is in the down position

```

ts
engine.input.keyboard.on("press", (evt:KeyEvent) => {...});
engine.input.keyboard.on("release", (evt:KeyEvent) => {...});
engine.input.keyboard.on("hold", (evt:KeyEvent) => {...});
Copy
```
```

ts
engine.input.keyboard.on("press", (evt:KeyEvent) => {...});
engine.input.keyboard.on("release", (evt:KeyEvent) => {...});
engine.input.keyboard.on("hold", (evt:KeyEvent) => {...});
Copy
```

  * Keyboard
    * Inspecting the keyboard
    * Keyboard Events


