Skip to content
# Application Lifecycle Threats
Tauri applications are composed of many pieces at different points in time of the application lifecycle. Here we describe classical threats and what you SHOULD do about them.
All of these distinct steps are described in the following sections.
![Threat Stages During Development](https://v2.tauri.app/_astro/application-flow-simple.X8I9EoEI_1s9LkI.svg)
## Upstream Threats
Tauri is a direct dependency on your project, and we maintain strict authorial control of commits, reviews, pull requests, and releases. We do our best to maintain up-to-date dependencies and take action to either update or fork and fix. Other projects may not be so well maintained, and may not even have ever been audited.
Please consider their health when integrating them, otherwise, you may have adopted architectural debt without even knowing it.
### Keep Your Applications Up-To-Date
When releasing your app into the wild, you are also shipping a bundle that has Tauri in it. Vulnerabilities affecting Tauri may impact the security of your application. By updating Tauri to the latest version, you ensure that critical vulnerabilities are already patched and cannot be exploited in your application. Also be sure to keep your compiler (`rustc`) and transpilers (`nodejs`) up to date, because there are often security issues that are resolved. This also is true for your development system in general.
### Evaluate Your Dependencies
While NPM and Crates.io provide many convenient packages, it is your responsibility to choose trustworthy third-party libraries - or rewrite them in Rust. If you do use outdated libraries which are affected by known vulnerabilities or are unmaintained, your application security and good night’s sleep could be in jeopardy.
Use tooling like `npm audit` and `cargo audit` to automate this process, and lean on the security community’s important work.
Recent trends in the rust ecosystem like `cargo-vet` or `cargo crev` can help to further reduce likelihood of supply chain attacks. To find out on whose shoulders you stand, you can use the `cargo supply chain` tool.
One practice that we highly recommend, is to only ever consume critical dependencies from git using hash revisions at best or named tags as second best. This holds for Rust as well as the Node ecosystem.
## Development Threats
We assume that you, the developer, care for your development environment. It is on you to make sure that your operating system, build toolchains, and associated dependencies are kept up to date and reasonable secured.
A genuine risk all of us face is what is known as “supply-chain attacks”, which are usually considered to be attacks on direct dependencies of your project. However, a growing class of attacks in the wild directly target development machines, and you would be well off to address this head-on.
### Development Server
Tauri application frontends can be developed using a number of web frameworks. Each of these frameworks usually ship their own development server, which is exposing the frontend assets via an open port to the local system or network. This allows the frontend to be hot-reloaded and debugged in the WebView or Browser.
In practice this connection is often neither encrypted nor authenticated by default. This is also the case for the built-in Tauri development server and exposes your frontend and assets to the local network. Additionally, this allows attackers to push their own frontend code to development devices in the same network as the attacker. Depending on what kind of functionality is exposed this could lead to device compromise in the worst case.
You should only develop on trusted networks where you can safely expose your development device. If this is not possible you MUST ensure that your development server uses **mutual** authentication and encryption (e.g. mTLS) for connections with your development devices.
### Harden Development machines
Hardening your development systems depends on various factors and on your personal threat model but some generic advice we recommend to follow:
  * Never use administrative accounts for day to day tasks like coding
  * Never use production secrets on development machines
  * Prevent secrets to be checked into source code version control
  * Use security hardware tokens or similar to reduce impact of compromised systems
  * Keep your system up to date
  * Keep your installed applications to a minimum


A more practical collection of procedures can be found in an awesome security hardening collection.
You can of course virtualise your development environment to keep attackers at bay, but this won’t protect you from attacks that target your project rather than just your machine.
### Ensure Source Control Authentication and Authorization
If you are working like the majority of developers, using source code version control tools and service providers is an essential step during development.
To ensure that your source code can not be modified by unauthorized actors it is important to understand and correctly set up up access control for your source code version control system.
Also, consider requiring all (regular) contributors to sign their commits to prevent situations where malicious commits are attributed to non-compromised or non-maliocious contributors.
## Buildtime Threats
Modern organizations use CI/CD to manufacture binary artifacts.
You need to be able to fully trust these remote (and third party owned) systems, as they have access to source code, secrets and are able to modify builds without you being able to verifiably prove that the produced binaries are the same as your local code. This means either you trust a reputable provider or host these systems on your own and controlled hardware.
At Tauri, we provide a GitHub Workflow for building on multiple platforms. If you create your own CI/CD and depend on third-party tooling, be wary of actions whose versions you have not explicitly pinned.
You should sign your binaries for the platform you are shipping to. While this can be complicated and somewhat costly to set up, end users expect that your app is verifiably from you.
If cryptographic secrets are properly stored on hardware tokens, a compromised build system won’t be able to leak involved signing keys, but could use them to sign malicious releases.
### Reproducible Builds
To combat backdoor injection at build time, you need your builds to be reproducible, so that you can verify that the build assets are exactly the same when you build them locally or on another independent provider.
The first problem is that Rust is by default not fully **reliably** producing reproducible builds. It supports this in theory, but there are still bugs, and it recently broke on a release.
You can keep track of the current state in the rust project’s public bug tracker.
The next problem you will encounter is that many common frontend bundlers do not produce reproducible output either, so the bundled assets may also break reproducible builds.
This means that you cannot fully rely on reproducible builds by default, and sadly need to fully trust your build systems.
## Distribution Threats
We have done our best to make shipping hot updates to the app as straightforward and secure as possible. However, all bets are off if you lose control of the manifest server, the build server, or the binary hosting service.
If you build your own system, consult a professional OPS architect and build it properly.
If you are looking for another trusted distribution solution for Tauri apps our partner CrabNebula has an offering: https://crabnebula.dev/cloud
## Runtime Threats
We assume the webview is insecure, which has led Tauri to implement several protections regarding webview access to system APIs in the context of loading untrusted userland content.
Using the Content Security Policy will lockdown types of communication that the Webview can undertake. Furthermore, Capabilities can prevent untrusted content or scripts from accessing the API within the Webview.
We also recommend to setup an easy and secure way to report vulnerabilities similar to our process.
© 2025 Tauri Contributors. CC-BY / MIT
