Skip to content
# Configuration Files
Since Tauri is a toolkit for building applications there can be many files to configure project settings. Some common files that you may run across are `tauri.conf.json`, `package.json` and `Cargo.toml`. We briefly explain each on this page to help point you in the right direction for which files to modify.
## Tauri Config
The Tauri configuration is used to define the source of your Web app, describe your application’s metadata, configure bundles, set plugin configurations, modify runtime behavior by configuring windows, tray icons, menus and more.
This file is used by the Tauri runtime and the Tauri CLI. You can define build settings (such as the command run before `tauri build` or `tauri dev` kicks in), set the name and version of your app, control the Tauri runtime, and configure plugins.
### Supported Formats
The default Tauri config format is JSON. The JSON5 or TOML format can be enabled by adding the `config-json5` or `config-toml` feature flag (respectively) to the `tauri` and `tauri-build` dependencies in `Cargo.toml`.
Cargo.toml```

[build-dependencies]
tauri-build = { version = "2.0.0", features = [ "config-json5" ] }
[dependencies]
tauri = { version = "2.0.0", features = [ "config-json5" ] }

```

The structure and values are the same across all formats, however, the formatting should be consistent with the respective file’s format:
tauri.conf.json```

{
build: {
devUrl: 'http://localhost:3000',
// start the dev server
beforeDevCommand: 'npm run dev',
},
bundle: {
active: true,
icon: ['icons/app.png'],
},
app: {
windows: [
{
title: 'MyApp',
},
],
},
plugins: {
updater: {
pubkey: 'updater pub key',
endpoints: ['https://my.app.updater/{{target}}/{{current_version}}'],
},
},
}

```

Tauri.toml```

[build]
dev-url = "http://localhost:3000"
# start the dev server
before-dev-command = "npm run dev"
[bundle]
active = true
icon = ["icons/app.png"]
[[app.windows]]
title = "MyApp"
[plugins.updater]
pubkey = "updater pub key"
endpoints = ["https://my.app.updater/{{target}}/{{current_version}}"]

```

Note that JSON5 and TOML supports comments, and TOML can use kebab-case for config names which are more idiomatic.
### Platform-specific Configuration
In addition to the default configuration file, Tauri can read a platform-specific configuration from:
  * `tauri.linux.conf.json` or `Tauri.linux.toml` for Linux
  * `tauri.windows.conf.json` or `Tauri.windows.toml` for Windows
  * `tauri.macos.conf.json` or `Tauri.macos.toml` for macOS
  * `tauri.android.conf.json` or `Tauri.android.toml` for Android
  * `tauri.ios.conf.json` or `Tauri.ios.toml` for iOS


The platform-specific configuration file gets merged with the main configuration object following the JSON Merge Patch (RFC 7396) specification.
For example, given the following base `tauri.conf.json`:
tauri.conf.json```

{
"productName": "MyApp",
"bundle": {
"resources": ["./resources"]
},
"plugins": {
"deep-link": {}
}
}

```

And the given `tauri.linux.conf.json`:
tauri.linux.conf.json```

{
"productName": "my-app",
"bundle": {
"resources": ["./linux-assets"]
},
"plugins": {
"cli": {
"description": "My app",
"subcommands": {
"update": {}
}
},
"deep-link": {}
}
}

```

The resolved configuration for Linux would be the following object:
```

{
"productName": "my-app",
"bundle": {
"resources": ["./linux-assets"]
},
"plugins": {
"cli": {
"description": "My app",
"subcommands": {
"update": {}
}
},
"deep-link": {}
}
}

```

Additionally you can provide a configuration to be merged via the CLI, see the following section for more information.
### Extending the Configuration
The Tauri CLI allows you to extend the Tauri configuration when running one of the `dev`, `android dev`, `ios dev`, `build`, `android build`, `ios build` or `bundle` commands. The configuration extension can be provided by the `--config` argument either as a raw JSON string or as a path to a JSON file. Tauri uses the JSON Merge Patch (RFC 7396) specification to merge the provided configuration value with the originally resolved configuration object.
This mechanism can be used to define multiple flavours of your application or have more flexibility when configuring your application bundles.
For instance to distribute a completely isolated _beta_ application you can use this feature to configure a separate application name and identifier:
src-tauri/tauri.beta.conf.json```

{
"productName": "My App Beta",
"identifier": "com.myorg.myappbeta"
}

```

And to distribute this separate _beta_ app you provide this configuration file when building it:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauribuild----configsrc-tauri/tauri.beta.conf.json

```

```

yarntauribuild--configsrc-tauri/tauri.beta.conf.json

```

```

pnpmtauribuild--configsrc-tauri/tauri.beta.conf.json

```

```

denotasktauribuild--configsrc-tauri/tauri.beta.conf.json

```

```

cargotauribuild--configsrc-tauri/tauri.beta.conf.json

```

## `Cargo.toml`
Cargo’s manifest file is used to declare Rust crates your app depends on, metadata about your app, and other Rust-related features. If you do not intend to do backend development using Rust for your app then you may not be modifying it much, but it’s important to know that it exists and what it does.
Below is an example of a barebones `Cargo.toml` file for a Tauri project:
Cargo.toml```

[package]
name = "app"
version = "0.1.0"
description = "A Tauri App"
authors = ["you"]
license = ""
repository = ""
default-run = "app"
edition = "2021"
rust-version = "1.57"
[build-dependencies]
tauri-build = { version = "2.0.0" }
[dependencies]
serde_json = "1.0"
serde = { version = "1.0", features = ["derive"] }
tauri = { version = "2.0.0", features = [ ] }

```

The most important parts to take note of are the `tauri-build` and `tauri` dependencies. Generally, they must both be on the latest minor versions as the Tauri CLI, but this is not strictly required. If you encounter issues while trying to run your app you should check that any Tauri versions (`tauri` and `tauri-cli`) are on the latest versions for their respective minor releases.
Cargo version numbers use Semantic Versioning. Running `cargo update` in the `src-tauri` folder will pull the latest available Semver-compatible versions of all dependencies. For example, if you specify `2.0.0` as the version for `tauri-build`, Cargo will detect and download version `2.0.0.0` because it is the latest Semver-compatible version available. Tauri will update the major version number whenever a breaking change is introduced, meaning you should always be capable of safely upgrading to the latest minor and patch versions without fear of your code breaking.
If you want to use a specific crate version you can use exact versions instead by prepending `=` to the version number of the dependency:
```

tauri-build = { version = "=2.0.0.0" }

```

An additional thing to take note of is the `features=[]` portion of the `tauri` dependency. Running `tauri dev` and `tauri build` will automatically manage which features need to be enabled in your project based on the your Tauri configuration. For more information about `tauri` feature flags see the documentation.
When you build your application a `Cargo.lock` file is produced. This file is used primarily for ensuring that the same dependencies are used across machines during development (similar to `yarn.lock`, `pnpm-lock.yaml` or `package-lock.json` in Node.js). It is recommended to commit this file to your source repository so you get consistent builds.
To learn more about the Cargo manifest file please refer to the official documentation.
## `package.json`
This is the package file used by Node.js. If the frontend of your Tauri app is developed using Node.js-based technologies (such as `npm`, `yarn`, or `pnpm`) this file is used to configure the frontend dependencies and scripts.
An example of a barebones `package.json` file for a Tauri project might look a little something like this:
package.json```

{
"scripts": {
"dev": "command to start your app development mode",
"build": "command to build your app frontend",
"tauri": "tauri"
},
"dependencies": {
"@tauri-apps/api": "^2.0.0.0",
"@tauri-apps/cli": "^2.0.0.0"
}
}

```

It’s common to use the `"scripts"` section to store the commands used to launch and build the frontend used by your Tauri application. The above `package.json` file specifies the `dev` command that you can run using `yarn dev` or `npm run dev` to start the frontend framework and the `build` command that you can run using `yarn build` or `npm run build` to build your frontend’s Web assets to be added by Tauri in production. The most convenient way to use these scripts is to hook them with the Tauri CLI via the Tauri configuration’s beforeDevCommand and beforeBuildCommand hooks:
tauri.conf.json```

{
"build": {
"beforeDevCommand": "yarn dev",
"beforeBuildCommand": "yarn build"
}
}

```

The dependencies object specifies which dependencies Node.js should download when you run either `yarn`, `pnpm install` or `npm install` (in this case the Tauri CLI and API).
In addition to the `package.json` file you may see either a `yarn.lock`, `pnpm-lock.yaml` or `package-lock.json` file. These files assist in ensuring that when you download the dependencies later you’ll get the exact same versions that you have used during development (similar to `Cargo.lock` in Rust).
To learn more about the `package.json` file format please refer to the official documentation.
© 2025 Tauri Contributors. CC-BY / MIT
