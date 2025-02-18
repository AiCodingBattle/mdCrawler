Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Swift Packages are Apple's new first-party tool for software dependencies. Traditionally Capacitor has used CocoaPods for managing dependencies internally and for plugins, however now is the time to move to a supported solution.
Since Capacitor 6, you can choose between using CocoaPods or Swift Package Manager (SPM). Almost all current capacitor-team supported plugins support SPM, namely the plugins in capacitor-plugins.
We've tried our best to make sure you don't have to change much about how you work with Capacitor to use SPM, but there are a few things to understand.
### How it works​
When a Capacitor project is using SPM we use a 'Base SPM' package that will serve as the place that references all of your projects dependencies:
![Base SPM Picture](https://capacitorjs.com/docs/assets/images/base-spm-7b9c60ba424f0ff6822cdbc416395de6.png)
The Capacitor CLI will modify the CapAPP-SPM package when you sync new plugins. It is important you do not touch the contents here because the CLI can and will change things.
### Using SPM in a new Capacitor project​
First we'll start with our normal `npm init @capacitor/app@latest`:
![Demo Step 1](https://capacitorjs.com/docs/assets/images/demo-step1-a5fe1b39eaa2c3ee519e83cd1badf68c.png)
Now we want to add the iOS platform to our project:
`npm install @capacitor/ios`
Next let's build the web project:
`npm run build`
After that is complete we can add the iOS project. We need to add the option `--packagemanager SPM` to the normal add command:
`npx cap add ios --packagemanager SPM`
Now you can use `npx cap open ios` to open the iOS project and run your app from there.
### Add and use a Capactior Plugin with SPM​
So let's add a plugin to this project and do something with that plugin.
Start with installing the Capacitor App plugin:
`npm install @capacitor/app`
Then let's sync the web app. This will add the App plugin SPM to the iOS project:
`npx cap sync`
You can now use the App plugin normally.
_More details coming soon_
### Converting existing plugins to SPM​
More details soon, but check this repository out: https://github.com/ionic-team/capacitor-plugin-converter
### Troubleshooting​
After adding plugins try to 'reset package caches' in Xcode:
![Demo Step 1](https://capacitorjs.com/docs/assets/images/reset-package-ce37ec73326432586d2e45b61841a96e.png)
## Contents
  * How it works
  * Using SPM in a new Capacitor project
  * Add and use a Capactior Plugin with SPM
  * Converting existing plugins to SPM
  * Troubleshooting


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fios%2Fspm&_biz_t=1739811940066&_biz_i=Swift%20Package%20Manager%20%7C%20Capacitor%20Documentation&_biz_n=59&rnd=758636&cdn_o=a&_biz_z=1739811940068)
