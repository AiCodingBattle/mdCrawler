Skip to content
# Plugin Development
Plugins are able to hook into the Tauri lifecycle, expose Rust code that relies on the web view APIs, handle commands with Rust, Kotlin or Swift code, and much more.
Tauri offers a windowing system with web view functionality, a way to send messages between the Rust process and the web view, and an event system along with several tools to enhance the development experience. By design, the Tauri core does not contain features not needed by everyone. Instead it offers a mechanism to add external functionalities into a Tauri application called plugins.
A Tauri plugin is composed of a Cargo crate and an optional NPM package that provides API bindings for its commands and events. Additionally, a plugin project can include an Android library project and a Swift package for iOS. You can learn more about developing plugins for Android and iOS in the Mobile Plugin Development guide.
## Naming Convention
Tauri plugins have a prefix followed by the plugin name. The plugin name is specified on the plugin configuration under `tauri.conf.json > plugins`.
By default Tauri prefixes your plugin crate with `tauri-plugin-`. This helps your plugin to be discovered by the Tauri community and to be used with the Tauri CLI. When initializing a new plugin project, you must provide its name. The generated crate name will be `tauri-plugin-{plugin-name}` and the JavaScript NPM package name will be `tauri-plugin-{plugin-name}-api` (although we recommend using an NPM scope if possible). The Tauri naming convention for NPM packages is `@scope-name/plugin-{plugin-name}`.
## Initialize Plugin Project
To bootstrap a new plugin project, run `plugin new`. If you do not need the NPM package, use the `--no-api` CLI flag. If you want to initialize the plugin with Android and/or iOS support, use the `--android` and/or `--ios` flags.
After installing, you can run the following to create a plugin project:
  * npm 


```

npx@tauri-apps/clipluginnew [name]

```

This will initialize the plugin at the directory `tauri-plugin-[name]` and, depending on the used CLI flags, the resulting project will look like this:
```

. tauri-plugin-[name]/
├── src/        - Rust code
│ ├── commands.rs    - Defines the commands the webview can use
| ├── desktop.rs    - Desktop implementation
| ├── error.rs     - Default error type to use in returned results
│ ├── lib.rs      - Re-exports appropriate implementation, setup state...
│ ├── mobile.rs     - Mobile implementation
│ └── models.rs     - Shared structs
├── permissions/    - This will host (generated) permission files for commands
├── android       - Android library
├── ios         - Swift package
├── guest-js      - Source code of the JavaScript API bindings
├── dist-js       - Transpiled assets from guest-js
├── Cargo.toml     - Cargo crate metadata
└── package.json    - NPM package metadata

```

If you have an existing plugin and would like to add Android or iOS capabilities to it, you can use `plugin android add` and `plugin ios add` to bootstrap the mobile library projects and guide you through the changes needed.
## Mobile Plugin Development
Plugins can run native mobile code written in Kotlin (or Java) and Swift. The default plugin template includes an Android library project using Kotlin and a Swift package. It includes an example mobile command showing how to trigger its execution from Rust code.
Read more about developing plugins for mobile in the Mobile Plugin Development guide.
## Plugin Configuration
In the Tauri application where the plugin is used, the plugin configuration is specified on `tauri.conf.json` where `plugin-name` is the name of the plugin:
```

{
"build": { ... },
"tauri": { ... },
"plugins": {
"plugin-name": {
"timeout": 30
}
}
}

```

The plugin’s configuration is set on the `Builder` and is parsed at runtime. Here is an example of the `Config` struct being used to specify the plugin configuration:
src/lib.rs```

use tauri::plugin::{Builder, Runtime, TauriPlugin};
use serde::Deserialize;
// Define the plugin config
#[derive(Deserialize)]
struct Config {
timeout: usize,
}
pubfninit<R: Runtime>() -> TauriPlugin<R, Config> {
// Make the plugin config optional
// by using `Builder::<R, Option<Config>>` instead
Builder::<R, Config>::new("<plugin-name>")
.setup(|app, api| {
lettimeout=api.config().timeout;
Ok(())
})
.build()
}

```

## Lifecycle Events
Plugins can hook into several lifecycle events:
  * setup: Plugin is being initialized
  * on_navigation: Web view is attempting to perform navigation
  * on_webview_ready: New window is being created
  * on_event: Event loop events
  * on_drop: Plugin is being deconstructed


There are additional lifecycle events for mobile plugins.
### setup
  * **When** : Plugin is being initialized
  * **Why** : Register mobile plugins, manage state, run background tasks


src/lib.rs```

use tauri::{Manager, plugin::Builder};
use std::{collections::HashMap, sync::Mutex, time::Duration};
struct DummyStore(Mutex<HashMap<String, String>>);
Builder::new("<plugin-name>")
.setup(|app, api| {
app.manage(DummyStore(Default::default()));
letapp_=app.clone();
std::thread::spawn(move|| {
loop {
app_.emit("tick", ());
std::thread::sleep(Duration::from_secs(1));
}
});
Ok(())
})

```

### on_navigation
  * **When** : Web view is attempting to perform navigation
  * **Why** : Validate the navigation or track URL changes


Returning `false` cancels the navigation.
src/lib.rs```

use tauri::plugin::Builder;
Builder::new("<plugin-name>")
.on_navigation(|window, url| {
println!("window {} is navigating to {}", window.label(), url);
// Cancels the navigation if forbidden
url.scheme() !="forbidden"
})

```

### on_webview_ready
  * **When** : New window has been created
  * **Why** : Execute an initialization script for every window


src/lib.rs```

use tauri::plugin::Builder;
Builder::new("<plugin-name>")
.on_webview_ready(|window| {
window.listen("content-loaded", |event| {
println!("webview content has been loaded");
});
})

```

### on_event
  * **When** : Event loop events
  * **Why** : Handle core events such as window events, menu events and application exit requested


With this lifecycle hook you can be notified of any event loop events.
src/lib.rs```

use std::{collections::HashMap, fs::write, sync::Mutex};
use tauri::{plugin::Builder, Manager, RunEvent};
struct DummyStore(Mutex<HashMap<String, String>>);
Builder::new("<plugin-name>")
.setup(|app, _api| {
app.manage(DummyStore(Default::default()));
Ok(())
})
.on_event(|app, event| {
matchevent {
RunEvent::ExitRequested { api, .. } => {
// user requested a window to be closed and there's no windows left
// we can prevent the app from exiting:
api.prevent_exit();
}
RunEvent::Exit => {
// app is going to exit, you can cleanup here
letstore=app.state::<DummyStore>();
write(
app.path().app_local_data_dir().unwrap().join("store.json"),
serde_json::to_string(&*store.0.lock().unwrap()).unwrap(),
)
.unwrap();
}
_=> {}
}
})

```

### on_drop
  * **When** : Plugin is being deconstructed
  * **Why** : Execute code when the plugin has been destroyed


See `Drop` for more information.
src/lib.rs```

use tauri::plugin::Builder;
Builder::new("<plugin-name>")
.on_drop(|app| {
// plugin has been destroyed...
})

```

## Exposing Rust APIs
The plugin APIs defined in the project’s `desktop.rs` and `mobile.rs` are exported to the user as a struct with the same name as the plugin (in pascal case). When the plugin is setup, an instance of this struct is created and managed as a state so that users can retrieve it at any point in time with a `Manager` instance (such as `AppHandle`, `App`, or` Window`) through the extension trait defined in the plugin.
For example, the `global-shortcut plugin` defines a `GlobalShortcut` struct that can be read by using the `global_shortcut` method of the `GlobalShortcutExt` trait:
src-tauri/src/lib.rs```

use tauri_plugin_global_shortcut::GlobalShortcutExt;
tauri::Builder::default()
.plugin(tauri_plugin_global_shortcut::init())
.setup(|app| {
app.global_shortcut().register(...);
Ok(())
})

```

## Adding Commands
Commands are defined in the `commands.rs` file. They are regular Tauri applications commands. They can access the AppHandle and Window instances directly, access state, and take input the same way as application commands. Read the Commands guide for more details on Tauri commands.
This command shows how to get access to the `AppHandle` and `Window` instance via dependency injection, and takes two input parameters (`on_progress` and `url`):
src/commands.rs```

use tauri::{command, ipc::Channel, AppHandle, Runtime, Window};
#[command]
asyncfnupload<R: Runtime>(app: AppHandle<R>, window: Window<R>, on_progress: Channel, url: String) {
// implement command logic here
on_progress.send(100).unwrap();
}

```

To expose the command to the webview, you must hook into the `invoke_handler()` call in `lib.rs`:
src/lib.rs```

Builder::new("<plugin-name>")
.invoke_handler(tauri::generate_handler![commands::upload])

```

Define a binding function in `webview-src/index.ts` so that plugin users can easily call the command in JavaScript:
```

import { invoke, Channel } from'@tauri-apps/api/core'
exportasyncfunctionupload(url:string, onProgressHandler:(progress:number)=>void):Promise<void> {
const onProgress = newChannel<number>()
onProgress.onmessage=onProgressHandler
awaitinvoke('plugin:<plugin-name>|upload', { url,onProgress })
}

```

Be sure to build the TypeScript code prior to testing it.
### Command Permissions
By default your commands are not accessible by the frontend. If you try to execute one of them, you will get a denied error rejection. To actually expose commands, you also need to define permissions that allow each command.
#### Permission Files
Permissions are defined as JSON or TOML files inside the `permissions` directory. Each file can define a list of permissions, a list of permission sets and your plugin’s default permission.
##### Permissions
A permission describes privileges of your plugin commands. It can allow or deny a list of commands and associate command-specific and global scopes.
permissions/start-server.toml```

"$schema" = "schemas/schema.json"
[[permission]]
identifier = "allow-start-server"
description = "Enables the start_server command."
commands.allow = ["start_server"]
[[permission]]
identifier = "deny-start-server"
description = "Denies the start_server command."
commands.deny = ["start_server"]

```

##### Scope
Scopes allow your plugin to define deeper restrictions to individual commands. Each permission can define a list of scope objects that define something to be allowed or denied either specific to a command or globally to the plugin.
Let’s define an example struct that will hold scope data for a list of binaries a `shell` plugin is allowed to spawn:
src/scope.rs```

#[derive(Debug, schemars::JsonSchema)]
pubstruct Entry {
pubbinary: String,
}

```

###### Command Scope
Your plugin consumer can define a scope for a specific command in their capability file (see the documentation). You can read the command-specific scope with the `tauri::ipc::CommandScope` struct:
src/commands.rs```

use tauri::ipc::CommandScope;
usecrate::scope::Entry;
asyncfnspawn<R: tauri::Runtime>(app: tauri::AppHandle<R>, command_scope: CommandScope<'_, Entry>) -> Result<()> {
letallowed=command_scope.allows();
letdenied=command_scope.denies();
todo!()
}

```

###### Global Scope
When a permission does not define any commands to be allowed or denied, it’s considered a scope permission and it should only define a global scope for your plugin:
permissions/spawn-node.toml```

[[permission]]
identifier = "allow-spawn-node"
description = "This scope permits spawning the `node` binary."
[[permission.scope.allow]]
binary = "node"

```

You can read the global scope with the `tauri::ipc::GlobalScope` struct:
src/commands.rs```

use tauri::ipc::GlobalScope;
usecrate::scope::Entry;
asyncfnspawn<R: tauri::Runtime>(app: tauri::AppHandle<R>, scope: GlobalScope<'_, Entry>) -> Result<()> {
letallowed=scope.allows();
letdenied=scope.denies();
todo!()
}

```

###### Schema
The scope entry requires the `schemars` dependency to generate a JSON schema so the plugin consumers know the format of the scope and have autocomplete in their IDEs.
To define the schema, first add the dependency to your Cargo.toml file:
```

# we need to add schemars to both dependencies and build-dependencies because the scope.rs module is shared between the app code and build script
[dependencies]
schemars = "0.8"
[build-dependencies]
schemars = "0.8"

```

In your build script, add the following code:
build.rs```

#[path ="src/scope.rs"]
mod scope;
constCOMMANDS:&[&str] =&[];
fnmain() {
tauri_plugin::Builder::new(COMMANDS)
.global_scope_schema(schemars::schema_for!(scope::Entry))
.build();
}

```

##### Permission Sets
Permission sets are groups of individual permissions that helps users manage your plugin with a higher level of abstraction. For instance if a single API uses multiple commands or if there’s a logical connection between a collection of commands, you should define a set containing them:
permissions/websocket.toml```

"$schema" = "schemas/schema.json"
[[set]]
identifier = "allow-websocket"
description = "Allows connecting and sending messages through a WebSocket"
permissions = ["allow-connect", "allow-send"]

```

##### Default Permission
The default permission is a special permission set with identifier `default`. It’s recommended that you enable required commands by default. For instance the `http` plugin is useless without the `request` command allowed:
permissions/default.toml```

"$schema" = "schemas/schema.json"
[default]
description = "Allows making HTTP requests"
permissions = ["allow-request"]

```

#### Autogenerated Permissions
The easiest way to define permissions for each of your commands is to use the autogeneration option defined in your plugin’s build script defined in the `build.rs` file. Inside the `COMMANDS` const, define the list of commands in snake_case (should match the command function name) and Tauri will automatically generate an `allow-$commandname` and a `deny-$commandname` permissions.
The following example generates the `allow-upload` and `deny-upload` permissions:
src/commands.rs```

constCOMMANDS:&[&str] =&["upload"];
fnmain() {
tauri_plugin::Builder::new(COMMANDS).build();
}

```

See the Permissions Overview documentation for more information.
## Managing State
A plugin can manage state in the same way a Tauri application does. Read the State Management guide for more information.
© 2025 Tauri Contributors. CC-BY / MIT
