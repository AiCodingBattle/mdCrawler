Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Compared to previous upgrades, the breaking changes between Capacitor 4 and 5 are extremely minimal. In this guide, you'll find steps to update your project to the current Capacitor 5 version as well as a list of breaking changes for our official plugins.
## NodeJS 16+​
Node 12 has reached end-of-life. Node 14 will reach end-of-life on April 30th, 2023. Capacitor 5 requires NodeJS 16 or greater. (Latest LTS version is recommended.)
## Using the CLI to Migrate​
Install the `latest-5` version of the Capacitor CLI to your project:
```
npm i -D @capacitor/cli@latest-5
```

Once installed, simply run the following to have the CLI handle the migration for you.
```
npx cap migrate
```

If any of the steps for the migration are not able to be completed, additional information will be made available in the output in the terminal. The steps for doing the migration manually are listed out below.
## Using the VS Code Extension to Migrate​
If you have the VS Code extension installed, simply check out the recomendations section of the extension to find the option to migrate your project to Capacitor 5.
## iOS​
The following guide describes how to upgrade your Capacitor 4 iOS project to Capacitor 5.
### Upgrade Xcode​
Capacitor 5 requires Xcode 14.1+.
### Update .gitignore​
Make the following changes to your `.gitignore` file:
```
- App/Podfile.lock+ App/output 
```

### Update Assets to use a single app icon​
Xcode 14 supports a single app icon of 1024x1024, so you can clean up your AppIcon.appiconset by removing all unnecessary sizes.
![Using Single Size App Icon](https://capacitorjs.com/docs/assets/images/single-app-icon-f75ca19915d642081c6915cb4b16a44b.png)
## Android​
The following guide describes how to upgrade your Capacitor 4 Android project to Capacitor 5.
### Upgrade Android Studio​
Capacitor 5 requires Android Studio Flamingo | 2022.2.1 or newer because of the usage of Gradle 8, that requires Java JDK 17. Java 17 ships with Android Studio Flamingo. No additional downloads needed!
Once it's updated, Android Studio can assist with some of the updates related to gradle and moving package into build files. To start, run `Tools -> AGP Upgrade Assistant`.
![APG Upgrade Assistant](https://capacitorjs.com/docs/assets/images/agp-upgrade-assistant-59a6aa5263bea07f9dd39eb8ed537743.png)
### Update Android Project Variables​
In your `variables.gradle` file, update your values to the following new minimums
```
minSdkVersion =22compileSdkVersion =33targetSdkVersion =33androidxActivityVersion ='1.7.0'androidxAppCompatVersion ='1.6.1'androidxCoordinatorLayoutVersion ='1.2.0'androidxCoreVersion ='1.10.0'androidxFragmentVersion ='1.5.6'coreSplashScreenVersion ='1.0.0'androidxWebkitVersion ='1.6.1'junitVersion ='4.13.2'androidxJunitVersion ='1.1.5'androidxEspressoCoreVersion ='3.5.1'cordovaAndroidVersion ='10.1.1'
```

### Update Google Services​
```
# build.gradle  dependencies {-    classpath 'com.google.gms:google-services:4.3.13'+    classpath 'com.google.gms:google-services:4.3.15'
```

### Update gradle plugin to 8.0.0​
```
# build.gradle  dependencies {-    classpath 'com.android.tools.build:gradle:7.2.1'+    classpath 'com.android.tools.build:gradle:8.0.0'
```

### Update gradle wrapper to 8.0.2​
```
# gradle-wrapper.propertiesdistributionBase=GRADLE_USER_HOMEdistributionPath=wrapper/dists- distributionUrl=https\://services.gradle.org/distributions/gradle-7.4.2-all.zip+ distributionUrl=https\://services.gradle.org/distributions/gradle-8.0.2-all.zipzipStoreBase=GRADLE_USER_HOMEzipStorePath=wrapper/dists
```

### Disable Jetifier​
If you don't have any plugin that still uses old android support libraries instead of their equivalent AndroidX libraries remove this line.
```
# gradle.properties# Android operating system, and which are packaged with your app's APK# https://developer.android.com/topic/libraries/support-library/androidx-rnandroid.useAndroidX=true- # Automatically convert third-party libraries to use AndroidX- android.enableJetifier=true
```

### Move package to `build.gradle`​
```
# AndroidManifest.xml<?xml version="1.0" encoding="utf-8"?>- <manifest xmlns:android="http://schemas.android.com/apk/res/android"-   package="[YOUR_PACKAGE_ID]">+ <manifest xmlns:android="http://schemas.android.com/apk/res/android">
```

```
# build.gradleandroid {+   namespace "[YOUR_PACKAGE_ID]"   compileSdkVersion rootProject.ext.compileSdkVersion
```

### Update androidScheme​
In Capacitor 6, `https` is going to be the default setting for `androidScheme` for **existing apps** to better enable Capacitor applications to make use of the system Autofill feature.
Changing the scheme is the equivalent to shipping your application on a different domain, which means any data stored in in cookies, localstorage, etc would no longer be accessible. To avoid data loss as a result of this change, in your Capacitor configuration file, you should set the scheme to `http` now even if it's the current default.
```
{ server:{  androidScheme:"http"}}
```

### Update kotlin version​
If your project is using kotlin, update the `kotlin_version` variable to `'1.8.20'`.
## Plugins​
The following plugin functionality has been modified or removed. Update your code accordingly.
### Action Sheet​
  * `androidxMaterialVersion` variable has been updated to `1.8.0`.


### Browser​
  * `androidxBrowserVersion` variable has been updated to `1.5.0`.


### Camera​
  * Android 13 requires to declare read media images permission (`<uses-permission android:name="android.permission.READ_MEDIA_IMAGES"/>`) in `AndroidManifest.xml`.
  * `androidxMaterialVersion` variable has been updated to `1.8.0`.
  * `androidxExifInterfaceVersion` variable has been updated to `1.3.6`.


### Device​
  * `DeviceId.uuid` changed to `DeviceId.identifier`
  * On iOS 16+, `DeviceInfo.name` will return a generic device name unless you add the appropriate entitlements.


### Geolocation​
  * `playServicesLocationVersion` has been updated to `21.0.1`.


### Google Maps​
  * `googleMapsPlayServicesVersion` has been updated to `18.1.0`.
  * `googleMapsUtilsVersion` has been updated to `3.4.0`.
  * `googleMapsKtxVersion` has been updated to `3.4.0`.
  * `googleMapsUtilsKtxVersion` has been updated to `3.4.0`.
  * `kotlinxCoroutinesVersion` has been updated to `1.6.4`.
  * `androidxCoreKTXVersion` has been updated to `1.10.0`.
  * `kotlin_version` has been updated to `1.8.20`.


### Local Notifications​
  * Android 13 requires a new runtime permission check in order to schedule local notifications. You are required to call `checkPermissions()` and `requestPermissions()` accordingly, when targeting SDK 33.


### Push Notifications​
  * Android 13 requires a new runtime permission check in order to receive push notifications. You are required to call `checkPermissions()` and `requestPermissions()` accordingly, when targeting SDK 33.
  * `firebaseMessagingVersion` variable has been updated to `23.1.2`.


### Status Bar​
  * On iOS, the default status bar animation has been changed to `FADE`.


## Contents
  * NodeJS 16+
  * Using the CLI to Migrate
  * Using the VS Code Extension to Migrate
  * iOS
    * Upgrade Xcode
    * Update .gitignore
    * Update Assets to use a single app icon
  * Android
    * Upgrade Android Studio
    * Update Android Project Variables
    * Update Google Services
    * Update gradle plugin to 8.0.0
    * Update gradle wrapper to 8.0.2
    * Disable Jetifier
    * Move package to `build.gradle`
    * Update androidScheme
    * Update kotlin version
  * Plugins
    * Action Sheet
    * Browser
    * Camera
    * Device
    * Geolocation
    * Google Maps
    * Local Notifications
    * Push Notifications
    * Status Bar


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=bfa08d03ffe94cbc8ad825d7c77fcc94&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fupdating%2F5-0&_biz_t=1739803063233&_biz_i=Capacitor%20Documentation&_biz_n=22&rnd=514114&cdn_o=a&_biz_z=1739803063233)
