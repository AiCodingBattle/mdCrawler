Menu
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Building Your ApplicationRoutingDynamic Routes
# Dynamic Routes
When you don't know the exact segment names ahead of time and want to create routes from dynamic data, you can use Dynamic Segments that are filled in at request time or prerendered at build time.
## Convention
A Dynamic Segment can be created by wrapping a file or folder name in square brackets: `[segmentName]`. For example, `[id]` or `[slug]`.
Dynamic Segments can be accessed from `useRouter`.
## Example
For example, a blog could include the following route `pages/blog/[slug].js` where `[slug]` is the Dynamic Segment for blog posts.
```
import { useRouter } from'next/router'
exportdefaultfunctionPage() {
constrouter=useRouter()
return <p>Post: {router.query.slug}</p>
}
```

Route| Example URL| `params`  
---|---|---  
`pages/blog/[slug].js`| `/blog/a`| `{ slug: 'a' }`  
`pages/blog/[slug].js`| `/blog/b`| `{ slug: 'b' }`  
`pages/blog/[slug].js`| `/blog/c`| `{ slug: 'c' }`  
## Catch-all Segments
Dynamic Segments can be extended to **catch-all** subsequent segments by adding an ellipsis inside the brackets `[...segmentName]`.
For example, `pages/shop/[...slug].js` will match `/shop/clothes`, but also `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`, and so on.
Route| Example URL| `params`  
---|---|---  
`pages/shop/[...slug].js`| `/shop/a`| `{ slug: ['a'] }`  
`pages/shop/[...slug].js`| `/shop/a/b`| `{ slug: ['a', 'b'] }`  
`pages/shop/[...slug].js`| `/shop/a/b/c`| `{ slug: ['a', 'b', 'c'] }`  
## Optional Catch-all Segments
Catch-all Segments can be made **optional** by including the parameter in double square brackets: `[[...segmentName]]`.
For example, `pages/shop/[[...slug]].js` will **also** match `/shop`, in addition to `/shop/clothes`, `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`.
The difference between **catch-all** and **optional catch-all** segments is that with optional, the route without the parameter is also matched (`/shop` in the example above).
Route| Example URL| `params`  
---|---|---  
`pages/shop/[[...slug]].js`| `/shop`| `{ slug: undefined }`  
`pages/shop/[[...slug]].js`| `/shop/a`| `{ slug: ['a'] }`  
`pages/shop/[[...slug]].js`| `/shop/a/b`| `{ slug: ['a', 'b'] }`  
`pages/shop/[[...slug]].js`| `/shop/a/b/c`| `{ slug: ['a', 'b', 'c'] }`  
## Next Steps
For more information on what to do next, we recommend the following sections
### Linking and Navigating
Learn how navigation works in Next.js, and how to use the Link Component and `useRouter` hook.
### useRouter
Learn more about the API of the Next.js Router, and access the router instance in your page with the useRouter hook.
Was this helpful?
supported.
Send
