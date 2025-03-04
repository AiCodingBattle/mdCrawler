Skip to main content
A sprite is a view into a ImageSource and a projection into a final destination size.
```

typescript
constimage=new ex.ImageSource('./img/myimage.png')
// keep in mind this wont work until the raw image is loaded
constsprite=new ex.Sprite({
 image: image,
 sourceView: {
// Take a small slice of the source image starting at pixel (10, 10) with dimension 20 pixels x 20 pixels
  x: 10,
  y: 10,
  width: 20,
  height: 20,
 },
 destSize: {
// Optionally specify a different projected size, otherwise use the source
  width: 100,
  height: 100,
 },
})
Copy
```
```

typescript
constimage=new ex.ImageSource('./img/myimage.png')
// keep in mind this wont work until the raw image is loaded
constsprite=new ex.Sprite({
 image: image,
 sourceView: {
// Take a small slice of the source image starting at pixel (10, 10) with dimension 20 pixels x 20 pixels
  x: 10,
  y: 10,
  width: 20,
  height: 20,
 },
 destSize: {
// Optionally specify a different projected size, otherwise use the source
  width: 100,
  height: 100,
 },
})
Copy
```

Many times a sprite is the exact same view and size as the source raw image so there is a quick static helper to do this
```

typescript
constimage=new ex.ImageSource('./img/myimage.png')
// keep in mind this wont work until the image source is loaded
constsprite= image.toSprite()
Copy
```
```

typescript
constimage=new ex.ImageSource('./img/myimage.png')
// keep in mind this wont work until the image source is loaded
constsprite= image.toSprite()
Copy
```

