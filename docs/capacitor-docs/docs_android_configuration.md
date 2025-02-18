Skip to main content
An **OutSystems** Company →
Version: v7
On this page
## Configuring `AndroidManifest.xml`​
Android apps manage permissions, device features, and other settings in the `AndroidManifest.xml` file, which is located at `android/app/src/main/AndroidManifest.xml`.
> `AndroidManifest.xml` may reference additional files such as `styles.xml` and `strings.xml` within the `android/app/src/main/res/values` directory via `@style` and `@string`. Read more about Android Resources.
This article covers the basic modifications you'll need to make to your app. Read the Android Manifest docs to learn a whole lot more.
## Changing the Package ID​
To change your app's Package ID (aka **Application ID** for Android), edit `applicationId` at the top of `android/app/build.gradle`:
```
defaultConfig {-    applicationId "com.capacitorjs.app"+    applicationId "com.mycompany.myapp"
```

## Changing the App Name​
To change the name of your app, change the value for `app_name` in `strings.xml`:
```
<stringname="app_name">MyApp</string>
```

It may make sense to change the activity name to match, especially if your app has a single activity:
```
<stringname="title_activity_main">MyApp</string>
```

## Deeplinks (aka Android App Links)​
> For a Deep Links guide, see here.
To enable deeplinking through Android App Links, follow the official Android guide on Adding Android App Links. Android Studio comes with a handy wizard for configuring App Links.
Once configured, the `getLaunchUrl()` method in the App API will provide any URL the app was launched with, and the `'appUrlOpen'` event will fire any time the app receives a new App Link deeplink.
## URL Schemes​
Your app can respond to custom URLs on launch, making it possible to handle deeplinks and app interactions.
To change the URL, search for and modify this line in `strings.xml`. It's recommended to set this to the Package ID.
```
<stringname="custom_url_scheme">com.capacitorjs.myapp</string>
```

In this example, the app will respond to URLs with the `com.capacitorjs.myapp://` scheme.
To get any custom URL the app may have launched with, see the Deeplinks section above.
## Setting Permissions​
In Android, permissions your app will need are defined in `AndroidManifest.xml` inside of the `<manifest>` tag, generally at the bottom of the file.
For example, here's what adding Network permissions looks like:
```
<manifestxmlns:android="http://schemas.android.com/apk/res/android"package="com.getcapacitor.myapp"><activity><!-- other stuff --></activity><!-- More stuff --><!-- Your permissions --><!-- Network API --><uses-permissionandroid:name="android.permission.ACCESS_NETWORK_STATE"/></manifest>
```

Generally, the plugin you choose to use will ask you to set a permission. Add it in this file.
## Contents
  * Configuring `AndroidManifest.xml`
  * Changing the Package ID
  * Changing the App Name
  * Deeplinks (aka Android App Links)
  * URL Schemes
  * Setting Permissions


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fandroid%2Fconfiguration&_biz_t=1739811941054&_biz_i=Capacitor%20Documentation&_biz_n=61&rnd=308143&cdn_o=a&_biz_z=1739811941054)
