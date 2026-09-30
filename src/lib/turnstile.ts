// Cloudflare Turnstile (free, privacy-friendly human check). No-op when no site key is configured.
let loading: Promise<void> | null = null;

function load(): Promise<void> {
  loading ??= new Promise((resolve, reject) => {
    const s = document.createElement("script");
    s.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit";
    s.async = true;
    s.onload = () => resolve();
    s.onerror = reject;
    document.head.append(s);
  });
  return loading;
}

type TurnstileApi = {
  render: (el: HTMLElement, opts: Record<string, unknown>) => string;
  reset: (id: string) => void;
};

/** Renders a widget into `el`; returns getToken() and reset(). */
export async function turnstile(el: HTMLElement, siteKey: string) {
  if (!siteKey) return { getToken: () => "", reset: () => {} };
  await load();
  const ts = (window as unknown as { turnstile: TurnstileApi }).turnstile;
  let token = "";
  const dark = getComputedStyle(document.documentElement).colorScheme.includes("dark");
  const id = ts.render(el, {
    sitekey: siteKey,
    theme: dark ? "dark" : "light",
    appearance: "interaction-only",
    callback: (t: string) => (token = t),
    "expired-callback": () => (token = ""),
  });
  return { getToken: () => token, reset: () => { token = ""; ts.reset(id); } };
}
