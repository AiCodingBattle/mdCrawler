Skip to main content
An **OutSystems** Company →
Version: v7
On this page
There are several steps required to fully migrate a web app using Cordova over to Capacitor.
> It's recommended to work in a separate code branch when applying these changes.
## Add Capacitor​
Begin by opening your project in the terminal, then either follow the guides for adding Capacitor to a web app or adding Capacitor to an Ionic app.
Initialize your app with Capacitor. Some of the information you will be prompted for is available in the Cordova `config.xml` file:
  * The app name can be found within the `<name>` element.
  * The Bundle ID can be found in the `id` attribute of the root `<widget>` element.


```
npx cap init
```

### Build your Web App​
You must build your web project at least once before adding any native platforms.
```
npm run build
```

This ensures that the `www` folder that Capacitor has been automatically configured to use as the `webDir` in the Capacitor configuration file.
### Add Platforms​
Capacitor native platforms exist in their own top-level folders. Cordova's are located under `platforms/ios` or `platforms/android`.
```
npx cap add iosnpx cap add android
```

Both android and ios folders at the root of the project are created. These are entirely separate native project artifacts that should be considered part of your app (i.e., check them into source control, edit them in their own IDEs, etc.). Additionally, any Cordova plugins found under `dependencies` in `package.json` are automatically installed by Capacitor into each new native project (minus any incompatible ones):
```
"dependencies":{"@ionic-native/camera":"^5.3.0","@ionic-native/core":"^5.3.0","@ionic-native/file":"^5.3.0","cordova-android":"8.0.0","cordova-ios":"5.0.0","cordova-plugin-camera":"4.0.3","cordova-plugin-file":"6.0.1",}
```

## Splash Screens and Icons​
If you've previously created icon and splash screen images, they can be found in the top-level `resources` folder of your project. With those images in place, you can use the `@capacitor/assets` tool to generate icons and splash screens for Capacitor-based iOS and Android projects.
Run the following to regenerate the images and copy them into the native projects:
```
npx @capacitor/assets generate --iosnpx @capacitor/assets generate --android
```

Complete details here.
## Migrate Plugins​
Begin by auditing your existing Cordova plugins - it's possible that you may be able to remove ones that are no longer needed.
Next, review all of Capacitor's official plugins as well as community plugins. You may be able to switch to the Capacitor-equivalent Cordova plugin.
Some plugins may not match functionality entirely, but based on the features you need that may not matter.
Note that any plugins that are incompatible or cause build issues are automatically skipped.
### Remove Cordova Plugin​
After replacing a Cordova plugin with a Capacitor one (or simply removing it entirely), uninstall the plugin then run the `sync` command to remove the plugin code from a native project:
```
npm uninstall cordova-plugin-namenpx cap sync
```

## Set Permissions​
By default, the entire initial permissions requested for the latest version of Capacitor are set for you in the default native projects for both iOS and Android. However, you may need to apply additional permissions manually by mapping between `plugin.xml` and required settings on iOS and Android. Consult the iOS and Android configuration guides for info on how to configure each platform.
## Cordova Plugin preferences​
When `npx cap init` is run, Capacitor reads all the preferences in `config.xml` and ports them to the Capacitor configuration file. You can manually add more preferences to the `cordova.preferences` object.
```
{"cordova":{"preferences":{"DisableDeploy":"true","CameraUsesGeolocation":"true"}}}
```

## Additional Fields from `config.xml`​
You may be curious about how other elements from `config.xml` work in Capacitor apps.
The Author element can be configured in `package.json`, but is not used by Capacitor or within your app:
```
<authoremail="email@test.com"href="http://ionicframework.com/">Ionic Framework Team</author>
```

Most of the `allow-intent` values are either not used or there are configurable alternatives.
```
<allow-intenthref="http://*/*"/><allow-intenthref="https://*/*"/><allow-intenthref="tel:*"/><allow-intenthref="sms:*"/><allow-intenthref="mailto:*"/><allow-intenthref="geo:*"/>
```

iOS `edit-config` elements need to be configured in Info.plist.
```
<edit-configfile="*-Info.plist"mode="merge"target="NSCameraUsageDescription"><string>Used to take photos</string></edit-config>
```

It's impossible to cover every `config.xml` element available. However, most questions relating to "How do I configure X in Capacitor?" should be thought of as "How do I configure X in [platform] (iOS/Android)?" when searching online for answers.
## Setting Scheme​
When using Ionic with Cordova, your app uses `cordova-plugin-ionic-webview` by default, which on iOS uses `ionic://` scheme for serving the content. Capacitor apps use `capacitor://` as default scheme on iOS. This means that using a origin-binded Web API like LocalStorage, will result in a loss of data as the origin is different. This can be fixed by changing the scheme that is used for serving the content:
```
{"server":{"iosScheme":"ionic"}}
```

## Removing Cordova​
Once you've tested that all migration changes have been applied and the app is working well, Cordova can be removed from the project. Delete `config.xml` as well as the `platforms` and `plugins` folders. Note that you don't technically have to remove Cordova, since Capacitor works alongside it. In fact, if you plan to continue using Cordova plugins or think you may in the future, you can leave the Cordova assets where they are.
## Next Steps​
This is just the beginning of your Capacitor journey. Learn more about using Cordova plugins in a Capacitor project or more details on the Capacitor development workflow.
## Contents
  * Add Capacitor
    * Build your Web App
    * Add Platforms
  * Splash Screens and Icons
  * Migrate Plugins
    * Remove Cordova Plugin
  * Set Permissions
  * Cordova Plugin preferences
  * Additional Fields from `config.xml`
  * Setting Scheme
  * Removing Cordova
  * Next Steps


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fcordova%2Fmigrating-from-cordova-to-capacitor&_biz_t=1739811925224&_biz_i=Cordova%20to%20Capacitor%20Migration%20%7C%20Capacitor%20Documentation&_biz_n=32&rnd=172006&cdn_o=a&_biz_z=1739811925225)
