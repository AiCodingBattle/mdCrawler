Skip to content
# Store
GitHub npm  crates.io 
API Reference 
This plugin provides a persistent key-value store. This is one of many options to handle state in your application. See the state management overview for more information on additional options.
This store will allow you to persist state to a file which can be saved and loaded on demand including between app restarts. Note that this process is asynchronous which will require handling it within your code. It can be used both in the webview or within Rust.
## Supported Platforms
_This plugin requires a Rust version of at least**1.77.2**_
Platform | Level | Notes  
---|---|---  
windows  
linux  
macos  
android  
ios  
## Setup
Install the store plugin to get started.
  * Automatic 
  * Manual 


Use your project’s package manager to add the dependency:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * bun 
  * cargo 


```

npmruntauriaddstore

```

```

yarnruntauriaddstore

```

```

pnpmtauriaddstore

```

```

denotasktauriaddstore

```

```

buntauriaddstore

```

```

cargotauriaddstore

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-store

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_store::Builder::new().build())
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

  3. Install the JavaScript Guest bindings using your preferred JavaScript package manager:
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
```

npminstall@tauri-apps/plugin-store

```

```

yarnadd@tauri-apps/plugin-store

```

```

pnpmadd@tauri-apps/plugin-store

```

```

denoaddnpm:@tauri-apps/plugin-store

```

```

bunadd@tauri-apps/plugin-store

```



## Usage
  * JavaScript 
  * Rust 


```

import { load } from'@tauri-apps/plugin-store';
// when using `"withGlobalTauri": true`, you may use
// const { load } = window.__TAURI__.store;
// Create a new store or load the existing one,
// note that the options will be ignored if a `Store` with that path has already been created
const store = await load('store.json', { autoSave: false });
// Set a value.
await store.set('some-key', { value: 5 });
// Get a value.
const val = await store.get<{ value:number }>('some-key');
console.log(val); // { value: 5 }
// You can manually save the store after making changes.
// Otherwise, it will save upon graceful exit
// And if you set `autoSave` to a number or left empty,
// it will save the changes to disk after a debounce delay, 100ms by default.
await store.save();

```

src-tauri/src/lib.rs```

use tauri::Wry;
use tauri_plugin_store::StoreExt;
use serde_json::json;
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_store::Builder::default().build())
.setup(|app| {
// Create a new store or load the existing one
// this also put the store in the app's resource table
// so your following calls `store` calls (from both rust and js)
// will reuse the same store
letstore=app.store("store.json")?;
// Note that values must be serde_json::Value instances,
// otherwise, they will not be compatible with the JavaScript bindings.
store.set("some-key", json!({ "value":5 }));
// Get a value from the store.
letvalue=store.get("some-key").expect("Failed to get value from store");
println!("{}", value); // {"value":5}
// Remove the store from the resource table
store.close_resource();
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

### LazyStore
There’s also a high level JavaScript API `LazyStore` which only loads the store on first access
```

import { LazyStore } from'@tauri-apps/plugin-store';
const store = newLazyStore('settings.json');

```

## Migrating from v1 and v2 beta/rc
  * JavaScript 
  * Rust 


```

import { Store } from '@tauri-apps/plugin-store';
import { LazyStore } from '@tauri-apps/plugin-store';

```

```

with_store(app.handle().clone(), stores, path, |store| {
store.insert("some-key".to_string(), json!({ "value": 5 }))?;
Ok(())
});
let store = app.store(path)?;
store.set("some-key".to_string(), json!({ "value": 5 }));

```

## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"permissions": [
...,
"store:default",
]
}

```

## Default Permission
This permission set configures what kind of operations are available from the store plugin.
#### Granted Permissions
All operations are enabled by default.
  * `allow-load`
  * `allow-get-store`
  * `allow-set`
  * `allow-get`
  * `allow-has`
  * `allow-delete`
  * `allow-clear`
  * `allow-reset`
  * `allow-keys`
  * `allow-values`
  * `allow-entries`
  * `allow-length`
  * `allow-reload`
  * `allow-save`


## Permission Table
Identifier | Description  
---|---  
`store:allow-clear` |  Enables the clear command without any pre-configured scope.  
`store:deny-clear` |  Denies the clear command without any pre-configured scope.  
`store:allow-delete` |  Enables the delete command without any pre-configured scope.  
`store:deny-delete` |  Denies the delete command without any pre-configured scope.  
`store:allow-entries` |  Enables the entries command without any pre-configured scope.  
`store:deny-entries` |  Denies the entries command without any pre-configured scope.  
`store:allow-get` |  Enables the get command without any pre-configured scope.  
`store:deny-get` |  Denies the get command without any pre-configured scope.  
`store:allow-get-store` |  Enables the get_store command without any pre-configured scope.  
`store:deny-get-store` |  Denies the get_store command without any pre-configured scope.  
`store:allow-has` |  Enables the has command without any pre-configured scope.  
`store:deny-has` |  Denies the has command without any pre-configured scope.  
`store:allow-keys` |  Enables the keys command without any pre-configured scope.  
`store:deny-keys` |  Denies the keys command without any pre-configured scope.  
`store:allow-length` |  Enables the length command without any pre-configured scope.  
`store:deny-length` |  Denies the length command without any pre-configured scope.  
`store:allow-load` |  Enables the load command without any pre-configured scope.  
`store:deny-load` |  Denies the load command without any pre-configured scope.  
`store:allow-reload` |  Enables the reload command without any pre-configured scope.  
`store:deny-reload` |  Denies the reload command without any pre-configured scope.  
`store:allow-reset` |  Enables the reset command without any pre-configured scope.  
`store:deny-reset` |  Denies the reset command without any pre-configured scope.  
`store:allow-save` |  Enables the save command without any pre-configured scope.  
`store:deny-save` |  Denies the save command without any pre-configured scope.  
`store:allow-set` |  Enables the set command without any pre-configured scope.  
`store:deny-set` |  Denies the set command without any pre-configured scope.  
`store:allow-values` |  Enables the values command without any pre-configured scope.  
`store:deny-values` |  Denies the values command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
