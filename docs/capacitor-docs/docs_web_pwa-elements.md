Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Some Capacitor plugins, such as `Camera` or `Toast`, have web-based UI available when not running natively. For example, calling `Camera.getPhoto()` will load a responsive photo-taking experience when running on the web:
![PWA Elements](https://capacitorjs.com/docs/assets/images/pwa-elements-83772729c23c280653593cc5f28d543b.png)
This UI is implemented using web components. Due to the elements being encapsulated by the Shadow DOM, these components should not conflict with your own UI.
## Installation​
To enable these controls, you must add `@ionic/pwa-elements` to your app.
A typical installation involves importing the package and registering the elements, or adding a script tag to the `<head>` of the `index.html` for your app:
#### Importing PWA Elements​
```
npminstall @ionic/pwa-elements
```

Then, depending on your framework of choice, import the element loader and call it at the correct time:
##### React​
`main.tsx` or `index.tsx` or `index.js`:
```
import{ defineCustomElements }from'@ionic/pwa-elements/loader';// Call the element loader before the render calldefineCustomElements(window);
```

##### Vue​
`main.ts`:
```
// Above the createApp() lineimport{ defineCustomElements }from'@ionic/pwa-elements/loader';defineCustomElements(window);
```

##### Angular​
`main.ts`:
```
import{ defineCustomElements }from'@ionic/pwa-elements/loader';// Call the element loader before the bootstrapModule/bootstrapApplication calldefineCustomElements(window);if(environment.production){enableProdMode();}
```

#### Including through script tag​
PWA Elements can be included through a script tag in your `index.html`. However, keep in mind this will not work for offline scenarios:
```
<scripttype="module"src="https://unpkg.com/@ionic/pwa-elements@latest/dist/ionicpwaelements/ionicpwaelements.esm.js"></script><scriptnomodulesrc="https://unpkg.com/@ionic/pwa-elements@latest/dist/ionicpwaelements/ionicpwaelements.js"></script>
```

## Contents
  * Installation


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fweb%2Fpwa-elements&_biz_t=1739811944687&_biz_i=PWA%20Elements%20%7C%20Capacitor%20Documentation&_biz_n=68&rnd=989629&cdn_o=a&_biz_z=1739811944688)
