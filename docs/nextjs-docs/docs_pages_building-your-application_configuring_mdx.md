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
Building Your ApplicationConfiguringMDX
# Markdown and MDX
Markdown is a lightweight markup language used to format text. It allows you to write using plain text syntax and convert it to structurally valid HTML. It's commonly used for writing content on websites and blogs.
You write...
```
I **love** using [Next.js](https://nextjs.org/)
```

Output:
```
<p>I <strong>love</strong> using <ahref="https://nextjs.org/">Next.js</a></p>
```

MDX is a superset of markdown that lets you write JSX directly in your markdown files. It is a powerful way to add dynamic interactivity and embed React components within your content.
Next.js can support both local MDX content inside your application, as well as remote MDX files fetched dynamically on the server. The Next.js plugin handles transforming markdown and React components into HTML, including support for usage in Server Components (the default in App Router).
> **Good to know** : View the Portfolio Starter Kit template for a complete working example.
## Install dependencies
The `@next/mdx` package, and related packages, are used to configure Next.js so it can process markdown and MDX. **It sources data from local files** , allowing you to create pages with a `.md` or `.mdx` extension, directly in your `/pages` or `/app` directory.
Install these packages to render MDX with Next.js:
Terminal
```
npminstall@next/mdx@mdx-js/loader@mdx-js/react@types/mdx
```

## Configure `next.config.mjs`
Update the `next.config.mjs` file at your project's root to configure it to use MDX:
next.config.mjs
```
import createMDX from'@next/mdx'
/** @type{import('next').NextConfig} */
constnextConfig= {
// Configure `pageExtensions` to include markdown and MDX files
 pageExtensions: ['js','jsx','md','mdx','ts','tsx'],
// Optionally, add any other Next.js config below
}
constwithMDX=createMDX({
// Add markdown plugins here, as desired
})
// Merge MDX config with Next.js config
exportdefaultwithMDX(nextConfig)
```

This allows `.md` and `.mdx` files to act as pages, routes, or imports in your application.
## Add an `mdx-components.tsx` file
Create an `mdx-components.tsx` (or `.js`) file in the root of your project to define global MDX Components. For example, at the same level as `pages` or `app`, or inside `src` if applicable.
mdx-components.tsx
TypeScript
JavaScriptTypeScript
```
importtype { MDXComponents } from'mdx/types'
exportfunctionuseMDXComponents(components:MDXComponents):MDXComponents {
return {
...components,
 }
}
```

> **Good to know** :
>   * `mdx-components.tsx` is **required** to use `@next/mdx` with App Router and will not work without it.
>   * Learn more about the `mdx-components.tsx` file convention.
>   * Learn how to use custom styles and components.
> 

## Rendering MDX
You can render MDX using Next.js's file based routing or by importing MDX files into other pages.
### Using file based routing
When using file based routing, you can use MDX pages like any other page.
Create a new MDX page within the `/pages` directory:
```
 my-project
 |── mdx-components.(tsx/js)
 ├── pages
 │  └── mdx-page.(mdx/md)
 └── package.json
```

You can use MDX in these files, and even import React components, directly inside your MDX page:
```
import { MyComponent } from'my-component'
# Welcome to my MDX page!
This is some **bold** and _italics_ text.
This is a list in markdown:
- One
- Two
- Three
Checkout my React component:
<MyComponent />
```

Navigating to the `/mdx-page` route should display your rendered MDX page.
### Using imports
Create a new page within the `/pages` directory and an MDX file wherever you'd like:
```
 my-project
 ├── pages
 │  └── mdx-page.(tsx/js)
 ├── markdown
 │  └── welcome.(mdx/md)
 |── mdx-components.(tsx/js)
 └── package.json
```

You can use MDX in these files, and even import React components, directly inside your MDX page:
Import the MDX file inside the page to display the content:
pages/mdx-page.tsx
TypeScript
JavaScriptTypeScript
```
import Welcome from'@/markdown/welcome.mdx'
exportdefaultfunctionPage() {
return <Welcome />
}
```

Navigating to the `/mdx-page` route should display your rendered MDX page.
## Using custom styles and components
Markdown, when rendered, maps to native HTML elements. For example, writing the following markdown:
```
## This is a heading
This is a list in markdown:
- One
- Two
- Three
```

Generates the following HTML:
```
<h2>This is a heading</h2>
<p>This is a list in markdown:</p>
<ul>
 <li>One</li>
 <li>Two</li>
 <li>Three</li>
</ul>
```

To style your markdown, you can provide custom components that map to the generated HTML elements. Styles and components can be implemented globally, locally, and with shared layouts.
### Global styles and components
Adding styles and components in `mdx-components.tsx` will affect _all_ MDX files in your application.
mdx-components.tsx
TypeScript
JavaScriptTypeScript
```
importtype { MDXComponents } from'mdx/types'
import Image, { ImageProps } from'next/image'
// This file allows you to provide custom React components
// to be used in MDX files. You can import and use any
// React component you want, including inline styles,
// components from other libraries, and more.
exportfunctionuseMDXComponents(components:MDXComponents):MDXComponents {
return {
// Allows customizing built-in components, e.g. to add styling.
h1: ({ children }) => (
   <h1style={{ color:'red', fontSize:'48px' }}>{children}</h1>
  ),
img: (props) => (
   <Image
sizes="100vw"
style={{ width:'100%', height:'auto' }}
    {...(props asImageProps)}
   />
  ),
...components,
 }
}
```

### Local styles and components
You can apply local styles and components to specific pages by passing them into imported MDX components. These will merge with and override global styles and components.
pages/mdx-page.tsx
TypeScript
JavaScriptTypeScript
```
import Welcome from'@/markdown/welcome.mdx'
functionCustomH1({ children }) {
return <h1style={{ color:'blue', fontSize:'100px' }}>{children}</h1>
}
constoverrideComponents= {
 h1: CustomH1,
}
exportdefaultfunctionPage() {
return <Welcomecomponents={overrideComponents} />
}
```

### Shared layouts
To share a layout around MDX pages, create a layout component:
components/mdx-layout.tsx
TypeScript
JavaScriptTypeScript
```
exportdefaultfunctionMdxLayout({ children }: { children:React.ReactNode }) {
// Create any shared layout or styles here
return <divstyle={{ color:'blue' }}>{children}</div>
}
```

Then, import the layout component into the MDX page, wrap the MDX content in the layout, and export it:
```
import MdxLayout from'../components/mdx-layout'
# Welcome to my MDX page!
exportdefaultfunctionMDXPage({ children }) {
return <MdxLayout>{children}</MdxLayout>
}
```

### Using Tailwind typography plugin
If you are using Tailwind to style your application, using the `@tailwindcss/typography` plugin will allow you to reuse your Tailwind configuration and styles in your markdown files.
The plugin adds a set of `prose` classes that can be used to add typographic styles to content blocks that come from sources, like markdown.
Install Tailwind typography and use with shared layouts to add the `prose` you want.
To share a layout around MDX pages, create a layout component:
components/mdx-layout.tsx
TypeScript
JavaScriptTypeScript
```
exportdefaultfunctionMdxLayout({ children }: { children:React.ReactNode }) {
// Create any shared layout or styles here
return (
  <divclassName="prose prose-headings:mt-8 prose-headings:font-semibold prose-headings:text-black prose-h1:text-5xl prose-h2:text-4xl prose-h3:text-3xl prose-h4:text-2xl prose-h5:text-xl prose-h6:text-lg dark:prose-headings:text-white">
   {children}
  </div>
 )
}
```

Then, import the layout component into the MDX page, wrap the MDX content in the layout, and export it:
```
import MdxLayout from'../components/mdx-layout'
# Welcome to my MDX page!
exportdefaultfunctionMDXPage({ children }) {
return <MdxLayout>{children}</MdxLayout>
}
```

## Frontmatter
Frontmatter is a YAML like key/value pairing that can be used to store data about a page. `@next/mdx` does **not** support frontmatter by default, though there are many solutions for adding frontmatter to your MDX content, such as:
  * remark-frontmatter
  * remark-mdx-frontmatter
  * gray-matter


`@next/mdx` **does** allow you to use exports like any other JavaScript component:
Metadata can now be referenced outside of the MDX file:
pages/blog.tsx
TypeScript
JavaScriptTypeScript
```
import BlogPost, { metadata } from'@/content/blog-post.mdx'
exportdefaultfunctionPage() {
console.log('metadata: ', metadata)
//=> { author: 'John Doe' }
return <BlogPost />
}
```

A common use case for this is when you want to iterate over a collection of MDX and extract data. For example, creating a blog index page from all blog posts. You can use packages like Node's `fs` module or globby to read a directory of posts and extract the metadata.
> **Good to know** :
>   * Using `fs`, `globby`, etc. can only be used server-side.
>   * View the Portfolio Starter Kit template for a complete working example.
> 

## remark and rehype Plugins
You can optionally provide remark and rehype plugins to transform the MDX content.
For example, you can use `remark-gfm` to support GitHub Flavored Markdown.
Since the remark and rehype ecosystem is ESM only, you'll need to use `next.config.mjs` or `next.config.ts` as the configuration file.
next.config.mjs
```
import remarkGfm from'remark-gfm'
import createMDX from'@next/mdx'
/** @type{import('next').NextConfig} */
constnextConfig= {
// Allow .mdx extensions for files
 pageExtensions: ['js','jsx','md','mdx','ts','tsx'],
// Optionally, add any other Next.js config below
}
constwithMDX=createMDX({
// Add markdown plugins here, as desired
 options: {
  remarkPlugins: [remarkGfm],
  rehypePlugins: [],
 },
})
// Combine MDX and Next.js config
exportdefaultwithMDX(nextConfig)
```

### Using Plugins with Turbopack
To use plugins with Turbopack, upgrade to the latest `@next/mdx` and specify plugin names using a string:
next.config.mjs
```
import createMDX from'@next/mdx'
/** @type{import('next').NextConfig} */
constnextConfig= {
 pageExtensions: ['js','jsx','md','mdx','ts','tsx'],
}
constwithMDX=createMDX({
 options: {
  remarkPlugins: [],
  rehypePlugins: [['rehype-katex', { strict:true, throwOnError:true }]],
 },
})
exportdefaultwithMDX(nextConfig)
```

> **Good to know** :
> remark and rehype plugins without serializable options cannot be used yet with Turbopack, due to inability to pass JavaScript functions to Rust
## Remote MDX
If your MDX files or content lives _somewhere else_ , you can fetch it dynamically on the server. This is useful for content stored in a CMS, database, or anywhere else. A popular community package for this use is `next-mdx-remote`.
> **Good to know** : Please proceed with caution. MDX compiles to JavaScript and is executed on the server. You should only fetch MDX content from a trusted source, otherwise this can lead to remote code execution (RCE).
The following example uses `next-mdx-remote`:
pages/mdx-page-remote.tsx
TypeScript
JavaScriptTypeScript
```
import { serialize } from'next-mdx-remote/serialize'
import { MDXRemote, MDXRemoteSerializeResult } from'next-mdx-remote'
interfaceProps {
 mdxSource:MDXRemoteSerializeResult
}
exportdefaultfunctionRemoteMdxPage({ mdxSource }:Props) {
return <MDXRemote {...mdxSource} />
}
exportasyncfunctiongetStaticProps() {
// MDX text - can be from a database, CMS, fetch, anywhere...
constres=awaitfetch('https:...')
constmdxText=awaitres.text()
constmdxSource=awaitserialize(mdxText)
return { props: { mdxSource } }
}
```

Navigating to the `/mdx-page-remote` route should display your rendered MDX.
## Deep Dive: How do you transform markdown into HTML?
React does not natively understand markdown. The markdown plaintext needs to first be transformed into HTML. This can be accomplished with `remark` and `rehype`.
`remark` is an ecosystem of tools around markdown. `rehype` is the same, but for HTML. For example, the following code snippet transforms markdown into HTML:
```
import { unified } from'unified'
import remarkParse from'remark-parse'
import remarkRehype from'remark-rehype'
import rehypeSanitize from'rehype-sanitize'
import rehypeStringify from'rehype-stringify'
main()
asyncfunctionmain() {
constfile=awaitunified()
.use(remarkParse) // Convert into markdown AST
.use(remarkRehype) // Transform to HTML AST
.use(rehypeSanitize) // Sanitize HTML input
.use(rehypeStringify) // Convert AST into serialized HTML
.process('Hello, Next.js!')
console.log(String(file)) // <p>Hello, Next.js!</p>
}
```

The `remark` and `rehype` ecosystem contains plugins for syntax highlighting, linking headings, generating a table of contents, and more.
When using `@next/mdx` as shown above, you **do not** need to use `remark` or `rehype` directly, as it is handled for you. We're describing it here for a deeper understanding of what the `@next/mdx` package is doing underneath.
## Using the Rust-based MDX compiler (experimental)
Next.js supports a new MDX compiler written in Rust. This compiler is still experimental and is not recommended for production use. To use the new compiler, you need to configure `next.config.js` when you pass it to `withMDX`:
next.config.js
```
module.exports=withMDX({
 experimental: {
  mdxRs:true,
 },
})
```

`mdxRs` also accepts an object to configure how to transform mdx files.
next.config.js
```
module.exports=withMDX({
 experimental: {
  mdxRs: {
   jsxRuntime?: string      // Custom jsx runtime
   jsxImportSource?: string    // Custom jsx import source,
   mdxType?:'gfm'|'commonmark'// Configure what kind of mdx syntax will be used to parse & transform
  },
 },
})
```

## Helpful Links
  * MDX
  * `@next/mdx`
  * remark
  * rehype
  * Markdoc


Was this helpful?
supported.
Send
