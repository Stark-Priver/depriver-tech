// Talks with a web presenter. Files live in public/talks/<slug>/ (deck.json, img/, thumbs/, <slug>.pptx, <slug>.pdf),
// exported from the deck project with web_export.py. Add a talk here to get /talks/<slug>/, /present/ and /pdf/.
export type Talk = {
  slug: string;
  title: string;
  subtitle: string;
  date: string; // YYYY-MM-DD
  event: string;
  place: string;
  description: string;
  slides: number;
  pptxMB: number;
  pdfMB: number;
  credits?: string[];
};

export const talks: Talk[] = [
  {
    slug: "life-in-uni-vs-real-world-in-tech",
    title: "Life in Uni vs Real World in Tech",
    subtitle: "Your starting point is not your destination",
    date: "2026-10-07",
    event: "Field Practical Training 2026 guest talk",
    place: "Mbeya University of Science and Technology (MUST)",
    description:
      "A guest talk for MUST students finishing field practical training: what changes between campus and a tech job, the skills that matter, money and betting, and a 30-day challenge.",
    slides: 33,
    pptxMB: 21,
    pdfMB: 9.7,
    credits: [
      "Feed photos (Wikimedia Commons): popcorn, Alex Munsell (CC0) · betting shop, Ardfern (CC BY-SA 3.0) · cat, Emilian Robert Vicol (CC BY 2.0) · Python code, MikeRun (CC BY-SA 4.0) · network switch, Mvdiogo (CC BY-SA 4.0) · laptop desk, Shixart1985 (CC BY 2.0).",
      "Game screenshots from official store listings: PUBG: Battlegrounds © KRAFTON · Call of Duty: Mobile © Activision · eFootball © Konami. Used for illustration in an educational talk.",
    ],
  },
];

export const talkBase = (slug: string) => `/talks/${slug}/`;
