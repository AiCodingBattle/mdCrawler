Skip to content
# Future Work
This section describes topics we started or would like to tackle in the future to make Tauri apps even more secure. If you feel interested in these topics or have pre-existing knowledge we are always happy to welcome new contributors and advice via GitHub or other community platforms like Discord.
### Binary Analysis
To allow pentesters, auditors and automated security checks do to their job properly it is very valuable to provide insight even from compiled binaries. Not all companies are open source or provide source code for audits, red-teams and other security testing.
Another often overlooked point is that providing inbuilt metadata empowers users of your application to audit their systems for known vulnerabilities at scale without dedicating their lifetime and efforts into it.
If your threatmodel depends on security by obscurity this section will be providing some tools and points which hopefully will make you reconsider.
For Rust there is `cargo-auditable` to create SBOMs and provide exact crate versions and dependencies of a binary without breaking reproducible builds.
For the frontend stack we are not aware of similar solutions, so extracting the frontend assets from the binary should be a straightforward process. Afterwards it should be possible to use tooling like `npm audit` or similar. There are already blog posts about the process but no simple tooling is available.
We are planning to provide such tooling or make it easier to extract assets, when compiling a Tauri app with certain features.
To use pentesting tools like Burpsuite, Zap or Caido it is necessary to intercept traffic from the webview and pass it through the testing proxy. Currently Tauri has no inbuilt method to do so but there is ongoing work to ease this process.
All of these tools allow to properly test and inspect Tauri applications without source code access and should be considered when building a Tauri application.
We are planning to further support and implement related features in the future.
### WebView Hardening
In Tauri’s current threat model and boundaries we are not able to add more security constraints to the WebView itself and since it is the biggest part of our stack which is written in an memory unsafe language, we are planning to research and consider ways to further sandbox and isolate the webview processes.
Inbuilt and external sandboxing methods will be evaluated to reduce attack impact and to enforce the IPC bridge for system access. We believe that this part of our stack is the weak link but current generation WebViews are improving in their hardening and exploit resilience.
### Fuzzing
To allow more efficient and simplify the process of fuzzing Tauri applications we aim to further implement our mock runtimes and other tooling to make it easier to configure and build for individual Tauri applications.
Tauri is supporting a multitude of Operating Systems and CPU architectures, usually apps have only few or no possible memory unsafe code. No pre-existing fuzzing tooling and libraries support these uncommon fuzzing use case, so we need to implement it and support existing libraries like libAFL to build Tauri fuzzing frameworks.
The goal is to make fuzzing accessible and efficient for Tauri application developers.
© 2025 Tauri Contributors. CC-BY / MIT
