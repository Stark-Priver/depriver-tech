"""Carousel: Techtember, what September taught me + what's loading for October (9 slides, 1080x1350, exported at 2x).
Same editorial / print direction as tech-advice-i-learnt-the-hard-way (panorama paper, navy wave, seam badges,
outlined numerals, print art, swashes, stickers), with a lighter, funnier voice. The photo appears as a taped polaroid."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools
TOTAL = 9
M = 72
RULE = (200, 206, 218)
WHITE_T = (255, 255, 255)
SOFT = (190, 202, 226)
SNAP = os.path.join(STUDIO, "assets", "techtember.jpg")
POST_URL = "depriver.tech/blog/techtember"

# ── print illustrations for this deck (600x420 art board, navy outlines, no faces) ──────────────
ART.update({
    "offline": svg(GROUND + f'''
      <path d="M380 120 a46 46 0 0 1 88-14 a38 38 0 0 1 52 44 a30 30 0 0 1-14 58 H388 a40 40 0 0 1-8-88z" fill="#fff" {ST}/>
      <path d="M430 138 l40 40 M470 138 l-40 40" stroke="#e8603a" stroke-width="10" stroke-linecap="round"/>
      <rect x="180" y="70" width="150" height="300" rx="26" fill="#0b1e3f" {ST}/>
      <rect x="194" y="104" width="122" height="220" rx="10" fill="#e7ecf6"/>
      <g fill="#c9d4ea" {ST} stroke-width="4"><rect x="210" y="140" width="14" height="16" rx="3" fill="#e8603a"/>
        <rect x="232" y="128" width="14" height="28" rx="3"/><rect x="254" y="116" width="14" height="40" rx="3"/><rect x="276" y="104" width="14" height="52" rx="3"/></g>
      <rect x="208" y="190" width="94" height="22" rx="6" fill="#a9c4f5"/><rect x="208" y="224" width="70" height="22" rx="6" fill="#a9c4f5"/>
      <rect x="208" y="268" width="94" height="36" rx="10" fill="#e8603a"/>
      <path d="M236 286 h38" stroke="#fff" stroke-width="7" stroke-linecap="round"/>
      <g transform="translate(110 290)"><circle r="44" fill="#ffc857" {ST}/>
        <path d="M-20-6 a22 22 0 0 1 38-10 M20 6 a22 22 0 0 1-38 10" fill="none" {ST} stroke-width="6"/>
        <path d="M18-28 v14 h-14 M-18 28 v-14 h14" fill="none" {ST} stroke-width="6"/></g>'''),

    "twins": svg(GROUND + f'''
      {"".join(f'<g transform="translate({120 + i * 64} {60 + i * 44})"><rect width="230" height="170" rx="16" fill="{c}" {ST}/><circle cx="44" cy="48" r="20" fill="#a9c4f5" {ST} stroke-width="4"/><path d="M80 40 h110 M80 62 h70 M28 104 h170 M28 130 h120" stroke="#c9d4ea" stroke-width="10" stroke-linecap="round"/></g>' for i, c in enumerate(["#fff", "#fff", "#fff"]))}
      <rect x="248" y="148" width="230" height="170" rx="16" fill="none" stroke="#e8603a" stroke-width="7" stroke-dasharray="16 12"/>
      <g transform="translate(470 330)"><rect x="-70" y="-30" width="140" height="60" rx="16" fill="#e8603a" {ST}/>
        <text x="0" y="12" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="30" fill="#fff">SAVE</text></g>
      <path d="M520 360 l0 50 l12-12 l14 26 l12-6 l-14-26 l18-2z" fill="#fff" {ST} stroke-width="5"/>
      <text x="80" y="60" font-family="Poppins" font-weight="700" font-size="44" fill="#e8603a">x3</text>'''),

    "verify": svg(GROUND + f'''
      <rect x="90" y="60" width="400" height="290" rx="20" fill="#fff" {ST}/>
      <path d="M90 116 V80 a20 20 0 0 1 20-20 h360 a20 20 0 0 1 20 20 v36z" fill="#0b1e3f" {ST}/>
      <g fill="#fff"><circle cx="122" cy="88" r="8"/><circle cx="148" cy="88" r="8"/><circle cx="174" cy="88" r="8"/></g>
      <rect x="210" y="76" width="250" height="24" rx="12" fill="#a9c4f5"/>
      <rect x="120" y="146" width="150" height="110" rx="12" fill="#e7ecf6" {ST} stroke-width="4"/>
      <path d="M300 160 h150 M300 190 h110 M300 220 h140 M120 292 h200" stroke="#c9d4ea" stroke-width="12" stroke-linecap="round"/>
      <g transform="translate(470 320)"><circle r="66" fill="#e8603a" {ST}/><path d="M-28 2 l18 20 l36-40" fill="none" stroke="#fff" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></g>'''),

    "details": svg(GROUND + f'''
      <rect x="90" y="70" width="300" height="300" rx="18" fill="#fff" {ST}/>
      <rect x="90" y="70" width="300" height="56" rx="18" fill="#a9c4f5" {ST}/>
      <path d="M120 170 h120 M120 220 h180 M120 270 h150 M120 320 h90" stroke="#c9d4ea" stroke-width="12" stroke-linecap="round"/>
      <text x="270" y="178" font-family="Poppins" font-weight="700" font-size="26" fill="#e8603a">#48213</text>
      <g transform="translate(400 230)"><circle r="92" fill="#fff" fill-opacity=".55" {ST} stroke-width="10"/>
        <text x="0" y="12" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="40" fill="#e8603a">#48213</text>
        <path d="M-70 4 h140" stroke="#0b1e3f" stroke-width="6" opacity=".8"/>
        <path d="M66 66 l70 70" stroke="#0b1e3f" stroke-width="26" stroke-linecap="round"/></g>
      <text x="420" y="80" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="48" fill="#0b1e3f">??</text>'''),

    "map": svg(GROUND + f'''
      <path d="M70 110 L200 70 L330 110 L460 70 V330 L330 370 L200 330 L70 370Z" fill="#e7ecf6" {ST}/>
      <path d="M200 70 V330 M330 110 V370" {ST} fill="none" stroke-width="5"/>
      <path d="M100 300 C160 250 220 280 260 220 S360 160 430 130" fill="none" stroke="#a9c4f5" stroke-width="12" stroke-linecap="round" stroke-dasharray="2 22"/>
      <path d="M260 230 c-34-40-34-64-34-74 a34 34 0 0 1 68 0 c0 10 0 34-34 74z" fill="#e8603a" {ST} stroke-width="5"/>
      <circle cx="260" cy="156" r="12" fill="#fff" {ST} stroke-width="4"/>
      <g transform="translate(470 290)"><circle r="68" fill="#fff" {ST} stroke-width="8"/><circle r="52" fill="none" stroke="#e8603a" stroke-width="14"/>
        <path d="M-36 36 L36-36" stroke="#e8603a" stroke-width="14" stroke-linecap="round"/></g>
      <text x="470" y="200" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="26" fill="#0b1e3f">429</text>'''),

    "patience": svg(GROUND + f'''
      <path d="M60 330 h330 l34 40 H26z" fill="#c9d4ea" {ST}/>
      <rect x="84" y="120" width="282" height="210" rx="16" fill="#fff" {ST}/>
      <rect x="104" y="140" width="242" height="170" rx="8" fill="#0b1e3f"/>
      <path d="M200 170 h50 l-20 34 l20 34 h-50 l20-34z" fill="#ffc857" stroke="#fff" stroke-width="5" stroke-linejoin="round"/>
      <rect x="140" y="268" width="170" height="16" rx="8" fill="#26406c"/><rect x="140" y="268" width="40" height="16" rx="8" fill="#e8603a"/>
      <rect x="430" y="170" width="96" height="190" rx="22" fill="#c9d4ea" {ST}/>
      <rect x="422" y="150" width="112" height="40" rx="12" fill="#0b1e3f" {ST}/>
      <path d="M440 240 h76" stroke="#fff" stroke-width="8" stroke-linecap="round"/>
      <path d="M460 120 q-14-20 0-40 M496 120 q-14-20 0-40" fill="none" stroke="#a9c4f5" stroke-width="7" stroke-linecap="round"/>'''),
})

LESSONS = [
    ("offline", "No network?", "No problem.", "Bila mtandao, kazi inaendelea",
     "Users don't live next to the Wi-Fi router. If your app panics at one bar of signal, so will they.",
     ["Save on the device first", "Sync when the signal comes back", "Test with airplane mode ON"]),
    ("twins", "Click twice,", "save once.", "Bonyeza mara moja tu",
     "Weak network + impatient thumb = three copies of the same record. Your database never asked for triplets.",
     ["Give every record its ID early", "Make retries safe to repeat", "Disable the button while saving"]),
    ("verify", "Deployed", "is not done.", "Usiamini, hakikisha",
     "“It works on my machine” is not a release note. Open the live app and check it yourself.",
     ["Check the live version number", "Click through the main flows", "Only then start the next task"]),
    ("details", "Users notice", "tiny things.", "Vitu vidogo vina maana",
     "A report that says “#48213” instead of a real name? That's how trust quietly leaves the chat.",
     ["Show readable codes, not raw IDs", "Read your reports like a user", "Fix the small stuff first"]),
    ("map", "Free tools", "have rules too.", "Bure si bure kila mara",
     "Monday the map loads. Tuesday: blocked. Free services have usage policies, and yes, they enforce them.",
     ["Read the terms before you ship", "Keep a plan B provider ready", "Cache what you can"]),
    ("patience", "My laptop and I", "need to talk.", "Subira huvuta heri",
     "Every build felt like waiting for ugali on a tiny fire. Slow tools taught me patience, and better planning.",
     ["Batch your builds and tests", "Let CI do the heavy lifting", "Save up for better tools"]),
]
assert len(LESSONS) + 3 == TOTAL
BASE = 1060


def page(n, label_left, label_right="depriver.tech"):
    s = Slide()
    panorama_paper(s, n, TOTAL)
    smallcaps(s, M, 96, label_left, 17, ORANGE)
    s.text(W - M, 96, label_right, f(SEMI, 20), NAVY, anchor="rs")
    hairline(s, M, W - M, 118, RULE)
    return s


def horizon(s, n):
    navy_wave(s, n, BASE)
    seam_nodes(s, n, TOTAL, BASE)


def arrow(s, x, y, color=WHITE_T, w=3.4, size=12):
    s.d.line([k(x - size - 6), k(y), k(x + size - 2), k(y)], fill=color, width=k(w))
    s.d.line([k(x), k(y - size + 2), k(x + size - 2), k(y), k(x), k(y + size - 2)], fill=color, width=k(w), joint="curve")


def polaroid(s, cx, cy, width, angle, caption, cap_size=40):
    """The photo as a printed polaroid, taped on at a slight angle, with a handwritten caption."""
    pw = k(width - 44)
    ph = int(pw * 1.12)
    src = Image.open(SNAP).convert("RGB")
    src = ImageOps.fit(src, (pw, ph), Image.LANCZOS, centering=(0.5, 0.32))
    src = ImageEnhance.Color(src).enhance(0.86)
    src = ImageEnhance.Contrast(src).enhance(1.06)
    src = grain(src, 0.06)
    pad, foot = k(22), k(cap_size * 2.4)
    card = Image.new("RGBA", (pw + 2 * pad, ph + pad + foot), (252, 251, 247, 255))
    card.paste(src, (pad, pad))
    cd = ImageDraw.Draw(card)
    cd.text((card.width // 2, ph + pad + foot // 2 + k(6)), caption, font=f(SIG, cap_size), fill=NAVY + (255,), anchor="mm")
    for tx in (0.2, 0.8):                                      # two strips of tape
        tape = Image.new("RGBA", (k(110), k(34)), (233, 214, 160, 190))
        tape = tape.rotate(-14 if tx < 0.5 else 12, resample=Image.BICUBIC, expand=True)
        card.alpha_composite(tape, (int(card.width * tx) - tape.width // 2, -k(4)))
    big = Image.new("RGBA", (card.width + k(60), card.height + k(60)), (0, 0, 0, 0))
    big.paste(card, (k(30), k(30)))
    big = big.rotate(angle, resample=Image.BICUBIC, expand=True)
    sh = big.getchannel("A").filter(ImageFilter.GaussianBlur(k(12))).point(lambda v: v * 80 // 255)
    px, py = k(cx) - big.width // 2, k(cy) - big.height // 2
    s.im.paste(Image.new("RGB", big.size, INK), (px + k(10), py + k(16)), sh)
    s.im.paste(big, (px, py), big)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Monthly recap · September 2026")
size = fit(s, "Techtember", BOLD, 170, W - 2 * M)
s.text(M - 8, 300, "Techtember", f(BOLD, size), NAVY)
s.text(M - 4, 400, "was a whole movie.", f(BOLD, 76), ORANGE)
s.text(M, 486, "Septemba imenifundisha mengi", f(SIG, 58), ORANGE)
swash(s, M + 10, M + 520, 514, ORANGE, 6)
s.para(M, 600, "6 lessons I learnt the funny way, plus what's loading for October.", f(REG, 28), 380, 42, GREY)
horizon(s, 1)
polaroid(s, 770, 820, 440, -4, "me vs. bugs, sept '26")
sticker(s, 230, 860, "Oktoba loading...", angle=-7, size=22)
s.text(M, 1262, "Swipe for the lessons", f(SEMI, 30), WHITE_T)
arrow(s, M + s.width("Swipe for the lessons", f(SEMI, 30)) + 34, 1251)
finish(s)
s.save(1)

# ── 2–7 · lessons ────────────────────────────────────────────────────────────────────────────────
for i, (art_key, t1, t2, sw, body, todo) in enumerate(LESSONS):
    n = i + 2
    s = page(n, f"Lesson {i + 1:02d} / 06")
    outline_text(s, W - M + 20, 590, f"{i + 1:02d}", f(BOLD, 380), stroke=3, color=RULE, anchor="rs")
    art = print_art(art_key, k(640))
    paste_print(s, art, 50, 150)

    size = min(fit(s, t1, BOLD, 88, W - 2 * M), fit(s, t2, BOLD, 88, W - 2 * M))
    s.text(M - 4, 730, t1, f(BOLD, size), NAVY)
    s.text(M - 4, 730 + size * 1.02, t2, f(BOLD, size), ORANGE)
    sy = 730 + size * 1.02 + 70
    sws = fit(s, sw, SIG, 56, W - 2 * M - 40)
    s.text(M, sy, sw, f(SIG, sws), ORANGE)
    swash(s, M + 6, M + min(s.width(sw, f(SIG, sws)) * 0.9, 620), sy + 24, ORANGE, 5, seed=i)
    s.para(M, sy + 60, body, f(REG, 25), 760, 36, GREY)

    horizon(s, n)
    sticker(s, W - M - 150, wave_y((n - 1) * W + W - M - 150) - 4, "Kiswahili", angle=-6, size=20)
    smallcaps(s, M, BASE + 72, "Fanya hivi · Do this", 16, ORANGE)
    for j, t in enumerate(todo):
        y = BASE + 122 + j * 62
        s.text(M, y, f"{j + 1:02d}", f(BOLD, 22), ORANGE)
        s.text(M + 56, y, t, f(MED, 27), WHITE_T)
        if j < len(todo) - 1:
            hairline(s, M, W - M, y + 26, (38, 60, 100))
    finish(s)
    s.save(n)

# ── 8 · October ──────────────────────────────────────────────────────────────────────────────────
s = page(8, "Next episode · Oktoba")
s.text(M - 6, 270, "October", f(BOLD, 120), NAVY)
s.text(M - 6, 384, "is loading...", f(BOLD, 104), ORANGE)
bx0, by, bx1 = M, 450, W - M                                  # loading bar: day 1 of 31
s.rect(bx0, by, bx1, by + 34, NAVY, r=17)
s.rect(bx0 + 5, by + 5, bx1 - 5, by + 29, PAPER, r=12)
s.rect(bx0 + 5, by + 5, bx0 + 5 + (bx1 - bx0 - 10) / 31, by + 29, ORANGE, r=12)
smallcaps(s, M, by + 76, "Day 01 / 31", 16, NAVY)
smallcaps(s, W - M, by + 76, "Please don't refresh", 16, GREY, anchor="right")
items = [("Real people test what I built", "be gentle, please"),
         ("Old data moves to its new home", "no record left behind"),
         ("Finish what I started", "yes, all of it"),
         ("Start a brand-new app", "the fun part"),
         ("Write the docs", "I promise. Hold me to it.")]
y = 600
for j, (a, b) in enumerate(items):
    s.d.rounded_rectangle([k(M), k(y - 30), k(M + 34), k(y + 4)], radius=k(7), outline=NAVY, width=k(3))
    s.text(M + 56, y, a, f(SEMI, 32), NAVY)
    s.text(M + 56 + s.width(a, f(SEMI, 32)) + 18, y + 4, b, f(SIG, 38), ORANGE)
    if j < len(items) - 1:
        hairline(s, M, W - M, y + 32, RULE)
    y += 82
horizon(s, 8)
smallcaps(s, M, BASE + 72, "Coming soon to a feed near you", 17, SOFT)
s.text(M, BASE + 138, "Follow along, one commit at a time.", f(SEMI, 34), WHITE_T)
s.text(W - M, BASE + 224, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
sticker(s, 900, 230, "Sasa ni zamu ya Oktoba", angle=6, size=20)
finish(s)
s.save(8)

# ── 9 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
s.text(M - 6, 290, "Your turn.", f(BOLD, 112), NAVY)
s.para(M, 380, "What did your Techtember teach you?", f(BOLD, 52), 520, 64, ORANGE)
s.text(M, 560, "Niambie kwenye comments", f(SIG, 52), ORANGE)
swash(s, M + 6, M + 440, 586, ORANGE, 5, seed=9)
rows = [("Save", "for October"), ("Share", "with your dev friend"), ("Comment", "your lesson")]
y = 680
for j, (a, b) in enumerate(rows):
    s.text(M, y, f"{j + 1:02d}", f(BOLD, 22), ORANGE)
    s.text(M + 56, y, a, f(BOLD, 36), NAVY)
    s.text(M + 56, y + 40, b, f(REG, 24), GREY)
    y += 108
polaroid(s, 800, 760, 380, 5, "tell me below!", cap_size=36)
horizon(s, TOTAL)
smallcaps(s, M, BASE + 72, "Read the full post · Soma zaidi", 17, SOFT)
s.text(M, BASE + 132, POST_URL, f(BOLD, fit(s, POST_URL, BOLD, 40, W - 2 * M)), WHITE_T)
hairline(s, M, W - M, BASE + 162, (38, 60, 100))
s.text(M, BASE + 224, "Questions? Ask my AI assistant", f(REG, 24), SOFT)
s.text(M + s.width("Questions? Ask my AI assistant", f(REG, 24)) + 18, BASE + 228, "viora", f(SIG, 52), ORANGE)
s.text(W - M, BASE + 224, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(TOTAL)
print("ok")
