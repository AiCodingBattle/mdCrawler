Skip to content
# Window Customization
Tauri provides lots of options for customizing the look and feel of your app’s window. You can create custom titlebars, have transparent windows, enforce size constraints, and more.
## Configuration
There are three ways to change the window configuration:
  * Through tauri.conf.json
  * Through the JavaScript API
  * Through the Window in Rust


## Usage
  * Creating a Custom Titlebar
  * (macOS) Transparent Titlebar with Custom Window Background Color


### Creating a Custom Titlebar
A common use of these window features is creating a custom titlebar. This short tutorial will guide you through that process.
#### tauri.conf.json
Set `decorations` to `false` in your `tauri.conf.json`:
tauri.conf.json```

"tauri": {
"windows": [
{
"decorations": false
}
]
}

```

#### Permissions
Add window permissions in capability file.
By default, all plugin commands are blocked and cannot be accessed. You must define a list of permissions in your `capabilities` configuration.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"$schema": "../gen/schemas/desktop-schema.json",
"identifier": "main-capability",
"description": "Capability for the main window",
"windows": ["main"],
"permissions": ["core:window:default", "core:window:allow-start-dragging"]
}

```

Permission| Description  
---|---  
`core:window:default`| Default permissions for the plugin. Except `window:allow-start-dragging`.  
`core:window:allow-close`| Enables the close command without any pre-configured scope.  
`core:window:allow-minimize`| Enables the minimize command without any pre-configured scope.  
`core:window:allow-start-dragging`| Enables the start_dragging command without any pre-configured scope.  
`core:window:allow-toggle-maximize`| Enables the toggle_maximize command without any pre-configured scope.  
`core:window:allow-internal-toggle-maximize`| Enables the internal_toggle_maximize command without any pre-configured scope.  
#### CSS
Add this CSS sample to keep it at the top of the screen and style the buttons:
```

.titlebar {
height: 30px;
background: #329ea3;
user-select: none;
display: flex;
justify-content: flex-end;
position: fixed;
top: 0;
left: 0;
right: 0;
}
.titlebar-button {
display: inline-flex;
justify-content: center;
align-items: center;
width: 30px;
height: 30px;
user-select: none;
-webkit-user-select: none;
}
.titlebar-button:hover {
background: #5bbec3;
}

```

#### HTML
Put this at the top of your `<body>` tag:
```

<divdata-tauri-drag-regionclass="titlebar">
<divclass="titlebar-button"id="titlebar-minimize">
<img
src="https://api.iconify.design/mdi:window-minimize.svg"
alt="minimize"
/>
</div>
<divclass="titlebar-button"id="titlebar-maximize">
<img
src="https://api.iconify.design/mdi:window-maximize.svg"
alt="maximize"
/>
</div>
<divclass="titlebar-button"id="titlebar-close">
<imgsrc="https://api.iconify.design/mdi:close.svg"alt="close" />
</div>
</div>

```

Note that you may need to move the rest of your content down so that the titlebar doesn’t cover it.
#### JavaScript
Use this code snippet to make the buttons work:
```

import { getCurrentWindow } from'@tauri-apps/api/window';
// when using `"withGlobalTauri": true`, you may use
// const { getCurrentWindow } = window.__TAURI__.window;
const appWindow = getCurrentWindow();
document
.getElementById('titlebar-minimize')
?.addEventListener('click', ()=>appWindow.minimize());
document
.getElementById('titlebar-maximize')
?.addEventListener('click', ()=>appWindow.toggleMaximize());
document
.getElementById('titlebar-close')
?.addEventListener('click', ()=>appWindow.close());

```

Note that if you are using a Rust-based frontend, you can copy the code above into a `<script>` element in your `index.html` file.
### Manual Implementation of `data-tauri-drag-region`
For use cases where you customize the drag behavior, you can manually add an event listener with `window.startDragging` instead of using `data-tauri-drag-region`.
#### HTML
From the code in the previous section, we remove `data-tauri-drag-region` and add an `id`:
```

<divdata-tauri-drag-regionclass="titlebar">
<divid="titlebar"class="titlebar">
<!-- ... -->
</div>
</div>

```

#### Javascript
Add an event listener to the titlebar element:
```

// ...
document.getElementById('titlebar')?.addEventListener('mousedown', (e)=> {
if (e.buttons===1) {
// Primary (left) button
e.detail===2
?appWindow.toggleMaximize() // Maximize on double click
:appWindow.startDragging(); // Else start dragging
}
});

```

### (macOS) Transparent Titlebar with Custom Window Background Color
We are going to create the main window and change its background color from the Rust side.
Remove the main window from the `tauri.conf.json` file:
tauri.conf.json```

"tauri": {
"windows": [
{
"title": "Transparent Titlebar Window",
"width": 800,
"height": 600
}
],
}

```

Add `cocoa` crate to dependencies so that we can use it to call the macOS native API:
src-tauri/Cargo.toml```

[target."cfg(target_os = \"macos\")".dependencies]
cocoa = "0.26"

```

Create the main window and change its background color:
src-tauri/src/lib.rs```

use tauri::{TitleBarStyle, WebviewUrl, WebviewWindowBuilder};
pubfnrun() {
tauri::Builder::default()
.setup(|app| {
letwin_builder=
WebviewWindowBuilder::new(app, "main", WebviewUrl::default())
.title("Transparent Titlebar Window")
.inner_size(800.0, 600.0);
// set transparent title bar only when building for macOS
#[cfg(target_os ="macos")]
letwin_builder=win_builder.title_bar_style(TitleBarStyle::Transparent);
letwindow=win_builder.build().unwrap();
// set background color only when building for macOS
#[cfg(target_os ="macos")]
{
use cocoa::appkit::{NSColor, NSWindow};
use cocoa::base::{id, nil};
letns_window=window.ns_window().unwrap() asid;
unsafe {
letbg_color= NSColor::colorWithRed_green_blue_alpha_(
nil,
50.0/255.0,
158.0/255.0,
163.5/255.0,
1.0,
);
ns_window.setBackgroundColor_(bg_color);
}
}
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

© 2025 Tauri Contributors. CC-BY / MIT
