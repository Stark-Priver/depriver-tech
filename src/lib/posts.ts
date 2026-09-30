import { getCollection, type CollectionEntry } from "astro:content";
import { readdirSync, existsSync } from "node:fs";
import { join } from "node:path";

export type Post = CollectionEntry<"blog">;

/** Live posts, newest first. Drafts never reach the built site. */
export async function livePosts(): Promise<Post[]> {
  const posts = await getCollection("blog", ({ data }) => data.status === "live");
  return posts.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
}

/** Slide image URLs for a carousel folder in public/carousels/<name>. */
export function slidesFor(name?: string): string[] {
  if (!name) return [];
  const dir = join(process.cwd(), "public", "carousels", name);
  if (!existsSync(dir)) throw new Error(`Carousel folder not found: public/carousels/${name}`);
  return readdirSync(dir)
    .filter((f) => /^\d+\.(webp|jpe?g|png)$/i.test(f))
    .sort((a, b) => parseInt(a) - parseInt(b))
    .map((f) => `/carousels/${name}/${f}`);
}

/** Card/cover image: explicit cover, else the carousel's first slide. */
export function coverFor(post: Post): string | undefined {
  return post.data.cover ?? (post.data.carousel ? slidesFor(post.data.carousel)[0] : undefined);
}

export function readingMinutes(post: Post): number {
  const words = (post.body ?? "").split(/\s+/).filter(Boolean).length + (post.data.slides.join(" ").split(/\s+/).length);
  return Math.max(1, Math.round(words / 200));
}

export const formatDate = (d: Date, month: "short" | "long" = "short") =>
  d.toLocaleDateString("en-GB", { day: "numeric", month, year: "numeric" });
