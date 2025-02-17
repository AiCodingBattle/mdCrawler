Skip to content
# Command Line Interface
The Tauri command line interface (CLI) is the way to interact with Tauri throughout the development lifecycle.
You can add the Tauri CLI to your current project using your package manager of choice:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npminstall--save-dev@tauri-apps/cli@latest

```

```

yarnadd-D@tauri-apps/cli@latest

```

```

pnpmadd-D@tauri-apps/cli@latest

```

```

denoadd-Dnpm:@tauri-apps/cli@latest

```

```

cargoinstalltauri-cli--version"^2.0.0"--locked

```

## List of Commands
Command| Description  
---|---  
`init`| Initialize a Tauri project in an existing directory  
`dev`| Run your app in development mode  
`build`| Build your app in release mode and generate bundles and installers  
`bundle`| Generate bundles and installers for your app (already built by `tauri build`)  
`android`| Android commands  
`android init`| Initialize Android target in the project  
`android dev`| Run your app in development mode on Android  
`android build`| Build your app in release mode for Android and generate APKs and AABs  
`migrate`| Migrate from v1 to v2  
`info`| Show a concise list of information about the environment, Rust, Node.js and their versions as well as a few relevant project configurations  
`add`| Add a tauri plugin to the project  
`remove`| Remove a tauri plugin from the project  
`plugin`| Manage or create Tauri plugins  
`plugin new`| Initializes a new Tauri plugin project  
`plugin init`| Initialize a Tauri plugin project on an existing directory  
`plugin android`| Manage the Android project for a Tauri plugin  
`plugin ios`| Manage the iOS project for a Tauri plugin  
`plugin android init`| Initializes the Android project for an existing Tauri plugin  
`plugin ios init`| Initializes the iOS project for an existing Tauri plugin  
`icon`| Generate various icons for all major platforms  
`signer`| Generate signing keys for Tauri updater or sign files  
`signer sign`| Sign a file  
`signer generate`| Generate a new signing key to sign files  
`completions`| Generate Tauri CLI shell completions for Bash, Zsh, PowerShell or Fish  
`permission`| Manage or create permissions for your app or plugin  
`permission new`| Create a new permission file  
`permission add`| Add a permission to capabilities  
`permission rm`| Remove a permission file, and its reference from any capability  
`permission ls`| List permissions available to your application  
`capability`| Manage or create capabilities for your app  
`capability new`| Create a new permission file  
`inspect`| Manage or create permissions for your app or plugin  
`inspect wix-upgrade-code`| Print the default Upgrade Code used by MSI installer derived from productName  
### `init`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriinit

```

```

yarntauriinit

```

```

pnpmtauriinit

```

```

denotasktauriinit

```

```

cargotauriinit

```

```

Initialize a Tauri project in an existing directory
Usage: tauri init [OPTIONS]
Options:
--ci
Skip prompting for values [env: CI=true]
-v, --verbose...
Enables verbose logging
-f, --force
Force init to overwrite the src-tauri folder
-l, --log
Enables logging
-d, --directory <DIRECTORY>
Set target directory for init [default: /opt/build/repo/packages/cli-generator]
-t, --tauri-path <TAURI_PATH>
Path of the Tauri project to use (relative to the cwd)
-A, --app-name <APP_NAME>
Name of your Tauri application
-W, --window-title <WINDOW_TITLE>
Window title of your Tauri application
-D, --frontend-dist <FRONTEND_DIST>
Web assets location, relative to <project-dir>/src-tauri
-P, --dev-url <DEV_URL>
Url of your dev server
--before-dev-command <BEFORE_DEV_COMMAND>
A shell command to run before `tauri dev` kicks in
--before-build-command <BEFORE_BUILD_COMMAND>
A shell command to run before `tauri build` kicks in
-h, --help
Print help
-V, --version
Print version

```

### `dev`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauridev

```

```

yarntauridev

```

```

pnpmtauridev

```

```

denotasktauridev

```

```

cargotauridev

```

```

Run your app in development mode with hot-reloading for the Rust code. It makes use of the `build.devUrl` property from your `tauri.conf.json` file. It also runs your `build.beforeDevCommand` which usually starts your frontend devServer.
Usage: tauri dev [OPTIONS] [ARGS]...
Arguments:
[ARGS]...
Command line arguments passed to the runner. Use `--` to explicitly mark the start of the arguments. Arguments after a second `--` are passed to the application e.g. `tauri dev -- [runnerArgs] -- [appArgs]`
Options:
-r, --runner <RUNNER>
Binary to use to run the application
-v, --verbose...
Enables verbose logging
-t, --target <TARGET>
Target triple to build against
-f, --features [<FEATURES>...]
List of cargo features to activate
-e, --exit-on-panic
Exit on panic
-c, --config <CONFIG>
JSON string or path to JSON file to merge with tauri.conf.json
--release
Run the code in release mode
--no-dev-server-wait
Skip waiting for the frontend dev server to start before building the tauri application
[env: TAURI_CLI_NO_DEV_SERVER_WAIT=]
--no-watch
Disable the file watcher
--no-dev-server
Disable the built-in dev server for static files
--port <PORT>
Specify port for the built-in dev server for static files. Defaults to 1430
[env: TAURI_CLI_PORT=]
-h, --help
Print help (see a summary with '-h')
-V, --version
Print version

```

### `build`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauribuild

```

```

yarntauribuild

```

```

pnpmtauribuild

```

```

denotasktauribuild

```

```

cargotauribuild

```

```

Build your app in release mode and generate bundles and installers. It makes use of the `build.frontendDist` property from your `tauri.conf.json` file. It also runs your `build.beforeBuildCommand` which usually builds your frontend into `build.frontendDist`. This will also run `build.beforeBundleCommand` before generating the bundles and installers of your app.
Usage: tauri build [OPTIONS] [ARGS]...
Arguments:
[ARGS]...
Command line arguments passed to the runner. Use `--` to explicitly mark the start of the arguments
Options:
-r, --runner <RUNNER>
Binary to use to build the application, defaults to `cargo`
-v, --verbose...
Enables verbose logging
-d, --debug
Builds with the debug flag
-t, --target <TARGET>
Target triple to build against.
It must be one of the values outputted by `$rustc --print target-list` or `universal-apple-darwin` for an universal macOS application.
Note that compiling an universal macOS application requires both `aarch64-apple-darwin` and `x86_64-apple-darwin` targets to be installed.
-f, --features [<FEATURES>...]
Space or comma separated list of features to activate
-b, --bundles [<BUNDLES>...]
Space or comma separated list of bundles to package.
Note that the `updater` bundle is not automatically added so you must specify it if the updater is enabled.
[possible values: deb, rpm, appimage, updater]
--no-bundle
Skip the bundling step even if `bundle > active` is `true` in tauri config
-c, --config <CONFIG>
JSON string or path to JSON file to merge with tauri.conf.json
--ci
Skip prompting for values
[env: CI=true]
-h, --help
Print help (see a summary with '-h')
-V, --version
Print version

```

### `bundle`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauribundle

```

```

yarntauribundle

```

```

pnpmtauribundle

```

```

denotasktauribundle

```

```

cargotauribundle

```

```

Generate bundles and installers for your app (already built by `tauri build`). This run `build.beforeBundleCommand` before generating the bundles and installers of your app.
Usage: tauri bundle [OPTIONS]
Options:
-d, --debug
Builds with the debug flag
-v, --verbose...
Enables verbose logging
-b, --bundles [<BUNDLES>...]
Space or comma separated list of bundles to package.
Note that the `updater` bundle is not automatically added so you must specify it if the updater is enabled.
[possible values: deb, rpm, appimage, updater]
-c, --config <CONFIG>
JSON string or path to JSON file to merge with tauri.conf.json
-f, --features [<FEATURES>...]
Space or comma separated list of features, should be the same features passed to `tauri build` if any
-t, --target <TARGET>
Target triple to build against.
It must be one of the values outputted by `$rustc --print target-list` or `universal-apple-darwin` for an universal macOS application.
Note that compiling an universal macOS application requires both `aarch64-apple-darwin` and `x86_64-apple-darwin` targets to be installed.
--ci
Skip prompting for values
[env: CI=true]
-h, --help
Print help (see a summary with '-h')
-V, --version
Print version

```

### `android`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriandroid

```

```

yarntauriandroid

```

```

pnpmtauriandroid

```

```

denotasktauriandroid

```

```

cargotauriandroid

```

```

Android commands
Usage: tauri android [OPTIONS] <COMMAND>
Commands:
init  Initialize Android target in the project
dev  Run your app in development mode on Android
build Build your app in release mode for Android and generate APKs and AABs
help  Print this message or the help of the given subcommand(s)
Options:
-v, --verbose... Enables verbose logging
-h, --help    Print help
-V, --version   Print version

```

#### `android init`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriandroidinit

```

```

yarntauriandroidinit

```

```

pnpmtauriandroidinit

```

```

denotasktauriandroidinit

```

```

cargotauriandroidinit

```

```

Initialize Android target in the project
Usage: tauri android init [OPTIONS]
Options:
--ci          Skip prompting for values [env: CI=true]
-v, --verbose...      Enables verbose logging
--skip-targets-install Skips installing rust toolchains via rustup
-h, --help         Print help
-V, --version        Print version

```

#### `android dev`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriandroiddev

```

```

yarntauriandroiddev

```

```

pnpmtauriandroiddev

```

```

denotasktauriandroiddev

```

```

cargotauriandroiddev

```

```

Run your app in development mode on Android with hot-reloading for the Rust code. It makes use of the `build.devUrl` property from your `tauri.conf.json` file. It also runs your `build.beforeDevCommand` which usually starts your frontend devServer.
Usage: tauri android dev [OPTIONS] [DEVICE]
Arguments:
[DEVICE]
Runs on the given device name
Options:
-f, --features [<FEATURES>...]
List of cargo features to activate
-v, --verbose...
Enables verbose logging
-e, --exit-on-panic
Exit on panic
-c, --config <CONFIG>
JSON string or path to JSON file to merge with tauri.conf.json
--release
Run the code in release mode
--no-dev-server-wait
Skip waiting for the frontend dev server to start before building the tauri application
[env: TAURI_CLI_NO_DEV_SERVER_WAIT=]
--no-watch
Disable the file watcher
-o, --open
Open Android Studio instead of trying to run on a connected device
--force-ip-prompt
Force prompting for an IP to use to connect to the dev server on mobile
--host [<HOST>]
Use the public network address for the development server. If an actual address it provided, it is used instead of prompting to pick one.
On Windows we use the public network address by default.
This option is particularly useful along the `--open` flag when you intend on running on a physical device.
This replaces the devUrl configuration value to match the public network address host, it is your responsibility to set up your development server to listen on this address by using 0.0.0.0 as host for instance.
When this is set or when running on an iOS device the CLI sets the `TAURI_DEV_HOST` environment variable so you can check this on your framework's configuration to expose the development server on the public network address.
[default: <none>]
--no-dev-server
Disable the built-in dev server for static files
--port <PORT>
Specify port for the built-in dev server for static files. Defaults to 1430
[env: TAURI_CLI_PORT=]
-h, --help
Print help (see a summary with '-h')
-V, --version
Print version

```

#### `android build`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriandroidbuild

```

```

yarntauriandroidbuild

```

```

pnpmtauriandroidbuild

```

```

denotasktauriandroidbuild

```

```

cargotauriandroidbuild

```

```

Build your app in release mode for Android and generate APKs and AABs. It makes use of the `build.frontendDist` property from your `tauri.conf.json` file. It also runs your `build.beforeBuildCommand` which usually builds your frontend into `build.frontendDist`.
Usage: tauri android build [OPTIONS]
Options:
-d, --debug
Builds with the debug flag
-v, --verbose...
Enables verbose logging
-t, --target [<TARGETS>...]
Which targets to build (all by default)
[possible values: aarch64, armv7, i686, x86_64]
-f, --features [<FEATURES>...]
List of cargo features to activate
-c, --config <CONFIG>
JSON string or path to JSON file to merge with tauri.conf.json
--split-per-abi
Whether to split the APKs and AABs per ABIs
--apk
Build APKs
--aab
Build AABs
-o, --open
Open Android Studio
--ci
Skip prompting for values
[env: CI=true]
-h, --help
Print help (see a summary with '-h')
-V, --version
Print version

```

### `migrate`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntaurimigrate

```

```

yarntaurimigrate

```

```

pnpmtaurimigrate

```

```

denotasktaurimigrate

```

```

cargotaurimigrate

```

```

Migrate from v1 to v2
Usage: tauri migrate [OPTIONS]
Options:
-v, --verbose... Enables verbose logging
-h, --help    Print help
-V, --version   Print version

```

### `info`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriinfo

```

```

yarntauriinfo

```

```

pnpmtauriinfo

```

```

denotasktauriinfo

```

```

cargotauriinfo

```

```

Show a concise list of information about the environment, Rust, Node.js and their versions as well as a few relevant project configurations
Usage: tauri info [OPTIONS]
Options:
--interactive Interactive mode to apply automatic fixes
-v, --verbose...  Enables verbose logging
-h, --help     Print help
-V, --version   Print version

```

### `add`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriadd

```

```

yarntauriadd

```

```

pnpmtauriadd

```

```

denotasktauriadd

```

```

cargotauriadd

```

```

Add a tauri plugin to the project
Usage: tauri add [OPTIONS] <PLUGIN>
Arguments:
<PLUGIN> The plugin to add
Options:
-t, --tag <TAG>    Git tag to use
-v, --verbose...    Enables verbose logging
-r, --rev <REV>    Git rev to use
-b, --branch <BRANCH> Git branch to use
--no-fmt      Don't format code with rustfmt
-h, --help       Print help
-V, --version     Print version

```

### `remove`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriremove

```

```

yarntauriremove

```

```

pnpmtauriremove

```

```

denotasktauriremove

```

```

cargotauriremove

```

```

Remove a tauri plugin from the project
Usage: tauri remove [OPTIONS] <PLUGIN>
Arguments:
<PLUGIN> The plugin to remove
Options:
-v, --verbose... Enables verbose logging
-h, --help    Print help
-V, --version   Print version

```

### `plugin`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriplugin

```

```

yarntauriplugin

```

```

pnpmtauriplugin

```

```

denotasktauriplugin

```

```

cargotauriplugin

```

```

Manage or create Tauri plugins
Usage: tauri plugin [OPTIONS] <COMMAND>
Commands:
new   Initializes a new Tauri plugin project
init   Initialize a Tauri plugin project on an existing directory
android Manage the Android project for a Tauri plugin
ios   Manage the iOS project for a Tauri plugin
help   Print this message or the help of the given subcommand(s)
Options:
-v, --verbose... Enables verbose logging
-h, --help    Print help
-V, --version   Print version

```

#### `plugin new`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauripluginnew

```

```

yarntauripluginnew

```

```

pnpmtauripluginnew

```

```

denotasktauripluginnew

```

```

cargotauripluginnew

```

```

Initializes a new Tauri plugin project
Usage: tauri plugin new [OPTIONS] <PLUGIN_NAME>
Arguments:
<PLUGIN_NAME>
Name of your Tauri plugin
Options:
--no-api
Initializes a Tauri plugin without the TypeScript API
-v, --verbose...
Enables verbose logging
--no-example
Initialize without an example project
-d, --directory <DIRECTORY>
Set target directory for init
-a, --author <AUTHOR>
Author name
--android
Whether to initialize an Android project for the plugin
--ios
Whether to initialize an iOS project for the plugin
--mobile
Whether to initialize Android and iOS projects for the plugin
--ios-framework <IOS_FRAMEWORK>
Type of framework to use for the iOS project
[default: spm]
Possible values:
- spm:  Swift Package Manager project
- xcode: Xcode project
--github-workflows
Generate github workflows
-t, --tauri-path <TAURI_PATH>
Path of the Tauri project to use (relative to the cwd)
-h, --help
Print help (see a summary with '-h')
-V, --version
Print version

```

#### `plugin init`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriplugininit

```

```

yarntauriplugininit

```

```

pnpmtauriplugininit

```

```

denotasktauriplugininit

```

```

cargotauriplugininit

```

```

Initialize a Tauri plugin project on an existing directory
Usage: tauri plugin init [OPTIONS] [PLUGIN_NAME]
Arguments:
[PLUGIN_NAME]
Name of your Tauri plugin. If not specified, it will be inferred from the current directory
Options:
--no-api
Initializes a Tauri plugin without the TypeScript API
-v, --verbose...
Enables verbose logging
--no-example
Initialize without an example project
-d, --directory <DIRECTORY>
Set target directory for init
[default: /opt/build/repo/packages/cli-generator]
-a, --author <AUTHOR>
Author name
--android
Whether to initialize an Android project for the plugin
--ios
Whether to initialize an iOS project for the plugin
--mobile
Whether to initialize Android and iOS projects for the plugin
--ios-framework <IOS_FRAMEWORK>
Type of framework to use for the iOS project
[default: spm]
Possible values:
- spm:  Swift Package Manager project
- xcode: Xcode project
--github-workflows
Generate github workflows
-t, --tauri-path <TAURI_PATH>
Path of the Tauri project to use (relative to the cwd)
-h, --help
Print help (see a summary with '-h')
-V, --version
Print version

```

#### `plugin android`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauripluginandroid

```

```

yarntauripluginandroid

```

```

pnpmtauripluginandroid

```

```

denotasktauripluginandroid

```

```

cargotauripluginandroid

```

```

Manage the Android project for a Tauri plugin
Usage: tauri plugin android [OPTIONS] <COMMAND>
Commands:
init Initializes the Android project for an existing Tauri plugin
help Print this message or the help of the given subcommand(s)
Options:
-v, --verbose... Enables verbose logging
-h, --help    Print help
-V, --version   Print version

```

##### `plugin android init`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauripluginandroidinit

```

```

yarntauripluginandroidinit

```

```

pnpmtauripluginandroidinit

```

```

denotasktauripluginandroidinit

```

```

cargotauripluginandroidinit

```

```

Initializes the Android project for an existing Tauri plugin
Usage: tauri plugin android init [OPTIONS] [PLUGIN_NAME]
Arguments:
[PLUGIN_NAME] Name of your Tauri plugin. Must match the current plugin's name. If not specified, it will be inferred from the current directory
Options:
-o, --out-dir <OUT_DIR> The output directory [default: /opt/build/repo/packages/cli-generator]
-v, --verbose...     Enables verbose logging
-h, --help        Print help
-V, --version      Print version

```

#### `plugin ios`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauripluginios

```

```

yarntauripluginios

```

```

pnpmtauripluginios

```

```

denotasktauripluginios

```

```

cargotauripluginios

```

```

Manage the iOS project for a Tauri plugin
Usage: tauri plugin ios [OPTIONS] <COMMAND>
Commands:
init Initializes the iOS project for an existing Tauri plugin
help Print this message or the help of the given subcommand(s)
Options:
-v, --verbose... Enables verbose logging
-h, --help    Print help
-V, --version   Print version

```

##### `plugin ios init`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauripluginiosinit

```

```

yarntauripluginiosinit

```

```

pnpmtauripluginiosinit

```

```

denotasktauripluginiosinit

```

```

cargotauripluginiosinit

```

```

Initializes the iOS project for an existing Tauri plugin
Usage: tauri plugin ios init [OPTIONS] [PLUGIN_NAME]
Arguments:
[PLUGIN_NAME]
Name of your Tauri plugin. Must match the current plugin's name. If not specified, it will be inferred from the current directory
Options:
-o, --out-dir <OUT_DIR>
The output directory
[default: /opt/build/repo/packages/cli-generator]
-v, --verbose...
Enables verbose logging
--ios-framework <IOS_FRAMEWORK>
Type of framework to use for the iOS project
[default: spm]
Possible values:
- spm:  Swift Package Manager project
- xcode: Xcode project
-h, --help
Print help (see a summary with '-h')
-V, --version
Print version

```

### `icon`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriicon

```

```

yarntauriicon

```

```

pnpmtauriicon

```

```

denotasktauriicon

```

```

cargotauriicon

```

```

Generate various icons for all major platforms
Usage: tauri icon [OPTIONS] [INPUT]
Arguments:
[INPUT] Path to the source icon (squared PNG or SVG file with transparency) [default: ./app-icon.png]
Options:
-o, --output <OUTPUT>    Output directory. Default: 'icons' directory next to the tauri.conf.json file
-v, --verbose...       Enables verbose logging
-p, --png <PNG>       Custom PNG icon sizes to generate. When set, the default icons are not generated
--ios-color <IOS_COLOR> The background color of the iOS icon - string as defined in the W3C's CSS Color Module Level 4 <https://www.w3.org/TR/css-color-4/> [default: #fff]
-h, --help          Print help
-V, --version        Print version

```

### `signer`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntaurisigner

```

```

yarntaurisigner

```

```

pnpmtaurisigner

```

```

denotasktaurisigner

```

```

cargotaurisigner

```

```

Generate signing keys for Tauri updater or sign files
Usage: tauri signer [OPTIONS] <COMMAND>
Commands:
sign   Sign a file
generate Generate a new signing key to sign files
help   Print this message or the help of the given subcommand(s)
Options:
-v, --verbose... Enables verbose logging
-h, --help    Print help
-V, --version   Print version

```

#### `signer sign`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntaurisignersign

```

```

yarntaurisignersign

```

```

pnpmtaurisignersign

```

```

denotasktaurisignersign

```

```

cargotaurisignersign

```

```

Sign a file
Usage: tauri signer sign [OPTIONS] <FILE>
Arguments:
<FILE> Sign the specified file
Options:
-k, --private-key <PRIVATE_KEY>
Load the private key from a string [env: TAURI_PRIVATE_KEY=]
-v, --verbose...
Enables verbose logging
-f, --private-key-path <PRIVATE_KEY_PATH>
Load the private key from a file [env: TAURI_PRIVATE_KEY_PATH=]
-p, --password <PASSWORD>
Set private key password when signing [env: TAURI_PRIVATE_KEY_PASSWORD=]
-h, --help
Print help
-V, --version
Print version

```

#### `signer generate`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntaurisignergenerate

```

```

yarntaurisignergenerate

```

```

pnpmtaurisignergenerate

```

```

denotasktaurisignergenerate

```

```

cargotaurisignergenerate

```

```

Generate a new signing key to sign files
Usage: tauri signer generate [OPTIONS]
Options:
-p, --password <PASSWORD>   Set private key password when signing
-v, --verbose...        Enables verbose logging
-w, --write-keys <WRITE_KEYS> Write private key to a file
-f, --force          Overwrite private key even if it exists on the specified path
--ci            Skip prompting for values [env: CI=true]
-h, --help           Print help
-V, --version         Print version

```

### `completions`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauricompletions

```

```

yarntauricompletions

```

```

pnpmtauricompletions

```

```

denotasktauricompletions

```

```

cargotauricompletions

```

```

Generate Tauri CLI shell completions for Bash, Zsh, PowerShell or Fish
Usage: tauri completions [OPTIONS] --shell <SHELL>
Options:
-s, --shell <SHELL>  Shell to generate a completion script for. [possible values: bash, elvish, fish, powershell, zsh]
-v, --verbose...    Enables verbose logging
-o, --output <OUTPUT> Output file for the shell completions. By default the completions are printed to stdout
-h, --help       Print help
-V, --version     Print version

```

### `permission`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauripermission

```

```

yarntauripermission

```

```

pnpmtauripermission

```

```

denotasktauripermission

```

```

cargotauripermission

```

```

Manage or create permissions for your app or plugin
Usage: tauri permission [OPTIONS] <COMMAND>
Commands:
new  Create a new permission file
add  Add a permission to capabilities
rm  Remove a permission file, and its reference from any capability
ls  List permissions available to your application
help Print this message or the help of the given subcommand(s)
Options:
-v, --verbose... Enables verbose logging
-h, --help    Print help
-V, --version   Print version

```

#### `permission new`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauripermissionnew

```

```

yarntauripermissionnew

```

```

pnpmtauripermissionnew

```

```

denotasktauripermissionnew

```

```

cargotauripermissionnew

```

```

Create a new permission file
Usage: tauri permission new [OPTIONS] [IDENTIFIER]
Arguments:
[IDENTIFIER] Permission identifier
Options:
--description <DESCRIPTION> Permission description
-v, --verbose...         Enables verbose logging
-a, --allow <ALLOW>       List of commands to allow
-d, --deny <DENY>        List of commands to deny
--format <FORMAT>      Output file format [default: json] [possible values: json, toml]
-o, --out <OUT>         The output file
-h, --help            Print help
-V, --version          Print version

```

#### `permission add`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauripermissionadd

```

```

yarntauripermissionadd

```

```

pnpmtauripermissionadd

```

```

denotasktauripermissionadd

```

```

cargotauripermissionadd

```

```

Add a permission to capabilities
Usage: tauri permission add [OPTIONS] <IDENTIFIER> [CAPABILITY]
Arguments:
<IDENTIFIER> Permission to add
[CAPABILITY] Capability to add the permission to
Options:
-v, --verbose... Enables verbose logging
-h, --help    Print help
-V, --version   Print version

```

#### `permission rm`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauripermissionrm

```

```

yarntauripermissionrm

```

```

pnpmtauripermissionrm

```

```

denotasktauripermissionrm

```

```

cargotauripermissionrm

```

```

Remove a permission file, and its reference from any capability
Usage: tauri permission rm [OPTIONS] <IDENTIFIER>
Arguments:
<IDENTIFIER>
Permission to remove.
To remove all permissions for a given plugin, provide `<plugin-name>:*`
Options:
-v, --verbose...
Enables verbose logging
-h, --help
Print help (see a summary with '-h')
-V, --version
Print version

```

#### `permission ls`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauripermissionls

```

```

yarntauripermissionls

```

```

pnpmtauripermissionls

```

```

denotasktauripermissionls

```

```

cargotauripermissionls

```

```

List permissions available to your application
Usage: tauri permission ls [OPTIONS] [PLUGIN]
Arguments:
[PLUGIN] Name of the plugin to list permissions
Options:
-f, --filter <FILTER> Permission identifier filter
-v, --verbose...    Enables verbose logging
-h, --help       Print help
-V, --version     Print version

```

### `capability`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauricapability

```

```

yarntauricapability

```

```

pnpmtauricapability

```

```

denotasktauricapability

```

```

cargotauricapability

```

```

Manage or create capabilities for your app
Usage: tauri capability [OPTIONS] <COMMAND>
Commands:
new  Create a new permission file
help Print this message or the help of the given subcommand(s)
Options:
-v, --verbose... Enables verbose logging
-h, --help    Print help
-V, --version   Print version

```

#### `capability new`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauricapabilitynew

```

```

yarntauricapabilitynew

```

```

pnpmtauricapabilitynew

```

```

denotasktauricapabilitynew

```

```

cargotauricapabilitynew

```

```

Create a new permission file
Usage: tauri capability new [OPTIONS] [IDENTIFIER]
Arguments:
[IDENTIFIER] Capability identifier
Options:
--description <DESCRIPTION> Capability description
-v, --verbose...         Enables verbose logging
--windows <WINDOWS>     Capability windows
--permission <PERMISSION>  Capability permissions
--format <FORMAT>      Output file format [default: json] [possible values: json, toml]
-o, --out <OUT>         The output file
-h, --help            Print help
-V, --version          Print version

```

### `inspect`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriinspect

```

```

yarntauriinspect

```

```

pnpmtauriinspect

```

```

denotasktauriinspect

```

```

cargotauriinspect

```

```

Manage or create permissions for your app or plugin
Usage: tauri inspect [OPTIONS] <COMMAND>
Commands:
wix-upgrade-code Print the default Upgrade Code used by MSI installer derived from productName
help       Print this message or the help of the given subcommand(s)
Options:
-v, --verbose... Enables verbose logging
-h, --help    Print help
-V, --version   Print version

```

#### `inspect wix-upgrade-code`
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriinspectwix-upgrade-code

```

```

yarntauriinspectwix-upgrade-code

```

```

pnpmtauriinspectwix-upgrade-code

```

```

denotasktauriinspectwix-upgrade-code

```

```

cargotauriinspectwix-upgrade-code

```

```

Print the default Upgrade Code used by MSI installer derived from productName
Usage: tauri inspect wix-upgrade-code [OPTIONS]
Options:
-v, --verbose... Enables verbose logging
-h, --help    Print help
-V, --version   Print version

```

© 2025 Tauri Contributors. CC-BY / MIT
