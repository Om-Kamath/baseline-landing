# Baseline landing page

A responsive, buildless marketing page. Serve `dist/` with any static HTTP server:

```sh
python3 -m http.server 4173 --directory dist
```

Includes a persistent light/dark theme, native keyboard-accessible FAQ, scroll-snap screenshot carousel, reduced-motion support, and SEO/social metadata. No JavaScript dependencies or build step. Screenshot SVGs are lightweight illustrative placeholders based on the app references; replace them with production captures when ready. Recreate those illustrations with `python3 make-assets.py`.


## Cloudflare Workers deployment

The repository is configured as a static-assets Worker. Wrangler uploads and serves `dist/` directly; no Worker script, dependencies, or application build step is needed.

Use these settings in the connected Cloudflare Workers build:

| Setting | Value |
| --- | --- |
| Worker name | `baseline-omkamath-tech` |
| Production branch | `main` |
| Build command | Leave blank (or `exit 0`) |
| Deploy command | `npx wrangler deploy` |
| Root directory | Repository root |

For manual deployment with an authenticated Cloudflare account:

```sh
npx wrangler deploy
```

Validate deployment configuration without publishing:

```sh
npx wrangler deploy --dry-run
```

After deployment, configure `baseline.omkamath.tech` in the Worker's Settings → Domains & Routes → Add → Custom Domain. Workers custom domains require an active Cloudflare DNS zone in the same account; a CNAME to a `workers.dev` address alone does not configure a custom domain. Cloudflare manages the DNS record and HTTPS certificate when the custom domain is added.

`.openai/hosting.json` belongs to the earlier Sites preview. Cloudflare uses `wrangler.jsonc`.
