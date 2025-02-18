Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Capacitor iOS is the native runtime that powers Capacitor apps on iOS.
## Bridge​
The iOS bridge is the heart of the Capacitor iOS library. There are several properties and methods available on the bridge which provide information or change behavior.
When registered with Capacitor, plugins have a weak reference to the bridge:
```
self.bridge?
```

> If your method requires the bridge, you can use a guard to unwrap it and perform an early exit:
> ```
guardlet bridge =self.bridge else{return}
```

### viewController​
```
var viewController:UIViewController?{get}
```

This property contains the main view controller for Capacitor, which can be used to present native views over the app.
Examples:
```
DispatchQueue.main.async{self.bridge?.viewController.present(ourCustomViewController, animated:true, completion:nil)}
```

On iPad devices it is possible to present popovers:
```
self.setCenteredPopover(ourCustomViewController)self.bridge.viewController.present(ourCustomViewController, animated:true, completion:nil)
```

### config​
```
var config:InstanceConfiguration{get}
```

This property contains the configuration object known to the Capacitor runtime.
### triggerJSEvent(...)​
```
functriggerJSEvent(eventName:String, target:String)functriggerJSEvent(eventName:String, target:String, data:String)
```

Fire an event on a JavaScript `EventTarget` such as `window` or `document`. If possible, it is preferred to use Plugin Events instead.
Examples:
```
bridge.triggerJSEvent(eventName:"myCustomEvent", target:"window")bridge.triggerJSEvent(eventName:"myCustomEvent", target:"document", data:"{ 'dataKey': 'dataValue' }")
```

Note: `data` must be a serialized JSON string value.
### localURL(...)​
```
funclocalURL(fromWebURL webURL:URL?)->URL?
```

Translate a URL from the web view into a file URL for native iOS.
The web view may be handling several different types of URLs:
  * `res://` (shortcut scheme to web assets)
  * `file://` (fully qualified URL to file on the local device)


### portablePath(...)​
```
funcportablePath(fromLocalURL localURL:URL?)->URL?
```

Translate a file URL for native iOS into a URL to load in the web view.
## Passing data​
Notes on how to work with data that is passed between environments can be found here.
## Saving CAPPluginCall​
Notes on persisting plugin calls for asynchronous or repeated operations can be found here.
## Contents
  * Bridge
    * viewController
    * config
    * triggerJSEvent(...)
    * localURL(...)
    * portablePath(...)
  * Passing data
  * Saving CAPPluginCall


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fcore-apis%2Fios&_biz_t=1739811945946&_biz_i=Capacitor%20iOS%20API%20%7C%20Capacitor%20Documentation&_biz_n=70&rnd=749106&cdn_o=a&_biz_z=1739811945947)
