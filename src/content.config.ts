import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

// Every post is a Markdown file in src/content/blog, tracked in git.
// status: live  -> published on the next push
// status: draft -> hidden (page and listing are removed on the next push)
const blog = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/blog" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    status: z.enum(["live", "draft"]).default("live"),
    tags: z.array(z.string()).default([]),
    cover: z.string().optional(),
    // carousel posts: folder name in public/carousels (import with scripts/add-carousel.py)
    carousel: z.string().optional(),
    // optional caption per slide, shown under the viewer and used as image alt text
    slides: z.array(z.string()).default([]),
  }),
});

export const collections = { blog };
