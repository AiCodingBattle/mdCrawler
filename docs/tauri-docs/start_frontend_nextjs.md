Skip to content
# Next.js
Next.js is a meta framework for React. Learn more about Next.js at https://nextjs.org. This guide is accurate as of Next.js 14.2.3.
## Checklist
  * Use static exports by setting `output: 'export'`. Tauri doesn’t support server-based solutions.
  * Use the `out` directory as `frontendDist` in `tauri.conf.json`.


## Example Configuration
  1. ##### Update Tauri configuration
     * npm 
     * yarn 
     * pnpm 
     * deno 
src-tauri/tauri.conf.json```

{
"build": {
"beforeDevCommand": "npm run dev",
"beforeBuildCommand": "npm run build",
"devUrl": "http://localhost:3000",
"frontendDist": "../out"
}
}

```

src-tauri/tauri.conf.json```

{
"build": {
"beforeDevCommand": "yarn dev",
"beforeBuildCommand": "yarn build",
"devUrl": "http://localhost:3000",
"frontendDist": "../out"
}
}

```

src-tauri/tauri.conf.json```

{
"build": {
"beforeDevCommand": "pnpm dev",
"beforeBuildCommand": "pnpm build",
"devUrl": "http://localhost:3000",
"frontendDist": "../out"
}
}

```

src-tauri/tauri.conf.json```

{
"build": {
"beforeDevCommand": "deno task dev",
"beforeBuildCommand": "deno task build",
"devUrl": "http://localhost:3000",
"frontendDist": "../out"
}
}

```

  2. ##### Update Next.js configuration
next.conf.mjs```

const isProd = process.env.NODE_ENV === 'production';
const internalHost = process.env.TAURI_DEV_HOST || 'localhost';
/** @type{import('next').NextConfig} */
const nextConfig = {
// Ensure Next.js uses SSG instead of SSR
// https://nextjs.org/docs/pages/building-your-application/deploying/static-exports
output: 'export',
// Note: This feature is required to use the Next.js Image component in SSG mode.
// See https://nextjs.org/docs/messages/export-image-api for different workarounds.
images: {
unoptimized: true,
},
// Configure assetPrefix or else the server won't properly resolve your assets.
assetPrefix: isProd ? undefined : `http://${internalHost}:3000`,
};
exportdefault nextConfig;

```

  3. ##### Update package.json configuration
```

"scripts": {
"dev": "next dev",
"build": "next build",
"start": "next start",
"lint": "next lint",
"tauri": "tauri"
}

```



© 2025 Tauri Contributors. CC-BY / MIT
