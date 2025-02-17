Skip to content
# Android Code Signing
To publish on the Play Store, you need to sign your app with a digital certificate.
Android App Bundles and APKs must be signed before being uploaded for distribution.
Google also provides an additional signing mechanism for Android App Bundles distributed in the Play Store. See the official Play App Signing documentation for more information.
## Creating a keystore and upload key
Android signing requires a Java Keystore file that can be generated using the official `keytool` CLI:
  * macOS/Linux 
  * Windows 


```

keytool -genkey -v -keystore ~/upload-keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias upload

```

```

keytool -genkey -v -keystore $env:USERPROFILE\upload-keystore.jks -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 -alias upload

```

This command stores the `upload-keystore.jks` file in your home directory. If you want to store it elsewhere, change the argument you pass to the `-keystore` parameter.
See the official documentation for more information.
## Configure the signing key
Create a file named `[project]/src-tauri/gen/android/keystore.properties` that contains a reference to your keystore:
```

password=<password defined when keytool was executed>
keyAlias=upload
storeFile=<location of the key store file, such as /Users/<user name>/upload-keystore.jks or C:\\Users\\<user name>\\upload-keystore.jks>

```

You will usually generate this file in your CI/CD platform. The following snippet contains an example job step for GitHub Actions:
```

- name: setup Android signing
run: |
cd src-tauri/gen/android
echo "keyAlias=${{ secrets.ANDROID_KEY_ALIAS }}" > keystore.properties
echo "password=${{ secrets.ANDROID_KEY_PASSWORD }}" >> keystore.properties
base64 -d <<< "${{ secrets.ANDROID_KEY_BASE64 }}" > $RUNNER_TEMP/keystore.jks
echo "storeFile=$RUNNER_TEMP/keystore.jks" >> keystore.properties

```

In this example the keystore was exported to base64 with `base64 -i /path/to/keystore.jks` and set as the `ANDROID_KEY_BASE64` secret.
### Configure Gradle to use the signing key
Configure gradle to use your upload key when building your app in release mode by editing the `[project]/src-tauri/gen/android/app/build.gradle.kts` file.
  1. Add the needed import at the beginning of the file:
```

import java.io.FileInputStream

```

  2. Add the `release` signing config before the `buildTypes` block:
```

signingConfigs {
create("release") {
val keystorePropertiesFile = rootProject.file("keystore.properties")
val keystoreProperties =Properties()
if (keystorePropertiesFile.exists()) {
keystoreProperties.load(FileInputStream(keystorePropertiesFile))
}
keyAlias = keystoreProperties["keyAlias"] as String
keyPassword = keystoreProperties["password"] as String
storeFile =file(keystoreProperties["storeFile"] as String)
storePassword = keystoreProperties["password"] as String
}
}
buildTypes {
...
}

```

  3. Use the new `release` signing config in the `release` config in `buildTypes` block:
```

buildTypes {
getByName("release") {
signingConfig = signingConfigs.getByName("release")
}
}

```



Release builds of your app will now be signed automatically.
© 2025 Tauri Contributors. CC-BY / MIT
