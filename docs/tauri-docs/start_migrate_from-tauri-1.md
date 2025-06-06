Skip to content
# Upgrade from Tauri 1.0
This guide walks you through upgrading your Tauri 1.0 application to Tauri 2.0.
## Preparing for Mobile
The mobile interface of Tauri requires your project to output a shared library. If you are targeting mobile for your existing application, you must change your crate to produce that kind of artifact along with the desktop executable.
  1. Change the Cargo manifest to produce the library. Append the following block:


src-tauri/Cargo.toml```

[lib]
name = "app_lib"
crate-type = ["staticlib", "cdylib", "rlib"]

```

  1. Rename `src-tauri/src/main.rs` to `src-tauri/src/lib.rs`. This file will be shared by both desktop and mobile targets.
  2. Rename the `main` function header in `lib.rs` to the following:


src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
// your code here
}

```

The `tauri::mobile_entry_point` macro prepares your function to be executed on mobile.
  1. Recreate the `main.rs` file calling the shared run function:


src-tauri/src/main.rs```

#![cfg_attr(not(debug_assertions), windows_subsystem ="windows")]
fnmain() {
app_lib::run();
}

```

## Automated Migration
The Tauri v2 CLI includes a `migrate` command that automates most of the process and helps you finish the migration:
  * npm 
  * yarn 
  * pnpm 
  * cargo 


```

npminstall@tauri-apps/cli@latest
npmruntaurimigrate

```

```

yarnupgrade@tauri-apps/cli@latest
yarntaurimigrate

```

```

pnpmupdate@tauri-apps/cli@latest
pnpmtaurimigrate

```

```

cargoinstalltauri-cli--version"^2.0.0"--locked
cargotaurimigrate

```

Learn more about the `migrate` command in the Command Line Interface reference
## Summary of Changes
Below is a summary of the changes from Tauri 1.0 to Tauri 2.0:
### Tauri Configuration
  * `package > productName` and `package > version` moved to top-level object.
  * the binary name is no longer renamed to match `productName` automatically, so you must add a `mainBinaryName` string to the top-level object matching `productName`.
  * `package` removed.
  * `tauri` key renamed to `app`.
  * `tauri > allowlist` removed. Refer to Migrate Permissions.
  * `tauri > allowlist > protocol > assetScope` moved to `app > security > assetProtocol > scope`.
  * `tauri > cli` moved to `plugins > cli`.
  * `tauri > windows > fileDropEnabled` renamed to `app > windows > dragDropEnabled`.
  * `tauri > updater > active` removed.
  * `tauri > updater > dialog` removed.
  * `tauri > updater` moved to `plugins > updater`.
  * `bundle > createUpdaterArtifacts` added, must be set when using the app updater. 
    * set it to `v1Compatible` when upgrading from v1 apps that were already distributed. See the updater guide for more information.
  * `tauri > systemTray` renamed to `app > trayIcon`.
  * `tauri > pattern` moved to `app > security > pattern`.
  * `tauri > bundle` moved top-level.
  * `tauri > bundle > identifier` moved to top-level object.
  * `tauri > bundle > dmg` moved to `bundle > macOS > dmg`
  * `tauri > bundle > deb` moved to `bundle > linux > deb`
  * `tauri > bundle > appimage` moved to `bundle > linux > appimage`
  * `tauri > bundle > macOS > license` removed, use `bundle > licenseFile` instead.
  * `tauri > bundle > windows > wix > license` removed, use `bundle > licenseFile` instead.
  * `tauri > bundle > windows > nsis > license` removed, use `bundle > licenseFile` instead.
  * `tauri > bundle > windows > webviewFixedRuntimePath` removed, use `bundle > windows > webviewInstallMode` instead.
  * `build > withGlobalTauri` moved to `app > withGlobalTauri`.
  * `build > distDir` renamed to `frontendDist`.
  * `build > devPath` renamed to `devUrl`.


Tauri 2.0 Configuration API reference
### New Cargo Features
  * linux-protocol-body: Enables custom protocol request body parsing, allowing the IPC to use it. Requires webkit2gtk 2.40.


### Removed Cargo Features
  * reqwest-client: reqwest is now the only supported client.
  * reqwest-native-tls-vendored: use `native-tls-vendored` instead.
  * process-command-api: use the `shell` plugin instead (see instructions in the following section).
  * shell-open-api: use the `shell` plugin instead (see instructions in the following section).
  * windows7-compat: moved to the `notification` plugin.
  * updater: Updater is now a plugin.
  * linux-protocol-headers: Now enabled by default since we upgraded our minimum webkit2gtk version.
  * system-tray: renamed to `tray-icon`.


### Rust Crate Changes
  * `api` module removed. Each API module can be found in a Tauri plugin.
  * `api::dialog` module removed. Use `tauri-plugin-dialog` instead. Migration
  * `api::file` module removed. Use Rust’s `std::fs` instead.
  * `api::http` module removed. Use `tauri-plugin-http` instead. Migration
  * `api::ip` module rewritten and moved to `tauri::ipc`. Check out the new APIs, specially `tauri::ipc::Channel`.
  * `api::path` module functions and `tauri::PathResolved` moved to `tauri::Manager::path`. Migration
  * `api::process::Command`, `tauri::api::shell` and `tauri::Manager::shell_scope` APIs removed. Use `tauri-plugin-shell` instead. Migration
  * `api::process::current_binary` and `tauri::api::process::restart` moved to `tauri::process`.
  * `api::version` module has been removed. Use the semver crate instead.
  * `App::clipboard_manager` and `AppHandle::clipboard_manager` removed. Use `tauri-plugin-clipboard` instead. Migration
  * `App::get_cli_matches` removed. Use `tauri-plugin-cli` instead. Migration
  * `App::global_shortcut_manager` and `AppHandle::global_shortcut_manager` removed. Use `tauri-plugin-global-shortcut` instead. Migration
  * `Manager::fs_scope` removed. The file system scope can be accessed via `tauri_plugin_fs::FsExt`.
  * `Plugin::PluginApi` now receives a plugin configuration as a second argument.
  * `Plugin::setup_with_config` removed. Use the updated `tauri::Plugin::PluginApi` instead.
  * `scope::ipc::RemoteDomainAccessScope::enable_tauri_api` and `scope::ipc::RemoteDomainAccessScope::enables_tauri_api` removed. Enable each core plugin individually via `scope::ipc::RemoteDomainAccessScope::add_plugin` instead.
  * `scope::IpcScope` removed, use `scope::ipc::Scope` instead.
  * `scope::FsScope`, `scope::GlobPattern` and `scope::FsScopeEvent` removed, use `scope::fs::Scope`, `scope::fs::Pattern` and `scope::fs::Event` respectively.
  * `updater` module removed. Use `tauri-plugin-updater` instead. Migration
  * `Env.args` field has been removed, use `Env.args_os` field instead.
  * `Menu`, `MenuEvent`, `CustomMenuItem`, `Submenu`, `WindowMenuEvent`, `MenuItem` and `Builder::on_menu_event` APIs removed. Migration
  * `SystemTray`, `SystemTrayHandle`, `SystemTrayMenu`, `SystemTrayMenuItemHandle`, `SystemTraySubmenu`, `MenuEntry` and `SystemTrayMenuItem` APIs removed. Migration


### JavaScript API Changes
The `@tauri-apps/api` package no longer provides non-core modules. Only the previous `tauri` (now `core`), `path`, `event` and `window` modules are exported. All others have been moved to plugins.
  * `@tauri-apps/api/tauri` module renamed to `@tauri-apps/api/core`. Migration
  * `@tauri-apps/api/cli` module removed. Use `@tauri-apps/plugin-cli` instead. Migration
  * `@tauri-apps/api/clipboard` module removed. Use `@tauri-apps/plugin-clipboard` instead. Migration
  * `@tauri-apps/api/dialog` module removed. Use `@tauri-apps/plugin-dialog` instead. Migration
  * `@tauri-apps/api/fs` module removed. Use `@tauri-apps/plugin-fs` instead. Migration
  * `@tauri-apps/api/global-shortcut` module removed. Use `@tauri-apps/plugin-global-shortcut` instead. Migration
  * `@tauri-apps/api/http` module removed. Use `@tauri-apps/plugin-http` instead. Migration
  * `@tauri-apps/api/os` module removed. Use `@tauri-apps/plugin-os` instead. Migration
  * `@tauri-apps/api/notification` module removed. Use `@tauri-apps/plugin-notification` instead. Migration
  * `@tauri-apps/api/process` module removed. Use `@tauri-apps/plugin-process` instead. Migration
  * `@tauri-apps/api/shell` module removed. Use `@tauri-apps/plugin-shell` instead. Migration
  * `@tauri-apps/api/updater` module removed. Use `@tauri-apps/plugin-updater` instead Migration
  * `@tauri-apps/api/window` module renamed to `@tauri-apps/api/webviewWindow`. Migration


The v1 plugins are now published as `@tauri-apps/plugin-<plugin-name>`. Previously they were available from git as `tauri-plugin-<plugin-name>-api`.
### Environment Variables Changes
Most of the environment variables read and written by the Tauri CLI were renamed for consistency and prevention of mistakes:
  * `TAURI_PRIVATE_KEY` -> `TAURI_SIGNING_PRIVATE_KEY`
  * `TAURI_KEY_PASSWORD` -> `TAURI_SIGNING_PRIVATE_KEY_PASSWORD`
  * `TAURI_SKIP_DEVSERVER_CHECK` -> `TAURI_CLI_NO_DEV_SERVER_WAIT`
  * `TAURI_DEV_SERVER_PORT` -> `TAURI_CLI_PORT`
  * `TAURI_PATH_DEPTH` -> `TAURI_CLI_CONFIG_DEPTH`
  * `TAURI_FIPS_COMPLIANT` -> `TAURI_BUNDLER_WIX_FIPS_COMPLIANT`
  * `TAURI_DEV_WATCHER_IGNORE_FILE` -> `TAURI_CLI_WATCHER_IGNORE_FILENAME`
  * `TAURI_TRAY` -> `TAURI_LINUX_AYATANA_APPINDICATOR`
  * `TAURI_APPLE_DEVELOPMENT_TEAM` -> `APPLE_DEVELOPMENT_TEAM`
  * `TAURI_PLATFORM` -> `TAURI_ENV_PLATFORM`
  * `TAURI_ARCH` -> `TAURI_ENV_ARCH`
  * `TAURI_FAMILY` -> `TAURI_ENV_FAMILY`
  * `TAURI_PLATFORM_VERSION` -> `TAURI_ENV_PLATFORM_VERSION`
  * `TAURI_PLATFORM_TYPE` -> `TAURI_ENV_PLATFORM_TYPE`
  * `TAURI_DEBUG` -> `TAURI_ENV_DEBUG`


### Event System
The event system was redesigned to be easier to use. Instead of relying on the source of the event, it now has a simpler implementation that relies on event targets.
  * The `emit` function now emits the event to all event listeners.
  * Added a new `emit_to`/`emitTo` function to trigger an event to a specific target.
  * `emit_filter` now filters based on `EventTarget` instead of a window.
  * Renamed `listen_global` to `listen_any`. It now listens to all events regardless of their filters and targets.
  * JavaScript: `event.listen()` behaves similar to `listen_any`. It now listens to all events regardless of their filters and targets, unless a target is set in the `Options`.
  * JavaScript: `WebviewWindow.listen` etc. only listen to events emitted to the respective `EventTarget`.


### Multiwebview support
Tauri v2 introduces multiwebview support currently behind an `unstable` feature flag. In order to support it, we renamed the Rust `Window` type to `WebviewWindow` and the Manager `get_window` function to `get_webview_window`.
The `WebviewWindow` JS API type is now re-exported from `@tauri-apps/api/webviewWindow` instead of `@tauri-apps/api/window`.
### New origin URL on Windows
On Windows the frontend files in production apps are now hosted on `http://tauri.localhost` instead of `https://tauri.localhost`. Because of this IndexedDB, LocalStorage and Cookies will be reset unless `dangerousUseHttpScheme` was used in v1. To prevent this you can set `app > windows > useHttpsScheme` to `true` or use `WebviewWindowBuilder::use_https_scheme` to keep using the `https` scheme.
## Detailed Migration Steps
Common scenarios you may encounter when migrating your Tauri 1.0 app to Tauri 2.0.
### Migrate to Core Module
The `@tauri-apps/api/tauri` module was renamed to `@tauri-apps/api/core`. Simply rename the module import:
```

import { invoke } from "@tauri-apps/api/tauri"
import { invoke } from "@tauri-apps/api/core"

```

### Migrate to CLI Plugin
The Rust `App::get_cli_matches` JavaScript `@tauri-apps/api/cli` APIs have been removed. Use the `@tauri-apps/plugin-cli` plugin instead:
  1. Add to cargo dependencies:


Cargo.toml```

[dependencies]
tauri-plugin-cli = "2"

```

  1. Use in JavaScript or Rust project:


  * JavaScript 
  * Rust 


```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_cli::init())
}

```

package.json```

{
"dependencies": {
"@tauri-apps/plugin-cli": "^2.0.0"
}
}

```

```

import { getMatches } from'@tauri-apps/plugin-cli';
const matches = await getMatches();

```

```

fnmain() {
use tauri_plugin_cli::CliExt;
tauri::Builder::default()
.plugin(tauri_plugin_cli::init())
.setup(|app| {
letcli_matches=app.cli().matches()?;
Ok(())
})
}

```

### Migrate to Clipboard Plugin
The Rust `App::clipboard_manager` and `AppHandle::clipboard_manager` and JavaScript `@tauri-apps/api/clipboard` APIs have been removed. Use the `@tauri-apps/plugin-clipboard-manager` plugin instead:
```

[dependencies]
tauri-plugin-clipboard-manager = "2"

```

  * JavaScript 
  * Rust 


```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_clipboard_manager::init())
}

```

package.json```

{
"dependencies": {
"@tauri-apps/plugin-clipboard-manager": "^2.0.0"
}
}

```

```

import { writeText, readText } from'@tauri-apps/plugin-clipboard-manager';
awaitwriteText('Tauri is awesome!');
assert(awaitreadText(), 'Tauri is awesome!');

```

```

use tauri_plugin_clipboard::{ClipboardExt, ClipKind};
tauri::Builder::default()
.plugin(tauri_plugin_clipboard::init())
.setup(|app| {
app.clipboard().write(ClipKind::PlainText {
label: None,
text:"Tauri is awesome!".into(),
})?;
Ok(())
})

```

### Migrate to Dialog Plugin
The Rust `tauri::api::dialog` JavaScript `@tauri-apps/api/dialog` APIs have been removed. Use the `@tauri-apps/plugin-dialog` plugin instead:
  1. Add to cargo dependencies:


Cargo.toml```

[dependencies]
tauri-plugin-dialog = "2"

```

  1. Use in JavaScript or Rust project:


  * JavaScript 
  * Rust 


```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_dialog::init())
}

```

package.json```

{
"dependencies": {
"@tauri-apps/plugin-dialog": "^2.0.0"
}
}

```

```

import { save } from'@tauri-apps/plugin-dialog';
const filePath = await save({
filters: [
{
name: 'Image',
extensions: ['png', 'jpeg'],
},
],
});

```

```

use tauri_plugin_dialog::DialogExt;
tauri::Builder::default()
.plugin(tauri_plugin_dialog::init())
.setup(|app| {
app.dialog().file().pick_file(|file_path| {
// do something with the optional file path here
// the file path is `None` if the user closed the dialog
});
app.dialog().message("Tauri is Awesome!").show();
Ok(())
})

```

### Migrate to File System Plugin
The Rust `App::get_cli_matches` JavaScript `@tauri-apps/api/fs` APIs have been removed. Use the `std::fs` for Rust and `@tauri-apps/plugin-fs` plugin for JavaScript instead:
  1. Add to cargo dependencies:


Cargo.toml```

[dependencies]
tauri-plugin-fs = "2"

```

  1. Use in JavaScript or Rust project:


  * JavaScript 
  * Rust 


```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_fs::init())
}

```

package.json```

{
"dependencies": {
"@tauri-apps/plugin-fs": "^2.0.0"
}
}

```

```

import { mkdir, BaseDirectory } from'@tauri-apps/plugin-fs';
awaitmkdir('db', { baseDir: BaseDirectory.AppLocalData });

```

Some functions and types have been renamed or removed:
  * `Dir` enum alias removed, use `BaseDirectory`.
  * `FileEntry`, `FsBinaryFileOption`, `FsDirOptions`, `FsOptions`, `FsTextFileOption` and `BinaryFileContents` interfaces and type aliases have been removed and replaced with new interfaces suited for each function.
  * `createDir` renamed to `mkdir`.
  * `readBinaryFile` renamed to `readFile`.
  * `removeDir` removed and replaced with `remove`.
  * `removeFile` removed and replaced with `remove`.
  * `renameFile` removed and replaced with `rename`.
  * `writeBinaryFile` renamed to `writeFile`.


Use the Rust `std::fs` functions.
### Migrate to Global Shortcut Plugin
The Rust `App::global_shortcut_manager` and `AppHandle::global_shortcut_manager` and JavaScript `@tauri-apps/api/global-shortcut` APIs have been removed. Use the `@tauri-apps/plugin-global-shortcut` plugin instead:
  1. Add to cargo dependencies:


Cargo.toml```

[dependencies]
[target."cfg(not(any(target_os = \"android\", target_os = \"ios\")))".dependencies]
tauri-plugin-global-shortcut = "2"

```

  1. Use in JavaScript or Rust project:


  * JavaScript 
  * Rust 


```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_global_shortcut::Builder::default().build())
}

```

package.json```

{
"dependencies": {
"@tauri-apps/plugin-global-shortcut": "^2.0.0"
}
}

```

```

import { register } from'@tauri-apps/plugin-global-shortcut';
awaitregister('CommandOrControl+Shift+C', ()=> {
console.log('Shortcut triggered');
});

```

```

use tauri_plugin_global_shortcut::GlobalShortcutExt;
tauri::Builder::default()
.plugin(
tauri_plugin_global_shortcut::Builder::new().with_handler(|app, shortcut| {
println!("Shortcut triggered: {:?}", shortcut);
})
.build(),
)
.setup(|app| {
// register a global shortcut
// on macOS, the Cmd key is used
// on Windows and Linux, the Ctrl key is used
app.global_shortcut().register("CmdOrCtrl+Y")?;
Ok(())
})

```

### Migrate to HTTP Plugin
The Rust `tauri::api::http` JavaScript `@tauri-apps/api/http` APIs have been removed. Use the `@tauri-apps/plugin-http` plugin instead:
  1. Add to cargo dependencies:


Cargo.toml```

[dependencies]
tauri-plugin-http = "2"

```

  1. Use in JavaScript or Rust project:


  * JavaScript 
  * Rust 


```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_http::init())
}

```

package.json```

{
"dependencies": {
"@tauri-apps/plugin-http": "^2.0.0"
}
}

```

```

import { fetch } from'@tauri-apps/plugin-http';
const response = await fetch(
'https://raw.githubusercontent.com/tauri-apps/tauri/dev/package.json'
);

```

```

use tauri_plugin_http::reqwest;
tauri::Builder::default()
.plugin(tauri_plugin_http::init())
.setup(|app| {
letresponse_data= tauri::async_runtime::block_on(async {
letresponse= reqwest::get(
"https://raw.githubusercontent.com/tauri-apps/tauri/dev/package.json",
)
.await
.unwrap();
response.text().await
})?;
Ok(())
})

```

The HTTP plugin re-exports reqwest so you can check out their documentation for more information.
### Migrate to Notification Plugin
The Rust `tauri::api::notification` JavaScript `@tauri-apps/api/notification` APIs have been removed. Use the `@tauri-apps/plugin-notification` plugin instead:
  1. Add to cargo dependencies:


Cargo.toml```

[dependencies]
tauri-plugin-notification = "2"

```

  1. Use in JavaScript or Rust project:


  * JavaScript 
  * Rust 


```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_notification::init())
}

```

package.json```

{
"dependencies": {
"@tauri-apps/plugin-notification": "^2.0.0"
}
}

```

```

import { sendNotification } from'@tauri-apps/plugin-notification';
sendNotification('Tauri is awesome!');

```

```

use tauri_plugin_notification::NotificationExt;
use tauri::plugin::PermissionState;
fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_notification::init())
.setup(|app| {
ifapp.notification().permission_state()?== PermissionState::Unknown {
app.notification().request_permission()?;
}
ifapp.notification().permission_state()?== PermissionState::Granted {
app.notification()
.builder()
.body("Tauri is awesome!")
.show()?;
}
Ok(())
})
}

```

### Migrate to Menu Module
The Rust `Menu` APIs were moved to the `tauri::menu` module and refactored to use the muda crate.
#### Use `tauri::menu::MenuBuilder`
Use `tauri::menu::MenuBuilder` instead of `tauri::Menu`. Note that its constructor takes a Manager instance (one of `App`, `AppHandle` or `WebviewWindow`) as an argument:
```

use tauri::menu::MenuBuilder;
tauri::Builder::default()
.setup(|app| {
letmenu= MenuBuilder::new(app)
.copy()
.paste()
.separator()
.undo()
.redo()
.text("open-url", "Open URL")
.check("toggle", "Toggle")
.icon("show-app", "Show App", app.default_window_icon().cloned().unwrap())
.build()?;
Ok(())
})

```

#### Use `tauri::menu::PredefinedMenuItem`
Use `tauri::menu::PredefinedMenuItem` instead of `tauri::MenuItem`:
```

use tauri::menu::{MenuBuilder, PredefinedMenuItem};
tauri::Builder::default()
.setup(|app| {
letmenu= MenuBuilder::new(app).item(&PredefinedMenuItem::copy(app)?).build()?;
Ok(())
})

```

#### Use `tauri::menu::MenuItemBuilder`
Use `tauri::menu::MenuItemBuilder` instead of `tauri::CustomMenuItem`:
```

use tauri::menu::MenuItemBuilder;
tauri::Builder::default()
.setup(|app| {
lettoggle= MenuItemBuilder::new("Toggle").accelerator("Ctrl+Shift+T").build(app)?;
Ok(())
})

```

#### Use `tauri::menu::SubmenuBuilder`
Use `tauri::menu::SubmenuBuilder` instead of `tauri::Submenu`:
```

use tauri::menu::{MenuBuilder, SubmenuBuilder};
tauri::Builder::default()
.setup(|app| {
letsubmenu= SubmenuBuilder::new(app, "Sub")
.text("Tauri")
.separator()
.check("Is Awesome")
.build()?;
letmenu= MenuBuilder::new(app).item(&submenu).build()?;
Ok(())
})

```

`tauri::Builder::menu` now takes a closure because the menu needs a Manager instance to be built. See the documentation for more information.
#### Menu Events
The Rust `tauri::Builder::on_menu_event` API was removed. Use `tauri::App::on_menu_event` or `tauri::AppHandle::on_menu_event` instead:
```

use tauri::menu::{CheckMenuItemBuilder, MenuBuilder, MenuItemBuilder};
tauri::Builder::default()
.setup(|app| {
lettoggle= MenuItemBuilder::with_id("toggle", "Toggle").build(app)?;
letcheck= CheckMenuItemBuilder::new("Mark").build(app)?;
letmenu= MenuBuilder::new(app).items(&[&toggle, &check]).build()?;
app.set_menu(menu)?;
app.on_menu_event(move|app, event| {
ifevent.id() ==check.id() {
println!("`check` triggered, do something! is checked? {}", check.is_checked().unwrap());
} elseifevent.id() =="toggle" {
println!("toggle triggered!");
}
});
Ok(())
})

```

Note that there are two ways to check which menu item was selected: move the item to the event handler closure and compare IDs, or define a custom ID for the item through the `with_id` constructor and use that ID string to compare.
### Migrate to OS Plugin
The Rust `tauri::api::os` JavaScript `@tauri-apps/api/os` APIs have been removed. Use the `@tauri-apps/plugin-os` plugin instead:
  1. Add to cargo dependencies:


Cargo.toml```

[dependencies]
tauri-plugin-os = "2"

```

  1. Use in JavaScript or Rust project:


  * JavaScript 
  * Rust 


```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_os::init())
}

```

package.json```

{
"dependencies": {
"@tauri-apps/plugin-os": "^2.0.0"
}
}

```

```

import { arch } from'@tauri-apps/plugin-os';
const architecture = await arch();

```

```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_os::init())
.setup(|app| {
letos_arch= tauri_plugin_os::arch();
Ok(())
})
}

```

### Migrate to Process Plugin
The Rust `tauri::api::process` JavaScript `@tauri-apps/api/process` APIs have been removed. Use the `@tauri-apps/plugin-process` plugin instead:
  1. Add to cargo dependencies:


Cargo.toml```

[dependencies]
tauri-plugin-process = "2"

```

  1. Use in JavaScript or Rust project:


  * JavaScript 
  * Rust 


```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_process::init())
}

```

package.json```

{
"dependencies": {
"@tauri-apps/plugin-process": "^2.0.0"
}
}

```

```

import { exit, relaunch } from'@tauri-apps/plugin-process';
awaitexit(0);
awaitrelaunch();

```

```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_process::init())
.setup(|app| {
// exit the app with a status code
app.handle().exit(1);
// restart the app
app.handle().restart();
Ok(())
})
}

```

### Migrate to Shell Plugin
The Rust `tauri::api::shell` JavaScript `@tauri-apps/api/shell` APIs have been removed. Use the `@tauri-apps/plugin-shell` plugin instead:
  1. Add to cargo dependencies:


Cargo.toml```

[dependencies]
tauri-plugin-shell = "2"

```

  1. Use in JavaScript or Rust project:


  * JavaScript 
  * Rust 


```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_shell::init())
}

```

package.json```

{
"dependencies": {
"@tauri-apps/plugin-shell": "^2.0.0"
}
}

```

```

import { Command, open } from'@tauri-apps/plugin-shell';
const output = await Command.create('echo', 'message').execute();
awaitopen('https://github.com/tauri-apps/tauri');

```

  * Open an URL


```

use tauri_plugin_shell::ShellExt;
fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_shell::init())
.setup(|app| {
app.shell().open("https://github.com/tauri-apps/tauri", None)?;
Ok(())
})
}

```

  * Spawn a child process and retrieve the status code


```

use tauri_plugin_shell::ShellExt;
fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_shell::init())
.setup(|app| {
letstatus= tauri::async_runtime::block_on(asyncmove { app.shell().command("which").args(["ls"]).status().await.unwrap() });
println!("`which` finished with status: {:?}", status.code());
Ok(())
})
}

```

  * Spawn a child process and capture its output


```

use tauri_plugin_shell::ShellExt;
fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_shell::init())
.setup(|app| {
letoutput= tauri::async_runtime::block_on(asyncmove { app.shell().command("echo").args(["TAURI"]).output().await.unwrap() });
assert!(output.status.success());
assert_eq!(String::from_utf8(output.stdout).unwrap(), "TAURI");
Ok(())
})
}

```

  * Spawn a child process and read its events asynchronously:


```

use tauri_plugin_shell::{ShellExt, process::CommandEvent};
fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_shell::init())
.setup(|app| {
lethandle=app.handle().clone();
tauri::async_runtime::spawn(asyncmove {
let (mutrx, mutchild) =handle.shell().command("cargo")
.args(["tauri", "dev"])
.spawn()
.expect("Failed to spawn cargo");
letmuti=0;
whilelet Some(event) =rx.recv().await {
iflet CommandEvent::Stdout(line) =event {
println!("got: {}", String::from_utf8(line).unwrap());
i+=1;
ifi==4 {
child.write("message from Rust\n".as_bytes()).unwrap();
i=0;
}
}
}
});
Ok(())
})
}

```

### Migrate to Tray Icon Module
The Rust `SystemTray` APIs were renamed to `TrayIcon` for consistency. The new APIs can be found in the Rust `tray` module.
#### Use `tauri::tray::TrayIconBuilder`
Use `tauri::tray::TrayIconBuilder` instead of `tauri::SystemTray`:
```

lettray= tauri::tray::TrayIconBuilder::with_id("my-tray").build(app)?;

```

See TrayIconBuilder for more information.
#### Migrate to Menu
Use `tauri::menu::Menu` instead of `tauri::SystemTrayMenu`, `tauri::menu::Submenu` instead of `tauri::SystemTraySubmenu` and `tauri::menu::PredefinedMenuItem` instead of `tauri::SystemTrayMenuItem`.
#### Tray Events
`tauri::SystemTray::on_event` have been split into `tauri::tray::TrayIconBuilder::on_menu_event` and `tauri::tray::TrayIconBuilder::on_tray_icon_event`:
```

use tauri::{
menu::{MenuBuilder, MenuItemBuilder},
tray::{MouseButton, MouseButtonState, TrayIconBuilder, TrayIconEvent},
};
tauri::Builder::default()
.setup(|app| {
lettoggle= MenuItemBuilder::with_id("toggle", "Toggle").build(app)?;
letmenu= MenuBuilder::new(app).items(&[&toggle]).build()?;
lettray= TrayIconBuilder::new()
.menu(&menu)
.on_menu_event(move|app, event|matchevent.id().as_ref() {
"toggle"=> {
println!("toggle clicked");
}
_=> (),
})
.on_tray_icon_event(|tray, event| {
iflet TrayIconEvent::Click {
button: MouseButton::Left,
button_state: MouseButtonState::Up,
..
} =event
{
letapp=tray.app_handle();
iflet Some(webview_window) =app.get_webview_window("main") {
let_=webview_window.show();
let_=webview_window.set_focus();
}
}
})
.build(app)?;
Ok(())
})

```

### Migrate to Updater Plugin
The Rust `tauri::updater` and JavaScript `@tauri-apps/api-updater` APIs have been removed. To set a custom updater target with the `@tauri-apps/plugin-updater`:
  1. Add to cargo dependencies:


```

[dependencies]
tauri-plugin-updater = "2"

```

  1. Use in JavaScript or Rust project:


  * JavaScript 
  * Rust 


```

fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_updater::Builder::new().build())
}

```

package.json```

{
"dependencies": {
"@tauri-apps/plugin-updater": "^2.0.0"
}
}

```

```

import { check } from'@tauri-apps/plugin-updater';
import { relaunch } from'@tauri-apps/plugin-process';
const update = await check();
if (update?.available) {
console.log(`Update to ${update.version} available! Date: ${update.date}`);
console.log(`Release notes: ${update.body}`);
awaitupdate.downloadAndInstall();
// requires the `process` plugin
awaitrelaunch();
}

```

To check for updates:
```

use tauri_plugin_updater::UpdaterExt;
fnmain() {
tauri::Builder::default()
.plugin(tauri_plugin_updater::Builder::new().build())
.setup(|app| {
lethandle=app.handle();
tauri::async_runtime::spawn(asyncmove {
letresponse=handle.updater().check().await;
});
Ok(())
})
}

```

To set a custom updater target:
```

fnmain() {
letmutupdater= tauri_plugin_updater::Builder::new();
#[cfg(target_os ="macos")]
{
updater=updater.target("darwin-universal");
}
tauri::Builder::default()
.plugin(updater.build())
}

```

### Migrate Path to Tauri Manager
The Rust `tauri::api::path` module functions and `tauri::PathResolver` have been moved to `tauri::Manager::path`:
```

use tauri::{path::BaseDirectory, Manager};
tauri::Builder::default()
.setup(|app| {
lethome_dir_path=app.path().home_dir().expect("failed to get home dir");
letpath=app.path().resolve("path/to/something", BaseDirectory::Config)?;
Ok(())
})

```

### Migrate to new Window API
On the Rust side, `Window` was renamed to `WebviewWindow`, its builder `WindowBuilder` is now named `WebviewWindowBuilder` and `WindowUrl` is now named `WebviewUrl`.
Additionally, the `Manager::get_window` function was renamed to `get_webview_window` and the window’s `parent_window` API was renamed to `parent_raw` to support a high level window parent API.
On the JavaScript side, the `WebviewWindow` class is now exported in the `@tauri-apps/api/webviewWindow` path.
The `onMenuClicked` function was removed, you can intercept menu events when creating a menu in JavaScript instead.
### Migrate Embedded Additional Files (Resources)
On the JavaScript side, make sure you Migrate to File System Plugin. Additionally, note the changes made to the v1 allowlist in Migrate Permissions.
On the Rust side, make sure you Migrate Path to Tauri Manager.
### Migrate Embedded External Binaries (Sidecar)
In Tauri v1, the external binaries and their arguments were defined in the allowlist. In v2, use the new permissions system. Read Migrate Permissions for more information.
On the JavaScript side, make sure you Migrate to Shell Plugin.
On the Rust side, `tauri::api::process` API has been removed. Use `tauri_plugin_shell::ShellExt` and `tauri_plugin_shell::process::CommandEvent` APIs instead. Read the Embedding External Binaries guide to see how.
The “process-command-api” features flag has been removed in v2. So running the external binaries does not require this feature to be defined in the Tauri config anymore.
### Migrate Permissions
The v1 allowlist have been rewritten to a completely new system for permissions that works for individual plugins and is much more configurable for multiwindow and remote URL support. This new system works like an access control list (ACL) where you can allow or deny commands, allocate permissions to a specific set of windows and domains, and define access scopes.
To enable permissions for your app, you must create capability files inside the `src-tauri/capabilities` folder, and Tauri will automatically configure everything else for you.
The `migrate` CLI command automatically parses your v1 allowlist and generates the associated capability file.
To learn more about permissions and capabilities, see the security documentation.
© 2025 Tauri Contributors. CC-BY / MIT
