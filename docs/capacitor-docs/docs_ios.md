Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Capacitor features a native iOS runtime that enables developers to communicate between JavaScript and Native Swift or Objective-C code.
Capacitor iOS apps are configured and managed with Xcode and CocoaPods.
## iOS Support​
iOS 14+ is supported. Xcode 16.0+ is required (see Environment Setup). Capacitor uses WKWebView, not the deprecated UIWebView.
## Adding the iOS Platform​
First, install the `@capacitor/ios` package.
```
npminstall @capacitor/ios
```

Then, add the iOS platform.
```
npx cap add ios
```

## Opening the iOS Project​
To open the project in Xcode, run:
```
npx cap open ios
```

Alternatively, you can open Xcode manually by running:
```
open ios/App/App.xcworkspace
```

## Running Your App​
You can either run your app on the command-line or with Xcode.
### Running on the Command-Line​
To run the project on a device or simulator, run:
```
npx cap run ios
```

The command will prompt you to select a target. Learn more about `run`.
### Running in Xcode​
In Xcode, first select the device or simulator and then click the play button to run your app.
![Running your app](https://capacitorjs.com/docs/assets/images/running-73a1e8445eed0b82f25162277223276e.png)
## Troubleshooting​
If you encountered any issues while getting started, you can consult the iOS Troubleshooting Guide. Feel free to open a discussion if you need help.
## Next steps​
You are now ready to continue developing and building your app. Use the various APIs available, Capacitor or Cordova plugins, or custom native code to build out the rest of your app.
## Further Reading​
Follow these guides for more information on each topic:
Configuring and setting permissions for iOS ›
Building Native Plugins for iOS ›
## Contents
  * iOS Support
  * Adding the iOS Platform
  * Opening the iOS Project
  * Running Your App
    * Running on the Command-Line
    * Running in Xcode
  * Troubleshooting
  * Next steps
  * Further Reading


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fios&_biz_t=1739811936281&_biz_i=Getting%20Started%20%7C%20Capacitor%20Documentation&_biz_n=52&rnd=820109&cdn_o=a&_biz_z=1739811936282)
