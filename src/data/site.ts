// Site-wide settings. Empty values keep a feature hidden, so the site works before Cloudflare is set up.
export const site = {
  url: "https://depriver.tech",
  name: "Privatus Cosmas",
  // Cloudflare Worker in /worker: views, likes, comments, contact form and the "Ask AI" assistant.
  // e.g. "https://depriver-engage.<account>.workers.dev"
  engageApi: "",
  // Cloudflare Turnstile site key (public). Spam protection for comments and the contact form.
  turnstileSiteKey: "",
  // Cloudflare Web Analytics token (public). Privacy-friendly, cookie-free visitor stats.
  cfAnalyticsToken: "",
};
