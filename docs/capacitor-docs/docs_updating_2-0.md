Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Capacitor 2 makes some tooling updates including the adoption of Swift 5 in iOS and AndroidX for Android.
Read the Capacitor 2.0 announcement ›
## Update Capacitor dependencies​
First, update Capacitor Core and the CLI:
```
npminstall @capacitor/cli@2 @capacitor/core@2
```

Next, update each Capacitor platform that you use:
```
# iOSnpminstall @capacitor/ios@2npx cap sync ios# Androidnpminstall @capacitor/android@2npx cap sync android# Electroncd electronnpminstall @capacitor/electron@2
```

## Backward Incompatible Plugin Changes​
  * **Camera**
    * `saveToGallery` default value is now `false` on all platforms
    * if `allowEditing` is `true` and the edit is canceled, the original image is returned
  * **Push Notifications**
    * permissions will no longer be requested when `register()` is called, use `requestPermission()`
    * `PushNotificationChannel` renamed to `NotificationChannel`
  * **Local Notifications**
    * permissions will no longer be requested when `register()` is called, use `requestPermission()`
    * `schedule()` now returns `LocalNotificationScheduleResult`
  * **Toast**
    * unify duration across platforms: short 2000ms, long 3500ms
  * **Geolocation**
    * use Fused Location Provider on Android
    * `requireAltitude` removed from `GeolocationOptions`
    * change native location accuracy values on iOS (more info)
  * **Filesystem**
    * `createIntermediateDirectories` was removed from `MkdirOptions` (use `recursive` instead)
    * `recursive` option added to writeFile, which changes behavior on Android and web (more info)
    * `Application` directory option removed because it was broken
  * **Device**
    * `batteryLevel` and `isCharging` removed from `getInfo()`, use `getBatteryInfo()`
  * **Modals**
    * `inputPlaceholder` sets a placeholder instead of text, use `inputText` instead
  * **App**
    * `AppRestoredResult` is optional now, returned only if succeeded, otherwise it returns an error
  * **Clipboard**
    * `ReadOptions` was removed


## iOS​
Capacitor 2 requires Xcode 11+.
### Update native project to Swift 5​
Capacitor 2 uses Swift 5. It's recommended to update your native project to also use Swift 5.
  1. From Xcode click **Edit** -> **Convert** -> **To Current Swift Syntax**.
  2. **App.app** will appear selected, click **Next** button.
  3. Then a message will say **No source changes necessary**.
  4. Finally, click the **Update** button.


## Android​
### AndroidX​
Capacitor 2 uses AndroidX for Android support library dependencies as recommended by Google, so the native project needs to be updated to use AndroidX as well.
From Android Studio do **Refactor** -> **Migrate to AndroidX**. Then click on **Migrate** button and finally click on **Do Refactor**.
If using Cordova or Capacitor plugins that don't use AndroidX yet, you can use jetifier tool to patch them.
```
npminstall jetifiernpx jetifier
```

To run it automatically after every package install, add `"postinstall": "jetifier"` in the `package.json`.
### Create common variables​
Create a `android/variables.gradle` file with this content:
```
ext { minSdkVersion =21 compileSdkVersion =29 targetSdkVersion =29 androidxAppCompatVersion ='1.1.0' androidxCoreVersion ='1.2.0' androidxMaterialVersion ='1.1.0-rc02' androidxBrowserVersion ='1.2.0' androidxLocalbroadcastmanagerVersion ='1.0.0' firebaseMessagingVersion ='20.1.2' playServicesLocationVersion ='17.0.0' junitVersion ='4.12' androidxJunitVersion ='1.1.1' androidxEspressoCoreVersion ='3.2.0' cordovaAndroidVersion ='7.0.0'}
```

In `android/build.gradle` file, add `apply from: "variables.gradle"`:
```
    classpath 'com.android.tools.build:gradle:4.1.1'    classpath 'com.google.gms:google-services:4.3.3'    // NOTE: Do not place your application dependencies here; they belong    // in the individual module build.gradle files  }}+apply from: "variables.gradle"allprojects {  repositories {    google()    jcenter()
```

### Use common variables​
If you created the `variables.gradle` file, update your project to use them.
In the `android/app/build.gradle` file, make the following updates:
```
android {-  compileSdkVersion 28+  compileSdkVersion rootProject.ext.compileSdkVersion  defaultConfig {    applicationId "com.example.app"-    minSdkVersion 21-    targetSdkVersion 28+    minSdkVersion rootProject.ext.minSdkVersion+    targetSdkVersion rootProject.ext.targetSdkVersion    versionCode 1    versionName "1.0"    testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
```

```
dependencies {  implementation fileTree(include: ['*.jar'], dir: 'libs')-  implementation 'androidx.appcompat:appcompat:1.0.0'+  implementation "androidx.appcompat:appcompat:$androidxAppCompatVersion"  implementation project(':capacitor-android')-  testImplementation 'junit:junit:4.12'-  androidTestImplementation 'androidx.test.ext:junit:1.1.1'-  androidTestImplementation 'androidx.test.espresso:espresso-core:3.1.0'+  testImplementation "junit:junit:$junitVersion"+  androidTestImplementation "androidx.test.ext:junit:$androidxJunitVersion"+  androidTestImplementation "androidx.test.espresso:espresso-core:$androidxEspressoCoreVersion"  implementation project(':capacitor-cordova-android-plugins')
```

> Don't miss the change from single quotes to double quotes. Double quotes are required for variable interpolation.
### Android Studio plugin update recommended​
When you open the Android project in Android Studio, a **Plugin Update Recommended** message will appear. Click on **update**. It will tell you to update Gradle plugin and Gradle. Click **Update** button.
You can also manually update the Gradle plugin and Gradle.
To manually update Gradle plugin, in `android/build.gradle` file, update the `com.android.tool.build:gradle` version to 3.6.1.
To manually update Gradle, in `android/gradle/wrapper/gradle-wrapper.properties`, change `gradle-4.10.1-all.zip` to `gradle-5.6.4-all.zip`.
### Update Google Services plugin​
In `android/build.gradle` file, update the `com.google.gms:google-services` dependency version to 4.3.3.
```
  dependencies {    classpath 'com.android.tools.build:gradle:4.1.1'-    classpath 'com.google.gms:google-services:4.2.0'+    classpath 'com.google.gms:google-services:4.3.3'    // NOTE: Do not place your application dependencies here; they belong    // in the individual module build.gradle files  }
```

### Change `android:configChanges` to avoid app restarts​
In `android/app/src/main/AndroidManifest.xml`, add `|smallestScreenSize|screenLayout|uiMode` in the activity's `android:configChanges` attribute.
```
    <activity-      android:configChanges="orientation|keyboardHidden|keyboard|screenSize|locale"+      android:configChanges="orientation|keyboardHidden|keyboard|screenSize|locale|smallestScreenSize|screenLayout|uiMode"      android:name="com.example.app"      android:label="@string/title_activity_main"      android:theme="@style/AppTheme.NoActionBarLaunch"      android:launchMode="singleTask">
```

### Add caches folder to `FileProvider` file paths to avoid permission error when editing gallery images​
In `android/app/src/main/res/xml/file_paths.xml` add `<cache-path name="my_cache_images" path="." />`:
```
<?xml version="1.0" encoding="utf-8"?><paths xmlns:android="http://schemas.android.com/apk/res/android">  <external-path name="my_images" path="." />+  <cache-path name="my_cache_images" path="." /></paths>
```

### Remove `launch_splash.xml`​
The `android/app/src/main/res/drawable/launch_splash.xml` file can be removed because it is no longer used.
### Remove maven repository​
Capacitor is distributed on npm, so having the maven repository entry on `android/app/build.gradle` is no longer needed and can cause problems. Remove it from `repositories` section:
```
repositories {-  maven {-    url "https://dl.bintray.com/ionic-team/capacitor"-  }  flatDir {    dirs '../capacitor-cordova-android-plugins/src/main/libs', 'libs'  }}
```

## Contents
  * Update Capacitor dependencies
  * Backward Incompatible Plugin Changes
  * iOS
    * Update native project to Swift 5
  * Android
    * AndroidX
    * Create common variables
    * Use common variables
    * Android Studio plugin update recommended
    * Update Google Services plugin
    * Change `android:configChanges` to avoid app restarts
    * Add caches folder to `FileProvider` file paths to avoid permission error when editing gallery images
    * Remove `launch_splash.xml`
    * Remove maven repository


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fupdating%2F2-0&_biz_t=1739811922313&_biz_i=Capacitor%20Documentation&_biz_n=27&rnd=848505&cdn_o=a&_biz_z=1739811922313)
