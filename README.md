# Baseline landing page

A responsive, buildless marketing page. Serve `dist/` with any static HTTP server:

```sh
python3 -m http.server 4173 --directory dist
```

Includes a persistent light/dark theme, native keyboard-accessible FAQ, scroll-snap screenshot carousel, reduced-motion support, and SEO/social metadata. No JavaScript dependencies or build step. Screenshot SVGs are lightweight illustrative placeholders based on the app references; replace them with production captures when ready. Recreate those illustrations with `python3 make-assets.py`.


## GitHub Pages deployment

Push to `main` to publish `dist/` with the included GitHub Actions workflow. No build step or dependencies are required. In repository Settings → Pages, select GitHub Actions as the source.

Custom domain: `baseline.omkamath.tech`. Set the Pages custom domain to that hostname, then add this DNS record in the `omkamath.tech` zone:

| Type | Name | Target |
| --- | --- | --- |
| CNAME | baseline | Om-Kamath.github.io |

The CNAME target contains no path. Once DNS is verified and the certificate is issued, enable Enforce HTTPS in Pages settings.
