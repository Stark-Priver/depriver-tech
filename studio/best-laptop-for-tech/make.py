"""Carousel: the best laptop specs for tech students, from budget to serious, with brands and rough Tanzania prices
(10 slides, 1080x1350, exported at 2x). Same editorial / print direction as final-year-project-ideas. Every tier is a
shop "spec tag": tier ribbon, spec rows (CPU, RAM, storage, screen/GPU), brands to look for, and a rough price."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 10
POST_URL = "depriver.tech/blog/best-laptop-for-tech"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing

ART.update({
    "laptop": svg(GROUND + f'''
      <rect x="120" y="70" width="360" height="240" rx="16" fill="#fff" {ST}/>
      <rect x="138" y="88" width="324" height="204" rx="6" fill="#0b1e3f"/>
      <path d="M166 130 h70 M166 160 h150 M186 190 h110 M166 220 h60" stroke="#a9c4f5" stroke-width="10" stroke-linecap="round"/>
      <path d="M166 130 h26" stroke="#e8603a" stroke-width="10" stroke-linecap="round"/>
      <path d="M70 320 h460 l-30 40 H100z" fill="#c9d4ea" {ST}/>
      <g transform="translate(470 120) rotate(14)"><path d="M0 0 h110 l26 30 v120 h-136z" fill="#e8603a" {ST}/>
        <circle cx="104" cy="28" r="9" fill="#fff" {ST} stroke-width="4"/>
        <text x="58" y="88" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="22" fill="#fff">16GB</text>
        <text x="58" y="122" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="22" fill="#fff">SSD</text></g>'''),
})

TIERS = [
    ("Budget", "Learning & web", GREEN_OK, "TZS 550k – 900k", "Used / ex-UK",
     [("CPU", "Intel Core i5 8th gen+ or Ryzen 5 3000+"), ("RAM", "8GB, upgradeable to 16GB"),
      ("Storage", "256GB SSD (never a hard disk)"), ("Screen", "14\" Full HD")],
     "Lenovo ThinkPad T480 / T490 · HP EliteBook 840 G5 · Dell Latitude 7490",
     "HTML, CSS, JavaScript, Python, PHP, databases, office work"),
    ("Mid-range", "Full-stack & mobile", ORANGE, "TZS 1.2M – 2.2M", "Refurbished or new",
     [("CPU", "Core i5/i7 11th gen+ or Ryzen 5/7 5000+"), ("RAM", "16GB"),
      ("Storage", "512GB NVMe SSD"), ("Screen", "14–15.6\" Full HD IPS")],
     "ThinkPad T14 · Lenovo ThinkBook · HP ProBook 450 · Dell Latitude 5420 · ASUS Vivobook (Ryzen)",
     "Android Studio, Docker, React + backend, light design, VMs"),
    ("Serious", "AI, games & heavy work", RED_NO, "TZS 3M – 6M+", "New",
     [("CPU", "Core i7 / Ryzen 7, latest generations"), ("RAM", "32GB"),
      ("Storage", "1TB NVMe SSD"), ("GPU", "NVIDIA RTX 4050 or better")],
     "Lenovo Legion · ASUS ROG / TUF · Dell XPS / Precision · ThinkPad P",
     "Machine learning, game dev, 3D, video, many VMs at once"),
]


def spec_tag(s, box, tier):
    name, use, col, price, cond, specs, brands, good = tier
    x0, y0, x1, y1 = box
    card(s, box)
    s.d.rounded_rectangle([k(x0), k(y0), k(x1), k(y0 + 170)], radius=k(18), fill=NAVY)
    s.rect(x0, y0 + 130, x1, y0 + 170, NAVY)
    s.text(x0 + 30, y0 + 84, name, f(BOLD, 64), WHITE_T)
    s.text(x0 + 32, y0 + 134, use, f(MED, 28), SOFT)
    pw = s.width(price, f(BOLD, 30)) + 44
    s.d.rounded_rectangle([k(x1 - 28 - pw), k(y0 + 40), k(x1 - 28), k(y0 + 94)], radius=k(27), fill=col)
    s.text(x1 - 28 - pw / 2, y0 + 67, price, f(BOLD, 30), WHITE_T, anchor="mm")
    s.text(x1 - 28, y0 + 136, cond, f(SEMI, 22), SOFT, anchor="rs")
    y = y0 + 240
    for a, b in specs:
        smallcaps(s, x0 + 30, y, a, 16, ORANGE)
        s.text(x0 + 190, y + 2, b, f(SEMI, fit(s, b, SEMI, 31, x1 - x0 - 220)), NAVY)
        hairline(s, x0 + 30, x1 - 30, y + 28, RULE)
        y += 76
    smallcaps(s, x0 + 30, y + 26, "Look for", 16, GREY)
    y = s.para(x0 + 30, y + 72, brands, f(SEMI, 28), x1 - x0 - 60, 40, NAVY)
    smallcaps(s, x0 + 30, y + 18, "Good for", 16, GREY)
    s.para(x0 + 30, y + 62, good, f(REG, 27), x1 - x0 - 60, 38, GREY)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Tech students · Tanzania price guide")
s.text(M - 6, 250, "The right", f(BOLD, 104), NAVY)
s.text(M - 6, 360, "laptop for", f(BOLD, 104), NAVY)
s.text(M - 8, 490, "tech.", f(BOLD, 140), ORANGE)
s.text(M, 580, "Kuanzia bajeti mpaka kazi nzito", f(SIG, 56), NAVY)
swash(s, M + 8, M + 560, 606, ORANGE, 6)
s.para(M, 690, "Specs that matter, brands to look for, and rough prices from budget to serious.", f(REG, 27), 430, 40, GREY)
paste_print(s, print_art("laptop", k(520)), 500, 600)
sticker(s, W - M - 190, 990, "You don't need a MacBook", angle=-5, size=19, bg=NAVY)
horizon(s, 1)
cover_footer(s, "Swipe for your tier")
finish(s)
s.save(1)

# ── 2 · what matters ─────────────────────────────────────────────────────────────────────────────
s = page(2, "Specs that matter · Muhimu")
title2(s, "Four things", "actually matter.", y=230, size=84)
mats = [("SSD, not hard disk", "The biggest speed upgrade. A 5-year-old laptop with an SSD beats a new one without."),
        ("RAM", "8GB to start, 16GB for Android, Docker and VMs. Check it can be upgraded."),
        ("CPU generation", "Intel 8th gen+ or Ryzen 3000+. Avoid Celeron, Pentium and old i3s."),
        ("Battery", "Umeme ukikatika, battery ndiyo inakuokoa. Aim for 4+ hours real use.")]
numbered(s, mats, 450, gap=140, ts=35, bs=25)
horizon(s, 2)
navy_note(s, "Truth", "Brand matters less than specs and condition.", "Angalia specs, si jina", seed=2)
finish(s)
s.save(2)

# ── 3–5 · tiers ──────────────────────────────────────────────────────────────────────────────────
notes = [("Best value", "A used business laptop beats a new cheap one.", "Ex-UK ThinkPad ni rafiki"),
         ("Sweet spot", "16GB RAM is the line between waiting and working.", "16GB ni amani"),
         ("Only if", "Your work truly needs a GPU. Otherwise, save the money.", "Usinunue kwa sifa")]
for p, tier in enumerate(TIERS):
    n = p + 3
    s = page(n, f"Tier {p + 1:02d} · {tier[0]}", "Rough prices, 2026")
    spec_tag(s, (M, 160, W - M - 8, 1000), tier)
    horizon(s, n)
    navy_note(s, *notes[p], seed=n)
    finish(s)
    s.save(n)

# ── 6 · the mac question ─────────────────────────────────────────────────────────────────────────
s = page(6, "The Mac question · Swali la Mac")
title2(s, "Do you need", "a MacBook?", y=230, size=90)
s.text(M - 4, 420, "Only if...", f(BOLD, 64), ORANGE)
y = 500
for ok, a, b in [(True, "You want to build iPhone apps", "Xcode only runs on macOS."),
                 (True, "You want long battery life", "Apple M-series chips last all day."),
                 (False, "Everything else", "Web, Android, Python, data, networking all work great on Windows or Linux.")]:
    mark(s, M + 18, y - 10, ok)
    s.text(M + 56, y, a, f(BOLD, 31), NAVY)
    s.para(M + 56, y + 40, b, f(REG, 24), W - 2 * M - 60, 34, GREY)
    y += 130
card(s, (M, 900, W - M - 8, 990), r=14)
s.text(M + 30, 958, "Used MacBook Air M1, 16GB if you can: about TZS 1.4M – 2M", f(SEMI, fit(s, "Used MacBook Air M1, 16GB if you can: about TZS 1.4M – 2M", SEMI, 25, W - 2 * M - 70)), NAVY)
horizon(s, 6)
navy_note(s, "Remember", "Skills make you a developer, not the logo on the lid.", "Ujuzi kwanza", seed=6)
finish(s)
s.save(6)

# ── 7 · by track ─────────────────────────────────────────────────────────────────────────────────
s = page(7, "By track · Kwa fani yako")
title2(s, "What do you", "want to build?", y=220, size=84)
tracks = [("Web development", "8–16GB", "Budget"), ("Android apps", "16GB", "Mid-range"), ("iOS apps", "16GB, Mac", "Mac"),
          ("Data science", "16GB", "Mid-range"), ("AI / ML training", "32GB + RTX", "Serious"),
          ("Networking & cyber", "16GB (VMs)", "Mid-range"), ("UI/UX design", "16GB, good screen", "Mid-range"),
          ("Game dev & 3D", "32GB + RTX", "Serious")]
smallcaps(s, M, 410, "Track", 14, GREY)
smallcaps(s, M + 470, 410, "RAM", 14, GREY)
smallcaps(s, W - M, 410, "Tier", 14, GREY, anchor="right")
y = 470
cols = {"Budget": GREEN_OK, "Mid-range": ORANGE, "Serious": RED_NO, "Mac": NAVY}
for a, b, c in tracks:
    s.text(M, y, a, f(SEMI, 29), NAVY)
    s.text(M + 470, y, b, f(MED, 26), GREY)
    tw = s.width(c, f(BOLD, 20)) + 32
    s.d.rounded_rectangle([k(W - M - tw), k(y - 28), k(W - M), k(y + 8)], radius=k(18), fill=cols[c])
    s.text(W - M - tw / 2, y - 10, c, f(BOLD, 20), WHITE_T, anchor="mm")
    hairline(s, M, W - M, y + 22, RULE)
    y += 68
horizon(s, 7)
navy_note(s, "Not sure yet?", "Start with Budget. Upgrade when your work demands it.", "Anza na ulicho nacho", seed=7)
finish(s)
s.save(7)

# ── 8 · avoid ────────────────────────────────────────────────────────────────────────────────────
s = page(8, "Red flags · Epuka hizi")
title2(s, "Don't buy", "these.", y=230, size=96)
bad = [("Hard disk (HDD) only", "Slow forever. Or budget for an SSD swap."),
       ("4GB RAM, soldered", "Can't upgrade. Chrome alone will eat it."),
       ("Celeron, Pentium, Atom", "Fine for typing, painful for code."),
       ("Intel 2nd–6th gen", "Too old for modern tools and Windows 11."),
       ("“Gaming” looks, weak specs", "LEDs don't compile code. Check the CPU and RAM.")]
y = 440
for a, b in bad:
    mark(s, M + 18, y - 10, False)
    s.text(M + 56, y, a, f(BOLD, 31), NAVY)
    s.text(M + 56, y + 40, b, f(REG, 24), GREY)
    y += 118
horizon(s, 8)
navy_note(s, "Rule", "Read the spec sheet, not the sticker on the box.", "Usidanganywe na muonekano", seed=8)
finish(s)
s.save(8)

# ── 9 · buying used ──────────────────────────────────────────────────────────────────────────────
s = page(9, "Buying used · Kariakoo checklist")
title2(s, "Buying used?", "Check these first.", y=220, size=84)
checks = [("Battery health", "Ask to see it. Under 70% means a new battery soon."),
          ("Keyboard & ports", "Type every key. Test USB, charger and HDMI."),
          ("Screen", "Look for dead pixels and lines on a white page."),
          ("No BIOS password", "Restart and check. A locked laptop is a trap."),
          ("Real specs", "Check RAM, CPU and SSD in Settings, not the sticker."),
          ("Receipt + warranty", "Even 1–3 months. Keep the receipt.")]
y = 430
for a, b in checks:
    s.d.rounded_rectangle([k(M), k(y - 30), k(M + 34), k(y + 4)], radius=k(7), outline=NAVY, width=k(3))
    s.d.line([k(M + 7), k(y - 13), k(M + 15), k(y - 5), k(M + 28), k(y - 22)], fill=GREEN_OK, width=k(4), joint="curve")
    s.text(M + 56, y, a, f(BOLD, 30), NAVY)
    s.text(M + 56, y + 38, b, f(REG, 23), GREY)
    y += 100
horizon(s, 9)
navy_note(s, "Pro tip", "Go with a friend who knows laptops. Never pay before testing.", "Pima kabla hujalipa", seed=9)
finish(s)
s.save(9)

# ── 10 · closing ─────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What laptop are", "you coding on?", [("Save", "for when you go shopping"), ("Share", "with a classmate buying soon"),
                                               ("Comment", "your laptop and its specs")])
paste_print(s, print_art("laptop", k(380)), 640, 650)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
