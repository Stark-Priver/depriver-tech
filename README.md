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
- `public/admin/`: browser blog editor (Sveltia CMS) at `/admin`.
- `scripts/terrain.mjs`: generates the topographic background artwork.

## Writing a blog post
**In the browser:** open `https://depriver.tech/admin`, sign in with a GitHub personal access token
(repo scope), click *New Post*, write and publish. It commits to GitHub and the site redeploys.

**In code:** add a file to `src/content/blog/`:

    ---
    title: "My post title"
    description: "One or two sentences."
    date: 2026-10-01
    tags: ["tech"]
    cover: /img/blog/photo.jpg   # optional
    ---
    Write here in Markdown.
