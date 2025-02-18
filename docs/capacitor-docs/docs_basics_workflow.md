Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Working with Capacitor is slightly different than working with a traditional web app. To make your web native Capacitor application, you'll need to do the following steps.
## Building your web code​
Once you are ready to test your web app on a mobile device, you'll need to build your web app for distribution. If you are using a tool like Create React App or Vite that command will be `npm run build`; while a tool like Angular uses the command `ng build`. Whatever your command is, you will need to build your web code for distribution in order to use it with Capacitor.
## Syncing your web code to your Capacitor project​
Once your web code has been built for distribution, you will need to push your web code to the web native Capacitor application. To do this, you can use the Capacitor CLI to "sync" your web code and install/update the required native dependencies.
To sync your project, run:
```
npx cap sync
```

Running `npx cap sync` will **copy** over your already built web bundle to both your Android and iOS projects as well as **update** the native dependencies that Capacitor uses.
You can read our docs on `sync` and more on the Capacitor CLI reference documentation.
info
Did you get an error about "not being able to find the web assets directory?" Update your Capacitor configuration file to use the proper `webDir`.
## Testing your Capacitor app​
Once you've synced over your web bundle to your native project, it is time to test your application on a mobile device. There are a few different ways to do this, but the easiest way is to use the built in Capacitor CLI commands.
To run a debug build of your Capacitor app on an iOS device, you can run:
```
npx cap run ios
```

Similarly, to run a debug build of your Capacitor app on an Android device, you can run:
```
npx cap run android
```

Once you've iterated and tested your application, it is time to compile the final binary to distribute to other mobile devices.
info
You can also run your app on iOS via Xcode or run your app on Android via Android Studio as well. Both options are valid for development. Go ahead and try both to see which option you prefer!
### Open your Native IDE​
If you'd like more control over your native project you can quickly open the native IDEs using the Capacitor CLI.
To open the iOS Capacitor `.xcworkspace` project in Xcode, you can run:
```
npx cap open ios
```

Similarly, to open the Android Capacitor project in Android Studio, you can run:
```
npx cap open android
```

Opening the native project can give you full control over the native runtime of your application. You can create plugins, add custom native code, or compile your application for releasing.
## Compiling your native binary​
After `sync`, you are encouraged to open your target platform's IDE: Xcode for iOS or Android Studio for Android, for compiling your native app.
Alternatively, to compile your app in a terminal or in CI environments, you can use the cap build command to build the native project, outputting a signed AAB, APK or IPA file ready for distribution to a device or end users.
```
npx cap build android
```

We also suggest using tools such as Fastlane or a cloud build tool like Appflow to automate these processes for you. While every application is different, we have an example of a general release process for Capacitor projects. Go and read our publishing guides for iOS and Android for more info on how to deploy to the Apple App Store or the Google Play Store.
## Updating Capacitor​
Updating your Capacitor runtime is as straightforward as running `npm install`.
```
npm i @capacitor/core @capacitor/ios @capacitor/androidnpm i -D @capacitor/cli
```

When updating Capacitor, you want to make sure your Core, Android, and iOS libraries are all the same version. Capacitor Core, Android, and iOS releases are all uploaded simultaneously, meaning that if you install all of the libraries at the same time, you'll be fine!
info
You can subscribe to the Capacitor repo to be notified of new releases. At the top of the repository index, click **Watch** -> **Releases only**.
## Contents
  * Building your web code
  * Syncing your web code to your Capacitor project
  * Testing your Capacitor app
    * Open your Native IDE
  * Compiling your native binary
  * Updating Capacitor


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fbasics%2Fworkflow&_biz_t=1739811914787&_biz_i=Development%20Workflow%20%7C%20Capacitor%20Documentation&_biz_n=15&rnd=868668&cdn_o=a&_biz_z=1739811914787)
