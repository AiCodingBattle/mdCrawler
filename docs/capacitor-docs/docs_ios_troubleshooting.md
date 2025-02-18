Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Creating a 100% perfect native management tool is nearly impossible, and sooner or later you'll run into various issues with some part of the iOS workflow.
This guide attempts to document common iOS/Xcode issues with possible solutions.
## iOS Toolbox​
Every iOS developer learns a few common techniques for debugging iOS issues, and you should incorporate these into your workflow:
### Google, Google, Google​
Any time you encounter an issue with iOS, or Xcode, your first step should be to copy and paste the error into a Google search.
Capacitor uses the standard iOS toolchain, so chances are if you run into something, many iOS developers have as well, and there's a solution out there.
It could be as simple as updating a dependency, running clean, or removing Derived Data.
### Clean/Rebuild​
Cleaning and rebuilding can fix a number of build issues. Navigate to Product -> Clean Build Folder in the Xcode menu to clean your current build.
### Removing Derived Data​
Sometimes, Xcode clings to old, outdated build artifacts. To start fresh, you'll need to delete any Derived Data on disk.
To do this, open Xcode Preferences, choose the Locations tab, and click the small arrow next to your Derived Data path:
![Locations](https://capacitorjs.com/docs/assets/images/location-prefs-dc0aa793e31aa648bc58c436701e89a2.png)
This opens a Finder window to the location of Xcode's temporary Derived Data.
Next, select all items in that directory and delete:
![Deleting Derived Data](https://capacitorjs.com/docs/assets/images/deleting-derived-data-1c2a148c2a7ee5dda89b48f82595386b.png)
Finally, do a rebuild in Xcode.
## Error: Sandbox not in sync with the Podfile.lock​
This error can happen if CocoaPods hasn't been able to run to install your dependencies.
Run this to update your pods:
```
npx cap update ios
```

Perform a new build after running this command.
## Indexing FOREVER​
Xcode sometimes gets stuck indexing forever. This unfortunate situation looks like this:
![Xcode indexing](https://capacitorjs.com/docs/assets/images/indexing-5e10017b5fd52d9d4f7929dc5c0cd117.png)
The only solution is to Force Close Xcode (using Activity Monitor) and start it up again.
## Apple Silicon: `ffi` Bus Error​
If you installed CocoaPods with `sudo gem install cocoapods` and you're using an Apple Silicon-powered Mac, you might encounter something like this when running `npx cap update`:
```
[error] Analyzing dependencies    /Library/Ruby/Gems/2.6.0/gems/ffi-1.15.3/lib/ffi/library.rb:275: [BUG] Bus Error at 0x0000000000000000    ruby 2.6.3p62 (2019-04-16 revision 67580) [universal.arm64e-darwin20]
```

This is a CocoaPods bug related to `ffi` not installing on Apple Silicon computers. We recommend using Homebrew to installl CocoaPods. Alternatively, if you have Rosetta installed, you can install `ffi` on a `x86_64` architecture and run `pod install` using the simulated Intel architecture for the first time.
```
$ sudo arch -x86_64 gem install ffi$ arch -x86_64 pod install
```

After that, running Capacitor should work as expected.
## CocoaPods: Failed to connect to GitHub​
This error can happen on Macs with an old version of openssl and ruby installed, since GitHub restricted the allowed cryptographic protocols when accessing repos.
The solution is to update openssl and update Ruby:
```
brew install opensslbrew upgrade opensslbrew install rubybrew link--overwrite ruby
```

Finally, make sure your `PATH` environment variable does not put `/usr/local/bin` after `$PATH`, but rather _before_ it.
See this StackOverflow issue for other possible solutions to this problem.
## Plugin Not Implemented​
On iOS, this can happen if Capacitor doesn't find the plugins or can't inject its code into the WebView.
First of all, make sure the plugin is installed and appears in the `package.json`.
Then, run `npx cap sync ios`.
Finally, check that the plugin is in `ios/App/Podfile`. If the plugin is not listed, make sure your Podfile looks like this one and run `npx cap sync` again.
If still getting the "Plugin not implemented" error, make sure you don't have `WKAppBoundDomains` key in `ios/App/App/Info.plist`, that prevents Capacitor's and Plugins code from injecting. Remove the key if not needed, or if it can't be removed, add `limitsNavigationsToAppBoundDomains` to your capacitor config file with `true` value inside the `ios` object.
## Contents
  * iOS Toolbox
    * Google, Google, Google
    * Clean/Rebuild
    * Removing Derived Data
  * Error: Sandbox not in sync with the Podfile.lock
  * Indexing FOREVER
  * Apple Silicon: `ffi` Bus Error
  * CocoaPods: Failed to connect to GitHub
  * Plugin Not Implemented


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=ed6d98ad223740ddbf99774ce8c4ab02&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fios%2Ftroubleshooting&_biz_t=1739811939519&_biz_i=Capacitor%20Documentation&_biz_n=58&rnd=33129&cdn_o=a&_biz_z=1739811939519)
