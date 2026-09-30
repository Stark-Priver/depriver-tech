// depriver.tech engagement API: page views (one per visitor per day) and likes (one per visitor).
//   GET    /stats/:slug          -> { views, likes }
//   GET    /stats?slugs=a,b      -> { a: {views, likes}, b: {...} }
//   POST   /view/:slug           -> count a view, return stats
//   POST   /like/:slug           -> like, return stats
//   DELETE /like/:slug           -> unlike, return stats
// Visitors are identified by a salted SHA-256 of IP + user agent; raw IPs are never stored.

const SLUG = /^[a-z0-9][a-z0-9-]{0,119}$/;

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const allowed = (env.ALLOWED_ORIGINS || "").split(",").map((s) => s.trim());
    const cors = {
      "Access-Control-Allow-Origin": allowed.includes(origin) ? origin : allowed[0],
      "Access-Control-Allow-Methods": "GET, POST, DELETE, OPTIONS",
      "Access-Control-Max-Age": "86400",
      Vary: "Origin",
    };
    const json = (data, status = 200) =>
      new Response(JSON.stringify(data), { status, headers: { "Content-Type": "application/json", "Cache-Control": "no-store", ...cors } });

    if (request.method === "OPTIONS") return new Response(null, { headers: cors });

    const url = new URL(request.url);
    const [, action, slug] = url.pathname.split("/");

    const stats = async (s) => {
      const row = await env.DB.prepare(
        "SELECT (SELECT COUNT(*) FROM views WHERE slug = ?1) AS views, (SELECT COUNT(*) FROM likes WHERE slug = ?1) AS likes",
      ).bind(s).first();
      return { views: row.views, likes: row.likes };
    };

    try {
      if (action === "stats" && !slug && request.method === "GET") {
        const slugs = (url.searchParams.get("slugs") || "").split(",").filter((s) => SLUG.test(s)).slice(0, 60);
        const out = {};
        for (const s of slugs) out[s] = await stats(s);
        return json(out);
      }
      if (!slug || !SLUG.test(slug)) return json({ error: "bad slug" }, 400);
      if (action === "stats" && request.method === "GET") return json(await stats(slug));

      // write paths: only from the site itself
      if (origin && !allowed.includes(origin)) return json({ error: "forbidden" }, 403);
      const ip = request.headers.get("CF-Connecting-IP") || "";
      const ua = request.headers.get("User-Agent") || "";
      const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(`${env.SALT || "depriver"}|${ip}|${ua}`));
      const visitor = [...new Uint8Array(digest)].slice(0, 16).map((b) => b.toString(16).padStart(2, "0")).join("");

      if (action === "view" && request.method === "POST") {
        const day = new Date().toISOString().slice(0, 10);
        await env.DB.prepare("INSERT OR IGNORE INTO views (slug, visitor, day) VALUES (?1, ?2, ?3)").bind(slug, visitor, day).run();
        return json(await stats(slug));
      }
      if (action === "like" && request.method === "POST") {
        await env.DB.prepare("INSERT OR IGNORE INTO likes (slug, visitor) VALUES (?1, ?2)").bind(slug, visitor).run();
        return json(await stats(slug));
      }
      if (action === "like" && request.method === "DELETE") {
        await env.DB.prepare("DELETE FROM likes WHERE slug = ?1 AND visitor = ?2").bind(slug, visitor).run();
        return json(await stats(slug));
      }
      return json({ error: "not found" }, 404);
    } catch (e) {
      return json({ error: "server error" }, 500);
    }
  },
};
