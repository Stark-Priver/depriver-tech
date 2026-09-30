# depriver.tech

Personal storytelling site and blog for Privatus Cosmas. Built with Astro, GSAP and Lenis.
Colours and fonts match the Instagram carousels.

## Run it
    npm install
    npm run dev        # http://localhost:4321
    npm run build      # static site in dist/

## Pages
- `/`: the blog (home page)
- `/story/`: the life story, told as chapters
- `/blog/<post>/`: individual posts (`/blog` redirects to `/`)

## Themes
Press **T** anywhere (or click the palette icon) to open the theme menu, **Shift+T** to jump to the next theme.
It has Auto/Light/Dark, a search box, and grouped themes (Depriver plus every Omarchy theme on this machine)
with a live preview card. The choice is remembered per visitor.
After installing or changing Omarchy themes, run `npm run themes` to regenerate
`src/styles/themes.css` and `src/data/themes.json`, then commit them.

## Where things live
- `src/data/story.ts`: every chapter of the life story, services, lessons and contact details. Edit text here.
- `STORY.md`: the raw life-story notes (local only, git-ignored, never published).
- `src/content/blog/*.md`: blog posts (Markdown).
- `studio/`: carousel design sources (render with `npm run carousel -- <slug>`).
- `worker/`: views + likes API (Cloudflare Worker).
- `scripts/terrain.mjs`: generates the topographic background artwork.

## Publishing (everything lives in git)
Posts are Markdown files in `src/content/blog/`. The file name is the link:
`src/content/blog/coding-basics-for-beginners.md` → `https://depriver.tech/blog/coding-basics-for-beginners/`.
Use short, lowercase, hyphenated names.

```md
---
title: "My post title"
description: "One or two sentences, shown on cards and in link previews."
date: 2026-10-01
status: live          # live = published · draft = hidden
tags: ["tech"]
cover: /img/blog/photo.jpg     # optional (text posts)
carousel: my-carousel          # optional: folder in public/carousels
slides:                        # optional: one caption per slide (also alt text)
  - "Slide 1 caption"
---
Write the caption / article here in Markdown.
```

Push to `main` and GitHub Actions publishes it in about a minute. To take a post down, set `status: draft` and push.

## Carousels
Every carousel is designed in `studio/` (shared palette, fonts and helpers in `studio/base.py`, your photo in `studio/assets/`).

    npm run carousel -- coding-basics-for-beginners

renders `studio/<slug>/make.py` to full-size Instagram JPGs in `studio/<slug>/export/` (not committed) and imports
web slides into `public/carousels/<slug>/`. Then write `src/content/blog/<slug>.md` with `carousel: <slug>`.
New carousel: copy one of the `studio/<slug>/` folders, rename it to the new slug, and edit `make.py`.

## Link previews
Every post gets a branded 1200×630 share image at `/og/blog/<slug>.jpg` (built by `src/pages/og/`), plus full
Open Graph/Twitter tags, so links unfurl properly on WhatsApp, X, LinkedIn and Facebook.

## Comments, views and likes
- **Comments + reactions:** giscus (GitHub Discussions, category Announcements). Needs the giscus app installed on this repo.
- **Views + likes:** Cloudflare Worker in `worker/` (D1 database). Deploy, then put its URL in `src/data/site.ts` → `engageApi`.

      cd worker
      npx wrangler login
      npx wrangler d1 create depriver-engage          # paste the id into wrangler.toml
      npx wrangler d1 execute depriver-engage --remote --file schema.sql
      npx wrangler secret put SALT                     # any long random string
      npx wrangler deploy
