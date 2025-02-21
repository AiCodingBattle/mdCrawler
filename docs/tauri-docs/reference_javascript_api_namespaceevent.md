Skip to content
# event
The event system allows you to emit events to the backend and listen to events from it.
This package is also accessible with `window.__TAURI__.event` when `app.withGlobalTauri` in `tauri.conf.json` is set to `true`.
## Enumerations
### TauriEvent
#### Since
1.1.0
#### Enumeration Members
##### DRAG_DROP
```

DRAG_DROP: "tauri://drag-drop";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L62
##### DRAG_ENTER
```

DRAG_ENTER: "tauri://drag-enter";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L60
##### DRAG_LEAVE
```

DRAG_LEAVE: "tauri://drag-leave";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L63
##### DRAG_OVER
```

DRAG_OVER: "tauri://drag-over";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L61
##### WEBVIEW_CREATED
```

WEBVIEW_CREATED: "tauri://webview-created";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L59
##### WINDOW_BLUR
```

WINDOW_BLUR: "tauri://blur";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L55
##### WINDOW_CLOSE_REQUESTED
```

WINDOW_CLOSE_REQUESTED: "tauri://close-requested";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L52
##### WINDOW_CREATED
```

WINDOW_CREATED: "tauri://window-created";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L58
##### WINDOW_DESTROYED
```

WINDOW_DESTROYED: "tauri://destroyed";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L53
##### WINDOW_FOCUS
```

WINDOW_FOCUS: "tauri://focus";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L54
##### WINDOW_MOVED
```

WINDOW_MOVED: "tauri://move";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L51
##### WINDOW_RESIZED
```

WINDOW_RESIZED: "tauri://resize";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L50
##### WINDOW_SCALE_FACTOR_CHANGED
```

WINDOW_SCALE_FACTOR_CHANGED: "tauri://scale-change";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L56
##### WINDOW_THEME_CHANGED
```

WINDOW_THEME_CHANGED: "tauri://theme-changed";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L57
## Interfaces
### Event<T>
#### Type Parameters
Type Parameter  
---  
`T`  
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`event`| `EventName`| Event name| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L24  
`id`| `number`| Event identifier used to unlisten| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L26  
`payload`| `T`| Event payload| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L28  
### Options
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`target?`| `string` | `EventTarget`| The event target to listen to, defaults to `{ kind: 'Any' }`, see EventTarget. If a string is provided, EventTarget.AnyLabel is used.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L43  
## Type Aliases
### EventCallback()<T>
```

type EventCallback<T>: (event) => void;

```

#### Type Parameters
Type Parameter  
---  
`T`  
#### Parameters
Parameter| Type  
---|---  
`event`| `Event`<`T`>  
#### Returns
`void`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L31
### EventName
```

type EventName: `${TauriEvent}` | string & Record<never, never>;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L35
### EventTarget
```

type EventTarget:
| object
| object
| object
| object
| object
| object;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L14
### UnlistenFn()
```

type UnlistenFn: () => void;

```

#### Returns
`void`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L33
## Functions
### emit()
```

functionemit(event, payload?):Promise<void>

```

Emits an event to all targets.
#### Parameters
Parameter| Type| Description  
---|---|---  
`event`| `string`| Event name. Must include only alphanumeric characters, `-`, `/`, `:` and `_`.  
`payload`?| `unknown`| Event payload.  
#### Returns
`Promise`<`void`>
#### Example
```

import { emit } from'@tauri-apps/api/event';
awaitemit('frontend-loaded', { loggedIn: true, token: 'authToken' });

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L177
### emitTo()
```

functionemitTo(
target,
event,
payload?):Promise<void>

```

Emits an event to all targets matching the given target.
#### Parameters
Parameter| Type| Description  
---|---|---  
`target`| `string` | `EventTarget`| Label of the target Window/Webview/WebviewWindow or raw EventTarget object.  
`event`| `string`| Event name. Must include only alphanumeric characters, `-`, `/`, `:` and `_`.  
`payload`?| `unknown`| Event payload.  
#### Returns
`Promise`<`void`>
#### Example
```

import { emitTo } from'@tauri-apps/api/event';
awaitemitTo('main', 'frontend-loaded', { loggedIn: true, token: 'authToken' });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L199
### listen()
```

functionlisten<T>(
event,
handler,
options?):Promise<UnlistenFn>

```

Listen to an emitted event to any target.
#### Type Parameters
Type Parameter  
---  
`T`  
#### Parameters
Parameter| Type| Description  
---|---|---  
`event`| `EventName`| Event name. Must include only alphanumeric characters, `-`, `/`, `:` and `_`.  
`handler`| `EventCallback`<`T`>| Event handler callback.  
`options`?| `Options`| Event listening options.  
#### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event. Note that removing the listener is required if your listener goes out of scope e.g. the component is unmounted.
#### Example
```

import { listen } from'@tauri-apps/api/event';
const unlisten = await listen<string>('error', (event) => {
console.log(`Got error, payload: ${event.payload}`);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L103
### once()
```

functiononce<T>(
event,
handler,
options?):Promise<UnlistenFn>

```

Listens once to an emitted event to any target.
#### Type Parameters
Type Parameter  
---  
`T`  
#### Parameters
Parameter| Type| Description  
---|---|---  
`event`| `EventName`| Event name. Must include only alphanumeric characters, `-`, `/`, `:` and `_`.  
`handler`| `EventCallback`<`T`>| Event handler callback.  
`options`?| `Options`| Event listening options.  
#### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event. Note that removing the listener is required if your listener goes out of scope e.g. the component is unmounted.
#### Example
```

import { once } from'@tauri-apps/api/event';
interface LoadedPayload {
loggedIn:boolean,
token:string
}
const unlisten = await once<LoadedPayload>('loaded', (event) => {
console.log(`App is loaded, loggedIn: ${event.payload.loggedIn}, token: ${event.payload.token}`);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/event.ts#L147
© 2025 Tauri Contributors. CC-BY / MIT
