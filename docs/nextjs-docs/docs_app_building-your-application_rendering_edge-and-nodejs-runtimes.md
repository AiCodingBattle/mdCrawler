Menu
Using App Router
Features available in /app
Using Latest Version
15.2.0
Using App Router
Features available in /app
Using Latest Version
15.2.0
Building Your ApplicationRenderingRuntimes
# Runtimes
Next.js has two server runtimes you can use in your application:
  * The **Node.js Runtime** (default), which has access to all Node.js APIs and compatible packages from the ecosystem.
  * The **Edge Runtime** which contains a more limited set of APIs.


The Edge Runtime is the default runtime for Middleware. However, this can be changed to the Node.js runtime. See the Middleware documentation for more details.
## Use Cases
  * The Node.js Runtime is used for rendering your application.
  * The Edge Runtime is used for Middleware (routing rules like redirects, rewrites, and setting headers).


## Caveats
  * The Edge Runtime does not support all Node.js APIs. Some packages may not work as expected. Learn more about the unsupported APIs in the Edge Runtime.
  * The Edge Runtime does not support Incremental Static Regeneration (ISR).
  * Both runtimes can support streaming depending on your deployment infrastructure.


## Next Steps
View the Edge Runtime API reference.
### Edge Runtime
API Reference for the Edge Runtime.
Was this helpful?
supported.
Send
