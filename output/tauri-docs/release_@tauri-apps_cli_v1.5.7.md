Skip to content
# @tauri-apps/cli@1.5.7
ReturnView on GitHub
### Bug Fixes
  * `1d5aa38a`(#8162) Fixes errors on command output, occuring when the output stream contains an invalid UTF-8 character, or ends with a multi-bytes UTF-8 character.
  * `f26d9f08`(#8263) Fixes an issue in the NSIS installer which caused the uninstallation to leave empty folders on the system if the `resources` feature was used.
  * `92bc7d0e`(#8233) Fixes an issue in the NSIS installer which caused the installation to take much longer than expected when many `resources` were added to the bundle.


### Dependencies
  * Upgraded to `tauri-cli@1.5.7`


© 2025 Tauri Contributors. CC-BY / MIT
