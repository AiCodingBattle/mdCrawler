Skip to main content
The line graphic object can be used to draw lines using Excalibur. The Actor GraphicsComponent centers graphics by default, so it might be desireable to set the anchor to (0, 0);
```

typescript
constlineActor=new ex.Actor({
 pos: ex.vec(100, 0),
})
lineActor.graphics.anchor = ex.Vector.Zero
lineActor.graphics.use(
new ex.Line({
  start: ex.vec(0, 0),
  end: ex.vec(200, 200),
  color: ex.Color.Green,
  thickness: 10,
 })
)
game.add(lineActor)
Copy
```
```

typescript
constlineActor=new ex.Actor({
 pos: ex.vec(100, 0),
})
lineActor.graphics.anchor = ex.Vector.Zero
lineActor.graphics.use(
new ex.Line({
  start: ex.vec(0, 0),
  end: ex.vec(200, 200),
  color: ex.Color.Green,
  thickness: 10,
 })
)
game.add(lineActor)
Copy
```

