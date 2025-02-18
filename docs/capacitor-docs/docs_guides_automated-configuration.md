Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Many large-scale apps need to automate the configuration of their Capacitor project. This could mean incrementing iOS and Android build numbers, configuring manifest and plist files, adding build dependencies in Gradle files, modifying resources, and more.
Capacitor comes with a two useful packages that can be used for managing projects: `@trapezedev/project` and `@trapezedev/configure`. `@trapezedev/project` is a lower-level project management library and `@trapezedev/configure` is an automated tool that uses the library under the hood but presents a more convenient configuration option for certain use cases.
Both projects and their documentation are available in the Trapeze repo.
## Project API​
The `@trapezedev/project` library provides a typed JavaScript interface for Capacitor projects and the native iOS and Android projects that they contain.
```
import{ MobileProject, MobileProjectConfig }from'@trapezedev/project';// This takes a MobileProjectConfig// to know where the ios and android projects areconst config: MobileProjectConfig ={ ios:{  path:'ios/App',}, android:{  path:'android',},};const project =newMobileProject(process.cwd(), config);await project.load();
```

Once the project is loaded, operations can be performed against it. For example, here is how versions and build numbers can be managed:
```
await project.ios?.setVersion('App','Debug','1.4.5');await project.ios?.incrementBuild('App');await project.ios?.getBuild('App','Debug');await project.ios?.getBuild('App','Release');await project.android?.setVersionName('1.0.2');await project.android?.getVersionName();await project.android?.setVersionCode(11);await project.android?.getVersionCode();await project.android?.incrementVersionCode();
```

The API works on a virtual filesystem to buffer changes without modifying files on the filesystem. When finished, to make sure changes are reflected in your files, run:
```
await project.commit();
```

There are many other options this library can perform. To see the full list, consult the project documentation.
## Configuration Tool​
Along with the project API, `@trapezedev/configure` provides an automated, configuration-driven experience for applying the underlying operations in `@trapezedev/project`, but from a convenient yaml configuration file format. There are some additional features as well, such as the ability to require and supply variables to populate values in the final configuration, and a way to test and see changes before they are applied against your project source files.
This tool is likely going to be most useful for Capacitor plugin authors that wish to publish a set of configuration changes their plugin requires, to avoid users having to manually configure their projects.
This tool is meant to be used as an npm script that is then supplied with a yaml format that follows the example configuration:
```
"scripts":{"cap-config":"trapeze run config.yaml"}
```

```
npm run cap-config
```

Consult the project documentation for more information on using this tool.
## Contents
  * Project API
  * Configuration Tool


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fguides%2Fautomated-configuration&_biz_t=1739811927709&_biz_i=Automated%20Configuration%20%7C%20Capacitor%20Documentation&_biz_n=36&rnd=745230&cdn_o=a&_biz_z=1739811927709)
