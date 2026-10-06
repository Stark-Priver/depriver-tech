"""Carousel: tech gigs you can do as a student in Tanzania, with a rough price guide
(10 slides, 1080x1350, exported at 2x). Same editorial / print direction as make-your-fpt-count.
Every gig is a menu-board price list (dotted leaders, like a kibanda price list) with a mobile-money style
"payment received" notification popping in. Prices are rough ranges, labelled as such on every slide."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools
TOTAL = 10
M = 72
RULE = (200, 206, 218)
WHITE_T = (255, 255, 255)
SOFT = (190, 202, 226)
MONEY = (34, 160, 90)
POST_URL = "depriver.tech/blog/tech-gigs-for-students"
BASE = 1060

# ── print illustrations (600x420 art board, navy outlines, no faces) ─────────────────────────────
def laptop(x, y, w, h, body=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#fff" {ST}/>'
            f'<rect x="{x + 16}" y="{y + 16}" width="{w - 32}" height="{h - 32}" rx="6" fill="#0b1e3f"/>{body}'
            f'<path d="M{x - 40} {y + h + 10} h{w + 80} l-24 30 H{x - 16}z" fill="#c9d4ea" {ST}/>')


ART.update({
    "fix": svg(GROUND + laptop(120, 110, 300, 190,
        '<path d="M170 160 h90 M170 190 h150 M170 220 h70" stroke="#a9c4f5" stroke-width="9" stroke-linecap="round"/>'
        '<rect x="170" y="246" width="200" height="14" rx="7" fill="#26406c"/><rect x="170" y="246" width="130" height="14" rx="7" fill="#3ddc84"/>') + f'''
      <g transform="translate(480 200) rotate(40)"><rect x="-14" y="-20" width="28" height="160" rx="10" fill="#e8603a" {ST}/>
        <path d="M-40 -60 a40 40 0 1 0 80 0 l-18 0 l0 24 l-44 0 l0 -24z" fill="#ffc857" {ST}/></g>'''),

    "network": svg(GROUND + f'''
      <rect x="150" y="220" width="300" height="100" rx="20" fill="#0b1e3f" {ST}/>
      {"".join(f'<circle cx="{200 + i * 40}" cy="270" r="9" fill="{c}"/>' for i, c in enumerate(["#3ddc84", "#3ddc84", "#ffc857", "#3ddc84"]))}
      <path d="M380 220 V120 M220 220 V140" {ST} stroke-width="10"/>
      {"".join(f'<path d="M{300 - r} {150 - r * 0.2} a{r} {r} 0 0 1 {2 * r} 0" fill="none" stroke="#e8603a" stroke-width="10" stroke-linecap="round"/>' for r in (40, 80, 120))}
      <circle cx="300" cy="160" r="12" fill="#e8603a"/>
      <path d="M80 360 C150 330 200 340 230 320 M520 360 C450 330 400 340 370 320" fill="none" stroke="#a9c4f5" stroke-width="8" stroke-linecap="round"/>'''),

    "web": svg(GROUND + f'''
      <rect x="70" y="70" width="460" height="300" rx="18" fill="#fff" {ST}/>
      <path d="M70 120 V88 a18 18 0 0 1 18-18 h424 a18 18 0 0 1 18 18 V120z" fill="#0b1e3f" {ST}/>
      {"".join(f'<circle cx="{100 + i * 26}" cy="95" r="8" fill="{c}"/>' for i, c in enumerate(["#e8603a", "#ffc857", "#3ddc84"]))}
      <rect x="216" y="84" width="260" height="22" rx="11" fill="#26406c"/>
      <path d="M100 150 h400 l-20 40 h-360z" fill="#e8603a" {ST} stroke-width="5"/>
      <path d="M120 190 q20 22 40 0 q20 22 40 0 q20 22 40 0 q20 22 40 0 q20 22 40 0 q20 22 40 0 q20 22 40 0 q20 22 40 0" fill="#fff" {ST} stroke-width="4"/>
      <text x="300" y="180" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="22" fill="#fff">MAMA SHOP</text>
      <rect x="120" y="240" width="110" height="100" rx="10" fill="#a9c4f5" {ST} stroke-width="5"/>
      <rect x="250" y="240" width="110" height="100" rx="10" fill="#ffc857" {ST} stroke-width="5"/>
      <rect x="380" y="240" width="100" height="44" rx="22" fill="#0b1e3f"/><text x="430" y="269" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="18" fill="#fff">Order</text>'''),

    "design": svg(GROUND + f'''
      <g transform="rotate(-6 210 230)"><rect x="90" y="70" width="240" height="310" rx="10" fill="#0b1e3f" {ST}/>
        <circle cx="210" cy="170" r="60" fill="#e8603a"/><path d="M120 300 h180 M140 334 h140" stroke="#fff" stroke-width="14" stroke-linecap="round"/>
        <text x="210" y="260" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="34" fill="#ffc857">SALE</text></g>
      <g transform="rotate(8 440 230)"><rect x="350" y="110" width="180" height="260" rx="26" fill="#fff" {ST}/>
        <rect x="366" y="140" width="148" height="148" rx="6" fill="#a9c4f5"/><path d="M380 270 l40-50 l30 30 l20-20 l30 40z" fill="#fff"/>
        <path d="M376 316 h70" stroke="#c9d4ea" stroke-width="10" stroke-linecap="round"/>
        <path d="M480 316 c-8-10-22-4-16 8 l16 14 l16-14 c6-12-8-18-16-8z" fill="#e8603a"/></g>'''),

    "teach": svg(GROUND + f'''
      <rect x="70" y="60" width="380" height="250" rx="12" fill="#26406c" {ST}/>
      <rect x="70" y="300" width="380" height="20" rx="6" fill="#c9d4ea" {ST} stroke-width="5"/>
      <text x="100" y="120" font-family="Liberation Mono" font-weight="700" font-size="26" fill="#fff">=SUM(B2:B9)</text>
      <text x="100" y="170" font-family="Liberation Mono" font-weight="700" font-size="26" fill="#ffc857">print("habari")</text>
      <path d="M100 210 h160 M100 250 h220" stroke="#a9c4f5" stroke-width="8" stroke-linecap="round" opacity=".8"/>
      <g transform="translate(500 250)"><rect x="-56" y="-120" width="112" height="150" rx="8" fill="#fff" {ST}/>
        <text x="0" y="-84" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="20" fill="#0b1e3f">CV</text>
        <path d="M-36 -60 h72 M-36 -36 h56 M-36 -12 h64" stroke="#c9d4ea" stroke-width="8" stroke-linecap="round"/>
        <path d="M-36 -60 h30" stroke="#e8603a" stroke-width="8" stroke-linecap="round"/></g>'''),
})


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


def navy_note(s, label, line, sw=None, seed=0):
    smallcaps(s, M, BASE + 74, label, 16, ORANGE)
    s.text(M, BASE + 130, line, f(SEMI, fit(s, line, SEMI, 31, W - 2 * M)), WHITE_T)
    if sw:
        sws = fit(s, sw, SIG, 54, W - 2 * M - 40)
        s.text(M, BASE + 214, sw, f(SIG, sws), ORANGE)
        swash(s, M + 6, M + min(s.width(sw, f(SIG, sws)) * 0.9, 620), BASE + 238, ORANGE, 5, seed=seed)


def title2(s, a, b, y=230, size=84):
    s.text(M - 4, y, a, f(BOLD, size), NAVY)
    s.text(M - 4, y + size * 1.08, b, f(BOLD, size), ORANGE)


def card(s, box, r=18):
    x0, y0, x1, y1 = box
    s.rect(x0 + 8, y0 + 10, x1 + 8, y1 + 10, (205, 211, 224), r=r)
    s.d.rounded_rectangle([k(x0), k(y0), k(x1), k(y1)], radius=k(r), fill=(255, 255, 255), outline=NAVY, width=k(3))


def paid(s, cx, cy, amount, who, angle=-5, w=440):
    """Mobile-money style notification: 'Umepokea TZS ...' (generic, no network branding)."""
    h = 118
    w = max(w, s.width("Umepokea " + amount, f(BOLD, 27)) + 150, s.width(who + " · sasa hivi", f(REG, 19)) + 150)
    lay = Image.new("RGBA", (k(w + 40), k(h + 40)), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    ld.rounded_rectangle([k(20), k(20), k(20 + w), k(20 + h)], radius=k(22), fill=(255, 255, 255, 255), outline=NAVY + (255,), width=k(3))
    ld.ellipse([k(40), k(44), k(110), k(114)], fill=MONEY + (255,))
    ld.line([k(58), k(80), k(71), k(93), k(93), k(66)], fill=(255, 255, 255, 255), width=k(7), joint="curve")
    ld.text((k(130), k(66)), "Umepokea " + amount, font=f(BOLD, 27), fill=NAVY + (255,), anchor="ls")
    ld.text((k(130), k(100)), who + " · sasa hivi", font=f(REG, 19), fill=GREY + (255,), anchor="ls")
    lay = lay.rotate(angle, resample=Image.BICUBIC, expand=True)
    sh = lay.getchannel("A").filter(ImageFilter.GaussianBlur(k(10))).point(lambda v: v * 90 // 255)
    px, py = k(cx) - lay.width // 2, k(cy) - lay.height // 2
    s.im.paste(Image.new("RGB", lay.size, INK), (px + k(6), py + k(12)), sh)
    s.im.paste(lay, (px, py), lay)
    s.d = ImageDraw.Draw(s.im)


def price_board(s, box, rows, note="Rough guide · prices vary by city and client"):
    """Menu board: service ........ TZS range, with dotted leaders."""
    x0, y0, x1, y1 = box
    card(s, box)
    s.d.rounded_rectangle([k(x0), k(y0), k(x1), k(y0 + 64)], radius=k(18), fill=NAVY)
    s.rect(x0, y0 + 40, x1, y0 + 64, NAVY)
    smallcaps(s, x0 + 28, y0 + 42, "Price list · Bei", 16, WHITE_T)
    smallcaps(s, x1 - 28, y0 + 42, "TZS", 16, ORANGE, anchor="right")
    gap = (y1 - y0 - 64 - 60) / len(rows)
    y = y0 + 64 + gap * 0.72
    for name, price in rows:
        fn, fp = f(SEMI, 26), f(BOLD, 26)
        nw, pw = s.width(name, fn), s.width(price, fp)
        s.text(x0 + 28, y, name, fn, NAVY)
        s.text(x1 - 28, y, price, fp, ORANGE, anchor="rs")
        dx = x0 + 28 + nw + 14
        while dx < x1 - 28 - pw - 14:
            s.d.ellipse([k(dx), k(y - 6), k(dx + 3.4), k(y - 2.6)], fill=(160, 170, 190))
            dx += 11
        y += gap
    s.text(x0 + 28, y1 - 26, note, f(REG, 18), GREY)


def chips(s, x, y, items, label):
    smallcaps(s, x, y, label, 15, ORANGE)
    y += 22
    cx = x
    for j, t in enumerate(items):
        fnt = f(SEMI, 22)
        w_ = s.width(t, fnt) + 40
        if cx + w_ > W - M:
            cx, y = x, y + 62
        s.d.rounded_rectangle([k(cx), k(y), k(cx + w_), k(y + 48)], radius=k(24), fill=(255, 255, 255), outline=NAVY, width=k(2.5))
        s.text(cx + w_ / 2, y + 25, t, fnt, NAVY, anchor="mm")
        cx += w_ + 12


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For tech students · Tanzania price guide")
s.text(M - 6, 250, "Your skills", f(BOLD, 100), NAVY)
s.text(M - 6, 358, "can pay", f(BOLD, 100), NAVY)
s.text(M - 10, 500, "your rent.", f(BOLD, 140), ORANGE)
s.text(M, 600, "Ujuzi ni pesa", f(SIG, 68), NAVY)
swash(s, M + 8, M + 360, 628, ORANGE, 6)
s.para(M, 720, "5 tech gigs you can start this semester, what to charge, and how to find your first clients.",
       f(REG, 27), 440, 40, GREY)
paid(s, 790, 700, "TZS 25,000", "Laptop format, jirani", angle=-6, w=430)
paid(s, 760, 840, "TZS 350,000", "Website, Mama Shop", angle=4, w=430)
paid(s, 800, 975, "TZS 50,000", "Poster design", angle=-3, w=430)
horizon(s, 1)
s.text(M, 1262, "Swipe for the price list", f(SEMI, 30), WHITE_T)
arrow(s, M + s.width("Swipe for the price list", f(SEMI, 30)) + 34, 1251)
s.text(W - M, 1262, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(1)

# ── 2 · paid twice ───────────────────────────────────────────────────────────────────────────────
s = page(2, "The rule · Kanuni")
title2(s, "A gig pays", "you twice.", y=240, size=100)
for j, (big, sw_, body, col) in enumerate([("Pesa", "money", "Rent, data bundles, a better laptop.", ORANGE),
                                          ("Uzoefu", "experience", "Real clients, real deadlines, real CV lines.", NAVY)]):
    x0 = M + j * ((W - 2 * M) / 2 + 12)
    x1 = x0 + (W - 2 * M) / 2 - 20
    card(s, (x0, 470, x1, 860))
    s.d.ellipse([k(x0 + 30), k(500), k(x0 + 130), k(600)], fill=col)
    s.text(x0 + 80, 552, "+", f(BOLD, 60), WHITE_T, anchor="mm")
    s.text(x0 + 30, 690, big, f(BOLD, 64), col)
    s.text(x0 + 30, 740, sw_, f(SIG, 44), NAVY)
    s.para(x0 + 30, 800, body, f(REG, 22), x1 - x0 - 60, 32, GREY)
s.text(M, 950, "And every job goes straight into your portfolio.", f(SEMI, 30), NAVY)
horizon(s, 2)
navy_note(s, "Truth", "Your first clients are not online. They're around you.", "Anza na waliokuzunguka", seed=2)
finish(s)
s.save(2)

# ── 3–7 · gigs ───────────────────────────────────────────────────────────────────────────────────
GIGS = [
    ("Gig 01 · Fix & install", ("Fix laptops", "and phones."), "fix",
     "Everyone around you has a slow laptop. Formatting, installing and cleaning is the easiest first gig.",
     [("Format + install Windows", "15k – 35k"), ("Install software / Office", "5k – 20k"),
      ("Virus cleanup + speed-up", "10k – 25k"), ("Data recovery / backup", "20k – 60k")],
     ["Students", "Neighbours", "Lecturers", "Small offices"], ("TZS 25,000", "Laptop format"),
     ("Start with", "A flash drive with clean installers and drivers.", "Kazi ndogo, jina kubwa")),
    ("Gig 02 · Networks & IT support", ("Keep shops", "online."), "network",
     "Shops, schools and pharmacies need Wi-Fi, printers and PCs that work. Many pay every month.",
     [("Wi-Fi / router setup", "30k – 80k"), ("Small office network", "100k – 300k"),
      ("Printer + PC sharing", "20k – 50k"), ("Monthly IT support", "50k – 200k")],
     ["Shops", "Pharmacies", "Schools", "Guest houses"], ("TZS 120,000", "Monthly IT support"),
     ("Pro move", "Offer a monthly support plan, not one-off visits.", "Mteja wa kudumu")),
    ("Gig 03 · Websites", ("Websites for", "local business."), "web",
     "Most businesses near you have WhatsApp but no website. Start simple: one clean page that sells.",
     [("One-page business site", "150k – 400k"), ("Site with menu / catalogue", "400k – 900k"),
      ("Domain + hosting setup", "50k – 150k"), ("Monthly updates", "30k – 100k")],
     ["Restaurants", "Salons", "Churches", "Hotels"], ("TZS 350,000", "Website, Mama Shop"),
     ("Pro move", "Show a free demo of their site before they pay.", "Waonyeshe kwanza")),
    ("Gig 04 · Design & social media", ("Make brands", "look good."), "design",
     "Posters, logos and Instagram pages. If you can use Canva or Figma, someone needs you this week.",
     [("Poster / flyer", "10k – 40k"), ("Logo + simple brand", "50k – 200k"),
      ("Event or wedding card", "15k – 50k"), ("Social media page / month", "100k – 300k")],
     ["Events", "Churches", "Shops", "Student leaders"], ("TZS 50,000", "Poster design"),
     ("Pro move", "Post every design you make. Your page is your shop.", "Kazi yako ni tangazo")),
    ("Gig 05 · Teach & type", ("Teach what", "you know."), "teach",
     "Computer basics, Excel and coding classes, CVs and typing. Your class notes can become income.",
     [("Computer / Excel class", "10k – 30k / hr"), ("Coding lessons", "15k – 40k / hr"),
      ("CV design + review", "10k – 25k"), ("Typing / data entry", "1k – 2k / page")],
     ["Form Six leavers", "Job seekers", "Parents", "Small offices"], ("TZS 30,000", "Excel class"),
     ("Pro move", "Teach a small group: same hour, more people.", "Fundisha, ujifunze")),
]
for p, (label, (t1, t2), art, desc, rows, who, (amt, what), (nl, nline, nsw)) in enumerate(GIGS):
    n = p + 3
    s = page(n, label)
    title2(s, t1, t2, y=220, size=80)
    paste_print(s, print_art(art, k(330)), 690, 140)
    s.para(M, 410, desc, f(REG, 25), W - 2 * M - 10, 36, GREY)
    price_board(s, (M, 500, W - M - 8, 850), rows)
    chips(s, M, 912, who, "Who pays you")
    paid(s, W - M - 190, 506, amt, what, angle=4 if p % 2 else -4, w=400)
    horizon(s, n)
    navy_note(s, nl, nline, nsw, seed=n)
    finish(s)
    s.save(n)

# ── 8 · how to win clients ───────────────────────────────────────────────────────────────────────
s = page(8, "Getting clients · Kupata wateja")
title2(s, "Skills get the gig.", "Reliability keeps it.", y=220, size=70)
tips = [("Start local", "Friends, family, shops near campus. Tell people what you do."),
        ("Do the first jobs very well", "Even cheap ones. Your reputation is your advert."),
        ("Keep a portfolio", "Before and after photos, screenshots, thank-you messages."),
        ("Write what's included", "Agree the price and the work before you start."),
        ("Take a deposit", "50% before you start on bigger jobs like websites."),
        ("Be on time, every time", "Many people have skills. Few are reliable.")]
y = 420
for j, (a, b) in enumerate(tips):
    s.text(M, y, f"{j + 1:02d}", f(BOLD, 30), ORANGE)
    s.text(M + 70, y, a, f(BOLD, fit(s, a, BOLD, 31, W - 2 * M - 70)), NAVY)
    s.text(M + 70, y + 38, b, f(REG, fit(s, b, REG, 23, W - 2 * M - 70)), GREY)
    if j < len(tips) - 1:
        hairline(s, M + 70, W - M, y + 62, RULE)
    y += 102
horizon(s, 8)
navy_note(s, "Remember", "A happy client sends you three more.", "Mdomo kwa mdomo", seed=8)
finish(s)
s.save(8)

# ── 9 · go online + scams ────────────────────────────────────────────────────────────────────────
s = page(9, "Level up · Then go online")
title2(s, "Local first.", "Online later.", y=220, size=84)
card(s, (M, 400, W - M - 8, 640))
smallcaps(s, M + 30, 450, "Once you have 5+ real jobs to show", 15, ORANGE)
s.text(M + 30, 520, "Upwork · Fiverr · LinkedIn", f(BOLD, 40), NAVY)
s.para(M + 30, 570, "Clients abroad pay in dollars, but they hire people with proof. Build it locally first.",
       f(REG, 23), W - 2 * M - 80, 33, GREY)
s.d.rounded_rectangle([k(M), k(680), k(W - M - 8), k(960)], radius=k(18), fill=NAVY)
smallcaps(s, M + 30, 730, "Scam alert · Tahadhari", 15, ORANGE)
s.text(M + 30, 800, "Pay to get a job? = SCAM.", f(BOLD, 44), WHITE_T)
for j, t in enumerate(["No real client asks for a “registration fee”.", "Never send money to unlock an online job.",
                       "Betting and forex are not side hustles."]):
    yy = 856 + j * 36
    s.d.line([k(M + 32), k(yy - 16), k(M + 46), k(yy - 2)], fill=ORANGE, width=k(3.5))
    s.d.line([k(M + 46), k(yy - 16), k(M + 32), k(yy - 2)], fill=ORANGE, width=k(3.5))
    s.text(M + 62, yy, t, f(MED, 23), SOFT)
horizon(s, 9)
navy_note(s, "Remember", "Real work pays you. Scams ask you to pay.", "Usitapeliwe", seed=9)
finish(s)
s.save(9)

# ── 10 · closing ─────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
s.text(M - 6, 290, "Your turn.", f(BOLD, 112), NAVY)
s.text(M, 380, "Which gig will you", f(BOLD, 50), ORANGE)
s.text(M, 444, "start this month?", f(BOLD, 50), ORANGE)
s.text(M, 540, "Niambie kwenye comments", f(SIG, 52), ORANGE)
swash(s, M + 6, M + 440, 566, ORANGE, 5, seed=10)
rows = [("Save", "for when someone asks “unaweza?”"), ("Share", "with a classmate who needs cash"), ("Comment", "your gig and your price")]
y = 680
for j, (a, b) in enumerate(rows):
    s.text(M, y, f"{j + 1:02d}", f(BOLD, 22), ORANGE)
    s.text(M + 56, y, a, f(BOLD, 36), NAVY)
    s.text(M + 56, y + 40, b, f(REG, 24), GREY)
    y += 108
paid(s, 815, 690, "TZS 150,000", "Your first client", angle=-5, w=400)
paid(s, 810, 845, "TZS 300,000", "Their friend", angle=4, w=400)
horizon(s, TOTAL)
smallcaps(s, M, BASE + 72, "Read the full post · Soma zaidi", 17, SOFT)
s.text(M, BASE + 132, POST_URL, f(BOLD, fit(s, POST_URL, BOLD, 40, W - 2 * M)), WHITE_T)
hairline(s, M, W - M, BASE + 162, (38, 60, 100))
s.text(M, BASE + 224, "Link in bio", f(SEMI, 24), SOFT)
s.text(W - M, BASE + 224, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(TOTAL)
print("ok")
