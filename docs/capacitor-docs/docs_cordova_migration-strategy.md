Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Migrating from Cordova to Capacitor can occur over time or can be fully replaced in many cases. The effort involved will largely depend on the complexity of the app.
## Why Migrate?​
Long-term stability and peace of mind.
Capacitor is backed by Ionic, a long-term contributor to Cordova and the larger open source ecosystem. Ionic still uses Cordova heavily and will continue to invest in the platform for a long time to come.
It's backward-compatible with Cordova, so you can comfortably switch your existing web apps to it whenever you're ready. Capacitor was designed from the start to support the rich Cordova plugin ecosystem out of the box. Thus, using Cordova plugins in Capacitor is easy.
## Why Use Ionic Framework with Capacitor?​
Capacitor is the officially supported native runtime for Ionic Framework. Using Ionic and Capacitor together is the best way to build a great app experience, since Ionic Framework provides UI and UX enhancements that Capacitor does not have. Additionally, it works with your favorite web app framework, including Angular, React, and Vue.
With the release of Capacitor, Ionic now controls almost all of its technology stack. When you build an Ionic app today, we now control the native runtime layer (Capacitor), the UI controls (Ionic Framework), and the "framework" used to build the controls (web components powered by Stencil). This is significant: If there's an issue in any part of the stack that we control, we can fix it right away. The only part we don't control is the frontend framework you use on top (Angular, React, Vue, or plain JavaScript).
## Migration Process Overview​
### Utilize the Ionic VS Code Extension​
The Ionic VS Code Extension provides tools to help assist your migration from Cordova to Capacitor by installing Capacitor's dependencies, replacing equivalent plugins, and more. It is a helpful tool that will automate much of the process of moving to Capacitor.
### Audit Then Migrate Existing Cordova Plugins​
Begin by auditing your existing Cordova plugins. It's possible that you may be able to remove ones that are no longer needed.
Next, review all of Capacitor's official plugins as well as community plugins. You may be able to switch to the Capacitor-equivalent Cordova plugin.
Some plugins may not match functionality entirely, but based on the features you need that may not matter.
### Continue to Use Cordova if Needed​
To leverage Cordova plugins in your Capacitor app, see here. If a replacement plugin doesn't exist, continue to use the Cordova plugin as-is. If there's a plugin you'd like to see supported, open a plugin proposal!
Ready to migrate to Capacitor?
## Contents
  * Why Migrate?
  * Why Use Ionic Framework with Capacitor?
  * Migration Process Overview
    * Utilize the Ionic VS Code Extension
    * Audit Then Migrate Existing Cordova Plugins
    * Continue to Use Cordova if Needed


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fcordova%2Fmigration-strategy&_biz_t=1739811924688&_biz_i=Migrating%20Strategy%20%7C%20Capacitor%20Documentation&_biz_n=31&rnd=992350&cdn_o=a&_biz_z=1739811924688)
