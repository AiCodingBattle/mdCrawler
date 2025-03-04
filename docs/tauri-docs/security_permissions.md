Skip to content
# Permissions
Permissions are descriptions of explicit privileges of commands.
```

[[permission]]
identifier = "my-identifier"
description = "This describes the impact and more."
commands.allow = [
"read_file"
]
[[scope.allow]]
my-scope = "$HOME/*"
[[scope.deny]]
my-scope = "$HOME/secret"

```

It can enable commands to be accessible in the frontend of a Tauri application. It can map scopes to commands and defines which commands are enabled. Permissions can enable or deny certain commands, define scopes or combine both.
Permissions can be grouped as a set under a new identifier. This is called a permission set. This allows you to combine scope related permissions with command related permissions. It also allows to group or bundle operating specific permissions into more usable sets.
As a plugin developer you can ship multiple, pre-defined, well named permissions for all of your exposed commands.
As an application developer you can extend existing plugin permissions or define them for your own commands. They can be grouped or extended in a set to be re-used or to simplify the main configuration files later.
## Permission Identifier
The permissions identifier is used to ensure that permissions can be re-used and have unique names.
  * `<name>:default` Indicates the permission is the default for a plugin or application
  * `<name>:<command-name>` Indicates the permission is for an individual command


The plugin prefix `tauri-plugin-` will be automatically prepended to the identifier of plugins at compile time and is not required to be manually specified.
Identifiers are limited to ASCII lower case alphabetic characters `[a-z]` and the maximum length of the identifier is currently limited to `116` due to the following constants:
```

constIDENTIFIER_SEPARATOR: u8 =b':';
constPLUGIN_PREFIX:&str ="tauri-plugin-";
// https://doc.rust-lang.org/cargo/reference/manifest.html#the-name-field
constMAX_LEN_PREFIX: usize =64-PLUGIN_PREFIX.len();
constMAX_LEN_BASE: usize =64;
constMAX_LEN_IDENTIFIER: usize =MAX_LEN_PREFIX+1+MAX_LEN_BASE;

```

## Configuration Files
Simplified example of an example Tauri **plugin** directory structure:
Terminal window```

tauri-plugin
├──README.md
├──src
│└──lib.rs
├──build.rs
├──Cargo.toml
├──permissions
│└──<identifier>.json/toml
│└──default.json/toml

```

The default permission is handled in a special way, as it is automatically added to the application configuration, as long as the Tauri CLI is used to add plugins to a Tauri application.
For **application** developers the structure is similar:
Terminal window```

tauri-app
├──index.html
├──package.json
├──src
├──src-tauri
│├──Cargo.toml
│├──permissions
│└──<identifier>.toml
|├──capabilities
│└──<identifier>.json/.toml
│├──src
│├──tauri.conf.json

```

## Examples
Example permissions from the `File System` plugin.
plugins/fs/permissions/autogenerated/base-directories/home.toml```

[[permission]]
identifier = "scope-home"
description = """This scope permits access to all files and
list content of top level directories in the `$HOME`folder."""
[[scope.allow]]
path = "$HOME/*"

```

plugins/fs/permissions/read-files.toml```

[[permission]]
identifier = "read-files"
description = """This enables all file read related
commands without any pre-configured accessible paths."""
commands.allow = [
"read_file",
"read",
"open",
"read_text_file",
"read_text_file_lines",
"read_text_file_lines_next"
]

```

plugins/fs/permissions/autogenerated/commands/mkdir.toml```

[[permission]]
identifier = "allow-mkdir"
description = "This enables the mkdir command."
commands.allow = [
"mkdir"
]

```

Example implementation extending above plugin permissions in your app:
my-app/src-tauri/permissions/home-read-extends.toml```

[[set]]
identifier = "allow-home-read-extended"
description = """ This allows non-recursive read access to files and to create directories
in the `$HOME` folder.
"""
permissions = [
"fs:read-files",
"fs:scope-home",
"fs:allow-mkdir"
]

```

© 2025 Tauri Contributors. CC-BY / MIT
