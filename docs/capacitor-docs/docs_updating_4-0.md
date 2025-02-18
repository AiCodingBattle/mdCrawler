Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Compared to previous upgrades, the breaking changes between Capacitor 3 and 4 are fairly minimal. In this guide, you'll find steps to update your project to the current Capacitor 4 version as well as a list of breaking changes for our official plugins.
## Using the CLI to Migrate​
Install the latest version of the Capacitor CLI to your project using `npm i -D @capacitor/cli@latest-4`. Once installed, simply run `npx cap migrate` to have the CLI handle the migration for you. If any of the steps for the migration are not able to be completed, additional information will be made available in the output in the terminal. The steps for doing the migration manually are listed out below.
## iOS​
The following guide describes how to upgrade your Capacitor 3 iOS project to Capacitor 4.
### Raise iOS Deployment Target​
Do the following for your Xcode project: select the **Project** within the project editor and open the **Build Settings** tab. Under the **Deployment** section, change **iOS Deployment Target** to **iOS 13.0**. Repeat the same steps for any app **Targets**.
Then, open `ios/App/Podfile` and follow these steps:
  1. Add this on the first line:


```
require_relative '../../node_modules/@capacitor/ios/scripts/pods_helpers'
```

  1. Update the iOS version to 13.0:


```
platform :ios,'13.0'
```

  1. Add this block on the last line:


```
post_install do|installer| assertDeploymentTarget(installer)end
```

### Remove Unnecessary Code​
Remove unused `touchesBegan` method from `AppDelegate.swift`
```
-override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {- super.touchesBegan(touches, with: event)-- let statusBarRect = UIApplication.shared.statusBarFrame- guard let touchPoint = event?.allTouches?.first?.location(in: self.window) else { return }-- if statusBarRect.contains(touchPoint) {-   NotificationCenter.default.post(name: .capacitorStatusBarTapped, object: nil)- }-}
```

### Optional: Remove NSAppTransportSecurity entry from Info.plist​
`NSAppTransportSecurity` is only used for live reload, if you are not using live reload or you are using Ionic CLI for live reload you no longer need this entry.
```
-<key>NSAppTransportSecurity</key>-<dict>-		 <key>NSAllowsArbitraryLoads</key>- 		<true/>-</dict>
```

## Android​
The following guide describes how to upgrade your Capacitor 3 Android project to Capacitor 4.
### Update Android Project Variables​
In your `variables.gradle` file, update your values to the following new minimums and add the new `coreSplashScreenVersion` and `androidxWebkitVersion`
```
minSdkVersion =22compileSdkVersion =32targetSdkVersion =32androidxActivityVersion ='1.4.0'androidxAppCompatVersion ='1.4.2'androidxCoordinatorLayoutVersion ='1.2.0'androidxCoreVersion ='1.8.0'androidxFragmentVersion ='1.4.1'coreSplashScreenVersion ='1.0.0-rc01'androidxWebkitVersion ='1.4.0'junitVersion ='4.13.2'androidxJunitVersion ='1.1.3'androidxEspressoCoreVersion ='3.4.0'cordovaAndroidVersion ='10.1.1'
```

### Add `android:exported` tag to your Android Manifest​
In your `AndroidManifest.xml` file, you'll need to add the following line to the `<activity>` tag.
```
android:exported="true"
```

This tag ensures that you can open this "Activity," or screen, in your app. For more information on this and other tags, check out Android's `<activity>` reference documentation.
info
By default, your `AndroidManifest.xml` will be located in `android/app/src/main/AndroidManifest.xml`.
### Update Gradle Google Services plugin​
In `android/build.gradle` file change `classpath 'com.google.gms:google-services:4.3.5'` to `classpath 'com.google.gms:google-services:4.3.13'` to update Google Services plugin.
### Update to Gradle 7​
Adjust your Gradle project settings in `File > Project Structure > Project`. The Android Gradle Plugin Version should be 7.2.1 or later and the Gradle Version should be 7.4.2 or later. Apply these changes and run a gradle sync by clicking on the Elephant Icon in the top right of Android Studio
info
Android Studio may provide an automatic migration to Gradle 7. Go ahead and take them up on the offer! To upgrade, go to your `build.gradle` file, and click on the 💡 icon, and click "Upgrade Gradle. Once your project is migrated over, run a gradle sync as described above.
Another alternative would be to use the Android Gradle Plugin Upgrade Assistant to handle the migration for you. Steps for this tool can be found in the Android documentation.
### Ensure you are using Java 11​
Capacitor 3 works with both Java 8 and Java 11. Moving forward, Capacitor 4 will only support Java 11. You can change this in your project by going to the following menu in Android Studio:
`Preferences > Build, Execution, Deployment > Build Tools > Gradle`
![Gradle preferences](https://capacitorjs.com/docs/assets/images/android-java-11-3a689fb5f10e972db655982aa0e8c0eb.png)
From there, you can modify the "Gradle JDK" to be Java 11.
info
Java 11 ships with the latest version of Android Studio. No additional downloads needed!
### Switch to automatic Android plugin loading​
This was an optional change in Capacitor 3, but it's now mandatory for the Capacitor 4 upgrade since the init method has been removed. In `MainActivity.java`, the `onCreate` method can be removed. You no longer have to edit this file when adding or removing plugins installed via npm.
```
public class MainActivity extends BridgeActivity {-  @Override-  public void onCreate(Bundle savedInstanceState) {-    super.onCreate(savedInstanceState);--    // Initializes the Bridge-    this.init(savedInstanceState, new ArrayList<Class<? extends Plugin>>() {{-      // Additional plugins you've installed go here-      add(Plugin1.class);-      add(Plugin2.class);-    }});-  }}
```

### Change registerPlugin order​
If your app includes custom plugins built specifically for your application, you have to register them before `super.onCreate`:
```
public class MainActivity extends BridgeActivity {  @Override  public void onCreate(Bundle savedInstanceState) {+    registerPlugin(PluginInMyApp.class);    super.onCreate(savedInstanceState);-    registerPlugin(PluginInMyApp.class);  }}
```

### Optional: Use the new Android 12 Splash Screen API​
To enable the new recommended **Android 12 Splash Screen API** this change is required:
  * In `android/app/src/main/res/values/styles.xml`, edit the theme `parent` attribute on the `AppTheme.NoActionBarLaunch` Theme from `AppTheme.NoActionBar` to `Theme.SplashScreen` and add desired options to the theme.


```
<stylename="AppTheme.NoActionBarLaunch"parent="Theme.SplashScreen"><itemname="android:background">@drawable/splash</item></style>
```

Not enabling the Android 12 Splash Screen will result in a double Splash Screen on Android 12+ devices and will use the old Splash Screen on older devices.
This change is optional but recommended to prevent Android Studio from showing `Cannot resolve symbol 'Theme.SplashScreen'` message after the previous change.
  * Add `implementation "androidx.core:core-splashscreen:$coreSplashScreenVersion"` in the dependencies section of `android/app/build.gradle`.


### Optional: Use a DayNight theme​
To benefit from automatic theme change (Dark/Light themes) based on the user's device theme, change `<style name="AppTheme.NoActionBar" parent="Theme.AppCompat.NoActionBar">` to `<style name="AppTheme.NoActionBar" parent="Theme.AppCompat.DayNight.NoActionBar">` in `android/app/src/main/res/values/styles.xml`.
### Optional: Remove `jcenter()` from your Gradle files​
In previous Capacitor versions, `jcenter()` was required due to our Cordova compatibility layer being hosted on Jcenter. However, we are now using the latest Cordova Android version, hosted on Maven Central. With this, you may be able to remove `jcenter()` entirely from your `build.gradle` file. If you are using other plugins or native dependencies, make sure they aren't hosted on Jcenter before removing it!
## Plugins​
The following plugin functions have been modified or removed. Update your code accordingly.
### Storage​
The `@capacitor/storage` plugin has been renamed to `@capacitor/preferences` to better reflect it's usage. The API remains the same.
### Camera​
  * The setting `preserveAspectRatio` has been removed.
  * The plugin will no longer alert that iOS usage descriptions are missing.
  * `androidxMaterialVersion` variable has been updated to `1.6.1`.
  * `androidxExifInterfaceVersion` variable has been updated to `1.3.3`.


### Action Sheet​
  * `ShowActionsOptions.title` is now optional.
  * `androidxMaterialVersion` variable has been updated to `1.6.1`.


#### iOS Only​
  * `buildActionSheet` title and message is now optional.


### Push Notifications​
  * Added new type, `RegistrationError`, for `registrationError` event.
  * `importance` is now optional. Defaults to `3`.
  * `deleteChannel` now only accepts the channel id instead of the whole object.
  * `firebaseMessagingVersion` variable has been updated to `23.0.5`.
  * Android now respect the `presentationOptions` configuration options.


### Local Notifications​
  * `importance` is now optional. Defaults to `3`.
  * `deleteChannel` now only accepts the channel id instead of the whole object.
  * Android 12+ requires a permission for exact notifications.


### App​
  * `App.exitApp()` now returns a promise.


### Geolocation​
  * Timeout is now ignored for `getCurrentPosition()`.
  * `playServicesLocationVersion` has been updated to `20.0.0`.
  * The plugin now stops location updates when the app goes into background state.
  * The plugin now throws an error if system location services are disabled.


### FileSystem​
  * `copy` now returns path of the copied file.
  * `ReaddirResult` now returns an array of `FileInfo` objects, which contain metadata related to each file in addition to its URI.
  * `StatResult` has been unified to return the same on all platforms.


### Device​
  * `model` now returns the exact model on iOS (from “iPhone” to “iPhone13.4”).
  * `getLanguageCode()` now returns short language code on web (as other platforms did), to get full code use `getLanguageTag()`.


### Dialog​
  * `title` is now optional.


### Keyboard​
  * `style` config option now uses the `KeyboardStyle` enum for options.


### Toast​
  * On Android 12 and newer all toasts are shown at the bottom.


### Browser​
  * `androidxBrowserVersion` variable has been updated to `1.4.0`.


### Splash Screen​
  * If switching to the new Android 12 Splash Screen API, most configuration options won't be available for the initial Splash Screen, but they will still be available for the Splash Screen that appears when calling `show()`. Also, on Android 12+ devices the initial Splash Screen is different from the Splash Screen shown by `show()` method.


## Contents
  * Using the CLI to Migrate
  * iOS
    * Raise iOS Deployment Target
    * Remove Unnecessary Code
    * Optional: Remove NSAppTransportSecurity entry from Info.plist
  * Android
    * Update Android Project Variables
    * Add `android:exported` tag to your Android Manifest
    * Update Gradle Google Services plugin
    * Update to Gradle 7
    * Ensure you are using Java 11
    * Switch to automatic Android plugin loading
    * Change registerPlugin order
    * Optional: Use the new Android 12 Splash Screen API
    * Optional: Use a DayNight theme
    * Optional: Remove `jcenter()` from your Gradle files
  * Plugins
    * Storage
    * Camera
    * Action Sheet
    * Push Notifications
    * Local Notifications
    * App
    * Geolocation
    * FileSystem
    * Device
    * Dialog
    * Keyboard
    * Toast
    * Browser
    * Splash Screen


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fupdating%2F4-0&_biz_t=1739811921033&_biz_i=Capacitor%20Documentation&_biz_n=25&rnd=149628&cdn_o=a&_biz_z=1739811921033)
