Skip to main content
An **OutSystems** Company →
Version: v7
On this page
With Capacitor, you are encouraged to write Java or Kotlin code to implement the native features your app needs.
There may not be a Capacitor plugin for everything--and that's okay! It is possible to write WebView-accessible native code right in your app.
## WebView-Accessible Native Code​
The easiest way to communicate between JavaScript and native code is to build a custom Capacitor plugin that is local to your app.
### `EchoPlugin.java`​
First, create a `EchoPlugin.java` file by opening Android Studio, expanding the **app** module and the **java** folder, right-clicking on your app's Java package, selecting **New** -> **Java Class** from the context menu, and creating the file.
![Android Studio app package](https://capacitorjs.com/docs/assets/images/studio-app-package-d8ea69501afb5af58ed1fddd0d007cbe.png)
Copy the following Java code into `EchoPlugin.java`:
```
packagecom.example.myapp;importcom.getcapacitor.JSObject;importcom.getcapacitor.Plugin;importcom.getcapacitor.PluginCall;importcom.getcapacitor.PluginMethod;importcom.getcapacitor.annotation.CapacitorPlugin;@CapacitorPlugin(name ="Echo")publicclassEchoPluginextendsPlugin{@PluginMethod()publicvoidecho(PluginCall call){String value = call.getString("value");JSObject ret =newJSObject();    ret.put("value", value);    call.resolve(ret);}}
```

### Register the Plugin​
We must register custom plugins on both Android and web so that Capacitor can bridge between Java and JavaScript.
#### `MainActivity.java`​
In your app's `MainActivity.java`, use `registerPlugin()` or `registerPlugins()` to register your custom plugin(s).
```
public class MainActivity extends BridgeActivity {  @Override  public void onCreate(Bundle savedInstanceState) {+    registerPlugin(EchoPlugin.class);    super.onCreate(savedInstanceState);  }}
```

#### JavaScript​
In JS, we use `registerPlugin()` from `@capacitor/core` to create an object which is linked to our Java plugin.
```
import{ registerPlugin }from'@capacitor/core';const Echo =registerPlugin('Echo');exportdefault Echo;
```

> The first parameter to `registerPlugin()` is the plugin name, which must match the `name` attribute of our `@CapacitorPlugin` annotation in `EchoPlugin.java`.
**TypeScript**
We can define types on our linked object by defining an interface and using it in the call to `registerPlugin()`.
```
import { registerPlugin } from '@capacitor/core';+export interface EchoPlugin {+ echo(options: { value: string }): Promise<{ value: string }>;+}-const Echo = registerPlugin('Echo');+const Echo = registerPlugin<EchoPlugin>('Echo');export default Echo;
```

The generic parameter of `registerPlugin()` is what defines the structure of the linked object. You can use `registerPlugin<any>('Echo')` to ignore types if you need to. No judgment. ❤️
### Use the Plugin​
Use the exported `Echo` object to call your plugin methods. The following snippet will call into Java on Android and print the result:
```
import Echo from'../path/to/echo-plugin';const{ value }=await Echo.echo({ value:'Hello World!'});console.log('Response from native:', value);
```

### Next Steps​
Read the Android Plugin Guide ›
## Contents
  * WebView-Accessible Native Code
    * `EchoPlugin.java`
    * Register the Plugin
    * Use the Plugin
    * Next Steps


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fandroid%2Fcustom-code&_biz_t=1739811941622&_biz_i=Custom%20Native%20Android%20Code%20%7C%20Capacitor%20Documentation&_biz_n=62&rnd=156189&cdn_o=a&_biz_z=1739811941623)
