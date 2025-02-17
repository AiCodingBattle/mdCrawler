Skip to content
# Vite
Vite is a build tool that aims to provide a faster and leaner development experience for modern web projects. This guide is accurate as of Vite 5.4.8.
## Checklist
  * Use `dist/` as `frontendDist` in `tauri.conf.json`.
  * Use `process.env.TAURI_DEV_HOST` as the development server host IP when set to run on iOS physical devices.


## Example configuration
  1. ##### Update Tauri configuration
Assuming you have the following `dev` and `build` scripts in your `package.json`:
```

{
"scripts": {
"dev": "vite dev",
"build": "vite build"
}
}

```

You can configure the Tauri CLI to use your Vite development server and dist folder along with the hooks to automatically run the Vite scripts:
     * npm 
     * yarn 
     * pnpm 
     * deno 
tauri.conf.json```

{
"build": {
"beforeDevCommand": "npm run dev",
"beforeBuildCommand": "npm run build",
"devUrl": "http://localhost:5173",
"frontendDist": "../dist"
}
}

```

tauri.conf.json```

{
"build": {
"beforeDevCommand": "yarn dev",
"beforeBuildCommand": "yarn build",
"devUrl": "http://localhost:5173",
"frontendDist": "../dist"
}
}

```

tauri.conf.json```

{
"build": {
"beforeDevCommand": "pnpm dev",
"beforeBuildCommand": "pnpm build",
"devUrl": "http://localhost:5173",
"frontendDist": "../dist"
}
}

```

tauri.conf.json```

{
"build": {
"beforeDevCommand": "deno task dev",
"beforeBuildCommand": "deno task build",
"devUrl": "http://localhost:5173",
"frontendDist": "../dist"
}
}

```

  2. ##### Update Vite configuration:
vite.config.js```

import { defineConfig } from'vite';
const host = process.env.TAURI_DEV_HOST;
exportdefaultdefineConfig({
// prevent vite from obscuring rust errors
clearScreen: false,
server: {
// Tauri expects a fixed port, fail if that port is not available
strictPort: true,
// if the host Tauri is expecting is set, use it
host: host||false,
port: 5173,
},
// Env variables starting with the item of `envPrefix` will be exposed in tauri's source code through `import.meta.env`.
envPrefix: ['VITE_', 'TAURI_ENV_*'],
build: {
// Tauri uses Chromium on Windows and WebKit on macOS and Linux
target:
process.env.TAURI_ENV_PLATFORM=='windows'
?'chrome105'
:'safari13',
// don't minify for debug builds
minify: !process.env.TAURI_ENV_DEBUG?'esbuild':false,
// produce sourcemaps for debug builds
sourcemap: !!process.env.TAURI_ENV_DEBUG,
},
});

```



© 2025 Tauri Contributors. CC-BY / MIT
