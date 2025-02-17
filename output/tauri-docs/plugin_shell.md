Skip to content
# Shell
GitHub npm  crates.io 
API Reference 
Access the system shell. Allows you to spawn child processes.
## Supported Platforms
_This plugin requires a Rust version of at least**1.77.2**_
Platform | Level | Notes  
---|---|---  
windows  
linux  
macos  
android |  Only allows to open URLs via `open`  
ios |  Only allows to open URLs via `open`  
## Opener
If you’re looking for documentation for the `shell.open` API, check out the new Opener plugin instead.
## Setup
Install the shell plugin to get started.
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

npmruntauriaddshell

```

```

yarnruntauriaddshell

```

```

pnpmtauriaddshell

```

```

denotasktauriaddshell

```

```

buntauriaddshell

```

```

cargotauriaddshell

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-shell

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_shell::init())
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

npminstall@tauri-apps/plugin-shell

```

```

yarnadd@tauri-apps/plugin-shell

```

```

pnpmadd@tauri-apps/plugin-shell

```

```

denoaddnpm:@tauri-apps/plugin-shell

```

```

bunadd@tauri-apps/plugin-shell

```



## Usage
The shell plugin is available in both JavaScript and Rust.
  * JavaScript 
  * Rust 


```

import { Command } from'@tauri-apps/plugin-shell';
// when using `"withGlobalTauri": true`, you may use
// const { Command } = window.__TAURI__.shell;
let result = await Command.create('exec-sh', [
'-c',
"echo 'Hello World!'",
]).execute();
console.log(result);

```

```

use tauri_plugin_shell::ShellExt;
letshell=app_handle.shell();
letoutput= tauri::async_runtime::block_on(asyncmove {
shell
.command("echo")
.args(["Hello from Rust!"])
.output()
.await
.unwrap()
});
ifoutput.status.success() {
println!("Result: {:?}", String::from_utf8(output.stdout));
} else {
println!("Exit with code: {}", output.status.code().unwrap());
}

```

## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"$schema": "../gen/schemas/desktop-schema.json",
"identifier": "main-capability",
"description": "Capability for the main window",
"windows": ["main"],
"permissions": [
{
"identifier": "shell:allow-execute",
"allow": [
{
"name": "exec-sh",
"cmd": "sh",
"args": [
"-c",
{
"validator": "\\S+"
}
],
"sidecar": false
}
]
}
]
}

```

## Default Permission
This permission set configures which shell functionality is exposed by default.
#### Granted Permissions
It allows to use the `open` functionality without any specific scope pre-configured. It will allow opening `http(s)://`, `tel:` and `mailto:` links.
  * `allow-open`


## Permission Table
Identifier | Description  
---|---  
`shell:allow-execute` |  Enables the execute command without any pre-configured scope.  
`shell:deny-execute` |  Denies the execute command without any pre-configured scope.  
`shell:allow-kill` |  Enables the kill command without any pre-configured scope.  
`shell:deny-kill` |  Denies the kill command without any pre-configured scope.  
`shell:allow-open` |  Enables the open command without any pre-configured scope.  
`shell:deny-open` |  Denies the open command without any pre-configured scope.  
`shell:allow-spawn` |  Enables the spawn command without any pre-configured scope.  
`shell:deny-spawn` |  Denies the spawn command without any pre-configured scope.  
`shell:allow-stdin-write` |  Enables the stdin_write command without any pre-configured scope.  
`shell:deny-stdin-write` |  Denies the stdin_write command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
