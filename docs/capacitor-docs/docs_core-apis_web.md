Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Capacitor has several JavaScript utilities useful for ensuring apps run successfully across multiple platforms with the same codebase. To use them, import Capacitor then call the desired utility function:
## Capacitor Object​
The `Capacitor` object is a container for several utility functions. It is available at `window.Capacitor`, but the preferred usage for modern JavaScript apps is to import it:
```
import{ Capacitor }from'@capacitor/core';
```

### convertFileSrc(...)​
```
convertFileSrc:(filePath:string)=>string;
```

Convert a device filepath into a Web View-friendly path.
Capacitor apps are served on a different protocol than device files. To avoid difficulties between these protocols, paths to device files must be rewritten. For example, on Android, `file:///path/to/device/file` must be rewritten as `http://localhost/_capacitor_file_/path/to/device/file` before being used in the Web View.
```
// file:///path/to/device/photo.jpgconst savedPhotoFile =await Filesystem.writeFile({ path:"myFile.jpg", data: base64Data, directory: FilesystemDirectory.Data});// http://localhost/path/to/device/photo.jpgconst savedPhoto = Capacitor.convertFileSrc(savedPhotoFile.uri),document.getElementById("savedPhoto").src = savedPhoto;
```

```
<imgid="savedPhoto"/>
```

### getPlatform()​
```
getPlatform:()=>string;
```

Get the name of the platform the app is currently running on: `web`, `ios`, `android`.
```
if(Capacitor.getPlatform()==='ios'){// do something}
```

### isNativePlatform()​
```
isNativePlatform:()=>boolean;
```

Check whether the currently running platform is native (`ios`, `android`).
```
if(Capacitor.isNativePlatform()){// do something}
```

### isPluginAvailable(...)​
```
isPluginAvailable:(name:string)=>boolean;
```

Check if a plugin is available on the currently running platform. The plugin name is used in the plugin registry, which means it also works with custom plugins.
```
const isAvailable = Capacitor.isPluginAvailable('Camera');if(!isAvailable){// Have the user upload a file instead}else{// Otherwise, make the call:const image =await Camera.getPhoto({  resultType: CameraResultType.Uri,});}
```

## Contents
  * Capacitor Object
    * convertFileSrc(...)
    * getPlatform()
    * isNativePlatform()
    * isPluginAvailable(...)


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fcore-apis%2Fweb&_biz_t=1739811946977&_biz_i=Capacitor%20Web%20API%20%7C%20Capacitor%20Documentation&_biz_n=72&rnd=85776&cdn_o=a&_biz_z=1739811946978)
