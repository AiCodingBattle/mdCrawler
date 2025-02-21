Skip to content
# Tauri 2.0 Stable Release
Oct 2, 2024 
![Tillmann Weidinger](https://v2.tauri.app/authors/tweidinger.png)
Tillmann Weidinger
Tauri Security
We are very proud to finally announce the stable release for the new major version of Tauri. Welcome to Tauri 2.0!
## What is Tauri?
In a Tauri application the frontend is written in your favorite web frontend stack. This runs inside the operating system WebView and communicates with the application core written mostly in Rust.
![a graph showing the IPC bridge between the Application Core and the System's WebView](https://v2.tauri.app/_astro/tauri-trust-boundaries.C0cC9LAT_Z2iV8qr.svg)
### When Should I Use Tauri?
If you check **any** of the boxes below, you should use Tauri:
  * Do you want a single UI codebase for all platforms?
  * Do you want to reach as many users as possible on their platform (eg. Windows, MacOS, Linux, Android, iOS)?
  * Are you a frontend web developer and want to write native applications?
  * Are you a Rust developer looking to write applications with a nice looking UI with the option to do it in Rust?
  * Do you have an existing team of web developers and want to expand to native application markets with low upfront investment?
  * Do you have an existing team of rustaceans and want everything written in Rust?


## How Popular is Tauri?
![a graph showing the progression of Tauri GitHub stars over the years, starting with 0 at 2019 and continuing to grow past 80.000 in 2024](https://v2.tauri.app/_astro/tauri-star-history.Dr3CGlN3_Z174Gdc.webp)
On GitHub the Tauri repository has ~4,878 Pull Requests and ~3,570 Issues closed and around 1000 discussions, at the time of writing. To get a more detailed insight take a look at the OSSinsight analysis of the Tauri repository.
Our Discord Server currently has ~17,700 members. We are seeing a lot of individual user support, questions on Tauri itself, questions directly to the working group or just discussions between fellow Tauri app developers.
We are very happy about the positive and supportive community and grateful to all the community members answering or helping others in Discord or GitHub.
We maintain a curated list of Tauri related projects, applications, plugins, guides and more at awesome-tauri. Check this out if you want to get inspiration, see what others are building and ideally create a PR to add your project.
Of course this is only a representative sample set and we don’t know exactly who else is building on Tauri.
## How Did We Get to 2.0?
In June 2022 we released Tauri 1.0 with a great impact on the desktop operating system market and how cross platform applications can be built.
In the end of 2022 we released our initial alpha version of 2.0 to get initial feedback and to test out how mobile interaction should be defined.
After the initial alpha we spent close to two years refining and changing the architecture of Tauri in public. After we saw the broad picture clear enough ourselves we released the beta in Februrary this year. At the same time we collaborated and worked with external security auditors to check our decisions, architecture changes and much more.
This August we published the release candidate version of 2.0 to iron out major bugs and to get more feedback from productive use. At the same time the external audit was concluded and made public.
The release candidate time frame was considerably shorter and consisted mainly of high impact bugfixes and documentation improvements. Some breaking changes we had to make during the release candidate phase were bundled up until the end and are now included in the stable release. Take a look at the migration section if your main concern is upgrading from a previous version.
In total we spent over two years working on improvements, new features, bugfixes, documentation, rewrites and a lot of discussions.
This all happened while we released 8 minor versions of the Tauri 1.x branch and backported security fixes and other important bug fixes in several patch releases.
## Who Made This Release Possible?
This release and Tauri itself is only possible due to massive amount of contributions from Lucas, who has provided a constant stream of code changes over the years ❤️.
![Lucas' contribution graph, with 2744 commits, over 896.000 additions and 688.000 deletions.](https://v2.tauri.app/_astro/lucas-commit-graph.gQ6-XyEM_19scIV.webp)
Obviously, Lucas is not the only individual working and contributing to Tauri, but we feel he deserves a very special mention for carrying, starting, and supporting the project and its community throughout the years.
We have had major contributions to the Tauri repository in 2.0 from Amr, Fabian-Lars, Tony, Chip, Jason, YuWei, icb , Simon, Oliver Lemasle and many more contributors (source data).
We received an increasing number of drive-by contributors (one or very few PRs). We are grateful for these, but naming everyone would make this a very long list here.
We have a lot(!) of repositories in our organization, which are supporting the success of Tauri and without community and working group contributions Tauri would not be where it is now. A big thank you to everyone involved!
Another special shout out and thanks for their constant involvement in the community goes to Fabian-Lars and Simon. If you have been involved in Tauri’s Discord or Github discussions you likely know their name or avatar.
If you ever searched on Google or YouTube for Tauri, you have probably seen one of Jacob’s streams. If that’s not the case please make sure to check it out and subscribe as his sessions are beyond just educational.
Another special place in our heart has the Tauri Board, highlighting Daniel Yvetot-Thompson for the numerous hours, sweat, blood and dedication to make Tauri known and sustainable.
One important thing we should not forget, is that we acquired support from a stable partner of this open source project.
![CrabNebula Logo](https://v2.tauri.app/_astro/crabnebula.xh9nhpEF_1dCLwa.svg)
CrabNebula granted multiple people mentioned above and others that are not mentioned here, the privilege to work on the Tauri ecosystem not only in their private time, but also during work time. You can find the partnership announcement on our blog and we have been more than happy about this collaboration over the last year.
In 2024 alone they spent over **2,870** work hours on this project, which massively pushed the progress and allows us to announce the stable 2.0 release today.
If you were not aware of CrabNebula yet, make sure to check out their products and services and consider the symbiotic relationship with Tauri if you are interested in not only improving your workflows, but also supporting the Tauri ecosystem.
## What Makes 2.0 Great?
With this major release we improved and changed several aspects of how and where you can build, develop and publish your Tauri app. In the following sections we have more detailed insight. This does not cover everything, but should give you a decent impression on what you can expect from Tauri.
### Getting Started Experience
One thing you are always going to go through when starting with a new framework or tool is the initial onboarding or getting started process.
We value developer experience (DX) and try to make this initial process as seamless as building and distributing your final application.
For this we created another project, which is called `create-tauri-app` or in short CTA. This tool allows developers to start from scratch and get to a running Tauri app in a few minutes instead of hours.
  * Bash 
  * PowerShell 
  * npm 
  * Yarn 
  * pnpm 
  * deno 
  * bun 
  * Cargo 


```

sh<(curl https://create.tauri.app/sh)

```

```

irmhttps://create.tauri.app/ps|iex

```

```

npmcreatetauri-app@latest

```

```

yarncreatetauri-app

```

```

pnpmcreatetauri-app

```

```

denorun-Anpm:create-tauri-app

```

```

buncreatetauri-app

```

```

cargoinstallcreate-tauri-app--locked
cargocreate-tauri-app

```

Of course you need to install some prerequisites on your development system before you can start building your application. For this we have extensive guides with operating system specific sections in our official documentation.
This whole onboarding experience has been improved and now also bootstraps mobile development templates for iOS and Android.
### Hot-Module Replacement
After the initial onboarding you will regularly develop and debug your Tauri application. We considered what would improve your development process already in 1.x of Tauri and extended the Hot-Module Replacement (HMR) to mobile devices and emulators.
This means that all changes to the frontend of your application do not require a rebuild of your whole application and you can live preview how it will look like in the device or operating system your are developing for.
Your browser does not support the video tag.
### Plugins
With Tauri 2.0 we built a more advanced plugin system. We transferred a lot of our previous functionality into our official plugins (see plugins-workspace), to allow the community an easier entry into contributing to Tauri. We also hope to attract more maintainers for plugins and to speed up the process of implementing new features.
This move to plugins has another benefit. We are going to be able to define a definition of done for Tauri’s core. We hope to stabilize the core functionality and offer a stable framework, where the moving parts are mostly plugins offering access to system specific functionality.
You no longer need to understand all of Tauri to improve or implement specific features. The plugins usually do not depend on other plugins, with some exceptions. This means to implement a new file system access functionality it is only required to contribute to the `fs` plugin instead of Tauri itself.
As this release also targets mobile platforms, the plugin system also supports mobile plugins. You can write or re-use native code in Swift on iOS and Kotlin on Android and directly expose functions to the Tauri frontend using `Annotations` (`@Command` on Android), implementing a `Subclass` (`YourPluginClass: Plugin`) on iOS, or by invoking the Swift or Kotlin code from a Rust based Tauri command. Check out the documentation on how to write your own plugin.
As we are releasing Tauri as 2.0, the official plugins will follow the major version of Tauri to make compatibility with Tauri’s major version visible at a glance. Not all plugins are as stable as Tauri itself though.
Each plugin’s stableness is defined per plugin and documented (soon) in the plugin documentation. The plugin API can possibly break in minor versions, but we will try to keep these changes to a minimum, especially for plugins considered stable.
Autostart
Automatically launch your app at system startup.
Barcode Scanner
Allows your mobile application to use the camera to scan QR codes, EAN-13 and other types of barcodes.
Biometric
Prompt the user for biometric authentication on Android and iOS.
Clipboard
Read and write to the system clipboard.
Command Line Interface (CLI)
Parse arguments from the command line interface.
Deep Linking
Set your Tauri application as the default handler for an URL.
Dialog
Native system dialogs for opening and saving files along with message dialogs.
File System
Access the file system.
Global Shortcut
Register global shortcuts.
HTTP Client
Access the HTTP client written in Rust.
Localhost
Use a localhost server in production apps.
Logging
Configurable logging.
NFC
Read and write NFC tags on Android and iOS.
Notifications
Send native notifications to the user.
Opener
Open files and URLs in external applications.
OS Information
Read information about the operating system.
Persisted Scope
Persist runtime scope changes on the filesystem.
Positioner
Move windows to common locations.
Process
Access the current process.
Shell
Access the system shell to spawn child processes.
Single Instance
Ensure that a single instance of your Tauri app is running at a time.
SQL
Tauri Plugin providing an interface for the frontend to communicate with SQL databases through sqlx.
Store
Persistent key value storage.
Stronghold
Encrypted, secure database.
Updater
In-app updates for Tauri applications.
Upload
File uploads through HTTP.
Websocket
Open a WebSocket connection using a Rust client in JavaScript.
Window State
Persist window sizes and positions.
### Mobile Support
A very much awaited part of this release is the mobile operating system support. The previous version of Tauri allowed to have a single UI code base for desktop operating systems but now this extends to iOS and Android.
We have investigated and experimented with different solutions to support mobile and decided on using the operating system native language (Swift and Kotlin) to build an interface for the Rust code and to allow developers to write part of their functionality in these languages.
This means you can re-use existing logic of your Swift or Kotlin app that interacts with the system and expose it to Rust or the frontend. Right now this works as mentioned above via the plugin system.
We support development with an emulator or a real device and provide a lot of tooling to make the process as seamless as possible. We are not completely happy about the developer experience at the moment but are actively improving to bring it up to par with the desktop experience.
On mobile not all of the official plugins are supported. Some are by design not a good fit for mobile and some are just not implemented to support mobile yet. If you would like to contribute on this part check the last section of this post.
### The Allowlist is Dead, Long Live the Allowlist
Yes, there is no `allowlist` anymore, as we hit the limits of this system pretty quickly. We made it exclusive for Tauri core features and it did not even cover all of Tauri’s APIs. Our new system not only covers all of Tauri’s core API surface, it also supports app and plugin developers to implement their own access control and scoping with a unified approach.
The new system we implemented is using `permissions` - _“On-off toggles for Tauri commands”_ , `scopes` - _“Parameter validation for Tauri commands”_ and `capabilities` - _“Attaching permissions and scopes to Windows and WebViews”_ , to create a flexible but simple to use access control system.
It allows the creation of named permission or scoping files and to re-use and combine them with other named permissions or scopes. This makes it possible to build more fine grained descriptive sets containing several simple or complex permissions and scopes.
As a plugin developer you can abstract away several base permissions into a `default` permission. This can be based on your default security assumptions and threat model. All official Tauri plugin default permissions are reasonably secure by default.
As an app developer you can use, extend or reduce plugin permissions. Of course you can also build permissions and scopes for your own application.
With this addition, Tauri’s core is now able to understand if a command invoke message from a frontend WebView is allowed to reach the command function. It is also able to attach the configured scope to the message.
The command implementation is responsible for interpreting and enforcing the scope. You can read more about our Threat Model and approach to security in our documentation.
### External Security Audit
The major changes and architecture of v2 was independently audited by Radically Open Security during the beta and release candidate period. Please take your time to read the report and learn more about the awesome work of @gronke and @pcwizz.
The whole audit was funded by the great folks at NLNet via funding from NGI and we are super grateful to be in the privileged position to get fully funded external security audits for major releases.
The results of this audit caused us to rewrite parts of how our dev server is exposed, specifically for mobile development. Without the help and guidance of the auditors this rewrite would not have been possible ❤️.
Additionally, we hardened our iFrame API exposure, fixed scope validation and resource identifier access for the `fs` and `http` plugin, improved our inter-process communication stability, and many other security related fixes and improvements.
### Inter Process Communication (IPC) Rewrite
With the rewrite of our IPC layer we now support a long wished feature of Raw Payloads and generally changed how it works under the hood.
Previously **all** IPC payloads were json serialized and deserialized which caused an overhead. This was noticeable once more than a few kilobytes were transfered between frontend and backend.
The new system supports Raw Requests. These speed up the transfer of large data from backend to frontend and vice versa, where you can either use raw bytes directly or use your own (de)serialization process (eg. bson, protobuf, avro and others).
For directly reading files from the filesystem into the WebView we still recommend the `convertFileSrc` functionality, as it is most likely still faster if you do not need to process the data on the Rust backend.
### Distribution Guides
With Tauri 2.0 the distribution diversity greatly increased. Partially, due to the mobile ecosystem and partially due to our community contributions.
We have official guides on how to ship to the Apple Appstore, Google Play, Microsoft Store, CrabNebula Cloud, Flathub, Snapcraft, AUR and more distribution formats in our distribution docs.
## Changelog
This section contains all changes going from 1.x in a concise list.
_Show the Full List_
### Added
  * Added Mobile support.
  * Added multiwebview support behind the unstable feature flag. See WindowBuilder and WebviewBuilder for more information.
  * Added `rustls-tls` cargo feature flag
  * Added `shadow` option when creating a webview window,`WebviewWindow::set_shadow` method in Rust and equivalent API in JS.
  * Added `tauri::Webview`, `tauri::WebviewBuilder`, `tauri::WebviewWindow`, `tauri::WebviewWindowBuilder` structs in Rust and equivalent classes in Js. The old `tauri::Window` and `tauri::WindowBuilder` behaviors have moved to `tauri::WebviewWindow` and `tauri::WebviewWindowBuilder`.
  * Added `tauri::scope::fs` module
  * Added `tauri::App/AppHandle::default_window_icon` method.
  * Added `tauri::ipc` module with IPC primitives.
  * Added `tauri::ipc::Channel` type and equivalent JS `Channel` type to send data across the IPC.
  * Added `incognito` option when creating a webview window.
  * Added `windowEffects` option when creating a webview window and `WebviewWindow::set_effects` to try and change effects at runtime.
  * Added `tauri::path::PathResolver`
  * Added `tauri::Manager::path` method to access the new `PathResolver`
  * Added `visibleOnAllWorkspaces` option when creating a webview window.
  * Added `tauri::App/AppHandle::primary_monitor` and `App/AppHandle::available_monitors` methods.
  * Added `tauri::plugin::Builder::on_navigation` and `tauri::plugin::Plugin::on_navigation`.
  * Added `tauri::WebviewWindow::navigate` method
  * Added `tauri::RunEvent::Opened` on macOS and iOS for deep link support.
  * Added file associations support in bundler.
  * Added `tauri::App/AppHandle::cleanup_before_exit` to manually call the cleanup logic. You should always exit the tauri app immediately after this function returns and not use any tauri-related APIs.
  * On Linux, add `tauri::WebviewWindow::default_vbox` method to get a reference to the `gtk::Box` that contains the menu bar and the webview.
  * Added `linux-libxdo` cargo feature flag (disabled by default) to enable linking to `libxdo` which is used to make `Cut`, `Copy`, `Paste` and `SelectAll` native menu items work on Linux.
  * On macOS, add `tauri::WebviewWindow::ns_view` method to get a pointer to the `NSWindow` content view.
  * Added `tauri::Builder::register_asynchronous_uri_scheme_protocol` to allow resolving a custom URI scheme protocol request asynchronously to prevent blocking the main thread.
  * Included drop and hover position for drag and drop events.
  * Added `tauri::WebviewWindow::set_progress_bar` method
  * Added `tauri::WebviewWindow::set_always_on_bottom` method and `alwaysOnTop` option when creating a webview window.
  * Added `tauri::WebviewWindowBuilder::on_page_load` method.
  * Added `common-controls-v6` cargo feature flag (enabled by default).
  * Added `Window::destroy` to force close a window.
  * Added `tauri::EventId` type
  * Added `tauri::WindowBuilder::on_download` to handle download request events.
  * Added `tauri::WebviewWindowBuilder::parent` which is a convenient wrapper around parent functionality for Windows, Linux and macOS.
  * Added `tauri::WebviewWindowBuilder::owner` on Windows only.
  * Added `tauri::WebviewWindowBuilder::transient_for` and `tauri::WebviewWindowBuilder::transient_for_raw` on Linux only.
  * Added `tauri::WebviewWindow::start_resize_dragging` and `tauri::ResizeDirection` enum.
  * Added `tauri::WebviewWindowBuilder::proxy_url` method.
  * Added `tauri::WebviewEvent` enum
  * Added `tauri::RunEvent::WebviewEvent` variant.
  * Added `tauri::Builder::on_webview_event` and `tauri::Webview::on_webview_event` methods.
  * Added `tauri::image` module which includes`tauri::image::Image` and `tauri::image::JsImage` types and `tauri::image::include_img!` macro.
  * Added `tauri::is_dev` function to determine whether the app is running in development mode or not.
  * Added `tauri::Assets::setup` method on `tauri::Assets` trait that lets you run initialization code for your custom asset provider.
  * Added `tauri::Rect` struct.
  * Added `tauri::WebviewWindow::set_zoom` method
  * Added `zoomHotkeys` option when creating a webview window.
  * Added `window.isTauri` JS global function to check whether running in tauri or not.
  * Added `specta` feature flag which adds `specta` support for `AppHandle`, `State`, `Window`, `Webview` and `WebviewWindow` types.
  * Added `tauri::App/AppHandle/WebviewWindow::cursor_position` getter to get the current cursor position.
  * Added `tauri::App/AppHandle/WebviewWindow::monitor_from_point(x,y)` getter to get the monitor from a given point..
  * Added `tauri::RunEvent::Reopen` to handle click on dock icon on macOS.
  * Added `defaultWindowIcon` to the JS `app` module to retrieve the default window icon in JS.
  * Added `tauri::WebviewWindow::set_title_bar_style` to set title bar at runtime on macOS.
  * Add APIs to enable setting window size constraints separately: 
    * Added `tauri::WindowBuilder::inner_size_constraints` and `tauri::WebviewWindowBuilder::inner_size_constraints`
    * Added `tauri::WindowSizeConstraints` struct
    * Added `tauri::Window::set_size_constraints` and `tauri::WebviewWindow::set_size_constraints`


### Enhancements
  * Use custom protocols on the IPC implementation to enhance performance.
  * Enhance centering a newly created window, it will no longer jump to center after being visible.
  * The `custom-protocol` Cargo feature is no longer required on your application and is now ignored. To check if running on production, use `#[cfg(not(dev))]` instead of `#[cfg(feature = "custom-protocol")]`.
  * Improved the JS `path` APIs to return simplified paths on Windows when possible, i.e removing UNC (`\\?\`) prefix.
  * Improved the error message that is shown when deserializing the Tauri plugin config.
  * Set the gtk application id to the `identifier` defined in `tauri.conf.json` to ensure the app uniqueness. This can be disabled by setting `enableGtkAppId` option to `false`.
  * On Windows, handle resizing undecorated windows natively which improves performance and fixes a couple of annoyances with previous JS implementation: 
    * No more cursor flickering when moving the cursor across an edge.
    * Can resize from top even when `data-tauri-drag-region` element exists there.
    * Upon starting rezing, clicks don’t go through elements behind it so no more accidental clicks.
  * Mark `AppHandle::restart` and `process::restart` as diverging functions


### Bug Fixes
  * No longer unpacking and flattening the `payload` over the IPC so that commands with arguments called `cmd`, `callback`, `error`, `options` or `payload` aren’t breaking the IPC.
  * Fix calling `set_activation_policy` when the event loop is running.
  * Fix can not prevent closing a window from another webview.
  * On Windows, fix decorated window not transparent initially until resized.
  * Resolve symlinks on the filesystem scope check.
  * Fix the JS `basename(path, 'ext')` API implementation removing all occurances of `ext` where it should only remove the last one.
  * Fix window white flashing on exit on Windows
  * Apply `minWidth`, `minHieght`, `maxWidth` and `maxHeight` constraints separately, which fixes a long standing bug where these constraints were never applied unless width and height were constrained together.


### Changed
  * The window creation and setup hook are now called when the event loop is ready.
  * Renamed the `default-tls` feature to `native-tls` and.
  * Changed the plugin setup hook to take a second argument of type `PluginApi`
  * Changed `tauri::Window` struct behavior and moved its old behavior to the new `tauri::WebviewWindow` type.
  * Moved `tauri::api::path` module to `tauri::path`
  * Moved all functions from `tauri::api::path` to be methods on `tauri::path::PathResolver`
  * Renamed `system-tray` feature flag to `tray-icon`.
  * Changed `tauri::App::handle` and `tauri::Manager::app_handle` methods to return a reference to an `AppHandle` instead of an owned value.
  * Changed `tauri::Builder::register_uri_scheme_protocol` to return a `http::Response` instead of `Result<http::Response>`. To return an error response, manually create a response with status code >= 400.
  * The custom protocol on Windows and Android now uses the `http` scheme instead of `https`.
  * Changed `tauri::Env.args` to `tauri::Env.args_os` and now uses `OsString` instead of `String`
  * Changed `TAURI_AUTOMATION` env var to `TAURI_WEBVIEW_AUTOMATION`
  * Changed `tauri::Builder::invoke_system` to take references instead of owned values.
  * Changed`tauri::Builder::invoke_system`, `tauri::Builder::on_page_load` hooks to take a `tauri::Webview` argument instead of a `tauri::Window`.
  * Moved the `tauri::command` module items to the `tauri::ipc` module so its import name does not clash with the `tauri::command` macro.
  * Changed `tauri::App::run_iteration` to take a callback and removed its return value.
  * Changed `AppHandle::exit` and `AppHandle::restart` to trigger `RunEvent::ExitRequested` and `RunEvent::Exit`
  * Renamed `tauri::WebviewWindowBuilder::owner_window` to `tauri::WebviewWindowBuilder::owner_raw` and `tauri::WebviewWindowBuilder::parent_window` to `tauri::WebviewWindowBuilder::parent_raw`.
  * Renamed the `window-data-url` feature flag to `webview-data-url`.
  * Changed `tauri::WebviewWindow::close` to trigger a close requested event instead of forcing the window to be closed. Use `tauri::WebviewWindow::destroy` to force close.
  * Renamed `icon-ico` and `icon-png` feature flags to `image-ico` and `image-png` respectively.
  * Removed `tauri::Icon` enum, use the new `tauri::Image` type instead. All APIs that previously accepted `tauri::Icon` have changed to accept `tauri::Image` instead.
  * Changed `tauri::Context` struct and `tauri::Assets` trait to have a `R: Runtime` generic.
  * Renamed `tauri::Context::assets_mut` to `tauri::Context::set_assets`
  * Changed `tauri::Context` type to not have `<A: Assets>` generic so the assets implementation can be swapped with `Context::set_assets`.
  * Changed `tauri::Context::assets` to return `&dyn Assets` instead of `&A` generic.
  * Renamed `tauri::FileDropEvent` enum to `tauri::DragDropEvent` and renamed its variants. Also renamed the js events
  * Renamed `tauri::WindowEvent::FileDrop` enum variant to `tauri::WindowEvent::DragDrop`
  * Renamed file drop emitted events to `tauri://drag-enter`, `tauri://drag-over`, `tauri://drag-drop`, and `tauri://drag-leave`
  * Renamed `tauri::WebviewWindow::disable_file_drop_handler` to `tauri::WebviewWindow::disable_drag_drop_handler`.
  * Changed `tauri::WebviewWindow::url` getter to return a result.
  * Changed `tauri::Env.args_os`, to include the binary path, previously it was skipped.
  * Renamed `getAll` and `getCurrent` to `getAllWindows` and `getCurrentWindow` in the JS `window` module but you probably want `getAllWebviewWindows` and `getCurrentWebviewWindow` from the `webviewWindow` module.


### Removed
  * The `reqwest-*` Cargo features were removed
  * `UpdaterEvent`
  * Removed`tauri::api` module and moved them into standalone plugins in `plugins-workspace` repo.
  * Removed `tauri::scope::IpcScope`
  * Removed `tauri::scope::ipc` module and all its types.
  * Removed `tauri::scope::FsScope`, use `tauri::scope::fs::Scope`
  * Removed `tauri::scope::GlobPattern`, use `tauri::scope::fs::Pattern`
  * Removed `tauri::scope::FsScopeEvent`, use `tauri::scope::fs::Event`
  * Removed `tauri::scope::HttpScope`
  * Removed `tauri::scope::ShellScope`
  * Removed `tauri::scope::ShellScopeAllowedCommand`
  * Removed `tauri::scope::ShellScopeAllowedArg`
  * Removed `tauri::scope::ExecuteArgs`
  * Removed `tauri::scope::ShellScopeConfig`
  * Removed `tauri::scope::ShellScopeError`
  * Removed `linux-protocol-headers` cargo feature flag, now enabled by default.
  * Removed `tauri::path::Error` and `tauri::path::Result` and added its variants to `tauri::Error`
  * Removed `tauri::path::Result` and `tauri::plugin::Result` aliases, you should use `tauri::Result` or your own `Result` type.
  * Changed `tauri::Builder::on_page_load` handler to take references. The page load hook is now triggered for load started and finished events, to determine what triggered it see `tauri::PageLoadPayload::event` field.
  * Removed `tauri::GlobalWindowEvent` struct, and unpacked its fields to be passed directly to `tauri::Builder::on_window_event`.
  * Removed `tauri::EventHandler` type.
  * Renamed `tauri::Context::default_window_icon_mut` to `tauri::Context::set_default_window_icon` and changed it to accept `Option<T>`.


### Config restructure
Restructured Tauri config per RFC#5:
  * Moved `package.productName`, `package.version` and `tauri.bundle.identifier` fields to the top-level.
  * Removed `package` object.
  * Renamed `tauri` object to `app`.
  * Moved `tauri.bundle` object to the top-level.
  * Renamed `build.distDir` field to `frontendDist`.
  * Renamed `build.devPath` field to `devUrl` and will no longer accepts paths, it will only accept URLs.
  * Moved `tauri.pattern` to `app.security.pattern`.
  * Removed `tauri.bundle.updater` object, and its fields have been moved to the updater plugin under `plugins.updater` object.
  * Moved `build.withGlobalTauri` to `app.withGlobalTauri`.
  * Moved `tauri.bundle.dmg` object to `bundle.macOS.dmg`.
  * Moved `tauri.bundle.deb` object to `bundle.linux.deb`.
  * Moved `tauri.bundle.appimage` object to `bundle.linux.appimage`.
  * Removed all license fields from each bundle configuration object and instead added `bundle.license` and `bundle.licenseFile`.
  * Renamed `AppUrl` to `FrontendDist` and refactored its variants to be more explicit.
  * Renamed `tauri.window.fileDropEnabeld` to `app.window.dragDropEnabled`


## Migration
As we try to make the migration from previous Tauri versions as smooth as possible, we have documentation available to guide you through the process.
If you are migrating from a 1.x release please check out this migration guide.
For upgrading from a 2.0 beta or release candidate version check out this migration guide.
The Tauri v2 CLI includes a `migrate` command that automates most of the process and helps you finish the migration:
  * npm 
  * yarn 
  * pnpm 
  * cargo 


```

npminstall@tauri-apps/cli@next
npmruntaurimigrate

```

```

yarnupgrade@tauri-apps/cli@next
yarntaurimigrate

```

```

pnpmupdate@tauri-apps/cli@next
pnpmtaurimigrate

```

```

cargoinstalltauri-cli--version"^2.0.0"--locked
cargotaurimigrate

```

## Call To Action
If you are familiar with Tauri and have used it already during your journey, please take your time to check out the Github Discussions, Github Issues. Maybe you have already solved the issues your fellow newcomers to Tauri are experiencing right now.
If you think that some of these problems you have seen are generic and should be documented somewhere we probably have the perfect place for it in our official documentation.
To contribute improvements or additions we are open for PRs in the tauri-docs repository. Please make sure you’ve read the guidelines for contribution though.
If you are in the position to understand and translate the current documentation into your native language we appreciate content translations to our documentation.
The repositories surrounding Tauri are also looking for contributors, especially we would love more maintainers and contributors to the `plugin-workspace`.
The plugins are now a major part of the development and user experience of Tauri and all kind of help is welcome there. From discussing new plugin ideas, collaborating with others to write new plugins, contributing PRs to fix bugs in existing plugins or documenting weird workarounds and knowledge in the plugin readme or code.
## Roadmap
You probably expect solid plans for the future and new cool ideas from us. We currently have some in mind but have not committed to a roadmap beyond 2.x yet.
We mainly want to focus on improving this major version with a better developer experience, better documentation and less impactful bugs. We want to improve especially the mobile development experience and make the whole flow from idea to published application as seamless as possible.
Things on our radar for the future we feel we should mention at least:
  * Providing or Bundling Chromium Embedded Framework (CEF) for Linux as an alternative to WebKit2GTK
  * Servo as Tauri WebView (POC in Wry)


If you want to collaborate on these ideas, please let us know and we will figure it out together.
Tauri 2.0 Release Candidate
© 2025 Tauri Contributors. CC-BY / MIT
