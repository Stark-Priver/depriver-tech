// Site-wide settings for engagement features. Empty values keep a feature hidden.
export const site = {
  url: "https://depriver.tech",
  name: "Privatus Cosmas",
  // Views + likes API (Cloudflare Worker in /worker). e.g. "https://depriver-engage.<account>.workers.dev"
  engageApi: "",
  // Comments via giscus (GitHub Discussions). Fill after installing https://github.com/apps/giscus on the repo.
  giscus: {
    repo: "Stark-Priver/depriver-tech",
    repoId: "R_kgDOU1Exwg",
    // Announcements: only the owner (and giscus on his behalf) can open threads, so no spam discussions
    category: "Announcements",
    categoryId: "DIC_kwDOU1Exws4DGvfa",
  },
};
