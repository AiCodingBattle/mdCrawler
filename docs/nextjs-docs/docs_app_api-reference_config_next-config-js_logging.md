Menu
Using App Router
Features available in /app
Using Latest Version
15.1.7
Using App Router
Features available in /app
Using Latest Version
15.1.7
Configurationnext.config.jslogging
# logging
## Options
### Fetching
You can configure the logging level and whether the full URL is logged to the console when running Next.js in development mode.
Currently, `logging` only applies to data fetching using the `fetch` API. It does not yet apply to other logs inside of Next.js.
next.config.js
```
module.exports= {
 logging: {
  fetches: {
   fullUrl:true,
  },
 },
}
```

Any `fetch` requests that are restored from the Server Components HMR cache are not logged by default. However, this can be enabled by setting `logging.fetches.hmrRefreshes` to `true`.
next.config.js
```
module.exports= {
 logging: {
  fetches: {
   hmrRefreshes:true,
  },
 },
}
```

### Incoming Requests
By default all the incoming requests will be logged in the console during development. You can use the `incomingRequests` option to decide which requests to ignore. Since this is only logged in development, this option doesn't affect production builds.
next.config.js
```
module.exports= {
 logging: {
  incomingRequests: {
   ignore: [/\api\/v1\/health/],
  },
 },
}
```

Or you can disable incoming request logging by setting `incomingRequests` to `false`.
next.config.js
```
module.exports= {
 logging: {
  incomingRequests:false,
 },
}
```

### Disabling Logging
In addition, you can disable the development logging by setting `logging` to `false`.
next.config.js
```
module.exports= {
 logging:false,
}
```

Was this helpful?
supported.
Send
