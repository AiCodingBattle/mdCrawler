Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Below are a list of commonly asked Capacitor questions. If you don't find an answer here, check out our forum or our Discord. Check out the sidebar for a list of frequently asked questions 👉
## What platforms does Capacitor support?​
Capacitor can target virtually any device with our official and community platforms.
### Official Platforms​
Capacitor officially supports the following platforms:
  * iOS 13+
  * Android 5.1+ 
    * Requires Chrome WebView 60+
  * Modern Web Browsers 
    * Chrome
    * Firefox
    * Safari
    * Edge


### Community Platforms​
Capacitor also has community platforms to target cross platform desktop frameworks. The current community targets are the following.
  * Electron 
    * https://github.com/capacitor-community/electron
  * Tauri (alpha) 
    * https://github.com/capacitor-community/tauri


## Do I need to use Ionic Framework with Capacitor?​
No! You don't! Capacitor works with **any** web application, not just ones built with other Ionic tools. If you want a specific look and feel for your Capacitor app, and Ionic Framework isn't the right UI toolkit for you, you shouldn't feel forced to use it. There are plenty of apps in both app stores that utilize Capacitor and not Ionic Framework.
## Where can I find plugins for my Capacitor project?​
To find plugins for your project, you should check the following places in this order.
### Capacitor Community GitHub ⚡​
The Capacitor Community GitHub organization lists plugins that our excellent community of developers creates. They are Capacitor first plugins that are actively developed and should work in any Capacitor 3+ project. If you need a plugin, this should be one of the first places you look.
### Awesome Capacitor 😎​
Like many other Awesome lists, Awesome Capacitor is a community-curated list of great Capacitor plugins. If you can't find an official or community plugin, chances are that someone has already made the plugin you are looking for here.
### Project Fugu 🐡​
Project Fugu is the Chromium Team's tracker of web APIs that have been added to Chromium browsers. While some features may not be supported on both Android and iOS, features like Web Share and ContactsManager (Android Only), may replace `@capacitor/share` or `@capacitor-community/contacts` for your use case.
You can Can I Use...? to check if you can use these features on Android and iOS _without_ needing any native plugins.
### Cordova Plugins 🔌​
Did you know Capacitor supports Cordova plugins? If you are migrating off of Cordova, or have a Cordova plugin that doesn't have a Capacitor equivalent, you can use most Cordova plugins directly in Capacitor. You can read our guide on how to use Cordova plugins in Capacitor.
## Can I build iOS apps without a Mac with Capacitor?​
Short answer, no. The longer answer is that while you can use cloud services like Ionic AppFlow, you won't be able to test your application on a device or simulator. You should always be sure to test your application with a physical device to make sure that your Capacitor application is usable to people with Apple products.
## Why do I get a blank screen when running on an Android emulator?​
Capacitor requires Android 5.1 as well as a WebView version of 60 or higher. If you create an Android 6 or 7 emulator for example, the newest version of the WebView won't be installed, and you'll get a blank white screen. To get around this, you can install a newer Android emulator for testing your application.
## Why am I getting CocoaPods errors on my Apple Silicon Device?​
If you installed CocoaPods with `sudo gem install cocoapods` and you're using an Apple Silicon-powered Mac, you might encounter something like this when running `npx cap update`:
```
[error] Analyzing dependencies    /Library/Ruby/Gems/2.6.0/gems/ffi-1.15.3/lib/ffi/library.rb:275: [BUG] Bus Error at 0x0000000000000000    ruby 2.6.3p62 (2019-04-16 revision 67580) [universal.arm64e-darwin20]
```

This is a CocoaPods bug related to `ffi` not installing on Apple Silicon computers. We recommend using Homebrew to installl CocoaPods. Alternatively, if you have Rosetta installed, you can install `ffi` on a `x86_64` architecture and run `pod install` using the simulated Intel architecture for the first time.
```
$ sudo arch -x86_64 gem install ffi$ arch -x86_64 pod install
```

After that, running Capacitor should work as expected.
## Contents
  * What platforms does Capacitor support?
    * Official Platforms
    * Community Platforms
  * Do I need to use Ionic Framework with Capacitor?
  * Where can I find plugins for my Capacitor project?
    * Capacitor Community GitHub ⚡
    * Awesome Capacitor 😎
    * Project Fugu 🐡
    * Cordova Plugins 🔌
  * Can I build iOS apps without a Mac with Capacitor?
  * Why do I get a blank screen when running on an Android emulator?
  * Why am I getting CocoaPods errors on my Apple Silicon Device?


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fgetting-started%2Ffaqs&_biz_t=1739811914267&_biz_i=Frequently%20Asked%20Questions%20%7C%20Capacitor%20Documentation&_biz_n=14&rnd=571038&cdn_o=a&_biz_z=1739811914267)
