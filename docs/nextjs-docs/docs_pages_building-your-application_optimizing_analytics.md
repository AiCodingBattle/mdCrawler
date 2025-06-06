Menu
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Building Your ApplicationOptimizingAnalytics
# Analytics
Next.js has built-in support for measuring and reporting performance metrics. You can either use the `useReportWebVitals` hook to manage reporting yourself, or alternatively, Vercel provides a managed service to automatically collect and visualize metrics for you.
## Build Your Own
pages/_app.js
```
import { useReportWebVitals } from'next/web-vitals'
functionMyApp({ Component, pageProps }) {
useReportWebVitals((metric) => {
console.log(metric)
 })
return <Component {...pageProps} />
}
```

View the API Reference for more information.
## Web Vitals
Web Vitals are a set of useful metrics that aim to capture the user experience of a web page. The following web vitals are all included:
  * Time to First Byte (TTFB)
  * First Contentful Paint (FCP)
  * Largest Contentful Paint (LCP)
  * First Input Delay (FID)
  * Cumulative Layout Shift (CLS)
  * Interaction to Next Paint (INP)


You can handle all the results of these metrics using the `name` property.
pages/_app.js
```
import { useReportWebVitals } from'next/web-vitals'
functionMyApp({ Component, pageProps }) {
useReportWebVitals((metric) => {
switch (metric.name) {
case'FCP': {
// handle FCP results
   }
case'LCP': {
// handle LCP results
   }
// ...
  }
 })
return <Component {...pageProps} />
}
```

## Custom Metrics
In addition to the core metrics listed above, there are some additional custom metrics that measure the time it takes for the page to hydrate and render:
  * `Next.js-hydration`: Length of time it takes for the page to start and finish hydrating (in ms)
  * `Next.js-route-change-to-render`: Length of time it takes for a page to start rendering after a route change (in ms)
  * `Next.js-render`: Length of time it takes for a page to finish render after a route change (in ms)


You can handle all the results of these metrics separately:
```
exportfunctionreportWebVitals(metric) {
switch (metric.name) {
case'Next.js-hydration':
// handle hydration results
break
case'Next.js-route-change-to-render':
// handle route-change to render results
break
case'Next.js-render':
// handle render results
break
default:
break
 }
}
```

These metrics work in all browsers that support the User Timing API.
## Sending results to external systems
You can send results to any endpoint to measure and track real user performance on your site. For example:
```
useReportWebVitals((metric) => {
constbody=JSON.stringify(metric)
consturl='https://example.com/analytics'
// Use `navigator.sendBeacon()` if available, falling back to `fetch()`.
if (navigator.sendBeacon) {
navigator.sendBeacon(url, body)
 } else {
fetch(url, { body, method:'POST', keepalive:true })
 }
})
```

> **Good to know** : If you use Google Analytics, using the `id` value can allow you to construct metric distributions manually (to calculate percentiles, etc.)
> ```
useReportWebVitals((metric) => {
// Use `window.gtag` if you initialized Google Analytics as this example:
// https://github.com/vercel/next.js/blob/canary/examples/with-google-analytics
window.gtag('event',metric.name, {
  value:Math.round(
metric.name ==='CLS'?metric.value *1000:metric.value
  ),// values must be integers
  event_label:metric.id,// id unique to current page load
  non_interaction:true,// avoids affecting bounce rate.
 })
})
```

> Read more about sending results to Google Analytics.
Was this helpful?
supported.
Send
