// Recurring series and the small set of topics the blog is filtered by.
// A post joins a series or topic through its tags, so front matter stays as it is.

export type Series = { tag: string; name: string; blurb: string; day?: string };

export const series: Series[] = [
  { tag: "njia-za-tech", name: "Njia za Tech", blurb: "One tech career at a time: what the job is, the skills, and how to start." },
  { tag: "code-ya-wiki", name: "Code ya Wiki", blurb: "A short piece of broken code. Spot the bug, then see the fix explained." },
  { tag: "hiki-au-kile", name: "Hiki au Kile", blurb: "Two tools or choices side by side, and when to pick each one." },
  { tag: "kamusi", name: "Kamusi ya Tech", blurb: "Tech words explained in plain Kiswahili." },
  { tag: "inavyofanya-kazi", name: "Inavyofanya Kazi", blurb: "How everyday tech works under the hood: mobile money, WhatsApp, AI." },
  { tag: "jenga-kwa-tanzania", name: "Jenga kwa Tanzania", blurb: "Building for local reality: USSD, SMS, cheap phones and mobile money." },
  { tag: "swali-la-wiki", name: "Swali la Wiki", blurb: "Your questions, answered every Sunday.", day: "Sundays" },
];

export type Topic = { id: string; name: string; tags: string[] };

export const topics: Topic[] = [
  { id: "students", name: "Students", tags: ["students", "university", "fpt", "study", "exams", "holidays", "projects", "hackathons"] },
  { id: "career", name: "Career", tags: ["career", "careers", "cv", "interviews", "linkedin", "github", "junior developers", "portfolio", "remote-work", "njia-za-tech"] },
  { id: "skills", name: "Skills & code", tags: ["programming", "beginners", "roadmap", "git", "terminal", "linux", "sql", "databases", "debugging", "skills", "code-ya-wiki", "backend", "web", "developer-tools"] },
  { id: "security", name: "Security", tags: ["security", "scams", "passwords", "privacy"] },
  { id: "money", name: "Money", tags: ["money", "freelancing", "fintech", "mobile-money", "payments"] },
  { id: "gear", name: "Gear & tools", tags: ["gadgets", "laptops", "setup", "tools"] },
  { id: "personal", name: "Personal", tags: ["personal", "journey", "recap", "lessons", "services"] },
];

export const seriesOf = (tags: string[]) => series.find((s) => tags.includes(s.tag));
export const topicsOf = (tags: string[]) => topics.filter((t) => t.tags.some((x) => tags.includes(x))).map((t) => t.id);
