Skip to main content
An **OutSystems** Company →
Version: v7
On this page
You can create a new Capacitor application or add Capacitor to your existing web project. This can be done via CLI or using the VS Code extension.
Remember to make sure your environment is set up for the platforms you will be building for.
## Create a new Capacitor app​
The `@capacitor/create-app` package can be used to quickly create a Capacitor application. You can run the following command in an empty directory to scaffold a new Capacitor application.
```
npm init @capacitor/app@latest
```

## Add Capacitor to your web app​
Capacitor was designed to drop into any modern JavaScript web app. However, your project needs to have the following three requirements in order to use Capacitor with your existing application:
  * A `package.json` file
  * A separate directory for built web assets such as `dist` or `www`
  * An `index.html` file at the root of your web assets directory


info
Your `index.html` file must have a `<head>` tag in order to properly inject Capacitor. If you do not have a `<head>` in your Html, Capacitor plugins will not work.
### Install Capacitor​
In the root of your app, install Capacitor's main npm dependencies: the core JavaScript runtime and the command line interface (CLI).
```
npm i @capacitor/corenpm i -D @capacitor/cli
```

### Initialize your Capacitor config​
Then, initialize Capacitor using the CLI questionnaire:
```
npx cap init
```

The CLI will ask you a few questions, starting with your app name, and the package ID you would like to use for your app. It will create the capacitor-config file with these configuration details, including the expected output directory for the build process of your bundler (e.g. `www` for Angular, `build` for React, `public` for Vue, etc.).
info
You can customize the folder used by Capacitor by modifying the `webDir` variable in your Capacitor Config file that is created during `npx cap init`. Please note that Capacitor will try to detect the default for your web-project by checking the framework you are using. Nevertheless, it is a good idea to cross-check this configuration variable when having issues syncing your first build.
### Create your Android and iOS projects​
After the Capacitor core runtime is installed, you can install the Android and iOS platforms.
```
npm i @capacitor/android @capacitor/ios
```

Once the platforms have been added to your `package.json`, you can run the following commands to create your Android and iOS projects for your native application.
```
npx cap add androidnpx cap add ios
```

### Sync your web code to your native project​
Once you've created your native projects, you can sync your web application to your native project by running the following command.
```
npx cap sync
```

`npx cap sync` will copy your built web bundle expected to be found in `webDir` of the Capacitor Config file to your native project and install the native project's dependencies.
## Where to go next​
With your environment setup, and your project structure set up properly, you're ready to go! You can follow any of the links below if you need more specific documentation.
Get started with iOS ›
Get started with Android ›
Developer Workflow Guide ›
## Contents
  * Create a new Capacitor app
  * Add Capacitor to your web app
    * Install Capacitor
    * Initialize your Capacitor config
    * Create your Android and iOS projects
    * Sync your web code to your native project
  * Where to go next


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fgetting-started&_biz_t=1739811911856&_biz_i=Installing%20Capacitor%20%7C%20Capacitor%20Documentation&_biz_n=9&rnd=324302&cdn_o=a&_biz_z=1739811911857)
