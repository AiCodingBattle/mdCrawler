Skip to main content
An **OutSystems** Company →
Version: v7
On this page
## iOS​
### Changes to CAPBridgedPlugin protocol​
  * `CAPBridgedPlugin` protocol requirements have been moved to the instance level instead of the class level.
  * `pluginId` was renamed `identifier` to avoid clashing with `CAPPlugin.pluginId` and the `getMethod(_:)` requirement was removed altogether and put into an internal extension method.
  * `pluginMethods` was also updated to be more specific about its contents (was `Any` now is `CAPPluginMethod`).


The vast majority of users should not experience any issues since the status quo is to use the macro to generate conformance to `CAPBridgedPlugin`. Any users who cast to `CAPBridgedPlugin` to or manually conform to `CAPBridgedPlugin` without the macro will be affected.
## Android​
### PluginCall.getObject() / PluginCall.getArray()​
To match iOS behavior, `PluginCall.getObject()` and `PluginCall.getArray()` on Android can now return null. We recommend plugin authors to perform null checks around code handling returns from either of these methods.
# Updating Capacitor to 5.0 in your plugin
## Using @capacitor/plugin-migration-v4-to-v5​
From the plugin folder, run `npx @capacitor/plugin-migration-v4-to-v5@latest` and it will perform all the file changes automatically.
## Updating the files manually​
### Updating package.json​
Update `@capacitor/cli`, `@capacitor/core`, `@capacitor/android` and `@capacitor/ios` to `latest-5` version.
### Updating targetSDK / compileSDK to 33​
```
# build.gradleandroid {-  compileSdkVersion project.hasProperty('compileSdkVersion') ? rootProject.ext.compileSdkVersion : 32+  compileSdkVersion project.hasProperty('compileSdkVersion') ? rootProject.ext.compileSdkVersion : 33-  targetSdkVersion project.hasProperty('targetSdkVersion') ? rootProject.ext.targetSdkVersion : 32+  targetSdkVersion project.hasProperty('targetSdkVersion') ? rootProject.ext.targetSdkVersion : 33
```

### Update Android Plugin Variables​
In your `build.gradle` file, update the following package version minimums:
```
ext {  junitVersion = project.hasProperty('junitVersion') ? rootProject.ext.junitVersion : '4.13.2'-  androidxAppCompatVersion = project.hasProperty('androidxAppCompatVersion') ? rootProject.ext.androidxAppCompatVersion : '1.4.2'+  androidxAppCompatVersion = project.hasProperty('androidxAppCompatVersion') ? rootProject.ext.androidxAppCompatVersion : '1.6.1'-  androidxJunitVersion = project.hasProperty('androidxJunitVersion') ? rootProject.ext.androidxJunitVersion : '1.1.3'+  androidxJunitVersion = project.hasProperty('androidxJunitVersion') ? rootProject.ext.androidxJunitVersion : '1.1.5'-  androidxEspressoCoreVersion = project.hasProperty('androidxEspressoCoreVersion') ? rootProject.ext.androidxEspressoCoreVersion : '3.4.0'+  androidxEspressoCoreVersion = project.hasProperty('androidxEspressoCoreVersion') ? rootProject.ext.androidxEspressoCoreVersion : '3.5.1'
```

### Update gradle plugin to 8.0.0​
```
  dependencies {-    classpath 'com.android.tools.build:gradle:7.2.1'+    classpath 'com.android.tools.build:gradle:8.0.0'  }
```

### Update gradle wrapper to 8.0.2​
```
# gradle-wrapper.propertiesdistributionBase=GRADLE_USER_HOMEdistributionPath=wrapper/dists- distributionUrl=https\://services.gradle.org/distributions/gradle-7.4.2-all.zip+ distributionUrl=https\://services.gradle.org/distributions/gradle-8.0.2-all.zipzipStoreBase=GRADLE_USER_HOMEzipStorePath=wrapper/dists
```

### Move package to `build.gradle`​
```
# AndroidManifest.xml<?xml version="1.0" encoding="utf-8"?>- <manifest xmlns:android="http://schemas.android.com/apk/res/android"-   package="[YOUR_PACKAGE_ID]">+ <manifest xmlns:android="http://schemas.android.com/apk/res/android">
```

```
# build.gradleandroid {+   namespace "[YOUR_PACKAGE_ID]"   compileSdkVersion project.hasProperty('compileSdkVersion') ? rootProject.ext.compileSdkVersion : 33
```

### Disable Jetifier​
```
# gradle.properties# Android operating system, and which are packaged with your app's APK# https://developer.android.com/topic/libraries/support-library/androidx-rnandroid.useAndroidX=true- # Automatically convert third-party libraries to use AndroidX- android.enableJetifier=true
```

### Update to Java 17​
```
# build.gradlecompileOptions {-  sourceCompatibility JavaVersion.VERSION_11+  sourceCompatibility JavaVersion.VERSION_17-  targetCompatibility JavaVersion.VERSION_11+  targetCompatibility JavaVersion.VERSION_17}
```

### Update kotlin_version​
If your plugin uses kotlin, update the default `kotlin_version`
```
# build.gradlebuildscript {-  ext.kotlin_version = project.hasProperty("kotlin_version") ? rootProject.ext.kotlin_version : '1.7.0'+  ext.kotlin_version = project.hasProperty("kotlin_version") ? rootProject.ext.kotlin_version : '1.8.20'  repositories {
```

And replace `org.jetbrains.kotlin:kotlin-stdlib-jdk7` or `org.jetbrains.kotlin:kotlin-stdlib-jdk8` dependencies with `org.jetbrains.kotlin:kotlin-stdlib`.
```
# build.gradledependencies {-  implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk7:$kotlin_version"+  implementation "org.jetbrains.kotlin:kotlin-stdlib:$kotlin_version"
```

## Contents
  * iOS
    * Changes to CAPBridgedPlugin protocol
  * Android
    * PluginCall.getObject() / PluginCall.getArray()
  * Using @capacitor/plugin-migration-v4-to-v5
  * Updating the files manually
    * Updating package.json
    * Updating targetSDK / compileSDK to 33
    * Update Android Plugin Variables
    * Update gradle plugin to 8.0.0
    * Update gradle wrapper to 8.0.2
    * Move package to `build.gradle`
    * Disable Jetifier
    * Update to Java 17
    * Update kotlin_version


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fupdating%2Fplugins%2F5-0&_biz_t=1739811920393&_biz_i=Capacitor%20Documentation&_biz_n=24&rnd=786484&cdn_o=a&_biz_z=1739811920394)
