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
Using App Router
Features available in /app
Using Latest Version
15.2.0
Using App Router
Features available in /app
Using Latest Version
15.2.0
Building Your ApplicationDeployingMulti-Zones
# Multi-Zones
Examples
  * With Zones


Multi-Zones are an approach to micro-frontends that separate a large application on a domain into smaller Next.js applications that each serve a set of paths. This is useful when there are collections of pages unrelated to the other pages in the application. By moving those pages to a separate zone (i.e., a separate application), you can reduce the size of each application which improves build times and removes code that is only necessary for one of the zones. Since applications are decoupled, Multi-Zones also allows other applications on the domain to use their own choice of framework.
For example, let's say you have the following set of pages that you would like to split up:
  * `/blog/*` for all blog posts
  * `/dashboard/*` for all pages when the user is logged-in to the dashboard
  * `/*` for the rest of your website not covered by other zones


With Multi-Zones support, you can create three applications that all are served on the same domain and look the same to the user, but you can develop and deploy each of the applications independently.
![Three zones: A, B, C. Showing a hard navigation between routes from different zones, and soft navigations between routes within the same zone.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fmulti-zones.png&w=3840&q=75)![Three zones: A, B, C. Showing a hard navigation between routes from different zones, and soft navigations between routes within the same zone.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fmulti-zones.png&w=3840&q=75)
Navigating between pages in the same zone will perform soft navigations, a navigation that does not require reloading the page. For example, in this diagram, navigating from `/` to `/products` will be a soft navigation.
Navigating from a page in one zone to a page in another zone, such as from `/` to `/dashboard`, will perform a hard navigation, unloading the resources of the current page and loading the resources of the new page. Pages that are frequently visited together should live in the same zone to avoid hard navigations.
## How to define a zone
A zone is a normal Next.js application where you also configure an assetPrefix to avoid conflicts with pages and static files in other zones.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 assetPrefix:'/blog-static',
}
```

Next.js assets, such as JavaScript and CSS, will be prefixed with `assetPrefix` to make sure that they don't conflict with assets from other zones. These assets will be served under `/assetPrefix/_next/...` for each of the zones.
The default application handling all paths not routed to another more specific zone does not need an `assetPrefix`.
In versions older than Next.js 15, you may also need an additional rewrite to handle the static assets. This is no longer necessary in Next.js 15.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 assetPrefix:'/blog-static',
asyncrewrites() {
return {
   beforeFiles: [
    {
     source:'/blog-static/_next/:path+',
     destination:'/_next/:path+',
    },
   ],
  }
 },
}
```

## How to route requests to the right zone
With the Multi Zones set-up, you need to route the paths to the correct zone since they are served by different applications. You can use any HTTP proxy to do this, but one of the Next.js applications can also be used to route requests for the entire domain.
To route to the correct zone using a Next.js application, you can use `rewrites`. For each path served by a different zone, you would add a rewrite rule to send that path to the domain of the other zone. For example:
next.config.js
```
async rewrites() {
return [
    {
      source:'/blog',
      destination:`${process.env.BLOG_DOMAIN}/blog`,
    },
    {
      source:'/blog/:path+',
      destination:`${process.env.BLOG_DOMAIN}/blog/:path+`,
    }
  ];
}
```

`destination` should be a URL that is served by the zone, including scheme and domain. This should point to the zone's production domain, but it can also be used to route requests to `localhost` in local development.
> **Good to know** : URL paths should be unique to a zone. For example, two zones trying to serve `/blog` would create a routing conflict.
### Routing requests using middleware
Routing requests through `rewrites` is recommended to minimize latency overhead for the requests, but middleware can also be used when there is a need for a dynamic decision when routing. For example, if you are using a feature flag to decide where a path should be routed such as during a migration, you can use middleware.
middleware.js
```
exportasyncfunctionmiddleware(request) {
const { pathname,search } =req.nextUrl;
if (pathname ==='/your-path'&&myFeatureFlag.isEnabled()) {
returnNextResponse.rewrite(`${rewriteDomain}${pathname}${search});
 }
}
```

## Linking between zones
Links to paths in a different zone should use an `a` tag instead of the Next.js `<Link>` component. This is because Next.js will try to prefetch and soft navigate to any relative path in `<Link>` component, which will not work across zones.
## Sharing code
The Next.js applications that make up the different zones can live in any repository. However, it is often convenient to put these zones in a monorepo to more easily share code. For zones that live in different repositories, code can also be shared using public or private NPM packages.
Since the pages in different zones may be released at different times, feature flags can be useful for enabling or disabling features in unison across the different zones.
For Next.js on Vercel applications, you can use a monorepo to deploy all affected zones with a single `git push`.
## Server Actions
When using Server Actions with Multi-Zones, you must explicitly allow the user-facing origin since your user facing domain may serve multiple applications. In your `next.config.js` file, add the following lines:
next.config.js
```
constnextConfig= {
 experimental: {
  serverActions: {
   allowedOrigins: ['your-production-domain.com'],
  },
 },
}
```

See `serverActions.allowedOrigins` for more information.
Was this helpful?
supported.
Send
