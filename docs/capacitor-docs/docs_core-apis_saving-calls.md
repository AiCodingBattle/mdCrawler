Skip to main content
An **OutSystems** Company →
Version: v7
On this page
In most cases, a plugin method will get invoked to perform a task and can finish immediately. But there are situations where you will need to keep the plugin call available so it can be accessed later.
## Overview​
Two reasons you might need a plugin call (`CAPPluginCall` on iOS or `PluginCall` on Android) to persist outside of the method in your plugin are:
  1. To perform an asynchronous action, such as a network request.
  2. To provide repeated updates back to the JavaScript environment, such as streaming live geolocation data.


These two reasons can overlap but there is an important distinction. Specifically, whether or not a call will need to return data more than once. The Capacitor bridge records each call that is made from JavaScript to native so that it can match the result to the correct code when the plugin returns it, and the default behavior is to erase this bookkeeping after `resolve()` or `reject()` is called once. But if your method is a callback that will `resolve()` multiple times, then there is an extra step involved. More information about how to declare callbacks can be found here.
### Saving a call for a single completion​
If you need to save a call to be completed once in the future, you have two options. One option is to simply save it locally in an instance variable. The second is to use the bridge's set of methods to save it and then retrieve it later via the `callbackId`. After calling `resolve()` or `reject()`, you can dispose of the call object as it will no longer be relevant (don't forget to call `releaseCall()` if you used `saveCall()`).
**iOS**
```
funcsaveCall(_ call:CAPPluginCall)funcsavedCall(withID:String)->CAPPluginCall?funcreleaseCall(_ call:CAPPluginCall)funcreleaseCall(withID:String)
```

**Android**
```
voidsaveCall(PluginCall call)PluginCallgetSavedCall(String callbackId)voidreleaseCall(PluginCall call)voidreleaseCall(String callbackId)
```

### Saving a call for multiple completions​
Saving a call to be completed multiple times in the future means two things: saving the native call object itself (as above) and telling the bridge to preserve its bookkeeping so `resolve()` or `reject()` can be invoked repeatedly.
To mark a call this way, set its `keepAlive` property (this was called `isSaved` prior to version 3 but has been renamed to make the behavior clearer).
**iOS**
```
call.keepAlive =true
```

**Android**
```
call.setKeepAlive(true);
```

If `keepAlive` is true, then `resolve()` can be called as many times as necessary and the result will be returned as expected. Setting this flag to true also means that the bridge will automatically call `saveCall()` for you after your method returns.
## Contents
  * Overview
    * Saving a call for a single completion
    * Saving a call for multiple completions


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fcore-apis%2Fsaving-calls&_biz_t=1739811948023&_biz_i=Persisting%20Plugin%20Calls%20%7C%20Capacitor%20Documentation&_biz_n=74&rnd=494795&cdn_o=a&_biz_z=1739811948023)
