# Your Privacy
This site uses tracking technologies. You may opt in or opt out of the use of these technologies.
DenyAccept all
Consent Settings
Privacy Policy
Your Privacy
This site uses tracking technologies. You may opt in or opt out of the use of these technologies.
Marketing
Off
Marketing cookies and services are used to deliver personalized advertisements, promotions, and offers. These technologies enable targeted advertising and marketing campaigns by collecting information about users' interests, preferences, and online activities. 
Analytics
Off
Analytics cookies and services are used for collecting statistical information about how visitors interact with a website. These technologies provide insights into website usage, visitor behavior, and site performance to understand and improve the site and enhance user experience.
Functional
Off
Functional cookies and services are used to offer enhanced and personalized functionalities. These technologies provide additional features and improved user experiences, such as remembering your language preferences, font sizes, region selections, and customized layouts. Opting out of these cookies may render certain services or functionality of the website unavailable.
Essential
On
Essential cookies and services are used to enable core website features, such as ensuring the security of the website. 
SaveDenyAccept all
Privacy Policy
Menu
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Configurationnext.config.js OptionsexportPathMap
# exportPathMap
> This feature is exclusive to `next export` and currently **deprecated** in favor of `getStaticPaths` with `pages` or `generateStaticParams` with `app`.
`exportPathMap` allows you to specify a mapping of request paths to page destinations, to be used during export. Paths defined in `exportPathMap` will also be available when using `next dev`.
Let's start with an example, to create a custom `exportPathMap` for an app with the following pages:
  * `pages/index.js`
  * `pages/about.js`
  * `pages/post.js`


Open `next.config.js` and add the following `exportPathMap` config:
next.config.js
```
module.exports= {
exportPathMap:asyncfunction (
  defaultPathMap,
  { dev, dir, outDir, distDir, buildId }
 ) {
return {
'/': { page:'/' },
'/about': { page:'/about' },
'/p/hello-nextjs': { page:'/post', query: { title:'hello-nextjs' } },
'/p/learn-nextjs': { page:'/post', query: { title:'learn-nextjs' } },
'/p/deploy-nextjs': { page:'/post', query: { title:'deploy-nextjs' } },
  }
 },
}
```

> **Good to know** : the `query` field in `exportPathMap` cannot be used with automatically statically optimized pages or `getStaticProps` pages as they are rendered to HTML files at build-time and additional query information cannot be provided during `next export`.
The pages will then be exported as HTML files, for example, `/about` will become `/about.html`.
`exportPathMap` is an `async` function that receives 2 arguments: the first one is `defaultPathMap`, which is the default map used by Next.js. The second argument is an object with:
  * `dev` - `true` when `exportPathMap` is being called in development. `false` when running `next export`. In development `exportPathMap` is used to define routes.
  * `dir` - Absolute path to the project directory
  * `outDir` - Absolute path to the `out/` directory (configurable with `-o`). When `dev` is `true` the value of `outDir` will be `null`.
  * `distDir` - Absolute path to the `.next/` directory (configurable with the `distDir` config)
  * `buildId` - The generated build id


The returned object is a map of pages where the `key` is the `pathname` and the `value` is an object that accepts the following fields:
  * `page`: `String` - the page inside the `pages` directory to render
  * `query`: `Object` - the `query` object passed to `getInitialProps` when prerendering. Defaults to `{}`


> The exported `pathname` can also be a filename (for example, `/readme.md`), but you may need to set the `Content-Type` header to `text/html` when serving its content if it is different than `.html`.
## Adding a trailing slash
It is possible to configure Next.js to export pages as `index.html` files and require trailing slashes, `/about` becomes `/about/index.html` and is routable via `/about/`. This was the default behavior prior to Next.js 9.
To switch back and add a trailing slash, open `next.config.js` and enable the `trailingSlash` config:
next.config.js
```
module.exports= {
 trailingSlash:true,
}
```

## Customizing the output directory
`next export` will use `out` as the default output directory, you can customize this using the `-o` argument, like so:
Terminal
```
nextexport-ooutdir
```

> **Warning** : Using `exportPathMap` is deprecated and is overridden by `getStaticPaths` inside `pages`. We don't recommend using them together.
Was this helpful?
supported.
Send
