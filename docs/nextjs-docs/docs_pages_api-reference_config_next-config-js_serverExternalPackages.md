Menu
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Configurationnext.config.js OptionsserverExternalPackages
# serverExternalPackages
Opt-out specific dependencies from being included in the automatic bundling of the `bundlePagesRouterDependencies` option.
These pages will then use native Node.js `require` to resolve the dependency.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 serverExternalPackages: ['@acme/ui'],
}
module.exports= nextConfig
```

Next.js includes a short list of popular packages that currently are working on compatibility and automatically opt-ed out:
  * `@appsignal/nodejs`
  * `@aws-sdk/client-s3`
  * `@aws-sdk/s3-presigned-post`
  * `@blockfrost/blockfrost-js`
  * `@highlight-run/node`
  * `@huggingface/transformers`
  * `@jpg-store/lucid-cardano`
  * `@libsql/client`
  * `@mikro-orm/core`
  * `@mikro-orm/knex`
  * `@node-rs/argon2`
  * `@node-rs/bcrypt`
  * `@prisma/client`
  * `@react-pdf/renderer`
  * `@sentry/profiling-node`
  * `@sparticuz/chromium`
  * `@swc/core`
  * `@xenova/transformers`
  * `argon2`
  * `autoprefixer`
  * `aws-crt`
  * `bcrypt`
  * `better-sqlite3`
  * `canvas`
  * `chromadb-default-embed`
  * `cpu-features`
  * `cypress`
  * `dd-trace`
  * `eslint`
  * `express`
  * `firebase-admin`
  * `import-in-the-middle`
  * `isolated-vm`
  * `jest`
  * `jsdom`
  * `keyv`
  * `libsql`
  * `mdx-bundler`
  * `mongodb`
  * `mongoose`
  * `newrelic`
  * `next-mdx-remote`
  * `next-seo`
  * `node-cron`
  * `node-pty`
  * `node-web-audio-api`
  * `onnxruntime-node`
  * `oslo`
  * `pg`
  * `playwright`
  * `playwright-core`
  * `postcss`
  * `prettier`
  * `prisma`
  * `puppeteer-core`
  * `puppeteer`
  * `require-in-the-middle`
  * `rimraf`
  * `sharp`
  * `shiki`
  * `sqlite3`
  * `ts-node`
  * `ts-morph`
  * `typescript`
  * `vscode-oniguruma`
  * `webpack`
  * `websocket`
  * `zeromq`


Was this helpful?
supported.
Send
