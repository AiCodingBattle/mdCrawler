Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Creating a 100% perfect native management tool is nearly impossible, and sooner or later you'll run into various issues with some part of the Android workflow.
This guide attempts to document common Android issues with possible solutions.
## Android Toolbox​
Every Android developer learns a few common techniques for debugging Android issues, and you should incorporate these into your workflow:
### Google, Google, Google​
Any time you encounter an issue with Android, or Gradle, or Emulators, your first step should be to copy and paste the error into a Google search.
Capacitor uses the standard Android toolkit, so chances are if you run into something, many Android developers have as well, and there's a solution out there.
It could be as simple as updating a dependency, running Gradle sync, or invalidating caches.
### Gradle Sync​
If you have installed a new Plugin from npm and are unable to use or see the plugins in your Android build, try using the "Sync Project with Gradle Files" button in the top right of Android Studio (the icon looks like an elephant). This will re-sync your native Android code to include the new plugin code and should allow use of your new plugin. For more info, see this issue on Github.
It can also help with many other seemingly random issues, so running "Sync Project with Gradle Files" is always a good first step when running into most Android build issues.
### Clean/Rebuild​
Cleaning and rebuilding can fix a number of build issues:
![Android Clean and Build](https://capacitorjs.com/docs/assets/images/clean-rebuild-c9262604bc3eaf70413eae3cbe9c210a.png)
### Invalidate Caches/Restart​
If you're confident you fixed an issue, but Android Studio or Gradle doesn't agree, often the solution is to have Android Studio invalidate its caches and restart the program.
That can be done easily from the File menu:
![Android Invalidate Caches](https://capacitorjs.com/docs/assets/images/invalidate-caches-053e48cb4263c0597b12744a01f79f9b.png)
## Error: "package android.support.* does not exist"​
This error occurs when some Cordova or Capacitor plugin has old android support dependencies instead of using the new AndroidX equivalent. You should report the issue in the plugin repository so the maintainers can update the plugin to use AndroidX dependencies.
As a workaround, you can also patch the plugin using jetifier:
```
npminstall jetifiernpx jetifynpx cap sync android
```

## Error: "Please select Android SDK"​
This error is often due to Gradle needing to be synced, something you'll need to do periodically after updating dependencies and changing project settings.
To manually sync Gradle, open File -> Sync Project with Gradle Files from the main menu bar:
![Sync Gradle](https://capacitorjs.com/docs/assets/images/sync-gradle-35d7e33e532f078afdd3ce6aa36efb20.png)
## Error: "APK Can't be installed"​
An APK not installing to an Emulator or Device is often due to having an existing app with the same package name. You may see an error like this when trying to run your app:
![Android APK Failed](https://capacitorjs.com/docs/assets/images/apk-failed-61aea79e082faa2f7c7d3e8ee27b1eee.png)
The solution is to remove any old apps and make sure your package name is up to date in `AndroidManifest.xml` and not conflicting with other apps you are developing.
Finally, do a clean and rebuild just in case.
## Error: "Unable to locate a Java Runtime"​
This error may occur when using the `run` command if the `JAVA_HOME` environment variable is not set.
To resolve, set `JAVA_HOME` as an environment or system variable using the path found in Android Studio under Preferences > Build, Execution, Deployment, Build Tools > Gradle > Gradle JDK.
![JDK Path in Android Studio](https://capacitorjs.com/docs/assets/images/jdk-path-f1b87b49e3e1f58570ae2ae6d93652ae.png)
On Mac, this can be updated in your `.zshrc` or `.bashrc` file or exported in your environment.
```
exportJAVA_HOME="/Applications/Android Studio.app/Contents/jbr/Contents/Home"
```

On Windows, you can set `JAVA_HOME` as a System Variable under your Environment Variables settings.
## Recreating your project​
Capacitor lets you manage your own Android project. Like any IDE-backed project, sometimes things get so out of sync that the only solution is to rebuild the project.
To do this, follow these steps:
  1. Copy any source code you created (such as Java files in `app/android/src`, manifest files, or resource files) into a safe location outside of `app/android`.
  2. Next, make sure you are running an updated version of the Capacitor CLI: `npm install @capacitor/cli@latest`
  3. Remove the android directory: `rm -rf android/`
  4. Re-create the Android app from Capacitor: `npx cap add android`
  5. Copy your saved source files back into the project


## Plugin Not Implemented​
On Android, this can happen if Capacitor doesn't find the plugins or can't inject its code into the WebView.
First of all, make sure the plugin is installed and appears in the `package.json`.
Then, run `npx cap sync android`.
Finally, use the "Sync Project with Gradle Files" button in the top right of Android Studio (the icon looks like an elephant). This will re-sync your native Android code to include the new plugin code and should allow use of your new plugin.
Also, if you are migrating from Capacitor 1 or 2, make sure you enabled the automatic plugin loading.
If still getting the "Plugin not implemented" error, make sure you are not using service workers, that prevents Capacitor's and Plugins code from injecting. Or if you want to use them, you can use this workaround for making the injection work.
## Using Proguard​
ProGuard is a tool used to shrink, obfuscate, and reduce the size of your app. It is enabled by setting the `minifyEnabled` option in `build.gradle` to `true`. This process can sometimes lead to issues in Capacitor when using a plugin or some custom native code that relies on its code being being readable at run time, such as code reflection. ProGuard scans code to try and optimize and shink the size of an app and sometimes this process can remove classes or methods that are important for the functionality of a plugin.
As of Capacitor v3.2.3 there are ProGuard rules included in Capacitor that cover the core functionality of Capacitor plugins, permissions, and activity results. If you are using an earlier version of Capacitor than v3.2.3, add the following rules to your Android project's `proguard-rules.pro` file. Those rules should resolve problems with any of the core Capacitor features and core plugins.
If you still encounter any issues after adding those rules, try to identify the source plugin or native code and add a rule to cover the specific plugin code, for example:
```
-keep class com.mythirdpartyplugin.** { *; }
```

If you are certain a Capacitor plugin is causing the ProGuard issue the following ProGuard rule will cover any plugin class code, if you don't mind all plugins being exempt from ProGuard processing:
```
-keep public class * extends com.getcapacitor.Plugin
```

## Contents
  * Android Toolbox
    * Google, Google, Google
    * Gradle Sync
    * Clean/Rebuild
    * Invalidate Caches/Restart
  * Error: "package android.support.* does not exist"
  * Error: "Please select Android SDK"
  * Error: "APK Can't be installed"
  * Error: "Unable to locate a Java Runtime"
  * Recreating your project
  * Plugin Not Implemented
  * Using Proguard


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fandroid%2Ftroubleshooting&_biz_t=1739811943184&_biz_i=Capacitor%20Documentation&_biz_n=65&rnd=536924&cdn_o=a&_biz_z=1739811943185)
