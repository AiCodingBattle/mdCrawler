Skip to main content
An **OutSystems** Company →
Version: v7
On this page
You can generate Splash Screens and Icons for your iOS, Android or Progressive Web Application using the @capacitor/assets tool.
First, install `@capacitor/assets`:
```
npminstall @capacitor/assets --save-dev
```

Provide icon and splash screen source images using this folder/filename structure:
```
assets/├── icon-only.png├── icon-foreground.png├── icon-background.png├── splash.png└── splash-dark.png
```

  * Icon files should be at least `1024px` x `1024px`.
  * Splash screen files should be at least `2732px` x `2732px`.
  * The format can be `jpg` or `png`.


Then generate (which applies to your native projects or generates a PWA manifest file):
```
npx capacitor-assets generate
```

Alternatively you can generate for a specific platform with `--ios`, `--android` or `--pwa`.
note
The VS Code Extension can also generate Splash Screen and Icon assets.
## Android 12+​
In Android 12 and above Google changed the way Splash Screens are displayed, using a smaller icon with colored background instead of a full screen image that was possible with Android 11 and below. Additional documentation about this change can be found at developer.android.com.
## Contents
  * Android 12+


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fguides%2Fsplash-screens-and-icons&_biz_t=1739811934865&_biz_i=Splash%20Screens%20and%20Icons%20%7C%20Capacitor%20Documentation&_biz_n=49&rnd=226798&cdn_o=a&_biz_z=1739811934865)
