Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Capacitor has first-class support for Progressive Web Apps, making it easy to build an app that runs natively on iOS and Android, but also on the web as a mobile web app or "Progressive Web App."
## What is a Progressive Web App?​
Put simply, a Progressive Web App (PWA) is a web app that uses modern web capabilities to deliver an app-like experience to users. These apps are deployed to traditional web servers, are accessible through URLs, and can be indexed by search engines.
A Progressive Web App is, for all practical purposes, just another term for a website that has been optimized for mobile performance and that utilizes newly available Web APIs to deliver features that are similar to a traditional native app, such as push notifications and offline storage.
## Capacitor and Progressive Web Apps​
Capacitor has first-class support for Progressive Web Apps _and_ native apps. That means that Capacitor's bridge supports running in either a native context or in the web, with many plugins available _in both contexts_ with the exact same API and calling conventions.
This means you use `@capacitor/core` and Capacitor plugins as dependencies for both your native app _and_ your Progressive Web App, and Capacitor seamlessly calls web code when required and native code when available.
Additionally, Capacitor offers a number of utilities for querying the current platform to provide customized experiences when running natively or on the web.
## Adding Progressive Web App Support to your app​
Progressive Web Apps should have an App Manifest and a Service Worker.
### App Manifest​
First, you'll need an App Manifest file (manifest.json) that sits alongside your `index.html` file and provides metadata about your app, such as its name, theme colors, and icons. This information will be used when your app is installed on the home screen, for example.
### Service Worker​
Next, in order to send push notifications and store data offline, a Service Worker will enable your web app to proxy network requests and perform background tasks needed to process and sync data.
Service Workers are powerful, but complicated. Generally, writing them from scratch is not recommended. Instead, take a look at tools like Workbox that provide common Service Worker recipes that you can easily incorporate into your app.
Read more about using Service Workers, including how to register them, on the Using Service Workers page on MDN.
## Progressive Web App Performance​
Progressive Web Apps are judged by several performance standards, including Time to Interactive and First Meaningful Paint.
Follow the Progressive Web App Checklist before going live, and use Lighthouse to audit and test your app.
If you're struggling to meet Progressive Web App performance standards with your existing frontend stack, take a look at Ionic Framework as an option for getting fast PWA support with nearly zero configuration.
## Contents
  * What is a Progressive Web App?
  * Capacitor and Progressive Web Apps
  * Adding Progressive Web App Support to your app
    * App Manifest
    * Service Worker
  * Progressive Web App Performance


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fweb%2Fprogressive-web-apps&_biz_t=1739811944237&_biz_i=Building%20Progressive%20Web%20Apps%20%7C%20Capacitor%20Documentation&_biz_n=67&rnd=332501&cdn_o=a&_biz_z=1739811944237)
