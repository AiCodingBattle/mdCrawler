Skip to content
# tauri@0.6.0
ReturnView on GitHub
  * Adds a command line interface option to tauri apps, configurable under tauri.conf.json > tauri > cli.
  * Fixes no-server mode not running on another machine due to fs::read_to_string usage instead of the include_str macro. Build no longer fails when compiling without environment variables, now the app will show an error.
  * Adds desktop notifications API.
  * Properly reflect tauri.conf.json changes on app when running tauri dev.


© 2025 Tauri Contributors. CC-BY / MIT
