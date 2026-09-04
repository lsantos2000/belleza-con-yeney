# CLAUDE.md

Guidance for AI coding agents working in this repository.

## Project intent

This is the official bilingual marketing site for Yeney López-Pérez and her Spanish-language book, *El Método Cabello Saludable*. Preserve its warm hair-health and self-care identity. The site is informational and intentionally has no authentication or authorization layer.

The repository is named **YeneyWellness**. Shared canonical assets belong in `resources/`; book-specific content and generators belong in `books/ElMetodoCabelloSaludable/`. Run `pnpm sync-assets` after resource changes. Do not treat generated public copies as canonical sources.

Production URL: `https://belleza-con-yeney.pages.dev/`

## Required workflow

1. Read this file and the relevant source files before editing.
2. Preserve the existing pnpm/Vinext/Vite architecture.
3. Make focused changes; do not replace the design system or introduce a new framework.
4. Run `pnpm build` after source changes. Fix real build errors before handing off.
5. Do not deploy, commit, push, or change Cloudflare configuration unless the user requests it.

## Language architecture

- Spanish is the default language at `/`.
- English pages live under `/en`.
- Every public content page must have a mirrored English route.
- When changing visible copy or navigation, update both language versions in the same change.
- `app/language-switcher.tsx` stores the choice in the `yeney_language` cookie for one year.
- The language selector must keep visitors on the equivalent route when switching languages.
- Do not translate the book title, author name, PDF contents, or filenames unless explicitly requested.

## Canonical routes

Spanish routes:

- `/`
- `/el-metodo`
- `/el-libro`
- `/demo-libro`
- `/la-autora`
- `/preguntas`

English routes mirror these under `/en`.

## Shared UI

- Use `app/site-chrome.tsx` for shared navigation, purchase buttons, mobile menu, and footer.
- Use `app/language-switcher.tsx` for language selection and cookie behavior.
- Use `app/author-carousel.tsx` for the author gallery.
- Keep the mobile menu at the top of the page and keyboard accessible.
- Preserve the responsive breakpoints and warm palette defined in `app/globals.css`.
- Author photographs must use `object-fit: contain`; do not crop heads or hair.

## Author carousel rules

- Keep the strongest full-hair portraits first.
- Do not reintroduce gallery images `09`, `27`, `47`, or `49`.
- The final two carousel images must be the book images `18` followed by `48`.
- Keep captions and the total photograph count generated from the array rather than hard-coded.

## Book and purchase data

Use these canonical purchase links:

- Amazon: `https://www.amazon.com/dp/B0HFHC2QL7`
- Google Play Books: `https://play.google.com/store/books/details?id=8VgDEgAAQBAJ`

The site should show two purchase buttons only:

- Amazon — Kindle/printed book
- Google Play Books — Ebook

The demo PDF public path is stable:

```text
/El-metodo-cabello-saludable-de-yeny-demo.pdf
```

If the demo changes, replace the file at that path and update the displayed page count in both languages. Do not rename the public path.

## Content and safety

- Keep the book's health information educational, measured, and free of miracle claims.
- Preserve the distinction between Yeney's personal experience and scientifically supported information.
- Do not present the site as medical advice.
- Do not modify, regenerate, or retouch author photographs or book artwork unless explicitly requested.
- Do not expose local paths, credentials, account identifiers, or deployment tokens.

## Commands

```bash
pnpm install
pnpm dev
pnpm build
pnpm start
pnpm lint
```

Node.js `22.13.0` or newer is required.

## Generated and local-only files

Do not commit build output, deployment staging directories, temporary renders, Wrangler state, or local credentials. Follow `.gitignore` and keep these directories local:

- `dist/`
- `work/`
- `tmp/`
- `.wrangler/`
- `.wrangler-config/`
