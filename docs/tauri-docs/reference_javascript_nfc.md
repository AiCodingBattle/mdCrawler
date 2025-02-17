Skip to content
# @tauri-apps/plugin-nfc
## Enumerations
### NFCTypeNameFormat
#### Enumeration Members
##### AbsoluteURI
```

AbsoluteURI: 3;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L84
##### Empty
```

Empty: 0;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L81
##### Media
```

Media: 2;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L83
##### NfcExternal
```

NfcExternal: 4;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L85
##### NfcWellKnown
```

NfcWellKnown: 1;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L82
##### Unchanged
```

Unchanged: 6;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L87
##### Unknown
```

Unknown: 5;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L86
### TechKind
#### Enumeration Members
##### IsoDep
```

IsoDep: 0;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L17
##### MifareClassic
```

MifareClassic: 1;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L18
##### MifareUltralight
```

MifareUltralight: 2;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L19
##### Ndef
```

Ndef: 3;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L20
##### NdefFormatable
```

NdefFormatable: 4;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L21
##### NfcA
```

NfcA: 5;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L22
##### NfcB
```

NfcB: 6;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L23
##### NfcBarcode
```

NfcBarcode: 7;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L24
##### NfcF
```

NfcF: 8;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L25
##### NfcV
```

NfcV: 9;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L26
## Interfaces
### NFCRecord
#### Properties
Property| Type| Defined in  
---|---|---  
`format`| `NFCTypeNameFormat`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L104  
`id`| `number`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L106  
`kind`| `number`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L105  
`payload`| `number`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L107  
### ScanOptions
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`keepSessionAlive?`| `boolean`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L63  
`message?`| `string`| Message displayed in the UI. iOS only.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L65  
`successMessage?`| `string`| Message displayed in the UI when the message has been read. iOS only.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L67  
### Tag
#### Properties
Property| Type| Defined in  
---|---|---  
`id`| `number`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L98  
`kind`| `string`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L99  
`records`| `TagRecord`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L100  
### TagRecord
#### Properties
Property| Type| Defined in  
---|---|---  
`id`| `number`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L93  
`kind`| `number`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L92  
`payload`| `number`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L94  
`tnf`| `NFCTypeNameFormat`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L91  
### UriFilter
#### Properties
Property| Type| Defined in  
---|---|---  
`host?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L12  
`pathPrefix?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L13  
`scheme?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L11  
### WriteOptions
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`kind?`| `ScanKind`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L71  
`message?`| `string`| Message displayed in the UI when reading the tag. iOS only.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L73  
`successfulReadMessage?`| `string`| Message displayed in the UI when the tag has been read. iOS only.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L75  
`successMessage?`| `string`| Message displayed in the UI when the message has been written. iOS only.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L77  
## Type Aliases
### ScanKind
```

type ScanKind: object | object;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L29
## Variables
### RTD_TEXT
```

const RTD_TEXT:number[];

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L7
### RTD_URI
```

const RTD_URI:number[];

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L8
## Functions
### isAvailable()
```

functionisAvailable():Promise<boolean>

```

#### Returns
`Promise`<`boolean`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L271
### record()
```

functionrecord(
format,
kind,
id,
payload):NFCRecord

```

#### Parameters
Parameter| Type  
---|---  
`format`| `NFCTypeNameFormat`  
`kind`| `string` | `number`[]  
`id`| `string` | `number`[]  
`payload`| `string` | `number`[]  
#### Returns
`NFCRecord`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L110
### scan()
```

functionscan(kind, options?):Promise<Tag>

```

Scans an NFC tag.
```

import { scan } from"@tauri-apps/plugin-nfc";
awaitscan({ type: "tag" });

```

See https://developer.android.com/develop/connectivity/nfc/nfc#ndef for more information.
#### Parameters
Parameter| Type| Description  
---|---|---  
`kind`| `ScanKind`  
`options`?| `ScanOptions`  
#### Returns
`Promise`<`Tag`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L231
### textRecord()
```

functiontextRecord(
text,
id?,
language?):NFCRecord

```

#### Parameters
Parameter| Type| Default value  
---|---|---  
`text`| `string`| `undefined`  
`id`?| `string` | `number`[]| `undefined`  
`language`?| `string`| `'en'`  
#### Returns
`NFCRecord`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L130
### uriRecord()
```

functionuriRecord(uri, id?):NFCRecord

```

#### Parameters
Parameter| Type  
---|---  
`uri`| `string`  
`id`?| `string` | `number`[]  
#### Returns
`NFCRecord`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L203
### write()
```

functionwrite(records, options?):Promise<void>

```

Write to an NFC tag.
```

import { uriRecord, write } from"@tauri-apps/plugin-nfc";
awaitwrite([uriRecord("https://tauri.app")], { kind: { type: "ndef" } });

```

If you did not previously call scan with ScanOptions.keepSessionAlive set to true, it will first scan the tag then write to it.
#### Parameters
Parameter| Type| Description  
---|---|---  
`records`| `NFCRecord`[]  
`options`?| `WriteOptions`  
#### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/nfc/guest-js/index.ts#L256
© 2025 Tauri Contributors. CC-BY / MIT
