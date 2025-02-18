Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Since Capacitor 3.0, you can subclass `CAPBridgeViewController` within your application. Most applications do not need this feature but it provides a supported mechanism for addressing some use-cases.
## When to create a subclass​
Some examples of when subclassing would be necessary are overriding Capacitor's configuration values at run-time, changing the properties of the `WKWebViewConfiguration`, subsituting a custom subclass of `WKWebView` for Capacitor to use, integrating a 3rd party SDK that suggests adding code to `viewDidLoad()`, manipulating native views before they appear onscreen, or registering custom plugins.
If you do need to create a custom subclass, there are a couple of steps to get started.
### Create `MyViewController.swift`​
First, create a `MyViewController.swift` file by opening Xcode, right-clicking on the **App** group (under the **App** target), selecting **New File...** from the context menu, choosing **Cocoa Touch Class** in the window, set the **Subclass of:** to `UIViewController` in the next screen, and save the file.
![New ViewController in Xcode](https://capacitorjs.com/docs/assets/images/xcode-create-viewcontroller-df74f96e1a5d5640f6e9c6b5fc07040b.png) ![Name ViewController in Xcode](https://capacitorjs.com/docs/assets/images/xcode-name-viewcontroller-d7fe79edd3e838a8ca4a469fbef4dd0d.png)
### Edit `Main.storyboard`​
Next, select the `Main.storyboard` file in the Project Navigator, select the **Bridge View Controller** in the **Bridge View Controller Scene** , select the **Identity Inspector** on the right, and change the name of the custom class to `MyViewController`.
![Editing Storyboard in Xcode](https://capacitorjs.com/docs/assets/images/xcode-edit-storyboard-4cf3fb4df80b7e45cfd99ee5b5c66fbe.png)
### Edit `MyViewController.swift`​
Finally, select the `MyViewController.swift` file in the Project Navigator and edit it to import Capacitor and change the parent class:
```
importUIKitimportCapacitorclassMyViewController:CAPBridgeViewController{// additional code}
```

You're done!
### Next Steps​
Xcode should have already created a `viewDidLoad()` method for you when it generated the file but look over the inline documentation in `CAPBridgeViewController` to find the Capacitor-specific methods you might need. Anything marked `open` is explicitly exposed for subclasses to override.
## Contents
  * When to create a subclass
    * Create `MyViewController.swift`
    * Edit `Main.storyboard`
    * Edit `MyViewController.swift`
    * Next Steps


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fios%2Fviewcontroller&_biz_t=1739811938957&_biz_i=Capacitor%20Documentation&_biz_n=57&rnd=990646&cdn_o=a&_biz_z=1739811938958)
