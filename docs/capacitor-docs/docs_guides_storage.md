Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Most apps need to persist and read local data. Depending on the specific use case, there are a few approaches one can take.
> Need your local data encrypted? Ionic provides an out of the box security suite for Capacitor apps that includes Authentication, Biometrics, and Secure Storage. Learn more.
## Why can't I just use LocalStorage or IndexedDB?​
Since Capacitor apps run primarily in a web view or browser, Web APIs for storage are available to Capacitor developers. However, there are some major caveats to keep in mind with these APIs.
Local Storage can be used for small amounts of temporary data, such as a user id, but _must be considered transient_ , meaning your app needs to expect that the data will be lost eventually. This is because the OS will reclaim local storage from Web Views if a device is running low on space. The same can be said for IndexedDB at least on iOS (on Android, the persisted storage API is available to mark IndexedDB as persisted). Read more on data storage eviction policies in the browser.
## Capacitor Preferences API​
Capacitor comes with a native Preferences API that avoids the eviction issues above, but is meant for small amounts of data.
The Preferences API provides a simple key/value API with no advanced query support:
```
import{ Preferences }from'@capacitor/preferences';// JSON "set" exampleasyncsetObject(){await Preferences.set({  key:'user',  value:JSON.stringify({   id:1,   name:'Max'})});}// JSON "get" exampleasyncgetObject(){const ret =await Preferences.get({ key:'user'});const user =JSON.parse(ret.value);}
```

## Large data or high performance storage options​
For storing large amounts of data and accessing it in a high performance way, there are a few options.
The most widely supported option is SQLite. There are a number of community-maintained SQLite plugins that should work in Capacitor, including capacitor-sqlite and cordova-plugin-sqlite.
The Capacitor team also offers an enterprise SQLite storage solution with encryption support and integration with secure key management APIs on device.
## Contents
  * Why can't I just use LocalStorage or IndexedDB?
  * Capacitor Preferences API
  * Large data or high performance storage options


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fguides%2Fstorage&_biz_t=1739811935322&_biz_i=Storage%20%7C%20Capacitor%20Documentation&_biz_n=50&rnd=72531&cdn_o=a&_biz_z=1739811935322)
