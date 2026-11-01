# Baseline landing page

A responsive, buildless marketing page. Serve `dist/` with any static HTTP server:

```sh
python3 -m http.server 4173 --directory dist
```

Includes a persistent light/dark theme, native keyboard-accessible FAQ, scroll-snap screenshot carousel, reduced-motion support, and SEO/social metadata. No JavaScript dependencies or build step. Screenshot SVGs are lightweight illustrative placeholders based on the app references; replace them with production captures when ready. Recreate those illustrations with `python3 make-assets.py`.


## Cloudflare Workers deployment

Production Worker: `baseline-landing`.
Default URL: `https://baseline-landing.omganesh402.workers.dev`.

Wrangler uploads `dist/` as static assets. No Worker script, dependency installation, or application build is required.

| Setting | Value |
| --- | --- |
| Worker name | `baseline-landing` |
| Production branch | `main` |
| Build command | Leave blank (or `exit 0`) |
| Deploy command | `npx wrangler deploy` |
| Root directory | Repository root |

Manual deployment:

```sh
npx wrangler login
npx wrangler deploy
```

Check the deployment configuration without publishing:

```sh
npx wrangler deploy --dry-run
```

### Custom domain

Workers custom domains require an active Cloudflare DNS zone in the same account. The domain registration can stay at .tech Domains.

1. Add `omkamath.tech` to Cloudflare DNS on the Free plan.
2. Review the imported DNS records against the existing provider, including the main website, `www`, `thoughts`, and all email and verification records. Do not change nameservers until those records are complete.
3. At the registrar, set the domain's nameservers to the exact pair assigned by Cloudflare. Existing DNSSEC must be migrated according to Cloudflare's DNSSEC instructions if enabled.
4. Once Cloudflare reports the zone as Active, open Worker `baseline-landing` → Domains → Add Domain, and enter `baseline.omkamath.tech`.
5. Cloudflare creates the DNS record and HTTPS certificate. If a stale `baseline` CNAME from the Pages setup exists, remove that record before adding the Workers custom domain.

A CNAME to a `workers.dev` hostname at an external DNS provider does not configure a Workers custom domain. The previous Pages deployment is no longer the deployment target.

`.openai/hosting.json` belongs to the earlier Sites preview. Cloudflare uses `wrangler.jsonc`.
