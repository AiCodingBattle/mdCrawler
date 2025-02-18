Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Every Capacitor developer is responsible for making sure their app is following security best practices. Without proper care, major security issues can crop up which can prove extremely damaging and expensive.
Security is a wide topic, but there are a number of areas that Capacitor developers should audit for security compliance, including Data, Authentication/Deep Linking, Network, and Web View security.
> Ionic provides an out of the box security suite for Capacitor apps that includes Authentication, Biometrics, and Encryption. Learn more.
## Data Security​
Data Security deals with the security of data stored locally and also in app code.
### Avoid Embedding Secrets in Code​
One of the most important security tips for Capacitor apps, and any frontend app for that matter, is to _never embed secrets_ in your app code. That means make sure your code never contains secret API keys, encryption keys, or any other sensitive data that could be easily stolen using basic app analysis techniques. Watch for environment variable plugins that could be injecting sensitive values into your app code at build time.
Instead, move most operations requiring secret keys or tokens to the server-side, where they can be protected and any requests can be forwarded from the server. This might be a serverless function or a traditional server-side app process.
For apps that must work with persisted sensitive keys or tokens on the client, such as an auth token or an encryption key, the recommended options are to only deal with the value in memory (i.e. never persist it to disk), or by using secure keychain/keystore techniques as detailed below.
### Storing Encryption Keys, Session Tokens, etc.​
Modern mobile devices and operating systems provide powerful security APIs and dedicated security hardware for storing sensitive values on device. This is how apps provide biometric or secure passcode authentication while managing highly sensitive values such as encryption keys or session tokens.
The APIs that provide this functionality are available in the iOS Keychain Services and Android Keystore APIs. These APIs are complex and low-level, so you will likely want to find a plugin that uses them for you (such as this cordova-plugin-ios-keychain community plugin).
For enterprise use cases, the Capacitor team provides Identity Vault which provides an easy-to-use API and frequently updated experience on top of these native security APIs. Identity Vault can be used with other Capacitor enterprise products such as Offline Storage and Auth Connect to provide the encryption key or authentication token management component of each experience, respectively.
## Authentication and Deep Linking​
Authentication flows in native apps require extra care, since authentication often happens through the use of Custom URL Schemes. Custom URL Schemes, such as `instagram://`, are not globally controlled like web domains are, so it's possible that a malicious app could intercept a request meant for one app by defining and overriding a custom URL scheme. Imagine a secure token being sent to the wrong app!
Generally, an app should never send sensitive data through a Custom URL scheme deep link (newer techniques such as Universal Links are more secure as they rely on actual web domain ownership, see the Deep Links guide for details).
This is especially important for oAuth2 flows, where the last step in the authentication experience relies on a deep link back to the app. To mitigate the possibility of a malicious app receiving a token, PKCE must be used for oAuth2 in Capacitor apps.
To ensure your oAuth2 flow is secure, make sure your plugin supports PKCE. For enterprise use cases, the official Auth Connect Capacitor solution fully supports PKCE for oAuth2 authentication flows.
See this great oAuth2 Best Practices for Native Apps guide for more info.
## Network Security​
Network security deals with making sure network requests are to trusted endpoints and encrypted to avoid sending sensitive data (such as passwords) in plain text.
### SSL​
Apps should only make requests to SSL-enabled endpoints. This means never make request to endpoints with `http://`, but rather always use `https://`. This makes sure data is never sent in plain text.
## Web View Security​
### Content Security Policy​
Content Security Policy (CSP) is a set of security features available in the browser (and, thus, your Capacitor Web View). CSP can be used to limit the resources the user agent is allowed to load in the Web View (such as images, XHR, videos, Web Sockets, etc).
CSP can be configured in your Capacitor app by adding a `meta` tag to the `<head>` with an acceptable CSP format (CSP can be configured both server and client side using the same format). For example, this configuration would allow all requests to the current origin and `foo.com`:
```
<metahttp-equiv="Content-Security-Policy"content="default-src 'self' foo.com"/>
```

CSP supports a wide variety of configurations, and the CSP reference is a must-read. Another useful resource is content-security-policy.com.
### JavaScript Security Techniques​
Since the bulk of a Capacitor app is a web app using JavaScript, typical JS security techniques apply.
JS security is beyond the scope of this document, and there are many existing resources out there for proper JS and web app security techniques. Here's one good one to get you started.
## Contents
  * Data Security
    * Avoid Embedding Secrets in Code
    * Storing Encryption Keys, Session Tokens, etc.
  * Authentication and Deep Linking
  * Network Security
    * SSL
  * Web View Security
    * Content Security Policy
    * JavaScript Security Techniques


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fguides%2Fsecurity&_biz_t=1739811934387&_biz_i=Security%20%7C%20Capacitor%20Documentation&_biz_n=48&rnd=355403&cdn_o=a&_biz_z=1739811934388)
