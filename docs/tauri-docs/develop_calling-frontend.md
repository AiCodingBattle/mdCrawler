Skip to content
# Calling the Frontend from Rust
This document includes guides on how to communicate with your application frontend from your Rust code. To see how to communicate with your Rust code from your frontend, see Calling Rust from the Frontend.
The Rust side of your Tauri application can call the frontend by leveraging the Tauri event system, using channels or directly evaluating JavaScript code.
## Event System
Tauri ships a simple event system you can use to have bi-directional communication between Rust and your frontend.
The event system was designed for situations where small amounts of data need to be streamed or you need to implement a multi consumer multi producer pattern (e.g. push notification system).
The event system is not designed for low latency or high throughput situations. See the channels section for the implementation optimized for streaming data.
The major differences between a Tauri command and a Tauri event are that events have no strong type support, event payloads are always JSON strings making them not suitable for bigger messages and there is no support of the capabilities system to fine grain control event data and channels.
The AppHandle and WebviewWindow types implement the event system traits Listener and Emitter.
Events are either global (delivered to all listeners) or webview-specific (only delivered to the webview matching a given label).
### Global Events
To trigger a global event you can use the Emitter#emit function:
src-tauri/src/lib.rs```

use tauri::{AppHandle, Emitter};
#[tauri::command]
fndownload(app: AppHandle, url: String) {
app.emit("download-started", &url).unwrap();
forprogressin [1, 15, 50, 80, 100] {
app.emit("download-progress", progress).unwrap();
}
app.emit("download-finished", &url).unwrap();
}

```

### Webview Event
To trigger an event to a listener registered by a specific webview you can use the Emitter#emit_to function:
src-tauri/src/lib.rs```

use tauri::{AppHandle, Emitter};
#[tauri::command]
fnlogin(app: AppHandle, user: String, password: String) {
letauthenticated=user=="tauri-apps"&&password=="tauri";
letresult=ifauthenticated { "loggedIn" } else { "invalidCredentials" };
app.emit_to("login", "login-result", result).unwrap();
}

```

It is also possible to trigger an event to a list of webviews by calling Emitter#emit_filter. In the following example we emit a open-file event to the main and file-viewer webviews:
src-tauri/src/lib.rs```

use tauri::{AppHandle, Emitter, EventTarget};
#[tauri::command]
fnopen_file(app: AppHandle, path: std::path::PathBuf) {
app.emit_filter("open-file", path, |target|matchtarget {
EventTarget::WebviewWindow { label } =>label=="main"||label=="file-viewer",
_=>false,
}).unwrap();
}

```

### Event Payload
The event payload can be any serializable type that also implements Clone. Let’s enhance the download event example by using an object to emit more information in each event:
src-tauri/src/lib.rs```

use tauri::{AppHandle, Emitter};
use serde::Serialize;
#[derive(Clone, Serialize)]
#[serde(rename_all ="camelCase")]
struct DownloadStarted<'a> {
url:&'a str,
download_id: usize,
content_length: usize,
}
#[derive(Clone, Serialize)]
#[serde(rename_all ="camelCase")]
struct DownloadProgress {
download_id: usize,
chunk_length: usize,
}
#[derive(Clone, Serialize)]
#[serde(rename_all ="camelCase")]
struct DownloadFinished {
download_id: usize,
}
#[tauri::command]
fndownload(app: AppHandle, url: String) {
letcontent_length=1000;
letdownload_id=1;
app.emit("download-started", DownloadStarted {
url:&url,
download_id,
content_length
}).unwrap();
forchunk_lengthin [15, 150, 35, 500, 300] {
app.emit("download-progress", DownloadProgress {
download_id,
chunk_length,
}).unwrap();
}
app.emit("download-finished", DownloadFinished { download_id }).unwrap();
}

```

### Listening to Events
Tauri provides APIs to listen to events on both the webview and the Rust interfaces.
#### Listening to Events on the Frontend
The `@tauri-apps/api` NPM package offers APIs to listen to both global and webview-specific events.
  * Listening to global events
```

import { listen } from'@tauri-apps/api/event';
type DownloadStarted = {
url:string;
downloadId:number;
contentLength:number;
};
listen<DownloadStarted>('download-started', (event)=> {
console.log(
`downloading ${event.payload.contentLength} bytes from ${event.payload.url}`
);
});

```

  * Listening to webview-specific events
```

import { getCurrentWebviewWindow } from'@tauri-apps/api/webviewWindow';
const appWebview = getCurrentWebviewWindow();
appWebview.listen<string>('logged-in', (event)=> {
localStorage.setItem('session-token', event.payload);
});

```



The `listen` function keeps the event listener registered for the entire lifetime of the application. To stop listening on an event you can use the `unlisten` function which is returned by the `listen` function:
```

import { listen } from'@tauri-apps/api/event';
const unlisten = await listen('download-started', (event) => {});
unlisten();

```

Additionally Tauri provides a utility function for listening to an event exactly once:
```

import { once } from'@tauri-apps/api/event';
import { getCurrentWebviewWindow } from'@tauri-apps/api/webviewWindow';
once('ready', (event)=> {});
const appWebview = getCurrentWebviewWindow();
appWebview.once('ready', ()=> {});

```

#### Listening to Events on Rust
Global and webview-specific events are also delivered to listeners registered in Rust.
  * Listening to global events
src-tauri/src/lib.rs```

use tauri::Listener;
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.setup(|app| {
app.listen("download-started", |event| {
iflet Ok(payload) = serde_json::from_str::<DownloadStarted>(&event.payload()) {
println!("downloading {}", payload.url);
}
});
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

  * Listening to webview-specific events
src-tauri/src/lib.rs```

use tauri::{Listener, Manager};
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.setup(|app| {
letwebview=app.get_webview_window("main").unwrap();
webview.listen("logged-in", |event| {
letsession_token=event.data;
// save token..
});
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```



The `listen` function keeps the event listener registered for the entire lifetime of the application. To stop listening on an event you can use the `unlisten` function:
```

// unlisten outside of the event handler scope:
letevent_id=app.listen("download-started", |event| {});
app.unlisten(event_id);
// unlisten when some event criteria is matched
lethandle=app.handle().clone();
app.listen("status-changed", |event| {
ifevent.data =="ready" {
handle.unlisten(event.id);
}
});

```

Additionally Tauri provides a utility function for listening to an event exactly once:
```

app.once("ready", |event| {
println!("app is ready");
});

```

In this case the event listener is immediately unregistered after its first trigger.
## Channels
The event system is designed to be a simple two way communication that is globally available in your application. Under the hood it directly evaluates JavaScript code so it might not be suitable to sending a large amount of data.
Channels are designed to be fast and deliver ordered data. They are used internally for streaming operations such as download progress, child process output and WebSocket messages.
Let’s rewrite our download command example to use channels instead of the event system:
src-tauri/src/lib.rs```

use tauri::{AppHandle, ipc::Channel};
use serde::Serialize;
#[derive(Clone, Serialize)]
#[serde(rename_all ="camelCase", tag ="event", content ="data")]
enum DownloadEvent<'a> {
#[serde(rename_all ="camelCase")]
Started {
url:&'a str,
download_id: usize,
content_length: usize,
},
#[serde(rename_all ="camelCase")]
Progress {
download_id: usize,
chunk_length: usize,
},
#[serde(rename_all ="camelCase")]
Finished {
download_id: usize,
},
}
#[tauri::command]
fndownload(app: AppHandle, url: String, on_event: Channel<DownloadEvent>) {
letcontent_length=1000;
letdownload_id=1;
on_event.send(DownloadEvent::Started {
url:&url,
download_id,
content_length,
}).unwrap();
forchunk_lengthin [15, 150, 35, 500, 300] {
on_event.send(DownloadEvent::Progress {
download_id,
chunk_length,
}).unwrap();
}
on_event.send(DownloadEvent::Finished { download_id }).unwrap();
}

```

When calling the download command you must create the channel and provide it as an argument:
```

import { invoke, Channel } from'@tauri-apps/api/core';
type DownloadEvent =
| {
event:'started';
data: {
url:string;
downloadId:number;
contentLength:number;
};
}
| {
event:'progress';
data: {
downloadId:number;
chunkLength:number;
};
}
| {
event:'finished';
data: {
downloadId:number;
};
};
const onEvent = newChannel<DownloadEvent>();
onEvent.onmessage=(message)=> {
console.log(`got download event ${message.event}`);
};
awaitinvoke('download', {
url: 'https://raw.githubusercontent.com/tauri-apps/tauri/dev/crates/tauri-schema-generator/schemas/config.schema.json',
onEvent,
});

```

## Evaluating JavaScript
To directly execute any JavaScript code on the webview context you can use the `WebviewWindow#eval` function:
src-tauri/src/lib.rs```

use tauri::Manager;
tauri::Builder::default()
.setup(|app| {
letwebview=app.get_webview_window("main").unwrap();
webview.eval("console.log('hello from Rust')")?;
Ok(())
})

```

If the script to be evaluated is not so simple and must use input from Rust objects we recommend using the serialize-to-javascript crate.
© 2025 Tauri Contributors. CC-BY / MIT
