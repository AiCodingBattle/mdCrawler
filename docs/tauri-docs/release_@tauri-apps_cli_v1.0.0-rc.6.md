Skip to content
# @tauri-apps/cli@1.0.0-rc.6
ReturnView on GitHub
  * Added `tsp` config option under `tauri &gt; bundle &gt; windows`, which enables Time-Stamp Protocol (RFC 3161) for the timestamping server under code signing on Windows if set to `true`. 
    * bdd5f7c2 fix: add support for Time-Stamping Protocol for Windows codesigning (fix #3563) (#3570) on 2022-03-07
  * Added `i686-pc-windows-msvc` to the prebuilt targets. 
    * fb6744da feat(cli.js): add 32bit cli for windows (#3540) on 2022-02-24
  * Change the `plugin init` templates to use the new `tauri::plugin::Builder` syntax. 
    * f7acb061 feat(cli): use plugin::Builder syntax on the plugin template (#3606) on 2022-03-03


© 2025 Tauri Contributors. CC-BY / MIT
