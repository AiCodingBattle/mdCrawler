Skip to content
# tauri@0.7.0
ReturnView on GitHub
  * The execute_promise and execute_promise_sync helpers now accepts any tauri::Result<T> where T: impl Serialize. This means that you do not need to serialize your response manually or deal with String quotes anymore. As part of this refactor, the event::emit function also supports impl Serialize instead of String.


© 2025 Tauri Contributors. CC-BY / MIT
