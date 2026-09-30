import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://depriver.tech",
  integrations: [sitemap()],
  redirects: { "/blog": "/" },
});
