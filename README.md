# Baseline landing page

A responsive, buildless marketing page. Serve `dist/` with any static HTTP server:

```sh
python3 -m http.server 4173 --directory dist
```

Includes a persistent light/dark theme, native keyboard-accessible FAQ, scroll-snap screenshot carousel, reduced-motion support, and SEO/social metadata. No JavaScript dependencies or build step. Screenshot SVGs are lightweight illustrative placeholders based on the app references; replace them with production captures when ready. Recreate those illustrations with `python3 make-assets.py`.
