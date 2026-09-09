---
name: yeneywellness-project
description: Project context, architecture, media rules, deployment workflow, and current handoff state for YeneyWellness. Use when working on this website, its bilingual book content, author gallery, promotional video, Cloudflare deployment, or GitHub synchronization.
---

# YeneyWellness project context

Updated: 2026-09-09

## Product

YeneyWellness is the official bilingual marketing website for Yeney López-Pérez and her Spanish-language book, *El Método Cabello Saludable*. Spanish is the default public experience; equivalent English routes live under `/en`.

Development documentation, code comments, script output, commits, and technical handoffs must be in English. Spanish remains only in Spanish public pages, the Spanish book, narration, and intentional promotional-video copy.

- Production: https://belleza-con-yeney.pages.dev/
- Cloudflare Pages project: `belleza-con-yeney`
- GitHub remote: `https://github.com/lsantos2000/belleza-con-yeney.git`
- Branch: `main`

## Repository architecture

The Git repository is the `site/` directory inside the Codex workspace, not the workspace parent.

- `app/`: bilingual Next.js/Vinext website.
- `books/ElMetodoCabelloSaludable/`: book-specific editorial content and video generator.
- `resources/`: canonical shared images, documents, videos, and audio.
- `public/`: generated web-ready copies; never canonical.
- `tools/sync-public-assets.mjs`: copies canonical resources into stable public paths.
- `tools/audit-carousel.py`: validates carousel uniqueness.

Run `pnpm sync-assets` after changing canonical resources. `predev` and `prebuild` also run the sync automatically.

## Routes and language behavior

Spanish routes are `/`, `/el-metodo`, `/el-libro`, `/demo-libro`, `/la-autora`, and `/preguntas`. English mirrors live under `/en`.

Update both language variants when changing shared public copy or navigation unless a request explicitly targets one language. Do not translate the book title, author name, established public route names, or stable asset filenames.

## Purchase information

- Amazon, printed and digital, Spanish routes: https://www.amazon.com/dp/B0HFHC2QL7
- Amazon, printed and digital, English routes under `/en`: https://www.amazon.com/dp/B0HJ55BM9L
- Google Play Books, digital, Spanish routes: https://play.google.com/store/books/details?id=8VgDEgAAQBAJ
- Google Play Books, digital, English routes under `/en`: https://play.google.com/store/books/details?id=Gm8KEgAAQBAJ
- YouTube demo, both languages: https://www.youtube.com/watch?v=xUI1K6fISGw

Each language links to its own Amazon and Google Play listing. The split is intentional; do not collapse either pair into one link. `app/site-chrome.tsx` selects the listings through `amazon(lang)` and `googlePlay(lang)` helpers, and `app/book-links.tsx` keeps `amazonEs`/`amazonEn` and `googlePlayEs`/`googlePlayEn`, so shared components stay the single place to change them. `app/page.tsx` is the Spanish-only home page and correctly hard-codes the Spanish listings.

The purchase component intentionally has two store buttons. YouTube is a separate demo link, not a third store button. Avoid repeated purchase information within the same block.

## PDF demo sample

- Spanish routes (`/demo-libro`, `/el-libro`): `/El-metodo-cabello-saludable-de-yeny-demo.pdf`, not translated.
- English routes (`/en/demo-libro`, `/en/el-libro`): `/The-Healthy-Hair-Method-demo-en.pdf`, an intentionally translated English sample distinct from the Spanish demo.
- Canonical sources live in `resources/demo/`: `El_Metodo_Cabello_Saludable-demo.pdf` (Spanish) and `The_Healthy_Hair_Method_v48_demo_en_20260909.pdf` (English). `tools/sync-public-assets.mjs` copies both to their public paths; run `pnpm sync-assets` after replacing either.
- `app/en/demo-libro/page.tsx` holds the English `pdf`/`downloadName` constants; update there if the file changes.

## Author photographs

- Do not crop heads or long hair; author photographs use `object-fit: contain`.
- Do not reintroduce gallery images `09`, `27`, `47`, or `49`.
- Keep gallery assets unique by path, SHA-256, and perceptual comparison.
- Preserve the final carousel-order rules in the root `CLAUDE.md`.
- Do not retouch or regenerate supplied author photographs unless explicitly requested.

## Promotional video

The approved video is 180 seconds, 1280 × 720, and 24 fps, with six 30-second chapters. It alternates Yeney between left and right, uses half-second fades, includes book content in every scene, and avoids repeated author photographs and repeated text-only panels.

- Generator: `books/ElMetodoCabelloSaludable/video-generator/generate.py`
- Storyboard: `books/ElMetodoCabelloSaludable/video-generator/storyboard.json`
- Current output: `resources/videos/ElMetodoCabelloSaludable/el-metodo-cabello-saludable-promo-3-minutos.mp4`

Spanish storyboard titles and narration are product content and must remain Spanish. Excluded photographs include `yeney-08.jpeg` and `yeney-16.jpeg`. Standalone portraits embedded in collage pages are also excluded from individual scenes. See `resources/docs/ElMetodoCabelloSaludable/VIDEO_ASSETS.md`.

## Development and validation

Node.js `22.13.0` or newer is required.

```bash
pnpm install
pnpm dev
pnpm build
pnpm lint
pnpm sync-assets
```

Preserve pnpm, Next.js, Vinext, Vite, TypeScript, and the existing design system. Run `pnpm build` after source changes.

## Cloudflare deployment

```powershell
$env:CLOUDFLARE_PAGES_EXPORT = '1'
node node_modules/vinext/dist/cli.js build
node node_modules/wrangler/bin/wrangler.js pages deploy dist/client --project-name belleza-con-yeney --branch main
```

The latest known production deployment succeeded. Cloudflare authentication and GitHub authentication are separate.

## Git authentication caveat

Recent GitHub pushes failed because the stored GitHub CLI token for `lsantos2000` was invalid, while Git's fallback prompt tried to spawn a missing `sh` executable. The user must complete `gh auth login -h github.com` before retrying. Never force-push, and verify the remote branch before reporting synchronization.

## Preservation rules

- Keep credentials, tokens, account identifiers, and local absolute paths out of commits and user-facing output.
- Do not delete source Downloads or original media.
- Do not modify the Spanish book artwork or PDF contents unless explicitly requested.
- The website is informational and intentionally has no authentication layer.
- Health content must remain educational and must not make miracle or medical claims.
