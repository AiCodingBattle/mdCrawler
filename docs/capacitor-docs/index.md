**Important Announcement:** The Future of Ionic’s Commercial Products →
# A cross-platform native runtime for web apps.
Capacitor is an open source native runtime for building Web Native apps. Create cross-platform iOS, Android, and Progressive Web Apps with JavaScript, HTML, and CSS.
Install Capacitor →Explore Plugins
Migrate from Cordova →
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2791%27%20height=%2716%27/%3e)![apple, android and pwa icons](https://capacitorjs.com/_next/image?url=https%3A%2F%2Fimages.prismic.io%2Fionicframeworkcom%2F2572b6ec-4952-4ba7-959a-d8aabe80a5c2_capacitor-homepage-top-1%25402x.png&w=256&q=75)
![multi layered phone](https://capacitorjs.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftop-0.4b4e40aa.png&w=1200&q=75)
## Get started _easily._
01
### Drop Capacitor into any existing web app.
```

npm install @capacitor/cli @capacitor/core
npx cap init

```

02
### Install the native platforms you want to target.
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2722%27%20height=%2726%27/%3e)![apple icon](https://capacitorjs.com)
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2727%27%20height=%2723%27/%3e)![android icon](https://capacitorjs.com)
```

npm install @capacitor/ios @capacitor/android
npx cap add ios
npx cap add android

```

03
### Access core Native APIs or extend with your own.
Capacitor’s native plugin APIs make it extremely easy to access and invoke common device functionality across multiple platforms.
```

```

import{ LocalNotifications }from'@capacitor/local-notifications';
LocalNotifications.schedule({
 notifications:[
{
   title:"On sale",
   body:"Widgets are 10% off. Act fast!",
   id:1,
   schedule:{ at:newDate(Date.now()+1000*5)},
   sound:null,
   attachments:null,
   actionTypeId:"",
   extra:null
}
]
});

```
```

import{ Geolocation }from'@capacitor/geolocation';
// get the users current position
const position =await Geolocation.getCurrentPosition();
// grab latitude & longitude
const latitude = position.coords.latitude;
const longitude = position.coords.longitude;

```
```

import{ Camera, CameraResultType }from'@capacitor/camera';
// Take a picture or video, or load from the library
const picture =await Camera.getPicture({
 resultType: CameraResultType.Uri
});

```
```

import Foundation
import Capacitor
// Custom platform code, easily exposed to your web app
// through Capacitor plugin APIs. Build APIs that work
// across iOS, Android, and the web!
@objc(MyAwesomePlugin)
publicclassMyAwesomePlugin: CAPPlugin {
@objcpublic func doNative(_ call: CAPPluginCall){
let alert =UIAlertController(title:"Title", message:"Please Select an Option", preferredStyle:.actionSheet)
// ....
}
}

```


```

## Building Cross-platform Apps with Capacitor
 _Ship cross-platform mobile apps 10X faster._ We wrote a free guide on when and why to use Capacitor to build cross-platform apps.
Read the free eBook →
## Connect web apps to _native functionality._
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2748%27%20height=%2764%27/%3e)![triple phone icon](https://capacitorjs.com)
#### Universal apps
Build web-based applications that run equally well across iOS, Android, and as Progressive Web Apps.
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2760%27%20height=%2764%27/%3e)![Cube with sphere inside icon](https://capacitorjs.com)
#### Native access
Access the full Native SDKs on each platform, and easily deploy to the App Stores (and the web).
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2760%27%20height=%2764%27/%3e)![Tripe phone stack layered icon](https://capacitorjs.com)
#### Native PWAs
Add custom native functionality with a simple Plugin API, or use existing Cordova plugins with our compatibility layer.
## Cross-platform, c _ore native plugins._
Explore APIs →
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2740%27%20height=%2732%27/%3e)![camera icon](https://capacitorjs.com)
#### Camera
Capture images, save photos, and configure hardware parameters like saturation and color balance.
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2740%27%20height=%2732%27/%3e)![file system icon](https://capacitorjs.com)
#### File System
Save and read documents, assets, and other content your users need to access via native file systems.
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2732%27%20height=%2732%27/%3e)![antenna icon](https://capacitorjs.com)
#### Geolocation
Gather critical information about a user’s device location, such as latitude and longitude.
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2733%27%20height=%2732%27/%3e)![spherical rings icon](https://capacitorjs.com)
#### Accelerometer
Access the device accelerometer sensors to measures changes in velocity of a device motion.
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2728%27%20height=%2732%27/%3e)![bell icon](https://capacitorjs.com)
#### Notifications
Schedule local notifications on the device or handle push notifications sent from a server.
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2732%27%20height=%2732%27/%3e)![person with circle around icon](https://capacitorjs.com)
#### Network
Monitor for network connectivity and capability changes to build resilient offline apps.
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2732%27%20height=%2732%27/%3e)![three encompassing circles icon](https://capacitorjs.com)
#### Haptics
Add physical feedback through haptic features available on modern devices.
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2732%27%20height=%2730%27/%3e)![slider adjustment icon](https://capacitorjs.com)
#### Your Own Plugin
Write your own custom plugins to access specialty features and easily integrate any 3rd-party SDK.
## Bring your own w _eb framework._
Drop Capacitor into any existing web project, framework or library. Convert an existing React, Svelte, Vue (or your preferred Web Framework) project to native mobile.
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27200%27/%3e)![react logo tile](https://capacitorjs.com)
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27200%27/%3e)![angular logo tile](https://capacitorjs.com)
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27200%27/%3e)![svelte logo tile](https://capacitorjs.com)
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27200%27/%3e)![vue logo tile](https://capacitorjs.com)
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27200%27/%3e)![stencil logo tile](https://capacitorjs.com)
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27200%27/%3e)![qwik logo tile](https://capacitorjs.com)
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27200%27/%3e)![bootstrap logo tile](https://capacitorjs.com)
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27200%27/%3e)![ionic logo tile](https://capacitorjs.com)
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27200%27/%3e)![material UI logo tile](https://capacitorjs.com)
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27200%27/%3e)![tailwind logo tile](https://capacitorjs.com)
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27200%27/%3e)![framework 7 logo tile](https://capacitorjs.com)
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27272%27%20height=%27200%27/%3e)![quasar logo tile](https://capacitorjs.com)
## What people are saying a _bout Capacitor._
### Austin Howard
@a_howard8
I’m reallllyyyy digging capacitor 👀
### Angular
@angular
Did you know @capacitorjs shows how to give your #Angular app access to mobile APIs and a presence in app stores?
### scriptkitty
@thr0wsException
I'm pretty hyped to be honest, from what I've seen so far this will be another major step for establishing web technology as the go-to method for developing cross platform apps ♥
### Adeniyi Tolulope
@tolutronics
@capacitorjs has been a great companion this year... with realtime updates.
### Guillermo Rauch
@rauchg
Amazing that this is @vercel Next.js + @tailwindcss + @capacitorjs 🤯
### Carlos Martinez
@cmartineztech
Yes, It works 😱 deep linking and google native authentication in iOS @capacitorjs
### Greg Marine
@gregmarine
One of the nice things about Capacitor is that you don’t have to use Ionic. I personally love Ionic and use it for UI components. But it isn’t required for Capacitor 😊
### Jacob Clark
@imjacobclark
We blogged about how we use Capacitor to build our 4 Children’s apps at the @BBC
### Dayana Jabif
@dayujabif
I still can't believe how easy is to turn an @Ionicframework app into a native iOS app using @capacitorjs 🤯
### Leo
@creativiii
I've tried React Native but coming from web dev the DX is such a step down. Give @capacitorjs a go if you're building apps 👀
### Tim S
@tdawgpharaoh
I am asking myself, how did I not hear about @capacitorjs until recently. Very nice.
### Daniel Rodrigues
@inspire_rd
Tried out @capacitorjs soon after it went stable - amazing! Simple & straight forward.
👋
The Capacitor Community is growing. _Connect with us and say Hello._
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2724%27%20height=%2724%27/%3e)![X icon](https://capacitorjs.com)
#### Follow us on X
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2724%27%20height=%2724%27/%3e)![Github icon](https://capacitorjs.com)
#### Star us on GitHub
![](data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2724.5%27%20height=%2724%27/%3e)![Chat bubble icon](https://capacitorjs.com)
#### Join the Forum
#### Installation Guide →
Install Capacitor and learn how to start building with it
#### Explore Native Plugins →
Explore Native Plugins that are available to all Capacitor apps
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs&_biz_t=1739811907220&_biz_i=Capacitor%20-%20Cross-platform%20Native%20Runtime%20for%20Web%20Apps%20%7C%20Capacitor%20Documentation&_biz_n=0&rnd=897736&cdn_o=a&_biz_z=1739811907528)![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2F&_biz_t=1739811907527&_biz_i=Capacitor%20by%20Ionic%20-%20Cross-platform%20apps%20with%20web%20technology&_biz_n=1&rnd=282338&cdn_o=a&_biz_z=1739811907528)![](https://cdn.bizibly.com/u?_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2F&_biz_t=1739811907528&_biz_i=Capacitor%20by%20Ionic%20-%20Cross-platform%20apps%20with%20web%20technology&rnd=528045&cdn_o=a&_biz_z=1739811907528)
