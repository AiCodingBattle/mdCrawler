Skip to content
# Linux Code Signing
This guide provides information on code signing for Linux packages. While artifact signing is not required for your application to be deployed on Linux, it can be used to increase trust into your deployed application. Signing the binaries allows your end user to verify that these are genuine and have not been modified by another untrusted entity.
## Signing for AppImages
The AppImage can be signed using either gpg or gpg2.
### Prerequisites
A key for signing must be prepared. A new one can be generated using:
Terminal window```

gpg2--full-gen-key

```

Please refer to the gpg or gpg2 documentation for additional information. You should take additional care to back up your private and public keys in a secure location.
### Signing
You can embed a signature in the AppImage by setting the following environment variables:
  * **SIGN** : set to `1` to sign the AppImage.
  * **SIGN_KEY** : optional variable to use a specific GPG Key ID for signing.
  * **APPIMAGETOOL_SIGN_PASSPHRASE** : the signing key password. If unset, gpg shows a dialog so you can input it. You must set this when building in CI/CD platforms.
  * **APPIMAGETOOL_FORCE_SIGN** : by default the AppImage is generated even if signing fails. To exit on errors, you can set this variable to `1`.


You can display the signature embedded in the AppImage by running the following command:
Terminal window```

./src-tauri/target/release/bundle/appimage/$APPNAME_$VERSION_amd64.AppImage--appimage-signature

```

Note that you need to change the $APPNAME and $VERSION values with the correct ones based on your configuration.
### Validate the signature
The AppImage validate tool can be downloaded from here. Select one of the `validate-$PLATFORM.AppImage` files.
Run the following command to validate the signature:
Terminal window```

chmod+xvalidate-$PLATFORM.AppImage
./validate-$PLATFORM.AppImage$TAURI_OUTPUT.AppImage

```

If the signature is valid, the output will be:
```

Validation result: validation successful
Signatures found with key fingerprints: $KEY_ID
====================
Validator report:
Signature checked for key with fingerprint $KEY_ID:
Validation successful

```

© 2025 Tauri Contributors. CC-BY / MIT
