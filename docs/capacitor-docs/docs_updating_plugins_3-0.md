Skip to main content
An **OutSystems** Company →
Version: v7
On this page
There are several required and recommended changes for plugins that are being updated to Capacitor 3.
## Planning for a Core API​
It is currently difficult for the core team to make changes to the internals of Capacitor without potentially affecting plugins. Because most classes and methods in Capacitor 2 are public for both iOS and Android, we have observed undesired usage of Capacitor APIs that we considered internal.
During Capacitor 3 development, we will be evaluating this problem and creating an official public API for plugins, which will be documented here.
## Android​
### Use the new `@CapacitorPlugin` annotation​
The `@NativePlugin` annotation is deprecated. We now recommend using the new `@CapacitorPlugin` annotation, which will allow for the new permissions API.
The `name` attribute is the same. The `requestCodes` and `permissionRequestCode` attributes are removed. The `permissions` attribute will need to be replaced with list of `@Permission` annotations, each containing a list of manifest strings and their corresponding `alias`, which you can omit for now until the new permissions API is implemented in your plugin.
```
-@NativePlugin(+@CapacitorPlugin(  name = "FooBar",-  requestCodes = {-    FooBarPlugin.REQUEST_SOME_METHOD,-    FooBarPlugin.REQUEST_SOME_OTHER_METHOD-  },-  permissionRequestCode = FooBarPlugin.REQUEST_ALL_PERMISSIONS,-  permissions = { Manifest.permission.FOO, Manifest.permission.BAR }+  permissions = {+    @Permission(strings = { Manifest.permission.FOO }, alias = "foo"),+    @Permission(strings = { Manifest.permission.BAR }, alias = "bar")+  }))public class FooBarPlugin extends Plugin {  static final int REQUEST_SOME_METHOD = 10051;  static final int REQUEST_SOME_OTHER_METHOD = 10052;
```

### Android request codes​
Capacitor 3.0 implements the AndroidX Activity Result API and removes manually defined request codes. Instead of providing a request code and overriding `handleOnActivityResult` or `handleRequestPermissionsResult`, plugins should provide callback methods using the `@ActivityCallback` or `@PermissionCallback` annotations. These callbacks can then be referenced when launching a new Activity or Permission request.
```
-static final int IMAGE_REQUEST = 10052;@PluginMethodpublic void chooseImage(PluginCall call) {  Intent intent = new Intent(Intent.ACTION_PICK);  intent.setType("image/*");-  startActivityForResult(call, intent, IMAGE_REQUEST);+  startActivityForResult(call, intent, "chooseImageResult");}+@ActivityCallback+private void chooseImageResult(PluginCall call, ActivityResult result) {+  if (result.getResultCode() == Activity.RESULT_CANCELED) {+    call.reject("Activity canceled");+  } else {+    Intent data = result.getData();+    // do something with the result data+    call.resolve("Success!");+  }+}
```

### Use WebColor.parseColor() over Color.parseColor()​
Android parses hex color strings with an alpha channel as _ARGB_ while in iOS and Web they are parsed as _RGBA_. If you are sharing colors with alpha channels across platforms be sure to use the new `WebColor` utility. `WebColor.parseColor()` works similar to the native Android `Color.parseColor()` function, but parses the string as RGBA instead.
```
String colorStringWithAlpha ="#FF000088";// Semi-transparent redint color =WebColor.parseColor(colorStringWithAlpha);
```

If you do not have an alpha channel on your colors both functions will return the same result.
### Change default compileSdkVersion and targetSdkVersion to 30​
In `android/build.gradle` change `compileSdkVersion` and `targetSdkVersion` default values to `30`.
```
android {-  compileSdkVersion project.hasProperty('compileSdkVersion') ? rootProject.ext.compileSdkVersion : 29+  compileSdkVersion project.hasProperty('compileSdkVersion') ? rootProject.ext.compileSdkVersion : 30  defaultConfig {    minSdkVersion project.hasProperty('minSdkVersion') ? rootProject.ext.minSdkVersion : 21-    targetSdkVersion project.hasProperty('targetSdkVersion') ? rootProject.ext.targetSdkVersion : 29+    targetSdkVersion project.hasProperty('targetSdkVersion') ? rootProject.ext.targetSdkVersion : 30    ...  }  ...}
```

## iOS​
### Weak References​
The relationship between objects was updated in Capacitor 3 to fix memory leaks. The consequence is that a plugin's references to objects higher in the hierarchy are now `weak`, which in Swift means they are optional. You are most likely to encounter this change when accessing `bridge` but it also applies to other properties such as `webView`. Calling a method on the bridge is relatively unchanged except that it now requires optional chaining:
```
-bridge.presentVC(myViewController, animated: true, completion: nil)+bridge?.presentVC(myViewController, animated: true, completion: nil)
```

The biggest impact of this change is that all return values from the bridge will be optional as well. Safely handling and unwrapping optionals can require extra steps.
```
if bridge?.isSimEnvironment {// BAD: Will not compile. The boolean is optional (because `bridge` is optional)// and must be unwrapped before it can be evaluated.}if bridge?.isSimEnvironment ==true{// NEUTRAL: An explicit comparison with an optional will work for a boolean but// may not be suitable for all data types.}iflet isSim = bridge?.isSimEnvironment, isSim {// GOOD: Using optional binding to unwrap the optional before examining its value.}
```

### Bridge Changes​
In addition to the reference changing from `strong` to `weak`, the API of the bridge itself has been updated (it is now exposed via a more formal protocol). Many of the properties and methods have been renamed but backwards support exists where possible by preserving and deprecating the old interfaces. Xcode will be able to automatically suggest the newer replacement in most cases. You should migrate any existing code so your plugin can build without compiler warnings.
![Xcode autocorrect suggestion](https://capacitorjs.com/docs/assets/images/bridge-naming-migration-333ce23cb2ba6157e8d129f2a8b25d7f.png)
### `CAPPluginCall` Parameters​
Capacitor includes a collection of convenience methods (`getString`, `getDate`, etc.) on `CAPPluginCall` to access the data passed from JavaScript to a plugin method. These have been updated for Capacitor 3.
  * `get()` has been removed. If you want to access the arguments directly, read the `options` dictionary.
  * `hasOption` has been deprecated. Use one of the typed accessors to check for a value.
  * Any accessor that takes a default value now requires a non-optional default but returns a non-optional result. This can change the optionality of your local variables but should reduce the usage of force unwrapping, which is an anti-pattern in Swift.
  * The behavior around dates and null values has been slightly changed and better documented. Find more information here.
  * The Obj-C convenience accessors have been split out to avoid conflicts with the Swift implementations. If you are working in Obj-C, you will need to import them separately by adding `#import <Capacitor/CAPBridgedJSTypes.h>` to your `.m` file.


## Changes to `PluginCall` & `CAPPluginCall`​
### Use `resolve()` and `reject()`​
We believe `resolve()` and `reject()` better reflect the Promise-like flow intended for plugin methods. They should be preferred over `success()` and `error()` (now deprecated), even in callback-style plugin methods.
### `resolve()` without arguments now resolves with `undefined`​
Previously, calling `resolve()` with no arguments resulted in an empty object being sent to the JavaScript layer. Because this is unlike the behavior of JavaScript's `Promise.resolve()`, as of Capacitor 3, `undefined` is sent instead.
### Saving calls​
The `save()` method has deprecated and a replacement `keepAlive` property has been added. The recommended patterns for saving a call have been documented to clarify the behavior. Read more about that here.
### Set iOS deployment target to 12.0​
Do the following for the Plugin Xcode project and Plugin target: open the **Build Settings** tab. Under the **Deployment** section, change **iOS Deployment Target** to **iOS 12.0**.
Then, open `ios/Podfile` and update the iOS version to 12.0:
```
-platform :ios, '11.0'+platform :ios, '12.0'use_frameworks!
```

Finally, open `pluginName.podspec` and update the iOS version to 12.0:
```
-s.ios.deployment_target = '11.0'+s.ios.deployment_target = '12.0'
```

### Set Swift version to 5​
Open the **Build Settings** tab in your Xcode target, then change **Swift Language Version** to **Swift 5** under the **Swift Compiler - Language** section.
Then, open `pluginName.podspec` and update the Swift version to 5.1:
```
-s.swift_version = '4.2'+s.swift_version = '5.1'
```

## Web​
### Registering Plugins​
The `registerWebPlugin(MyPlugin)` function has been deprecated. We recommend using the new `registerPlugin` function and lazily loading the web (and optionally, electron) plugins as shown below.
```
import{ registerPlugin }from'@capacitor/core';importtype{ CoolPlugin }from'./definitions';const MyCoolPlugin =registerPlugin<CoolPlugin>('MyCoolPlugin',{web:()=>import('./web').then(m =>newm.MyCoolPluginWeb()),// electron: () => ("./electron").then(m => new m.MyCoolPluginElectron())});export*from'./definitions';export{ MyCoolPlugin };
```

### Set TypeScript output to es2017​
If you are using TypeScript to develop your web plugins, we recommend you set the output target to `es2017` in your `tsconfig.json`.
## Evaluate error handling​
We are now recommending that plugin authors make use of the new error codes in Capacitor 3:
  * **Unavailable** : indicates the functionality can't be used right now
  * **Unimplemented** : indicates the functionality can't or won't be implemented, or may be implemented in the future


Read more about Error Handling for Web, iOS, and Android.
## Adopting the new Permissions API​
Prior to 3.0, it was expected that permissions were automatically requested by a plugin before feature use. For example, a Geolocation plugin would automatically request permission when the user location was requested for the first time and then continue appropriately if the permission was granted or denied.
One goal of Capacitor 3 is to give app developers the ability to request or check permissions at any time and control how and when the user prompts are presented. This provides more flexibility in the user experience by allowing the app to respond to the user's choice in a variety of ways.
It is perfectly fine to continue automatically requesting permissions, but you are encouraged to adopt the new permissions pattern as well to give app developers control over permissions.
Learn how to implement the Permissions API in your plugin ›
## Contents
  * Planning for a Core API
  * Android
    * Use the new `@CapacitorPlugin` annotation
    * Android request codes
    * Use WebColor.parseColor() over Color.parseColor()
    * Change default compileSdkVersion and targetSdkVersion to 30
  * iOS
    * Weak References
    * Bridge Changes
    * `CAPPluginCall` Parameters
  * Changes to `PluginCall` & `CAPPluginCall`
    * Use `resolve()` and `reject()`
    * `resolve()` without arguments now resolves with `undefined`
    * Saving calls
    * Set iOS deployment target to 12.0
    * Set Swift version to 5
  * Web
    * Registering Plugins
    * Set TypeScript output to es2017
  * Evaluate error handling
  * Adopting the new Permissions API


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fupdating%2Fplugins%2F3-0&_biz_t=1739811923487&_biz_i=Updating%20plugins%20to%203.0%20%7C%20Capacitor%20Documentation&_biz_n=29&rnd=866905&cdn_o=a&_biz_z=1739811923488)
