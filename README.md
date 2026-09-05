# YeneyWellness

Official bilingual website for **Yeney López-Pérez**, author of the Spanish-language book *El Método Cabello Saludable*. The site presents the book, its method, the author gallery, frequently asked questions, and a downloadable PDF preview.

**Production:** [belleza-con-yeney.pages.dev](https://belleza-con-yeney.pages.dev/)

## Features

- Spanish is the default public language; the complete English version lives under `/en`.
- The `Español / English` selector preserves the current page and stores the preference in a cookie.
- Responsive desktop and mobile layouts with an accessible mobile menu.
- An author carousel that preserves the original framing of each photograph.
- An embedded book preview with a PDF download option.
- Official purchase links for Amazon and Google Play Books.
- Informational site with no authentication or user-account collection.

## Routes

| Spanish | English | Purpose |
| --- | --- | --- |
| `/` | `/en/` | Home page |
| `/el-metodo/` | `/en/el-metodo/` | Method overview |
| `/el-libro/` | `/en/el-libro/` | Book contents and interior |
| `/demo-libro/` | `/en/demo-libro/` | PDF preview and download |
| `/la-autora/` | `/en/la-autora/` | Author biography and gallery |
| `/preguntas/` | `/en/preguntas/` | Frequently asked questions |

## Official book links

- [Amazon — Kindle and printed book](https://www.amazon.com/dp/B0HFHC2QL7)
- [Google Play Books — Ebook](https://play.google.com/store/books/details?id=8VgDEgAAQBAJ)
- [YouTube demo](https://www.youtube.com/watch?v=xUI1K6fISGw)

## Technology

- Next.js 16 and React 19
- Vinext and Vite
- TypeScript
- Tailwind CSS 4
- Cloudflare Pages
- pnpm

Node.js `22.13.0` or newer is required.

## Local development

```bash
pnpm install
pnpm dev
```

The development server prints the available local URL.

## Commands

```bash
pnpm dev          # Start local development
pnpm build        # Create a production build
pnpm start        # Run the production build locally
pnpm lint         # Check the source code
pnpm sync-assets  # Refresh generated public copies from canonical resources
```

## Repository structure

```text
app/
  en/                    # English public routes
  demo-libro/            # Spanish PDF preview route
  el-libro/              # Spanish book route
  el-metodo/             # Spanish method route
  la-autora/             # Spanish biography and carousel route
  preguntas/             # Spanish FAQ route
  author-carousel.tsx    # Carousel order and behavior
  language-switcher.tsx  # Language cookie and route switching
  site-chrome.tsx        # Navigation, purchase UI, and footer
books/
  ElMetodoCabelloSaludable/
    es/content/           # Spanish editorial content
    en/content/           # English editorial content
    video-generator/      # Reproducible promotional-video generator
resources/
  images/author/          # Shared canonical author photographs
  images/books/           # Canonical book pages and artwork
  docs/                   # Audits and production documentation
  videos/                 # Current final videos
  audio/                  # Narration and other audio
public/                   # Generated web-ready copies; not canonical
tools/                    # Development and validation utilities
```

Canonical assets belong in `resources/`. Run `pnpm sync-assets` after changing them. Do not edit generated copies under `public/` directly.

The public PDF keeps a stable name so future revisions can replace it without changing links:

```text
public/El-metodo-cabello-saludable-de-yeny-demo.pdf
```

## Cloudflare Pages deployment

The public site is hosted in the Cloudflare Pages project `belleza-con-yeney`. Build and verify all twelve Spanish and English routes before deployment.

```powershell
$env:CLOUDFLARE_PAGES_EXPORT = '1'
node node_modules/vinext/dist/cli.js build
node node_modules/wrangler/bin/wrangler.js pages deploy dist/client --project-name belleza-con-yeney --branch main
```

This requires a valid Wrangler session. Without `CLOUDFLARE_PAGES_EXPORT`, the build retains the project's normal behavior.

## Development language policy

Source-code comments, scripts, commit messages, and repository documentation must be written in English. Spanish is retained only where it is part of the Spanish public experience or the Spanish-language book and promotional-video content. Do not translate the book title, author name, established public routes, or stable asset filenames.

## Rights

The editorial content, book, and photographs belong to their respective rights holders. This repository does not include a reuse license, and public deployment does not grant reuse rights for those materials.
