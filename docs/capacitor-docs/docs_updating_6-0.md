Skip to main content
An **OutSystems** Company →
Version: v7
On this page
The breaking changes between Capacitor 5 and 6 are designed to be extremely minimal. In this guide, you'll find steps to update your project to the current Capacitor 6 version as well as a list of breaking changes for our official plugins.
## NodeJS 18+​
Node 16 has reached end-of-life as of September 11th, 2023. Capacitor 6 requires NodeJS 18 or greater. (Latest LTS version is recommended.)
## Using the CLI to Migrate​
Install the `latest` version of the Capacitor CLI to your project:
```
npm i -D @capacitor/cli@latest
```

Once installed, simply run the following to have the CLI handle the migration for you.
```
npx cap migrate
```

If any of the steps for the migration are not able to be completed, additional information will be made available in the output in the terminal. The steps for doing the migration manually are listed out below.
## Using the VS Code Extension to Migrate​
If you have the VS Code extension installed, simply check out the recomendations section of the extension to find the option to migrate your project to Capacitor 6.
## iOS​
The following guide describes how to upgrade your Capacitor 5 iOS project to Capacitor 6.
### Upgrade Xcode​
Capacitor 6 requires Xcode 15.0+.
### SPM Support​
Converting from using Cocoapods to SPM is a pretty large topic we will cover in a different article, coming soon.
### Register custom plugins​
In Capacitor 6, plugin classes are no longer automatically registered. For npm installed plugins, the CLI will generate a list of plugin classes to register them programmatically. But users following the custom code guide for creating local plugins not distributed through npm, they will have to create a custom view controller and register their plugins.
### Zooming​
To match Android behavior, iOS apps are no longer zoomable by default. To enable zooming, check `zoomEnabled` configuration option
## Android​
The following guide describes how to upgrade your Capacitor 5 Android project to Capacitor 6.
### Upgrade Android Studio​
Capacitor 6 requires Android Studio Hedgehog | 2023.1.1 or newer because of the usage of Gradle 8.2.
Once it's updated, Android Studio can assist with some of the updates related to gradle and moving package into build files. To start, run `Tools -> AGP Upgrade Assistant`.
![APG Upgrade Assistant](https://capacitorjs.com/docs/assets/images/agp-upgrade-assistant-59a6aa5263bea07f9dd39eb8ed537743.png)
### Update Android Project Variables​
In your `variables.gradle` file, update your values to the following new minimums
```
minSdkVersion =22compileSdkVersion =34targetSdkVersion =34androidxActivityVersion ='1.8.0'androidxAppCompatVersion ='1.6.1'androidxCoordinatorLayoutVersion ='1.2.0'androidxCoreVersion ='1.12.0'androidxFragmentVersion ='1.6.2'coreSplashScreenVersion ='1.0.1'androidxWebkitVersion ='1.9.0'junitVersion ='4.13.2'androidxJunitVersion ='1.1.5'androidxEspressoCoreVersion ='3.5.1'cordovaAndroidVersion ='10.1.1'
```

### Update google services plugin​
```
# build.gradle  dependencies {    classpath 'com.android.tools.build:gradle:8.0.0'-    classpath 'com.google.gms:google-services:4.3.15'+    classpath 'com.google.gms:google-services:4.4.0'
```

### Update gradle plugin to 8.2.1​
```
# build.gradle  dependencies {-    classpath 'com.android.tools.build:gradle:8.0.0'+    classpath 'com.android.tools.build:gradle:8.2.1'
```

### Update gradle wrapper to 8.2.1​
```
# gradle-wrapper.propertiesdistributionBase=GRADLE_USER_HOMEdistributionPath=wrapper/dists- distributionUrl=https\://services.gradle.org/distributions/gradle-8.0.2-all.zip+ distributionUrl=https\://services.gradle.org/distributions/gradle-8.2.1-all.zipzipStoreBase=GRADLE_USER_HOMEzipStorePath=wrapper/dists
```

### Update androidScheme​
In Capacitor 6, `https` is the default setting for `androidScheme` for **existing apps** to better enable Capacitor applications to make use of the system Autofill feature.
Changing the scheme is the equivalent to shipping your application on a different domain, which means any data stored in in cookies, localstorage, etc would no longer be accessible. To avoid data loss as a result of this change, if you didn't have a `androidScheme` entry in your Capacitor config file already set to `https`, you should set the scheme to `http`.
```
{ server:{  androidScheme:"http"}}
```

If you already had a `androidScheme` entry set to `https`, you can safely remove it now.
### Update kotlin version​
If your project is using kotlin, update the `kotlin_version` variable to `'1.9.10'`.
## Plugins​
The following plugin functionality has been modified or removed. Update your code accordingly.
For all plugins that had listeners, `addListener` now only returns a `Promise`, if you were storing the call result in a variable without using `await`, your code will no longer compile.
### Action Sheet​
  * `androidxMaterialVersion` variable has been updated to `1.10.0`.


### Camera​
  * Version 6 of Capacitor Camera plugin now uses the Photo Picker API, which no longer requires to declare camera permissions, unless using `saveToGallery: true`. If this is false, you can remove the following permissions from `AndroidManifest.xml` if no other plugin requires them.


```
<uses-permissionandroid:name="android.permission.READ_MEDIA_IMAGES"/><uses-permissionandroid:name="android.permission.READ_EXTERNAL_STORAGE"/><uses-permissionandroid:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
```

  * On Android, if the user cancels picking images from the gallery, the error returned is now `"User cancelled photos app"` as on the other platforms.
  * `androidxMaterialVersion` variable has been updated to `1.10.0`.


### Filesystem​
  * iOS now returns `ctime` and `mtime` as numbers instead of strings, as all the other platforms.


### Geolocation​
  * `NSLocationAlwaysUsageDescription` (`Privacy - Location Always Usage Description`) is deprecated and can be removed from the `Info.plist`.
  * `playServicesLocationVersion` variable has been updated to `21.1.0`.


### Google Maps​
  * iOS native libraries have been updated, check this for more details
  * `NSLocationAlwaysUsageDescription` (`Privacy - Location Always Usage Description`) is deprecated and can be removed from the `Info.plist`.
  * `googleMapsPlayServicesVersion` has been updated to `18.2.0`.
  * `googleMapsUtilsVersion` has been updated to `3.8.2`.
  * `googleMapsKtxVersion` has been updated to `5.0.0`.
  * `googleMapsUtilsKtxVersion` has been updated to `5.0.0`.
  * `kotlinxCoroutinesVersion` has been updated to `1.7.3`.
  * `androidxCoreKTXVersion` has been updated to `1.12.0`.
  * `kotlin_version` has been updated to `1.9.10`.


### Local Notifications​
  * On Android 14 the notifications are not exact by default even if using `<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />` permission, see this for more details


### Push Notifications​
  * `firebaseMessagingVersion` variable has been updated to `23.3.1`.


### Share​
  * `androidxCoreVersion` variable has been updated to `1.12.0`.


### Splash Screen​
  * `coreSplashScreenVersion` variable has been updated to `1.0.1`.


### Status Bar​
  * `androidxCoreVersion` variable has been updated to `1.12.0`.


## Contents
  * NodeJS 18+
  * Using the CLI to Migrate
  * Using the VS Code Extension to Migrate
  * iOS
    * Upgrade Xcode
    * SPM Support
    * Register custom plugins
    * Zooming
  * Android
    * Upgrade Android Studio
    * Update Android Project Variables
    * Update google services plugin
    * Update gradle plugin to 8.2.1
    * Update gradle wrapper to 8.2.1
    * Update androidScheme
    * Update kotlin version
  * Plugins
    * Action Sheet
    * Camera
    * Filesystem
    * Geolocation
    * Google Maps
    * Local Notifications
    * Push Notifications
    * Share
    * Splash Screen
    * Status Bar


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fupdating%2F6-0&_biz_t=1739811918545&_biz_i=Capacitor%20Documentation&_biz_n=21&rnd=956389&cdn_o=a&_biz_z=1739811918545)
