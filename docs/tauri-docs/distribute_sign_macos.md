Skip to content
# macOS Code Signing
Code signing is required on macOS to allow your application to be listed in the Apple App Store and to prevent a warning that your application is broken and can not be started, when downloaded from the browser.
## Prerequisites
Code signing on macOS requires an Apple Developer account which is either paid (99$ per year) or on the free plan. You also need an Apple device where you perform the code signing. This is required by the signing process and due to Apple’s Terms and Conditions.
## Signing
To setup code signing for macOS you must create an Apple code signing certificate and install it to your Mac computer keychain or export it to be used in CI/CD platforms.
### Creating a signing certificate
To create a new signing certificate, you must generate a Certificate Signing Request (CSR) file from your Mac computer. See creating a certificate signing request to learn how to create the CSR for code signing.
On your Apple Developer account, navigate to the Certificates, IDs & Profiles page and click on the `Create a certificate` button to open the interface to create a new certificate. Choose the appropriate certificate type (`Apple Distribution` to submit apps to the App Store, and `Developer ID Application` to ship apps outside the App Store). Upload your CSR, and the certificate will be created.
### Downloading the certificate
On the Certificates, IDs & Profiles page, click on the certificate you want to use and click on the `Download` button. It saves a `.cer` file that installs the certificate on the keychain once opened.
### Configuring Tauri
You can configure Tauri to use your certificate when building macOS apps on your local machine or when using CI/CD platforms.
#### Signing locally
With the certificate installed in your Mac computer keychain, you can configure Tauri to use it for code signing.
The name of the certificate’s keychain entry represents the `signing identity`, which can also be found by executing:
```

security find-identity -v -p codesigning

```

This identity can be provided in the `tauri.conf.json > bundle > macOS > signingIdentity` configuration option or via the `APPLE_SIGNING_IDENTITY` environment variable.
#### Signing in CI/CD platforms
To use the certificate in CI/CD platforms, you must export the certificate to a base64 string and configure the `APPLE_CERTIFICATE` and `APPLE_CERTIFICATE_PASSWORD` environment variables:
  1. Open the `Keychain Access` app, click the _My Certificates_ tab in the _login_ keychain and find your certificate’s entry.
  2. Expand the entry, right-click on the key item, and select `Export "$KEYNAME"`.
  3. Select the path to save the certificate’s `.p12` file and define a password for the exported certificate.
  4. Convert the `.p12` file to base64 running the following script on the terminal:


```

openssl base64 -in /path/to/certificate.p12 -out certificate-base64.txt

```

  1. Set the contents of the `certificate-base64.txt` file to the `APPLE_CERTIFICATE` environment variable.
  2. Set the certificate password to the `APPLE_CERTIFICATE_PASSWORD` environment variable.

Example GitHub Actions configuration
Required secrets:
  * `APPLE_ID` - Your Apple ID email
  * `APPLE_ID_PASSWORD` - Your Apple ID password
  * `APPLE_CERTIFICATE` - The base64 encoded `.p12` file
  * `APPLE_CERTIFICATE_PASSWORD` - The password for your exported `.p12` file
  * `KEYCHAIN_PASSWORD` - The password for your keychain


Check out the official GitHub guide to learn how to set up secrets.
```

name: 'build'
on:
push:
branches:
- main
jobs:
build-macos:
needs: prepare
strategy:
matrix:
include:
- args: '--target aarch64-apple-darwin'
arch: 'silicon'
- args: '--target x86_64-apple-darwin'
arch: 'intel'
runs-on: macos-latest
env:
APPLE_ID: ${{ secrets.APPLE_ID }}
APPLE_ID_PASSWORD: ${{ secrets.APPLE_ID_PASSWORD }}
steps:
- name: Import Apple Developer Certificate
env:
APPLE_CERTIFICATE: ${{ secrets.APPLE_CERTIFICATE }}
APPLE_CERTIFICATE_PASSWORD: ${{ secrets.APPLE_CERTIFICATE_PASSWORD }}
KEYCHAIN_PASSWORD: ${{ secrets.KEYCHAIN_PASSWORD }}
run: |
echo $APPLE_CERTIFICATE | base64 --decode > certificate.p12
security create-keychain -p "$KEYCHAIN_PASSWORD" build.keychain
security default-keychain -s build.keychain
security unlock-keychain -p "$KEYCHAIN_PASSWORD" build.keychain
security import certificate.p12 -k build.keychain -P "$APPLE_CERTIFICATE_PASSWORD" -T /usr/bin/codesign
security set-key-partition-list -S apple-tool:,apple:,codesign: -s -k "$KEYCHAIN_PASSWORD" build.keychain
security find-identity -v -p codesigning build.keychain
- name: Verify Certificate
run: |
CERT_INFO=$(security find-identity -v -p codesigning build.keychain | grep "Apple Development")
CERT_ID=$(echo "$CERT_INFO" | awk -F'"' '{print $2}')
echo "CERT_ID=$CERT_ID" >> $GITHUB_ENV
echo "Certificate imported."
- uses: tauri-apps/tauri-action@v0
env:
GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
APPLE_CERTIFICATE: ${{ secrets.APPLE_CERTIFICATE }}
APPLE_CERTIFICATE_PASSWORD: ${{ secrets.APPLE_CERTIFICATE_PASSWORD }}
APPLE_SIGNING_IDENTITY: ${{ env.CERT_ID }}
with:
args: ${{ matrix.args }}

```

## Notarization
To notarize your application, you must provide credentials for Tauri to authenticate with Apple:
  * APPLE_API_ISSUER, APPLE_API_KEY and APPLE_API_KEY_PATH: authenticate using an App Store Connect API key
Open the App Store Connect’s Users and Access page, select the Integrations tab, click on the Add button and select a name and the Developer access. The APPLE_API_ISSUER (Issuer ID) is presented above the keys table, and the APPLE_API_KEY is the value on the Key ID column on that table. You also need to download the private key, which can only be done once and is only visible after a page reload (the button is shown on the table row for the newly created key). The private key file path must be set via the APPLE_API_KEY_PATH environment variable.
  * APPLE_ID, APPLE_PASSWORD and APPLE_TEAM_ID: authenticate using your Apple ID
Alternatively, to authenticate with your Apple ID, set the APPLE_ID to your Apple account email and the APPLE_PASSWORD to an app-specific password for the Apple account.


© 2025 Tauri Contributors. CC-BY / MIT
