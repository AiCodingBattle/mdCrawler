Skip to main content
On this page
## Random​
You can instantiate the Random class with an optional seed number. You can reuse this seed anytime to get the exact sequence of random numbers back. If no seed is provided, it uses `Date.now()` ticks as the seed.
warning
Avoid creating multiple instances of `new ex.Random()`, if you create many in the same moment they will share the same `Date.now()` seed and will produce the same sequence of numbers.
It is recommended to create 1 instance of your seeded random and share it across your game.
```

ts
constrand=new ex.Random(1234)
// random integer between [min, max]
rand.integer(0, 10)
// random floating number between [min, max]
rand.floating(0, 10)
// random true or false
rand.bool()
// random true or false with 40% likelihood of being true
rand.bool(0.4)
// next floating point between [0, 1]
rand.next()
// next integer between 0 and Number.MAX_SAFE_INTEGER
rand.nextInt()
// pick a random element from an array
rand.pickOne([0, 1, 4, 10])
// pick a 2 random elements from an array
rand.pickSet([0, 1, 4, 10], 2)
// pick a 4 random elements from an array, allowing duplicates
rand.pickSet([0, 1, 4, 10], 4, true)
// generate an array of 9 random numbers between [min, max]
rand.range(9, 0, 10)
// randomly shuffle an array using Fisher/Yates algorithm
rand.shuffle([0, 1, 2, 3, 4])
// Multi-sided dice helpers
rand.d4()
rand.d6()
rand.d8()
rand.d10()
rand.d12()
rand.d20()
Copy
```
```

ts
constrand=new ex.Random(1234)
// random integer between [min, max]
rand.integer(0, 10)
// random floating number between [min, max]
rand.floating(0, 10)
// random true or false
rand.bool()
// random true or false with 40% likelihood of being true
rand.bool(0.4)
// next floating point between [0, 1]
rand.next()
// next integer between 0 and Number.MAX_SAFE_INTEGER
rand.nextInt()
// pick a random element from an array
rand.pickOne([0, 1, 4, 10])
// pick a 2 random elements from an array
rand.pickSet([0, 1, 4, 10], 2)
// pick a 4 random elements from an array, allowing duplicates
rand.pickSet([0, 1, 4, 10], 4, true)
// generate an array of 9 random numbers between [min, max]
rand.range(9, 0, 10)
// randomly shuffle an array using Fisher/Yates algorithm
rand.shuffle([0, 1, 2, 3, 4])
// Multi-sided dice helpers
rand.d4()
rand.d6()
rand.d8()
rand.d10()
rand.d12()
rand.d20()
Copy
```

A seeded random is very useful in games to do things like terrain generation, procedural content generation, etc. It allows you easily debug your algorithms by reusing the same seed, as well as to ensure your algorithms are deterministic.
  * Random


