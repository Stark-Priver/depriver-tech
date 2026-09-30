// Branded 1200x630 share images (Open Graph / Twitter cards), generated at build time.
import type { APIRoute, GetStaticPaths } from "astro";
import satori from "satori";
import { Resvg } from "@resvg/resvg-js";
import sharp from "sharp";
import { readFileSync, existsSync } from "node:fs";
import { join } from "node:path";
import { livePosts, slidesFor } from "../../lib/posts";

const root = process.cwd();
const font = (f: string) => readFileSync(join(root, "public/fonts", f));
const fonts = [
  { name: "Poppins", data: font("Poppins-Regular.ttf"), weight: 400 as const, style: "normal" as const },
  { name: "Poppins", data: font("Poppins-SemiBold.ttf"), weight: 600 as const, style: "normal" as const },
  { name: "Poppins", data: font("Poppins-Bold.ttf"), weight: 700 as const, style: "normal" as const },
  { name: "Dafoe", data: font("MrDafoe-Regular.ttf"), weight: 400 as const, style: "normal" as const },
];
const dataUri = (path: string, mime: string) => `data:${mime};base64,${readFileSync(path).toString("base64")}`;
const ME = dataUri(join(root, "src/assets/og-me.png"), "image/png");

type Card = { label: string; title: string; description: string; image?: string; badge?: string };

export const getStaticPaths: GetStaticPaths = async () => {
  const posts = await livePosts();
  const pages: { params: { slug: string }; props: Card }[] = posts.map((p) => {
    const cover = p.data.carousel ? join(root, "public/carousels", p.data.carousel, "cover.jpg") : undefined;
    const n = slidesFor(p.data.carousel).length;
    return {
      params: { slug: `blog/${p.id}` },
      props: {
        label: "Privatus Cosmas · Blog",
        title: p.data.title,
        description: p.data.description,
        image: cover && existsSync(cover) ? dataUri(cover, "image/jpeg") : undefined,
        badge: n ? `Carousel · ${n} slides` : p.data.tags[0],
      },
    };
  });
  pages.push(
    { params: { slug: "home" }, props: { label: "Privatus Cosmas · Blog", title: "Notes from the journey", description: "Software, learning, tech life and everything I pick up along the way. Written from Mbeya, Tanzania." } },
    { params: { slug: "story" }, props: { label: "My story", title: "From Kitwe Village to Writing Code", description: "The setbacks, the second chances and everything that made me a Software Engineer & Digital Innovator." } },
  );
  return pages;
};

const el = (type: string, style: Record<string, unknown>, children?: unknown, extra: Record<string, unknown> = {}) =>
  ({ type, props: { style, children, ...extra } });

export const GET: APIRoute = async ({ props }) => {
  const c = props as Card;
  const size = c.title.length > 60 ? 46 : c.title.length > 40 ? 54 : 66;
  const maxDesc = c.title.length > 40 ? 105 : 150;
  const visual = c.image
    ? el("div", { display: "flex", position: "relative", width: 330, height: 520, marginRight: 70 }, [
        el("div", { position: "absolute", top: 18, left: 34, width: 300, height: 375, borderRadius: 26, background: "#e8603a", transform: "rotate(7deg)" }),
        el("img", { position: "absolute", top: 40, left: 0, width: 330, height: 412, borderRadius: 26, objectFit: "cover", transform: "rotate(-3deg)",
          boxShadow: "0 30px 60px rgba(0,0,0,0.45)" }, undefined, { src: c.image, width: 330, height: 412 }),
      ])
    : el("div", { display: "flex", position: "relative", width: 380, height: 630, alignItems: "flex-end", justifyContent: "center" }, [
        el("div", { position: "absolute", bottom: 90, width: 330, height: 330, borderRadius: 330, border: "10px solid #e8603a", opacity: 0.9 }),
        el("img", { width: 360, height: 480 }, undefined, { src: ME, width: 360, height: 480 }),
      ]);

  const svg = await satori(
    el("div", { display: "flex", width: 1200, height: 630, background: "#0b1e3f", fontFamily: "Poppins", position: "relative", alignItems: "center", justifyContent: "space-between" }, [
      el("div", { position: "absolute", left: 0, top: 0, width: 1200, height: 10, background: "#e8603a" }),
      el("div", { display: "flex", flexDirection: "column", width: c.image ? 700 : 740, paddingLeft: 72 }, [
        el("div", { display: "flex", fontSize: 22, fontWeight: 600, letterSpacing: 3, color: "#e8603a", textTransform: "uppercase" }, c.label),
        el("div", { display: "flex", width: 64, height: 6, background: "#e8603a", borderRadius: 3, marginTop: 14 }),
        el("div", { display: "flex", fontSize: size, fontWeight: 700, color: "#ffffff", lineHeight: 1.08, marginTop: 26, letterSpacing: -1.5 }, c.title),
        el("div", { display: "flex", fontSize: 25, color: "#c4d0e8", lineHeight: 1.45, marginTop: 22 },
          c.description.length > maxDesc ? c.description.slice(0, maxDesc - 3).trimEnd() + "…" : c.description),
        el("div", { display: "flex", alignItems: "center", marginTop: 38 }, [
          el("div", { display: "flex", fontFamily: "Dafoe", fontSize: 44, color: "#ffffff" }, "Privatus"),
          el("div", { display: "flex", fontSize: 22, fontWeight: 600, color: "#a9c4f5", marginLeft: 22 }, "depriver.tech"),
          ...(c.badge ? [el("div", { display: "flex", fontSize: 19, fontWeight: 600, color: "#ffffff", background: "#e8603a", borderRadius: 999, padding: "8px 18px", marginLeft: 22 }, c.badge)] : []),
        ]),
      ]),
      visual,
    ]) as never,
    { width: 1200, height: 630, fonts },
  );
  const png = new Resvg(svg, { fitTo: { mode: "width", value: 1200 } }).render().asPng();
  // JPEG keeps previews well under WhatsApp's size limit
  const jpg = await sharp(png).jpeg({ quality: 86, mozjpeg: true }).toBuffer();
  return new Response(new Uint8Array(jpg), { headers: { "Content-Type": "image/jpeg" } });
};
