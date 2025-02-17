Skip to content
# Capabilities
Tauri provides application and plugin developers with a capabilities system, to granually enable and constrain the core exposure to the application frontend running in the system WebView.
Capabilities are a set of permissions mapped to application windows and webviews by their respective label. Capabilities can affect multiple windows and webviews and these can be referenced in multiple capabilities.
Capability files are either defined as a JSON or a TOML file inside the `src-tauri/capabilities` directory.
It is good practice to use individual files and only reference them by identifier in the `tauri.conf.json` but it is also possible to define them directly in the `capabilities` field.
All capabilities inside the `capabilities` directory are automatically enabled by default. Once capabilities are explicitly enabled in the `tauri.conf.json`, only these are used in the application build.
For a full reference of the configuration scheme please see the references section.
The following example JSON defines a capability that enables default functionality for core plugins and the `window.setTitle` API.
src-tauri/capabilities/default.json```

{
"$schema": "../gen/schemas/desktop-schema.json",
"identifier": "main-capability",
"description": "Capability for the main window",
"windows": ["main"],
"permissions": [
"core:path:default",
"core:event:default",
"core:window:default",
"core:app:default",
"core:resources:default",
"core:menu:default",
"core:tray:default",
"core:window:allow-set-title"
]
}

```

These snippets are part of the Tauri configuration file.
This is likely the most common configuration method, where the individual capabilities are inlined and only permissions are referenced by identifier.
This requires well defined capability files in the `capabilities` directory.
src-tauri/tauri.conf.json```

{
"app": {
"security": {
"capabilities": ["my-capability", "main-capability"]
}
}
}

```

Inline capabilities can be mixed with pre-defined capabilities.
src-tauri/tauri.conf.json```

{
"app": {
"security": {
"capabilities": [
{
"identifier": "my-capability",
"description": "My application capability used for all windows",
"windows": ["*"],
"permissions": ["fs:default", "allow-home-read-extended"]
},
"my-second-capability"
]
}
}
}

```

## Target Platform
Capabilities can be platform-specific by defining the `platforms` array. By default the capability is applied to all targets, but you can select a subset of the `linux`, `macOS`, `windows`, `iOS` and `android` targets.
For example a capability for desktop operating systems. Note it enables permissions on plugins that are only available on desktop:
src-tauri/capabilities/desktop.json```

{
"$schema": "../gen/schemas/desktop-schema.json",
"identifier": "desktop-capability",
"windows": ["main"],
"platforms": ["linux", "macOS", "windows"],
"permissions": ["global-shortcut:allow-register"]
}

```

And another example of a capability for mobile. Note it enables permissions on plugins that are only available on mobile:
src-tauri/capabilities/mobile.json```

{
"$schema": "../gen/schemas/mobile-schema.json",
"identifier": "mobile-capability",
"windows": ["main"],
"platforms": ["iOS", "android"],
"permissions": [
"nfc:allow-scan",
"biometric:allow-authenticate",
"barcode-scanner:allow-scan"
]
}

```

## Remote API Access
By default the API is only accessible to bundled code shipped with the Tauri App. To allow remote sources access to certain Tauri Commands it is possible to define this in the capability configuration file.
This example would allow to scan for NFC tags and to use the barcode scanner from all subdomains of `tauri.app`.
src-tauri/capabilities/remote-tags.json```

{
"$schema": "../gen/schemas/remote-schema.json",
"identifier": "remote-tag-capability",
"windows": ["main"],
"remote": {
"urls": ["https://*.tauri.app"]
},
"platforms": ["iOS", "android"],
"permissions": ["nfc:allow-scan", "barcode-scanner:allow-scan"]
}

```

## Security Boundaries
_What does it protect against?_
Depending on the permissions and capabilities it is able to:
  * Minimize impact of frontend compromise
  * Prevent or reduce (accidential) exposure of local system interfaces and data
  * Prevent or reduce possible privilege escalation from frontend to backend/system


_What does it**not** protect against?_
  * Malicious or insecure Rust code
  * Too lax scopes and configuration
  * Incorrect scope checks in the command implementation
  * Intentional bypasses from Rust code
  * Basically anything which was written in the rust core of an application
  * 0-days or unpatched 1-days in the system WebView
  * Supply chain attacks or otherwise compromised developer systems


## Schema Files
Tauri generates JSON schemas with all the permissions available to your application, allowing autocompletion in your IDE. To use a schema, set the `$schema` property in your configuration to one of the platform-specific schemas located in the `gen/schemas` directory. Usually you will set it to `../gen/schemas/desktop-schema.json` or `../gen/schemas/mobile-schema.json` though you can also define a capability for a specific target platform.
## Configuration Files
Simplified example of an example Tauri application directory structure:
Terminal window```

tauri-app
├──index.html
├──package.json
├──src
├──src-tauri
│├──Cargo.toml
│├──capabilities
│└──<identifier>.json/toml
│├──src
│├──tauri.conf.json

```

Everything can be inlined into the `tauri.conf.json` but even a little more advanced configuration would bloat this file and the goal of this approach is that the permissions are abstracted away whenever possible and simple to understand.
## Core Permissions
A list of all core permissions can be found on the Core Permissions page.
© 2025 Tauri Contributors. CC-BY / MIT
