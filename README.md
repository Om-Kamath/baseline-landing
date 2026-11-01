# Baseline landing page

A responsive, buildless marketing page. Serve `dist/` with any static HTTP server:

```sh
python3 -m http.server 4173 --directory dist
```

Includes a persistent light/dark theme, native keyboard-accessible FAQ, scroll-snap screenshot carousel, reduced-motion support, and SEO/social metadata. No JavaScript dependencies or build step. Screenshot SVGs are lightweight illustrative placeholders based on the app references; replace them with production captures when ready. Recreate those illustrations with `python3 make-assets.py`.


## Cloudflare Pages deployment

The production Pages project is `baseline-landing`, served at `https://baseline-landing.pages.dev` and `https://baseline.omkamath.tech` once the custom domain is active.

Cloudflare Pages uses `wrangler.jsonc`, with `pages_build_output_dir` set to `./dist`. The directory already contains the complete site, so no build step or dependency installation is required.

| Setting | Value |
| --- | --- |
| Project | `baseline-landing` |
| Production branch | `main` |
| Framework | None |
| Build command | `exit 0` (or leave blank) |
| Output directory | `dist` |
| Root directory | Repository root |

For direct upload from this directory:

```sh
npx wrangler login
npx wrangler pages deploy dist --project-name baseline-landing --branch main
```

For automatic updates, connect `Om-Kamath/baseline-landing` to this Pages project and ensure the Cloudflare Pages GitHub app has access to the repository.

Add `baseline.omkamath.tech` under the Pages project's Custom domains. In the external `omkamath.tech` DNS zone, set a CNAME record with host `baseline`, target `baseline-landing.pages.dev`, and TTL Auto. Cloudflare manages the HTTPS certificate. Nameservers can remain with the current DNS provider for this Pages subdomain setup.

`.openai/hosting.json` belongs to the earlier Sites preview. Cloudflare uses `wrangler.jsonc`.
