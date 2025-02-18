Skip to main content
An **OutSystems** Company →
Version: v7
On this page
## Configuring `Info.plist`​
The `Info.plist` file is the main configuration file for iOS apps. You may need to edit it whenever a Capacitor plugin requires new settings or permissions.
To modify it, open your project in Xcode, select the **App** project and the **App** target, and click the **Info** tab.
![Xcode info editor](https://capacitorjs.com/docs/assets/images/xcode-info-editor-4b475489f535a93850f8a18b57cb7d47.png)
> You can show the true key names by right-clicking in the table and checking **Raw Keys & Values** in the context menu.
> You can also open and edit the `ios/App/App/Info.plist` file manually to inspect the raw keys. Use this reference documentation for a list of possible keys.
## Managing Permissions​
iOS permissions do not need to be specified explicitly like they are in Android. However, iOS requires "Usage Descriptions" to be defined in `Info.plist`. These settings are human-readable descriptions that will be presented to the end user when permission is requested for a particular device API.
Consult the Cocoa Keys list for keys containing `UsageDescription` to see the various usage description settings that may be required for your app.
For more information, Apple has provided a guide to Resolving the Privacy-Sensitive Data App Rejection which contains more information on APIs that require usage descriptions.
## Setting Capabilities​
Capabilities are used to enable key features that your app may need. You may need to configure them whenever a Capacitor plugin requires it.
Unlike other configuration options and usage descriptions, capabilities are _not_ configured in `Info.plist`.
To add a new capability, open your app in Xcode, select the **App** project and the **App** target, click **Signing & Capabilities** in the tab bar, and then click the **+ Capability** button. See this article for more information about iOS capabilities.
![Xcode Capabilities](https://capacitorjs.com/docs/assets/images/xcode-capabilities-a6777da78cd883cfff5e81deed55460a.png)
## Renaming your App​
You can't rename the `App` directory, but you can set the name of your app by renaming the **App** target.
To rename the **App** target, open your project in Xcode, select the **App** project, and double-click the **App** target.
![Xcode Target](https://capacitorjs.com/docs/assets/images/xcode-target-dab040971aa4c1c12cbcfb96c5fa4a12.png)
Then, open `ios/App/Podfile` and rename the current target at the bottom of the file:
```
-target 'App' do+target 'MyRenamedApp' do capacitor_pods # Add your Pods hereend
```

Finally, add the `scheme` attribute inside the `ios` object in the Capacitor configuration file.
## Deeplinks (aka Universal Links)​
For a Deep Links guide, see here.
## Contents
  * Configuring `Info.plist`
  * Managing Permissions
  * Setting Capabilities
  * Renaming your App
  * Deeplinks (aka Universal Links)


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fios%2Fconfiguration&_biz_t=1739811936750&_biz_i=Capacitor%20Documentation&_biz_n=53&rnd=558074&cdn_o=a&_biz_z=1739811936751)
