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
Configurationnext.config.jsstaticGeneration*
# staticGeneration*
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on GitHub.
The `staticGeneration*` options allow you to configure the Static Generation process for advanced use cases.
next.config.ts
TypeScript
JavaScriptTypeScript
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  staticGenerationRetryCount:1,
  staticGenerationMaxConcurrency:8,
  staticGenerationMinPagesPerWorker:25,
 },
}
exportdefault nextConfig
```

## Config Options
The following options are available:
  * `staticGenerationRetryCount`: The number of times to retry a failed page generation before failing the build.
  * `staticGenerationMaxConcurrency`: The maximum number of pages to be processed per worker.
  * `staticGenerationMinPagesPerWorker`: The minimum number of pages to be processed before starting a new worker.


Was this helpful?
supported.
Send
