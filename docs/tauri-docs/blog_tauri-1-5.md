Skip to content
# Announcing Tauri 1.5.0
Sep 28, 2023 
![Lucas Nogueira](https://v2.tauri.app/authors/lucasfernog.jpeg)
Lucas Nogueira
Tauri Co-Founder
![Tauri 1.5 Launch Hero Image](https://v2.tauri.app/_astro/header.DdVdFRx8_Z2s5p2y.webp)
The Tauri team is excited to announce the 1.5 release. This version includes several new features and important bug fixes such as improved resources bundling, code signing enhancements, `notarytool` migration on macOS and Bun support.
## Upgrading
Make sure to update both NPM and Cargo dependencies to the 1.5.0 release. You can update the dependencies with:
  * npm 
  * yarn 
  * pnpm 
  * cargo 


```

npminstall@tauri-apps/cli@latest@tauri-apps/api@latest

```

```

yarnupgrade@tauri-apps/cli@tauri-apps/api--latest

```

```

pnpmupdate@tauri-apps/cli@tauri-apps/api--latest

```

```

cargoupdate

```

## What’s in 1.5.0
### Notarytool
At WWDC 2021 Apple introduced notarytool, a new tool for interacting with the Apple notary service. Before the 1.5 release, Tauri used altool to notarize your application, but that tool has been deprecated and will stop working for notarization on 2023-11-01. You **must** upgrade your Tauri CLI to 1.5 before that.
If you are using API keys for authentication with the notary service, notarytool no longer automatically searches for your APi key `.p8` file. We recommend users to define its path via the `APPLE_API_KEY_PATH` environment variable, though to avoid breaking changes we perform the same lookup done by altool to find your key file in case you did not set the environment variable. In the future, this might change, so please adjust your publish pipelines accordingly.
### Bun support
The Tauri CLI now supports the Bun package manager.
We would like to thank @colinhacks for submitting the pull requests for this feature!
### Code signing improvements
Starting on Tauri 1.5, our bundler now signs all executables (including sidecars, app executables and NSIS uninstaller) and macOS frameworks. We also improved our notarization algorithm adding support to the `APPLE_TEAM_ID` environment variable to properly define the team ID associated with your account in case you belong to multiple teams.
We would like to thank @tr3ysmith for submitting the pull requests for this feature!
### macOS frameworks
This release comes with enhanced macOS frameworks support by code signing all custom frameworks you inject via `tauri.conf.json > tauri > bundle > macOS > frameworks` and defining the `@rpath` value fixing a crash when updating your app.
We would like to thank @tr3ysmith for submitting the pull requests for this feature!
### Mixed content on Windows
We now offer a configuration option to switch our custom protocol on Windows to use the `http` scheme instead of `https`. This reduces the security of your application on Windows since it allows connecting to insecure endpoints such as `ws://url`, but it matches the behavior on Linux and macOS custom protocols. To enable it, set the `tauri.conf.json > tauri > security > dangerousUseHttpScheme` to true.
### Other changes
Check out the entire list of changes:
  * tauri
  * tauri-cli
  * tauri-bundler


Strengthening Tauri: Our Partnership with CrabNebula
Roadmap to Tauri 2.0
© 2025 Tauri Contributors. CC-BY / MIT
