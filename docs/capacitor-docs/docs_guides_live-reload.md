Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Live Reload is useful for debugging both the web portion of an app as well as native functionality on device hardware or simulators. Rather than deploy a new native binary every time you make a code change, it reloads the browser (or Web View) when changes in the app are detected.
> If running on a device, make sure it is on the same Wi-Fi network as your computer.
## Using with Ionic CLI​
The Ionic CLI includes a complete Live Reload experience, automating all of the steps that are detailed manually below. Install it along with `native-run` (a cross-platform command-line utility for running native binaries on devices and simulators/emulators):
```
npminstall-g @ionic/cli native-run
```

Next, use the `ionic cap run` command to start the Live Reload process:
```
ionic cap run android -l--externalionic cap run ios -l--external
```

This performs an `ionic build`, copies web assets into the specified native platform, then opens the IDE for your native project (Xcode for iOS, Android Studio for Android).
The `server` entry automatically created in `capacitor.config.json` is removed after the command terminates. For complete details on the `ionic cap run` command, see here.
## Using with Framework CLIs​
Capacitor supports CLIs with live reload capability.
First, determine your computer's IP address on your LAN.
  * On macOS, run `ifconfig`. The IP address is listed under `en0` entry, after `inet`. Alternatively, open System Preferences -> Network -> (select active network) then find the IP listed under Status.
  * On Windows, run `ipconfig`. Look for the `IPv4` address.


Next, start your local web server. The server must be bound to `0.0.0.0` in order to be accessible from the LAN. The command to run will vary, but is typically:
```
npm run start
```

> With react-scripts, use `HOST=0.0.0.0 npm run start`
Within `capacitor.config.json`, create a `server` entry then configure the `url` field using the local web server's IP address and port:
```
"server":{"url":"http://192.168.1.68:8100","cleartext":true},
```

Next, run `npx cap copy` to copy the updated Capacitor config into all native projects.
Open the native IDE if it's not already open:
```
npx cap open iosnpx cap open android
```

Finally, click the Run button to launch the app and start using Live Reload.
> Be careful not to commit the server config to source control.
## Contents
  * Using with Ionic CLI
  * Using with Framework CLIs


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fguides%2Flive-reload&_biz_t=1739811931435&_biz_i=Capacitor%20Documentation&_biz_n=43&rnd=892493&cdn_o=a&_biz_z=1739811931435)
