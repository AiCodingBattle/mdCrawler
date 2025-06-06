Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
The LangChain ecosystem is composed of different component packages (e.g., `langchain-core`, `langchain`, `langchain-community`, `langgraph`, `langserve`, partner packages etc.)
## Versioning​
### `langchain`, `langchain-core`, and integration packages​
`langchain`, `langchain-core`, `langchain-text-splitters`, and integration packages (`langchain-openai`, `langchain-anthropic`, etc.) follow semantic versioning in the format of 0.**Y**.**Z**. The packages are under rapid development, and so are currently versioning the packages with a major version of 0.
Minor version increases will occur for:
  * Breaking changes for any public interfaces _not_ marked as `beta`.


Patch version increases will occur for:
  * Bug fixes,
  * New features,
  * Any changes to private interfaces,
  * Any changes to `beta` features.


When upgrading between minor versions, users should review the list of breaking changes and deprecations.
From time to time, we will version packages as **release candidates**. These are versions that are intended to be released as stable versions, but we want to get feedback from the community before doing so. Release candidates will be versioned as 0.**Y**.**Z** rc**N**. For example, 0.2.0rc1. If no issues are found, the release candidate will be released as a stable version with the same version number. If issues are found, we will release a new release candidate with an incremented `N` value (e.g., 0.2.0rc2).
### `langchain-community`​
`langchain-community` is currently on version `0.2.x`.
Minor version increases will occur for:
  * Updates to the major/minor versions of required `langchain-x` dependencies. E.g., when updating the required version of `langchain-core` from `^0.2.x` to `0.3.0`.


Patch version increases will occur for:
  * Bug fixes,
  * New features,
  * Any changes to private interfaces,
  * Any changes to `beta` features,
  * Breaking changes to integrations to reflect breaking changes in the third-party service.


Whenever possible we will avoid making breaking changes in patch versions. However, if an external API makes a breaking change then breaking changes to the corresponding `langchain-community` integration can occur in a patch version.
### `langchain-experimental`​
`langchain-experimental` is currently on version `0.0.x`. All changes will be accompanied with patch version increases.
## Release cadence​
We expect to space out **minor** releases (e.g., from 0.2.x to 0.3.0) of `langchain` and `langchain-core` by at least 2-3 months, as such releases may contain breaking changes.
Patch versions are released frequently, up to a few times per week, as they contain bug fixes and new features.
## API stability​
The development of LLM applications is a rapidly evolving field, and we are constantly learning from our users and the community. As such, we expect that the APIs in `langchain` and `langchain-core` will continue to evolve to better serve the needs of our users.
Even though both `langchain` and `langchain-core` are currently in a pre-1.0 state, we are committed to maintaining API stability in these packages.
  * Breaking changes to the public API will result in a minor version bump (the second digit)
  * Any bug fixes or new features will result in a patch version bump (the third digit)


We will generally try to avoid making unnecessary changes, and will provide a deprecation policy for features that are being removed.
### Stability of other packages​
The stability of other packages in the LangChain ecosystem may vary:
  * `langchain-community` is a community maintained package that contains 3rd party integrations. While we do our best to review and test changes in `langchain-community`, `langchain-community` is expected to experience more breaking changes than `langchain` and `langchain-core` as it contains many community contributions.
  * Partner packages may follow different stability and versioning policies, and users should refer to the documentation of those packages for more information; however, in general these packages are expected to be stable.


### What is a "API stability"?​
API stability means:
  * All the public APIs (everything in this documentation) will not be moved or renamed without providing backwards-compatible aliases.
  * If new features are added to these APIs – which is quite possible – they will not break or change the meaning of existing methods. In other words, "stable" does not (necessarily) mean "complete."
  * If, for some reason, an API declared stable must be removed or replaced, it will be declared deprecated but will remain in the API for at least two minor releases. Warnings will be issued when the deprecated method is called.


### **APIs marked as internal**​
Certain APIs are explicitly marked as “internal” in a couple of ways:
  * Some documentation refers to internals and mentions them as such. If the documentation says that something is internal, it may change.
  * Functions, methods, and other objects prefixed by a leading underscore (**`_`**). This is the standard Python convention of indicating that something is private; if any method starts with a single**`_`**, it’s an internal API.
    * **Exception:** Certain methods are prefixed with `_` , but do not contain an implementation. These methods are _meant_ to be overridden by sub-classes that provide the implementation. Such methods are generally part of the **Public API** of LangChain.


## Deprecation policy​
We will generally avoid deprecating features until a better alternative is available.
When a feature is deprecated, it will continue to work in the current and next minor version of `langchain` and `langchain-core`. After that, the feature will be removed.
Since we're expecting to space out minor releases by at least 2-3 months, this means that a feature can be removed within 2-6 months of being deprecated.
In some situations, we may allow the feature to remain in the code base for longer periods of time, if it's not causing issues in the packages, to reduce the burden on users.
#### Was this page helpful?
  * Versioning
    * `langchain`, `langchain-core`, and integration packages
    * `langchain-community`
    * `langchain-experimental`
  * Release cadence
  * API stability
    * Stability of other packages
    * What is a "API stability"?
    * **APIs marked as internal**
  * Deprecation policy


