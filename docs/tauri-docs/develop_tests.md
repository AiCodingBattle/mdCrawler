Skip to content
# Tests
Tauri offers support for both unit and integration testing utilizing a mock runtime. Under the mock runtime, native webview libraries are not executed. See more about the mock runtime here.
Tauri also provides support for end-to-end testing support utilizing the WebDriver protocol. Both desktop and mobile work with it, except for macOS which does not provide a desktop WebDriver client. See more about WebDriver support here.
We offer tauri-action to help run GitHub actions, but any sort of CI/CD runner can be used with Tauri as long as each platform has the required libraries installed to compile against.
© 2025 Tauri Contributors. CC-BY / MIT
