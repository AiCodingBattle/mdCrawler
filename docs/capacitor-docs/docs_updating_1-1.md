Skip to main content
An **OutSystems** Company →
Version: v7
On this page
If you are using an earlier version of Capacitor in your app, there are some recommended changes to make in your app for Capacitor 1.1.0.
## iOS​
Add `Podfile.lock` to the `ios/.gitignore` file:
```
App/buildApp/PodsApp/public+App/Podfile.lockxcuserdata# Cordova plugins for Capacitor
```

## Android​
Remove the `fileprovider_authority` string from the `android/app/src/main/res/values/strings.xml` file:
```
  <string name="app_name">My App</string>  <string name="title_activity_main">My App</string>  <string name="package_name">com.getcapacitor.myapp</string>-  <string name="fileprovider_authority">com.getcapacitor.myapp.fileprovider</string>  <string name="custom_url_scheme">com.getcapacitor.myapp</string></resources>
```

## Contents
  * iOS
  * Android


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fupdating%2F1-1&_biz_t=1739811922922&_biz_i=Capacitor%20Documentation&_biz_n=28&rnd=952780&cdn_o=a&_biz_z=1739811922923)
