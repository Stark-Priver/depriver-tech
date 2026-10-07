// Web presenter for decks exported by the talk's web_export.py (public/talks/<slug>/deck.json).
// Each slide is a list of named shapes on a 1920x1080 stage. Moving between slides replays PowerPoint's Morph:
// shapes with the same name glide (position, size, rotation) and cross-fade if their look changed; the rest fade.

type Run = { t: string; sz?: number; b?: boolean; spc?: number; font?: string; color?: string; stroke?: [number, string] };
type Para = { align: string; line: number; runs: Run[] };
type Shape = {
  n: string; k: "img" | "box"; x: number; y: number; w: number; h: number; rot?: number; src?: string; r?: number; round?: boolean;
  fill?: [string, number]; line?: [number, string]; text?: Para[]; body?: { anchor: string; wrap: boolean; pad: number[] };
  shadow?: { blur: number; dist: number; color: [string, number] };
};
type Deck = { w: number; h: number; slides: { dur: number; shapes: Shape[] }[] };

const LINE = 1.2; // PowerPoint "single" line spacing for Poppins, relative to the font size
const EASE = "cubic-bezier(0.45, 0.05, 0.25, 1)";

const rgba = (hex: string, a = 1) => {
  const n = parseInt(hex.slice(1), 16);
  return `rgba(${n >> 16}, ${(n >> 8) & 255}, ${n & 255}, ${a})`;
};

function weight(r: Run) {
  if (r.font?.includes("SemiBold")) return 600;
  if (r.font?.includes("Medium")) return 500;
  return r.b ? 700 : 400;
}

function build(s: Shape, base: string): HTMLElement {
  const el = document.createElement("div");
  el.className = "shp";
  Object.assign(el.style, { left: `${s.x}px`, top: `${s.y}px`, width: `${s.w}px`, height: `${s.h}px`, transform: `rotate(${s.rot || 0}deg)` });
  if (s.k === "img") {
    const img = document.createElement("img");
    img.src = base + s.src;
    img.alt = "";
    img.draggable = false;
    el.appendChild(img);
    if (s.shadow) el.style.filter = `drop-shadow(0 ${s.shadow.dist}px ${s.shadow.blur / 2}px ${rgba(s.shadow.color[0], s.shadow.color[1])})`;
    return el;
  }
  if (s.fill) el.style.background = rgba(s.fill[0], s.fill[1]);
  if (s.line) el.style.boxShadow = `inset 0 0 0 ${s.line[0]}px ${s.line[1]}`;
  if (s.shadow) el.style.boxShadow = [el.style.boxShadow, `0 ${s.shadow.dist}px ${s.shadow.blur}px ${rgba(s.shadow.color[0], s.shadow.color[1])}`].filter(Boolean).join(", ");
  if (s.r) el.style.borderRadius = `${s.r}px`;
  if (s.round) el.style.borderRadius = "50%";
  if (s.text && s.body) {
    const b = s.body;
    const tx = document.createElement("div");
    tx.className = "tx";
    Object.assign(tx.style, {
      padding: b.pad.map((p) => `${p}px`).join(" "),
      justifyContent: { t: "flex-start", ctr: "center", b: "flex-end" }[b.anchor] || "flex-start",
      whiteSpace: b.wrap ? "pre-wrap" : "pre",
    });
    for (const p of s.text) {
      const pe = document.createElement("p");
      pe.style.textAlign = { l: "left", ctr: "center", r: "right", just: "justify" }[p.align] || "left";
      const size = Math.max(...p.runs.map((r) => r.sz || 18), 1);
      pe.style.fontSize = `${size}px`; // the strut must match the runs, or mixed sizes add extra leading
      pe.style.lineHeight = `${size * LINE * p.line}px`;
      for (const r of p.runs) {
        const sp = document.createElement("span");
        sp.textContent = r.t || " ";
        Object.assign(sp.style, { fontSize: `${r.sz}px`, fontWeight: String(weight(r)), letterSpacing: r.spc ? `${r.spc}px` : "" });
        if (r.stroke) {
          sp.style.color = "transparent";
          sp.style.setProperty("-webkit-text-stroke", `${r.stroke[0]}px ${r.stroke[1]}`);
        } else sp.style.color = r.color || "#0b1e3f";
        pe.appendChild(sp);
      }
      if (!p.runs.length) pe.innerHTML = "&nbsp;";
      tx.appendChild(pe);
    }
    el.appendChild(tx);
  }
  return el;
}

// a shape's look without its geometry: equal looks glide, different looks glide and cross-fade
const look = (s: Shape) => JSON.stringify({ ...s, x: 0, y: 0, w: 0, h: 0, rot: 0 });

export function startPresenter(root: HTMLElement) {
  const base = root.dataset.base!;
  const stage = root.querySelector<HTMLElement>(".stage")!;
  const counter = root.querySelector<HTMLElement>("[data-counter]")!;
  const bar = root.querySelector<HTMLElement>("[data-bar]")!;
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  let deck: Deck;
  let index = 0;
  let layer: HTMLElement | null = null;
  let current = new Map<string, { el: HTMLElement; s: Shape }>();
  let busy: Animation[] = [];

  const fit = () => {
    const k = Math.min(innerWidth / 1920, innerHeight / 1080);
    stage.style.transform = `translate(-50%, -50%) scale(${k})`;
  };

  function render(i: number) {
    const l = document.createElement("div");
    l.className = "layer";
    const map = new Map<string, { el: HTMLElement; s: Shape }>();
    deck.slides[i].shapes.forEach((s, z) => {
      const el = build(s, base);
      el.style.zIndex = String(z + 1);
      l.appendChild(el);
      map.set(map.has(s.n) ? `${s.n}#${z}` : s.n, { el, s });
    });
    return { l, map };
  }

  function flip(from: Shape, to: Shape) {
    const dx = from.x + from.w / 2 - (to.x + to.w / 2);
    const dy = from.y + from.h / 2 - (to.y + to.h / 2);
    const sx = to.w ? from.w / to.w : 1;
    const sy = to.h ? from.h / to.h : 1;
    return [`translate(${dx}px, ${dy}px) rotate(${from.rot || 0}deg) scale(${sx}, ${sy})`, `translate(0, 0) rotate(${to.rot || 0}deg) scale(1, 1)`];
  }

  function go(i: number, animate = true) {
    i = Math.max(0, Math.min(deck.slides.length - 1, i));
    if (i === index && layer) return;
    busy.forEach((a) => a.finish());
    busy = [];
    const { l, map } = render(i);
    const old = layer;
    const oldMap = current;
    stage.appendChild(l);
    const dur = reduce || !animate || !old ? 0 : deck.slides[Math.max(i, index)].dur * (i < index ? 0.7 : 1);
    if (dur && old) {
      const opt = { duration: dur, easing: EASE, fill: "both" as FillMode };
      for (const [name, { el, s }] of map) {
        const prev = oldMap.get(name);
        if (prev && name !== "paper") {
          busy.push(el.animate({ transform: flip(prev.s, s) }, opt));
          if (look(prev.s) === look(s)) {
            prev.el.style.visibility = "hidden";
          } else {
            busy.push(el.animate({ opacity: [0, 1] }, opt));
            const back = flip(s, prev.s).reverse();
            busy.push(prev.el.animate({ transform: back, opacity: [1, 0] }, opt));
          }
        } else if (!prev) {
          busy.push(el.animate({ opacity: [0, 1] }, { ...opt, easing: "ease-in-out" }));
        }
      }
      for (const [name, prev] of oldMap) {
        if (!map.has(name)) busy.push(prev.el.animate({ opacity: [1, 0] }, { ...opt, duration: dur * 0.6, easing: "ease-in" }));
      }
      // keep the old layer underneath only for shapes still fading or gliding out
      l.style.zIndex = "2";
      old.style.zIndex = "1";
      Promise.all(busy.map((a) => a.finished.catch(() => {}))).then(() => {
        if (old.isConnected) old.remove();
        busy.forEach((a) => a.cancel());
        busy = [];
      });
    } else if (old) {
      old.remove();
    }
    layer = l;
    current = map;
    index = i;
    counter.textContent = `${i + 1} / ${deck.slides.length}`;
    bar.style.transform = `scaleX(${(i + 1) / deck.slides.length})`;
    history.replaceState(null, "", `#${i + 1}`);
  }

  const next = () => go(index + 1);
  const prev = () => go(index - 1);

  addEventListener("keydown", (e) => {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const k = e.key;
    if (["ArrowRight", "ArrowDown", "PageDown", " ", "Enter", "n"].includes(k)) { e.preventDefault(); next(); }
    else if (["ArrowLeft", "ArrowUp", "PageUp", "Backspace", "p"].includes(k)) { e.preventDefault(); prev(); }
    else if (k === "Home") go(0, false);
    else if (k === "End") go(deck.slides.length - 1, false);
    else if (k === "f" || k === "F") toggleFull();
  });
  stage.parentElement!.addEventListener("click", (e) => {
    if ((e.target as HTMLElement).closest("button, a")) return;
    (e.clientX < innerWidth / 3 ? prev : next)();
  });
  let tx = 0, ty = 0;
  addEventListener("touchstart", (e) => { tx = e.touches[0].clientX; ty = e.touches[0].clientY; }, { passive: true });
  addEventListener("touchend", (e) => {
    const dx = e.changedTouches[0].clientX - tx, dy = e.changedTouches[0].clientY - ty;
    if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) (dx < 0 ? next : prev)();
  });

  function toggleFull() {
    if (document.fullscreenElement) document.exitFullscreen();
    else root.requestFullscreen?.().catch(() => {});
  }
  root.querySelector("[data-prev]")?.addEventListener("click", prev);
  root.querySelector("[data-next]")?.addEventListener("click", next);
  root.querySelector("[data-full]")?.addEventListener("click", toggleFull);

  let idle = 0;
  const wake = () => {
    root.classList.add("awake");
    clearTimeout(idle);
    idle = window.setTimeout(() => root.classList.remove("awake"), 2200);
  };
  addEventListener("mousemove", wake);
  addEventListener("resize", fit);
  fit();

  fetch(base + "deck.json")
    .then((r) => r.json())
    .then(async (d: Deck) => {
      deck = d;
      // warm the image cache so morphs never wait for a download
      const srcs = new Set(d.slides.flatMap((s) => s.shapes.filter((x) => x.src).map((x) => base + x.src)));
      srcs.forEach((src) => { const im = new Image(); im.src = src; });
      await document.fonts.ready;
      const start = parseInt(location.hash.slice(1), 10);
      go(Number.isFinite(start) ? start - 1 : 0, false);
      root.classList.add("ready");
      wake();
    });
}
