Skip to content
# Embedding External Binaries
You may need to embed external binaries to add additional functionality to your application or prevent users from installing additional dependencies (e.g., Node.js or Python). We call this binary a `sidecar`.
Binaries are executables written in any programming language. Common use cases are Python CLI applications or API servers bundled using `pyinstaller`.
To bundle the binaries of your choice, you can add the `externalBin` property to the `tauri > bundle` object in your `tauri.conf.json`. The `externalBin` configuration expects a list of strings targeting binaries either with absolute or relative paths.
Here is a Tauri configuration snippet to illustrate a sidecar configuration:
src-tauri/tauri.conf.json```

{
"bundle": {
"externalBin": [
"/absolute/path/to/sidecar",
"../relative/path/to/binary",
"binaries/my-sidecar"
]
}
}

```

To make the external binary work on each supported architecture, a binary with the same name and a `-$TARGET_TRIPLE` suffix must exist on the specified path. For instance, `"externalBin": ["binaries/my-sidecar"]` requires a `src-tauri/binaries/my-sidecar-x86_64-unknown-linux-gnu` executable on Linux or `src-tauri/binaries/my-sidecar-aarch64-apple-darwin` on Mac OS with Apple Silicon.
You can find your **current** platform’s `-$TARGET_TRIPLE` suffix by looking at the `host:` property reported by the following command:
Terminal window```

rustc-Vv

```

If the `grep` and `cut` commands are available, as they should on most Unix systems, you can extract the target triple directly with the following command:
Terminal window```

rustc-Vv|grephost|cut-f2-d''

```

On Windows you can use PowerShell instead:
Terminal window```

rustc -Vv |Select-String"host:"|ForEach-Object {$_.Line.split("")[1]}

```

Here’s a Node.js script to append the target triple to a binary:
```

import { execSync } from'child_process';
import fs from'fs';
const extension = process.platform === 'win32' ? '.exe' : '';
const rustInfo = execSync('rustc -vV');
const targetTriple =/host: (\S+)/g.exec(rustInfo)[1];
if (!targetTriple) {
console.error('Failed to determine platform target triple');
}
fs.renameSync(
`src-tauri/binaries/sidecar${extension}`,
`src-tauri/binaries/sidecar-${targetTriple}${extension}`
);

```

Note that this script will not work if you compile for a different architecture than the one its running on, so only use it as a starting point for your own build scripts.
## Running it from Rust
On the Rust side, import the `tauri_plugin_shell::ShellExt` trait and call the `shell().sidecar()` function on the AppHandle:
```

use tauri_plugin_shell::ShellExt;
use tauri_plugin_shell::process::CommandEvent;
letsidecar_command=app.shell().sidecar("my-sidecar").unwrap();
let (mutrx, mut_child) =sidecar_command
.spawn()
.expect("Failed to spawn sidecar");
tauri::async_runtime::spawn(asyncmove {
// read events such as stdout
whilelet Some(event) =rx.recv().await {
iflet CommandEvent::Stdout(line_bytes) =event {
letline= String::from_utf8_lossy(&line_bytes);
window
.emit("message", Some(format!("'{}'", line)))
.expect("failed to emit event");
// write to stdin
child.write("message from Rust\n".as_bytes()).unwrap();
}
}
});

```

You can place this code inside a Tauri command to easily pass the AppHandle or you can store a reference to the AppHandle in the builder script to access it elsewhere in your application.
## Running it from JavaScript
When running the sidecar, Tauri requires you to give the sidecar permission to run the `execute` or `spawn` method on the child process. To grant this permission, go to the file `<PROJECT ROOT>/src-tauri/capabilities/default.json` and add the section below to the permissions array. Don’t forget to name your sidecar according to the relative path mentioned earlier.
src-tauri/capabilities/default.json```

{
"permissions": [
"core:default",
{
"identifier": "shell:allow-execute",
"allow": [
{
"name": "binaries/app",
"sidecar": true
}
]
},
"shell:allow-open"
]
}

```

In the JavaScript code, import the `Command` class from the `@tauri-apps/plugin-shell` module and use the `sidecar` static method.
```

import { Command } from'@tauri-apps/plugin-shell';
const command = Command.sidecar('binaries/my-sidecar');
const output = await command.execute();

```

## Passing arguments
You can pass arguments to Sidecar commands just like you would for running normal Command.
Arguments can be either **static** (e.g. `-o` or `serve`) or **dynamic** (e.g. `<file_path>` or `localhost:<PORT>`). You define the arguments in the exact order in which you’d call them. Static arguments are defined as-is, while dynamic arguments can be defined using a regular expression.
First, define the arguments that need to be passed to the sidecar command in `src-tauri/capabilities/default.json`:
src-tauri/capabilities/default.json```

{
"$schema": "../gen/schemas/desktop-schema.json",
"identifier": "default",
"description": "Capability for the main window",
"windows": ["main"],
"permissions": [
"core:default",
{
"identifier": "shell:allow-execute",
"allow": [
{
"args": [
"arg1",
"-a",
"--arg2",
{
"validator": "\\S+"
}
],
"name": "binaries/my-sidecar",
"sidecar": true
}
]
},
"shell:allow-open"
]
}

```

Then, to call the sidecar command, simply pass in **all** the arguments as an array.
In Rust:
```

use tauri_plugin_shell::ShellExt;
#[tauri::command]
asyncfncall_my_sidecar(app: tauri::AppHandle) {
letsidecar_command=app
.shell()
.sidecar("my-sidecar")
.unwrap()
.args(["arg1", "-a", "--arg2", "any-string-that-matches-the-validator"]);
let (mut_rx, mut_child) =sidecar_command.spawn().unwrap();
}

```

In JavaScript:
```

import { Command } from'@tauri-apps/plugin-shell';
// notice that the args array matches EXACTLY what is specified in `capabilities/default.json`.
const command = Command.sidecar('binaries/my-sidecar', [
'arg1',
'-a',
'--arg2',
'any-string-that-matches-the-validator',
]);
const output = await command.execute();

```

© 2025 Tauri Contributors. CC-BY / MIT
