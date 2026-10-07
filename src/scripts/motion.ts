import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import Lenis from "lenis";

gsap.registerPlugin(ScrollTrigger);

const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// ── smooth scroll ─────────────────────────────────────────
let lenis: Lenis | null = null;
if (!reduce) {
  lenis = new Lenis({ duration: 1.15, smoothWheel: true });
  lenis.on("scroll", ScrollTrigger.update);
  gsap.ticker.add((t) => lenis!.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);
  document.querySelectorAll<HTMLAnchorElement>('a[href*="#"]').forEach((a) => {
    a.addEventListener("click", (e) => {
      const url = new URL(a.href, location.href);
      const el = url.hash ? document.querySelector(url.hash) : null;
      if (el && url.pathname === location.pathname) {
        e.preventDefault();
        // targets inside a scrolling panel (the post viewer) scroll that panel, not the page
        if (el.closest("[data-lenis-prevent]")) el.scrollIntoView({ behavior: "smooth", block: "start" });
        else lenis!.scrollTo(el as HTMLElement, { offset: -60 });
      }
    });
  });
}

// ── progress bar, nav state ───────────────────────────────
const bar = document.querySelector<HTMLElement>(".progress span");
const nav = document.querySelector<HTMLElement>("[data-nav]");
let lastY = 0;
function onScroll() {
  const y = window.scrollY;
  const max = document.documentElement.scrollHeight - innerHeight;
  if (bar) bar.style.transform = `scaleX(${max > 0 ? y / max : 0})`;
  if (nav) {
    nav.classList.toggle("scrolled", y > 30);
    nav.classList.toggle("hidden", y > 400 && y > lastY);
  }
  lastY = y;
}
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

if (reduce) {
  document.querySelectorAll<HTMLElement>("[data-count]").forEach((el) => (el.textContent = el.dataset.count!));
} else {
  // ── hero intro ──────────────────────────────────────────
  const hero = document.querySelector("[data-hero]");
  if (hero) {
    const lines = hero.querySelectorAll<SVGPathElement>(".contours path");
    lines.forEach((p) => {
      const len = p.getTotalLength();
      p.style.strokeDasharray = `${len}`;
      p.style.strokeDashoffset = `${len}`;
    });
    const tl = gsap.timeline({ defaults: { ease: "expo.out" } });
    tl.to(lines, { strokeDashoffset: 0, duration: 3.2, stagger: 0.06, ease: "power2.inOut" }, 0)
      .to(hero.querySelectorAll(".line-mask > span"), { y: 0, duration: 1.3, stagger: 0.1 }, 0.15)
      .from(hero.querySelector(".hero-photo"), { clipPath: "inset(100% 0 0 0)", duration: 1.6, ease: "expo.inOut" }, 0.1)
      .from(hero.querySelector(".hero-block"), { xPercent: -100, duration: 1.3, ease: "expo.inOut" }, 0.2)
      .from(hero.querySelector(".hero-name"), { clipPath: "inset(0 100% 0 0)", duration: 1.6, ease: "power3.inOut" }, 0.9)
      .to(hero.querySelectorAll("[data-reveal]"), { opacity: 1, y: 0, duration: 1.1, stagger: 0.1 }, 0.7);
    gsap.to(hero.querySelector(".hero-photo img"), {
      yPercent: 12, ease: "none",
      scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true },
    });
  }

  // ── generic reveals ─────────────────────────────────────
  // IntersectionObserver (not ScrollTrigger.batch) so reveals also fire after reloads and jumps mid-page.
  const io = new IntersectionObserver(
    (entries) => {
      const visible = entries.filter((e) => e.isIntersecting).map((e) => e.target);
      if (!visible.length) return;
      visible.forEach((el) => io.unobserve(el));
      const masks = visible.filter((el) => el.classList.contains("line-mask")).flatMap((m) => [...m.children]);
      const blocks = visible.filter((el) => !el.classList.contains("line-mask"));
      if (masks.length) gsap.to(masks, { y: 0, duration: 1.2, ease: "expo.out", stagger: 0.08 });
      if (blocks.length) gsap.to(blocks, { opacity: 1, y: 0, duration: 1.1, ease: "expo.out", stagger: 0.08 });
    },
    { rootMargin: "0px 0px -8% 0px" },
  );
  document
    .querySelectorAll("[data-reveal]:not([data-hero] [data-reveal]), .line-mask:not([data-hero] .line-mask)")
    .forEach((el) => io.observe(el));

  // ── counters ────────────────────────────────────────────
  gsap.utils.toArray<HTMLElement>("[data-count]").forEach((el) => {
    const target = parseFloat(el.dataset.count!);
    const obj = { v: 0 };
    gsap.to(obj, {
      v: target, duration: 2, ease: "power3.out",
      onUpdate: () => (el.textContent = Math.round(obj.v).toString()),
      scrollTrigger: { trigger: el, start: "top 85%", once: true },
    });
  });

  // ── Kaisho rank climb ───────────────────────────────────
  document.querySelectorAll<HTMLElement>("[data-rank]").forEach((el) => {
    const dot = el.querySelector(".rank-dot");
    const fill = el.querySelector(".rank-fill");
    const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: "top 75%", once: true } });
    tl.fromTo(fill, { scaleY: 0 }, { scaleY: 1, duration: 2.2, ease: "power3.inOut" })
      .fromTo(dot, { top: "92%" }, { top: "4%", duration: 2.2, ease: "power3.inOut" }, 0);
  });

  // ── story rail: big year follows the chapter in view ────
  const railYear = document.querySelector<HTMLElement>("[data-rail-year]");
  const railLine = document.querySelector<HTMLElement>("[data-rail-line]");
  const story = document.querySelector("#story");
  if (railYear && story) {
    gsap.utils.toArray<HTMLElement>("[data-chapter]").forEach((ch) => {
      ScrollTrigger.create({
        trigger: ch,
        start: "top 55%",
        end: "bottom 55%",
        onToggle: (self) => {
          if (!self.isActive || railYear.textContent === ch.dataset.chapter) return;
          gsap.to(railYear, {
            y: -30, opacity: 0, duration: 0.25, ease: "power2.in",
            onComplete: () => {
              railYear.textContent = ch.dataset.chapter!;
              gsap.fromTo(railYear, { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "expo.out" });
            },
          });
        },
      });
    });
    if (railLine)
      gsap.fromTo(railLine, { scaleY: 0 }, {
        scaleY: 1, ease: "none",
        scrollTrigger: { trigger: story, start: "top 50%", end: "bottom 50%", scrub: true },
      });
  }

  // ── big chapter numbers drift ───────────────────────────
  gsap.utils.toArray<HTMLElement>("[data-drift]").forEach((el) => {
    gsap.fromTo(el, { yPercent: 25 }, {
      yPercent: -25, ease: "none",
      scrollTrigger: { trigger: el.parentElement, start: "top bottom", end: "bottom top", scrub: true },
    });
  });

  // ── photo lines in the dark section draw on scroll ─────
  document.querySelectorAll<SVGPathElement>("[data-draw] path").forEach((p) => {
    const len = p.getTotalLength();
    gsap.fromTo(p, { strokeDasharray: len, strokeDashoffset: len }, {
      strokeDashoffset: 0, ease: "none",
      scrollTrigger: { trigger: p.closest("[data-draw]"), start: "top 80%", end: "bottom 30%", scrub: true },
    });
  });

  // ── 3D tilt on gratitude cards (fine pointers only) ─────
  if (matchMedia("(hover: hover) and (pointer: fine)").matches) {
    document.querySelectorAll<HTMLElement>("[data-tilt]").forEach((card) => {
      card.addEventListener("pointermove", (e) => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        card.style.setProperty("--ry", `${x * 10}deg`);
        card.style.setProperty("--rx", `${-y * 10}deg`);
      });
      card.addEventListener("pointerleave", () => {
        card.style.setProperty("--ry", "0deg");
        card.style.setProperty("--rx", "0deg");
      });
    });
  }

  window.addEventListener("load", () => ScrollTrigger.refresh());
}
