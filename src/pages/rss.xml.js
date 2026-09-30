import rss from "@astrojs/rss";
import { livePosts } from "../lib/posts";

export async function GET(context) {
  const posts = await livePosts();
  return rss({
    title: "Privatus Cosmas · Blog",
    description: "Notes on software, learning, tech life and the journey.",
    site: context.site,
    items: posts.map((p) => ({ title: p.data.title, description: p.data.description, pubDate: p.data.date, link: `/blog/${p.id}/` })),
  });
}
