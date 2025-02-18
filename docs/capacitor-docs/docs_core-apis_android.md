Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Capacitor Android is the native runtime that powers Capacitor apps on Android.
## Bridge​
The Android bridge is the heart of the Capacitor Android library. There are several methods available on the bridge which provide information or change behavior.
When registered with Capacitor, plugins have access to the bridge:
```
this.bridge
```

### getConfig()​
```
publicCapConfiggetConfig()
```

This property contains the configuration object known to the Capacitor runtime.
### triggerJSEvent(...)​
```
publicvoidtriggerJSEvent(finalString eventName,finalString target)publicvoidtriggerJSEvent(finalString eventName,finalString target,finalString data)
```

Fire an event on a JavaScript `EventTarget` such as `window` or `document`. If possible, it is preferred to use Plugin Events instead.
Examples:
```
bridge.triggerJSEvent("myCustomEvent","window");bridge.triggerJSEvent("myCustomEvent","document","{ 'dataKey': 'dataValue' }");
```

Note: `data` must be a serialized JSON string value.
## Passing data​
Notes on how to work with data that is passed between environments can be found here.
## Saving CAPPluginCall​
Notes on persisting plugin calls for asynchronous or repeated operations can be found here.
## Contents
  * Bridge
    * getConfig()
    * triggerJSEvent(...)
  * Passing data
  * Saving CAPPluginCall


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fcore-apis%2Fandroid&_biz_t=1739811946456&_biz_i=Capacitor%20Android%20API%20%7C%20Capacitor%20Documentation&_biz_n=71&rnd=898674&cdn_o=a&_biz_z=1739811946456)
