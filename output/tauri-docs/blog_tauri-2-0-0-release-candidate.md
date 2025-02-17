Skip to content
# Tauri 2.0 Release Candidate
Aug 1, 2024 
![Tillmann Weidinger](https://v2.tauri.app/authors/tweidinger.png)
Tillmann Weidinger
Tauri Security
We are very proud to finally announce the first release candidate for the new major version of Tauri.
After over half a year of beta versions, following over a year of alpha versions we are finally at the point where we consider Tauri 2 stabilized and do no longer expect breaking changes.
We want to use a comparably short release candidate time frame to focus on our documentation and important bug fixes, which have been reported by our awesome community and working group members.
A simplified TL;DR can be found at the end of this post.
## The Road to Stable and Beyond
With this release candidate we want to communicate our expectations and timeline for the stable release.
We have been asked countless times “ _Wen Tauri 2.0?_” and always gave broad answers. Especially in open source projects overpromising can be a quick way to burn out developers and maintainers or lead to angry comments from disappointed adopters.
This is one of the reasons for the long alpha and beta stage and why we waited with the release candidate, as we strive to get things right and simple to use.
Another reason is that we made the mistake of overpromising this major version with “ _mobile as a first class citizen_ ” and realized over the past months that we can only build the foundation for mobile on our own and need to iterate on this together with the community and our adopters to get it right.
This doesn’t mean that mobile is broken and unsupported. We have mobile plugins in our official plugin repository and have seen developers who have built cool apps on Android and iOS with Tauri.
Our partner CrabNebula also provided us with feedback on how easy (or complicated) the developer experience was when they built or supported mobile applications for customers. They even contributed multiple mobile plugins (NFC, Barcode Scanner, Biometric, Haptics, Geolocation) as part of their work.
We see improvements to be made in the development experience for mobile and we acknowledge that not all of our desktop features and plugins are ported or available on mobile yet.
This causes us to say that we don’t want to raise expectations that Tauri 2.0 will be _the_ “ _mobile as a first class citizen_ ” release but we want to make clear that you can develop production ready mobile applications with Tauri **NOW**.
What you can expect from stable after this release candidate is:
  * Clearer and comprehensive documentation
  * Less critical bugs preventing productive usage


We plan to release the stable version for 2.0 in the end of August. This will, at the time of writing, allow for a ~4 week release candidate cycle.
After the stable release our focus will be shifting to providing feature parity wherever possible and to improve the development process for mobile. This will happen in minor releases of Tauri.
Feature parity and plugin development will be aligned with major versions of Tauri but will be mostly independent from Tauri core features and happen in our plugin-workspace repository.
Developer experience is a very important topic for us. If you have improvement suggestions or want to improve the status quo on your own please do not hesitate to reach out with PRs, issues or friendly conversations on our discord server.
## Breaking Changes
Before we enter the “ _no more breaking changes_ ” expectation phase we discussed and planned some from our perspective necessary breaking changes a while ago.
These changes affect a lot of developers, so we wanted to bundle them and make it as painless as possible to upgrade from the latest beta to release candidate or stable.
For app developers we have breaking changes in how core plugins are referenced in the permissions.
You should be able to automatically migrate from the latest beta to release candidate. For this to succeed you must be sure to be on the latest (RC not beta) version of the Tauri CLI.
Otherwise please read the detailed section below explaining the changes and how to manually migrate.
For downstream consumers of Tauri as a library or app developers fiddling with the internals of Tauri we have a bigger refactor you should check out.
### Tauri Core Plugins
With Tauri 2.0 we migrated most of the 1.x core functionality into separate plugins, which allows us to iterate on these independently of Tauri’s core and lowers the barrier for first contributors on functionality.
This migration also included keeping some functionality inside Tauri as pseudo plugins. Fully qualified plugins need to implement the `Plugin Trait` and need to be individual crates following the `tauri-plugin-<plugin name>` naming scheme. For core plugins, the second condition was not possible as we would have circular dependencies on Tauri. So we created pseudo plugins, which are always initialized by Tauri itself and only implement the plugin trait. These are for example `window`, `path` or `webview`. Right now these are allowed in the capabilities of your Tauri application in the following way:
```

...
"permissions": [
"path:default",
"event:default",
"window:default",
"app:default",
"image:default",
"resources:default",
"menu:default",
"tray:default"
]
...

```

This has multiple problems:
  * Any plugin crate which has a colliding name will break our build process (e.g. `tauri-plugin-window` crate) and our cli for adding plugins (e.g. `cargo tauri add window`)
  * We can’t use any core pseudo plugin naming that is already used by existing plugins (e.g. if we would ever want to create`tauri-plugin-mobile-core` and it is already used we will encounter the first problem)
  * It is unclear for developers what is a core plugin and what is a dedicated plugin when looking at capabilities


Our approach is to use a fixed namespace for core plugins, which is documented and enforced by the Tauri core. All plugins starting with `core:` or the plugin name `core` are now considered core pseudo plugins and will only be initialized if they are in the Tauri codebase.
This will cause a breaking change to all capabilites enabling Tauri core features. The above example will be changed to look like this:
```

...
"permissions": [
"core:path:default",
"core:event:default",
"core:window:default",
"core:app:default",
"core:image:default",
"core:resources:default",
"core:menu:default",
"core:tray:default"
]
...

```

We also added a new special `core:default` permission set which will contain all default permissions of all core plugins, so you can simplify the permissions boilerplate in your capabilities config.
```

...
"permissions": [
"core:default"
]
...

```

We consider the core default exposure to be reasonably secure and safe to enable by default, with limited impact in case of a compromised frontend.
To migrate from the latest beta version you need to prepend all core permission identifiers in your capabilities with `core:` or switch to the `core:default` permission and remove old core plugin identifiers.
### Development Server for Mobile
We introduced changes to the network exposure of the built-in development server PR #10437 and PR #10456. With the changes shipped in the 2.0.0-rc.0 release of the Tauri CLI, we can connect to your development server running on localhost when targetting Android and iOS (previously this was only possible when developing a desktop application).
This means you no longer need to expose your development server on the public network.
### Rust API Surface Refactor
With a coordinated effort between multiple working group members we partially changed our Rust API exposure. This affects only consumers of our Rust API and should have no breaking change impact for Tauri application developers.
This was motivated by a recent security advisory CVE-2024-35222, as the fix needed to introduce additional fields to a structure that was directly publicly exposed and caused breaking changes to some projects and internal usage.
We concluded that this overexposure will hinder us in the future and will cause unnecessary breaking changes, so we decided that going from beta to RC will be the last chance for us to implement this until we start down the road of Tauri 3.0.
We reduced the amount of publicly exposed components, which are meant for internal use. Additionally, we made our publicly exposed structures either non-exhaustive or transformed them into exposing builder patterns or constructors. In some cases we added a new `extend` field to allow dynamic additions in the future. Finally, we made sure to document which modules of Tauri are considered unstable.
This will help us to provide (security) fixes or changes without breaking interfaces that are considered stable.
Please take a closer look at the introduced and discussed changes in the #10158 pull request.
## External Security Audit
We have been quiet on this front for some time as we have been busy fixing and discussing issues discovered during the beta versions.
We never marketed version 2 beta releases as production ready but were aware of some apps deployed into production. This caused us to announce and distribute a security patch for one of the findings (CVE-2024-35222) which was also independently discovered by a Tauri community member.
All other findings were fixed in multiple beta versions but we did not create advisories for these. We concluded a full heads up could wait until the release candidate, as the findings mainly affect the development phase or have no critical severity.
With the release candidate we will add the full report to our repository. Please take your time to read the report and learn more about the awesome work of @gronke and @pcwizz from RadicallyOpenSecurity.
The whole audit was funded by the great folks at NLNet and we are super grateful to be in the privileged position to get fully funded external security audits.
## Call to Action
All of the above topics share a common theme. These would not have been possible without the continuous support of the community, our working group and other movements working towards improving the status quo.
Before we are going to release Tauri 2.0 we want to make sure that your voices are heard, your PRs are acknowledged and the documentation is helpful for **YOU** so that you can build the next generation of cross platform apps.
Currently we have over 30 people in our working group on Github but even more involved in our Discord. These awesome people are mostly working on Tauri in their free time with very few exceptions. We currently see a number of issues, PRs and discussions being unsolved and open for longer than we would like to.
To improve this situation we ask **YOU** to get involved into the Tauri project.We have all kinds of situations where we are able to accept event the tiniest contribution.
If you are familiar with Tauri and have used it already during your journey, please take your time to check out the Github Discussions, Github Issues and our Discord Support. Maybe you have already solved the issues your fellow newcomers to Tauri are experiencing right now.
If you think that some of these problems you have seen are generic and should be documented somewhere we probably have the perfect place for it in our official documentation.
To contribute improvements or additions we are open for PRs in the tauri-docs repository. Please make sure you’ve read the guidelines for contribution though.
If you are in the position to understand and translate the current documentation into your native language we appreciate content translations to our documentation.
If you have followed our project for a while but never made a contribution we would be happy to understand what has prevented you from doing so and how we could improve this. Please reach out to us in our Discord or in our Github Discussions.
## Too Long Didn’t Read
  * Tauri 2.0 Release Candidate out now!
  * Some migration from beta is needed. Check out `tauri migrate`.
  * External Security Audit for 2.0 is available here
  * All findings are fixed and fixes were verified
  * Documentation is our focus until stable release
  * Tauri is looking for more contributors and community involvement


Tauri 2.0 Stable Release
Announcing Tauri 1.7.0
© 2025 Tauri Contributors. CC-BY / MIT
