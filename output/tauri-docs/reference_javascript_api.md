Skip to content
# @tauri-apps/api
The Tauri API allows you to interface with the backend layer.
This module exposes all other modules as an object where the key is the module name, and the value is the module exports.
## Examples
```

import { event, window, path } from'@tauri-apps/api'

```

### Vanilla JS API
The above import syntax is for JavaScript/TypeScript with a bundler. If you’re using vanilla JavaScript, you can use the global `window.__TAURI__` object instead. It requires `app.withGlobalTauri` configuration option enabled.
```

const { event, window: tauriWindow, path } = window.__TAURI__;

```

## Namespaces
  * app
  * core
  * dpi
  * event
  * image
  * menu
  * mocks
  * path
  * tray
  * webview
  * webviewWindow
  * window


© 2025 Tauri Contributors. CC-BY / MIT
