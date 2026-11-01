# Baseline landing page

A responsive, buildless marketing page. Serve `dist/` with any static HTTP server:

```sh
python3 -m http.server 4173 --directory dist
```

Includes a persistent light/dark theme, native keyboard-accessible FAQ, scroll-snap screenshot carousel, reduced-motion support, and SEO/social metadata. No JavaScript dependencies or build step. Screenshot SVGs are lightweight illustrative placeholders based on the app references; replace them with production captures when ready. Recreate those illustrations with `python3 make-assets.py`.


## Cloudflare Pages deployment

This uses the same hosting approach as `thoughts.omkamath.tech`: a private GitHub repository connected to Cloudflare Pages.

In Cloudflare → Workers & Pages → Create application → Pages → Import an existing Git repository, select `Om-Kamath/baseline-landing` and configure:

| Setting | Value |
| --- | --- |
| Project name | `baseline-omkamath-tech` |
| Production branch | `main` |
| Framework preset | None |
| Build command | `exit 0` |
| Build output directory | `dist` |

No dependencies or build step are needed. Cloudflare automatically deploys future pushes once the Git integration is connected.

After the first deployment, add `baseline.omkamath.tech` under the Pages project's Custom domains. At your DNS provider, add a CNAME with host `baseline` pointing to the exact `pages.dev` hostname shown by Cloudflare. The intended project hostname is `baseline-omkamath-tech.pages.dev`; verify it in the dashboard before changing DNS. Cloudflare handles the HTTPS certificate.
