Skip to main content
An **OutSystems** Company →
Version: v7
On this page
All Android applications must specify a target SDK version, or the version of Android that the application is designed to run on. Each year, Google releases updates to the Android operating system and subsequently bumps the version number that applications are required to target. Typically, this date is August 31st of each year. Because of this, it is important to keep your application up to date with the latest version of Android. In a Capacitor application, this is done by specifying your target SDK in the `/android/variables.gradle` file.
```
targetSdkVersion =34
```

## Capacitor Android Requirements​
In Capacitor, the Android target SDK version is strongly tied to the major version of Capacitor. This means that while you could change the target SDK to a higher version and rebuild your application, there's a very strong likelihood that your application will experience issues not otherwise present. The Capacitor team releases a new major version of Capacitor every year that includes support for the new target SDK version to ensure that applications remain compliant with Google's requirements. For this reason, it is important to keep your application up to date with the latest major version of Capacitor.
## Android Target SDK Matrix​
The following table shows the target SDK versions that are supported by Capacitor Android.
Capacitor Android| Target SDK Version  
---|---  
6.x| 34  
5.x| 33  
4.x| 32  
3.x| 30  
2.x| 29  
1.x| 28  
## Custom Target SDK Versions​
Capacitor Android does not support custom target SDK versions. Each version of Capacitor Android requires a specific target SDK version and support is only provided for that matching version.
## Contents
  * Capacitor Android Requirements
  * Android Target SDK Matrix
  * Custom Target SDK Versions


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fandroid%2Fsetting-target-sdk&_biz_t=1739811942174&_biz_i=Setting%20Android%20Target%20SDK%20%7C%20Capacitor%20Documentation&_biz_n=63&rnd=244380&cdn_o=a&_biz_z=1739811942174)
