"""Carousel: your student ID is worth millions, the free tools every tech student should claim before graduation
(10 slides, 1080x1350, exported at 2x). Same editorial / print direction as darasani-vs-kazini (panorama paper,
navy wave, seam badges, print art, swashes, stickers). Every perk is a perforated coupon ticket, and slide 8 is
a till receipt that adds them all up to TZS 0.00."""
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
POST_URL = "depriver.tech/blog/free-tools-for-students"
BASE = 1060
MONO, MONO_B = "LiberationMono-Regular.ttf", "LiberationMono-Bold.ttf"

# ── print illustrations (600x420 art board, navy outlines, no faces) ─────────────────────────────
BARS = "".join(f'<rect x="{x}" y="0" width="{w}" height="46" fill="#0b1e3f"/>' for x, w in
               [(0, 4), (8, 2), (13, 6), (22, 2), (27, 3), (34, 6), (43, 2), (48, 4), (56, 2), (61, 6), (70, 3), (76, 2), (81, 5), (90, 2), (95, 4)])

ART.update({
    # student ID card with a price tag hanging off it
    "idcard": svg(GROUND + f'''
      <g transform="rotate(-7 260 230)">
        <rect x="70" y="90" width="380" height="250" rx="22" fill="#fff" {ST}/>
        <path d="M70 150 V112 a22 22 0 0 1 22-22 h336 a22 22 0 0 1 22 22 V150z" fill="#0b1e3f" {ST}/>
        <text x="96" y="132" font-family="Poppins" font-weight="700" font-size="26" fill="#fff" letter-spacing="4">STUDENT</text>
        <circle cx="414" cy="120" r="12" fill="#e8603a"/>
        <rect x="96" y="176" width="110" height="130" rx="10" fill="#a9c4f5" {ST} stroke-width="5"/>
        <circle cx="151" cy="226" r="26" fill="#0b1e3f"/><path d="M106 306 c0-46 90-46 90 0z" fill="#0b1e3f"/>
        <path d="M232 192 h150 M232 226 h110 M232 260 h130" stroke="#c9d4ea" stroke-width="13" stroke-linecap="round"/>
        <path d="M232 192 h60" stroke="#e8603a" stroke-width="13" stroke-linecap="round"/>
        <g transform="translate(232 282)">{BARS}</g>
      </g>
      <path d="M440 120 C480 110 500 130 506 160" fill="none" {ST} stroke-width="4"/>
      <g transform="rotate(14 520 230)">
        <path d="M478 160 h84 l28 34 v120 h-140 v-120z" fill="#e8603a" {ST}/>
        <circle cx="520" cy="190" r="10" fill="#fff" {ST} stroke-width="4"/>
        <text x="520" y="252" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="30" fill="#fff">TZS</text>
        <text x="520" y="296" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="44" fill="#fff">0</text>
      </g>'''),

    # calendar with graduation day circled, and an hourglass running out
    "expiry": svg(GROUND + f'''
      <rect x="60" y="80" width="300" height="290" rx="18" fill="#fff" {ST}/>
      <path d="M60 150 V98 a18 18 0 0 1 18-18 h264 a18 18 0 0 1 18 18 V150z" fill="#e8603a" {ST}/>
      <path d="M120 60 v44 M300 60 v44" {ST} stroke-width="10"/>
      {"".join(f'<rect x="{88 + (i % 5) * 52}" y="{172 + (i // 5) * 48}" width="36" height="32" rx="6" fill="{"#c9d4ea" if i != 13 else "#fff"}"/>' for i in range(20))}
      <path d="M118 302 l24 24 M142 302 l-24 24 M170 302 l24 24 M194 302 l-24 24" stroke="#0b1e3f" stroke-width="5" stroke-linecap="round" opacity=".5"/>
      <ellipse cx="262" cy="270" rx="40" ry="32" fill="none" stroke="#e8603a" stroke-width="7" transform="rotate(-8 262 270)"/>
      <g transform="translate(470 230)">
        <path d="M-70-150 h140 M-70 150 h140" {ST} stroke-width="14"/>
        <path d="M-56-140 C-56-60 -10-30 -10 0 C-10 30 -56 60 -56 140 H56 C56 60 10 30 10 0 C10-30 56-60 56-140z" fill="#fff" fill-opacity=".85" {ST}/>
        <path d="M-30-80 C-18-50 -4-30 0-14 C4-30 18-50 30-80z" fill="#ffc857"/>
        <path d="M0 0 V110" stroke="#ffc857" stroke-width="4" stroke-dasharray="2 8" stroke-linecap="round"/>
        <path d="M-50 136 C-40 96 40 96 50 136z" fill="#ffc857" {ST} stroke-width="4"/>
      </g>'''),

    # three steps: email, ID photo on a phone, browser "students" page
    "claim": svg(GROUND + f'''
      <rect x="40" y="110" width="210" height="150" rx="14" fill="#fff" {ST}/>
      <path d="M40 124 L145 200 L250 124" fill="none" {ST}/>
      <text x="145" y="296" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="22" fill="#0b1e3f">@must.ac.tz</text>
      <rect x="300" y="60" width="150" height="290" rx="24" fill="#0b1e3f" {ST}/>
      <rect x="316" y="92" width="118" height="210" rx="8" fill="#a9c4f5"/>
      <rect x="328" y="150" width="94" height="64" rx="8" fill="#fff" {ST} stroke-width="4"/>
      <circle cx="350" cy="176" r="10" fill="#0b1e3f"/><path d="M372 172 h40 M372 192 h28" stroke="#c9d4ea" stroke-width="7" stroke-linecap="round"/>
      <circle cx="375" cy="326" r="10" fill="#fff"/>
      <g transform="translate(500 210)"><circle r="62" fill="#3ddc84" {ST}/>
        <path d="M-26 2 l18 18 l34-38" fill="none" stroke="#0b1e3f" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/></g>'''),
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


def ticket(s, box, stub=150, fill=(255, 255, 255), stub_fill=ORANGE, r=18, notch=17):
    """Coupon ticket: navy outline, notches cut at the perforation, coloured stub on the left, offset ink shadow.
    Returns the x where the main part starts."""
    x0, y0, x1, y1 = box
    px = x0 + stub
    shape = Image.new("L", s.im.size, 0)
    d = ImageDraw.Draw(shape)
    d.rounded_rectangle([k(x0), k(y0), k(x1), k(y1)], radius=k(r), fill=255)
    for cy in (y0, y1):
        d.ellipse([k(px - notch), k(cy - notch), k(px + notch), k(cy + notch)], fill=0)
    edge = shape.filter(ImageFilter.MaxFilter(7))
    s.im.paste(Image.new("RGB", s.im.size, INK), (k(8), k(10)), edge.point(lambda v: v * 40 // 255))
    s.im.paste(Image.new("RGB", s.im.size, NAVY), (0, 0), edge)
    s.im.paste(Image.new("RGB", s.im.size, fill), (0, 0), shape)
    stub_mask = Image.new("L", s.im.size, 0)
    ImageDraw.Draw(stub_mask).rectangle([0, 0, k(px), s.im.height], fill=255)
    s.im.paste(Image.new("RGB", s.im.size, stub_fill), (0, 0), ImageChops.multiply(shape, stub_mask))
    s.d = ImageDraw.Draw(s.im)
    y = y0 + notch + 8
    while y < y1 - notch - 8:  # perforation
        s.d.line([k(px), k(y), k(px), k(y + 7)], fill=NAVY, width=k(3))
        y += 15
    return px


def stub_text(s, px, box, top, bottom, color=WHITE_T):
    """Rotated words on the stub: big top line, small bottom line."""
    x0, y0, x1, y1 = box
    h, w = y1 - y0, px - x0
    lay = Image.new("RGBA", (k(h), k(w)), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    big = f(BOLD, min(44, w * 0.34))
    ld.text((k(h / 2), k(w * 0.47)), top, font=big, fill=color, anchor="mm")
    ld.text((k(h / 2), k(w * 0.78)), bottom.upper(), font=f(SEMI, 13), fill=color, anchor="mm")
    lay = lay.rotate(90, expand=True)
    s.im.paste(lay, (k(x0), k(y0)), lay)


def perk(s, box, name, gets, where, claim, stub="FREE", stub_small="for students", stub_fill=ORANGE, hero=False):
    x0, y0, x1, y1 = box
    px = ticket(s, box, stub=150 if not hero else 170, stub_fill=stub_fill)
    stub_text(s, px, box, stub, stub_small)
    tx, tw = px + 34, x1 - px - 60
    if hero:
        s.text(tx, y0 + 70, name, f(BOLD, fit(s, name, BOLD, 40, tw)), NAVY)
        y = y0 + 126
        for g in gets:
            s.d.ellipse([k(tx), k(y - 15), k(tx + 12), k(y - 3)], fill=ORANGE)
            s.text(tx + 28, y, g, f(MED, fit(s, g, MED, 26, tw - 28)), NAVY)
            y += 46
        hairline(s, tx, x1 - 30, y - 6, RULE)
        smallcaps(s, tx, y + 36, "Claim at", 13, GREY)
        s.text(tx + 110, y + 38, where, f(BOLD, 26), ORANGE)
        s.text(tx, y + 80, claim, f(REG, fit(s, claim, REG, 21, tw)), GREY)
    else:
        s.text(tx, y0 + 56, name, f(BOLD, fit(s, name, BOLD, 32, tw)), NAVY)
        s.text(tx, y0 + 98, gets, f(MED, fit(s, gets, MED, 23, tw)), NAVY)
        s.text(tx, y0 + 136, claim, f(REG, fit(s, claim, REG, 20, tw)), GREY)
        hairline(s, tx, x1 - 30, y0 + 156, RULE)
        s.text(tx, y0 + 194, where, f(BOLD, fit(s, where, BOLD, 23, tw)), ORANGE)


def title2(s, a, b, y=230, size=88):
    s.text(M - 4, y, a, f(BOLD, size), NAVY)
    s.text(M - 4, y + size * 1.08, b, f(BOLD, size), ORANGE)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For every tech student")
s.text(M - 6, 250, "Your student ID", f(BOLD, 92), NAVY)
s.text(M - 6, 350, "is worth", f(BOLD, 92), NAVY)
s.text(M - 10, 500, "millions.", f(BOLD, 158), ORANGE)
s.text(M, 600, "Usiache bure", f(SIG, 70), NAVY)
swash(s, M + 8, M + 330, 628, ORANGE, 6)
s.para(M, 710, "Free pro tools, cloud credits and courses that big tech gives students. Most never claim them.",
       f(REG, 27), 430, 40, GREY)
paste_print(s, print_art("idcard", k(560)), 480, 560)
horizon(s, 1)
sticker(s, W - M - 200, 990, "Expires on graduation day", angle=-5, size=20, bg=NAVY)
s.text(M, 1262, "Swipe to claim yours", f(SEMI, 30), WHITE_T)
arrow(s, M + s.width("Swipe to claim yours", f(SEMI, 30)) + 34, 1251)
s.text(W - M, 1262, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(1)

# ── 2 · the catch ────────────────────────────────────────────────────────────────────────────────
s = page(2, "The catch · Tahadhari")
paste_print(s, print_art("expiry", k(430)), 600, 150)
title2(s, "Free.", "For now.", y=300, size=118)
s.text(M, 530, "Muda unakwisha", f(SIG, 58), NAVY)
swash(s, M + 6, M + 380, 556, ORANGE, 5, seed=2)
y = s.para(M, 660, "These deals only work while you have a valid uni email or student ID. "
           "The day you graduate, most of them switch off.", f(MED, 30), W - 2 * M, 44, NAVY)
s.para(M, y + 20, "Most students find out in their final year, or after. Claim them in first year and you get three years of free tools.",
       f(REG, 26), W - 2 * M, 38, GREY)
horizon(s, 2)
sticker(s, W - M - 150, wave_y(W + W - M - 150) - 4, "Clock is ticking", angle=-6, size=20)
navy_note(s, "Quick maths", "Claim early = more years of free tools.", "Anza leo, si kesho", seed=2)
finish(s)
s.save(2)

# ── 3 · the big one ──────────────────────────────────────────────────────────────────────────────
s = page(3, "Coupon 01 · The big one")
title2(s, "Start with", "this one.", y=220, size=92)
s.text(W - M, 300, "Kifurushi kikubwa", f(SIG, 54), NAVY, anchor="rs")
swash(s, W - M - 360, W - M - 10, 324, ORANGE, 5, seed=3)
perk(s, (M, 400, W - M - 8, 900), "GitHub Student Developer Pack",
     ["GitHub Copilot Pro, free", "A free domain name for a year", "Cloud credits to host your projects",
      "Dozens of paid developer tools"],
     "education.github.com/pack", "Verify with your uni email or a photo of your student ID.",
     stub="FREE", stub_small="worth the most", hero=True)
sticker(s, W - M - 120, 900, "Claim first", angle=-6, size=22, bg=NAVY)
horizon(s, 3)
navy_note(s, "Why first?", "Some deals on this list also come through the pack.", "Moja, mengi ndani", seed=3)
finish(s)
s.save(3)

# ── 4–6 · coupons ────────────────────────────────────────────────────────────────────────────────
GROUPS = [
    ("Coupon 02 · Build like a pro", ("Pro tools", "for zero shillings."), [
        ("JetBrains IDEs", "IntelliJ, PyCharm, WebStorm, all of them", "Free licence with your uni email, renew yearly",
         "jetbrains.com/student"),
        ("Figma Education", "Pro design tools for UI and prototypes", "Verify your student status in Figma",
         "figma.com/education"),
        ("Notion for students", "Free Education Plan: unlimited pages & uploads", "Sign up with your uni email, verify yearly",
         "notion.com/students")],
     ("Do this", "Build your next project with the same tools pros use.", "Zana za kitaalamu, bure", NAVY)),
    ("Coupon 03 · Cloud & office", ("Your own", "cloud, free."), [
        ("Azure for Students", "$100 in credits, renewed every year", "No credit card needed, just your uni email",
         "azure.microsoft.com/free/students"),
        ("Microsoft 365", "Word, Excel, PowerPoint, OneDrive", "Free if your university is set up for it",
         "office.com · sign in with uni email"),
        ("AWS Educate", "Free cloud labs and digital badges", "No credit card, open to students 13+",
         "aws.amazon.com/education/awseducate")],
     ("Do this", "Put one project online this month, for free.", "Mradi wako mtandaoni", NAVY)),
    ("Coupon 04 · Learn & get certified", ("Certificates", "for your CV."), [
        ("Cisco Networking Academy", "Networking, cyber security, Python", "Free self-paced courses with certificates",
         "netacad.com"),
        ("Huawei ICT Academy", "Cloud, AI and networking tracks", "Through partner universities, ask your department",
         "huawei.com · ICT Academy"),
        ("Microsoft Learn", "Free courses, student exam discounts", "Learn paths for Azure, AI and data",
         "learn.microsoft.com")],
     ("Do this", "Finish one free certificate before next semester.", "Cheti kimoja kwa muhula", NAVY)),
]
for p, (label, (t1, t2), items, (nl, nline, nsw, _)) in enumerate(GROUPS):
    n = p + 4
    s = page(n, label)
    title2(s, t1, t2, y=210, size=80)
    y, h, gap = 330, 214, 22
    for j, (name, gets, claim, where) in enumerate(items):
        perk(s, (M, y, W - M - 8, y + h), name, gets, where, claim,
             stub="FREE", stub_small="student deal", stub_fill=ORANGE if j % 2 == 0 else NAVY)
        y += h + gap
    horizon(s, n)
    navy_note(s, nl, nline, nsw, seed=n)
    finish(s)
    s.save(n)

# ── 7 · how to claim ─────────────────────────────────────────────────────────────────────────────
s = page(7, "How to claim · Jinsi ya kupata")
title2(s, "Claim them", "this week.", y=220, size=92)
paste_print(s, print_art("claim", k(400)), 620, 150)
steps = [("Activate your uni email", "Most deals check it. Ask ICT if you don't have one."),
         ("Photo of your student ID", "Clear, all four corners, your name readable."),
         ("Look for “Students”", "or “Education” at the bottom of each website.")]
y = 470
for j, (a, b) in enumerate(steps):
    outline_text(s, M - 4, y + 120, f"0{j + 1}", f(BOLD, 150), stroke=3, color=ORANGE, opacity=0.9)
    s.text(M + 230, y + 50, a, f(BOLD, fit(s, a, BOLD, 38, W - 2 * M - 230)), NAVY)
    s.text(M + 230, y + 96, b, f(REG, fit(s, b, REG, 24, W - 2 * M - 230)), GREY)
    if j < len(steps) - 1:
        hairline(s, M + 230, W - M, y + 140, RULE)
    y += 180
horizon(s, 7)
navy_note(s, "Tip", "Rejected? Upload your admission letter or fee receipt instead.", "Usikate tamaa", seed=7)
finish(s)
s.save(7)

# ── 8 · the receipt ──────────────────────────────────────────────────────────────────────────────
s = page(8, "Your receipt · Risiti yako")
s.text(M - 4, 230, "Add it", f(BOLD, 92), NAVY)
s.text(M - 4, 330, "all up.", f(BOLD, 92), ORANGE)
s.para(M, 420, "Pro tools, cloud credits, courses and certificates for a whole degree.", f(REG, 26), 380, 38, GREY)
s.text(M, 600, "You pay", f(SEMI, 30), NAVY)
s.text(M - 4, 700, "TZS 0", f(BOLD, 110), ORANGE)
s.text(M, 790, "Ni bure kabisa", f(SIG, 56), NAVY)
swash(s, M + 6, M + 320, 814, ORANGE, 5, seed=8)

RW, RH = 470, 860
rc = Image.new("RGBA", (k(RW + 40), k(RH + 40)), (0, 0, 0, 0))
rs = Slide.__new__(Slide)
rs.im, rs.d = rc, ImageDraw.Draw(rc)
teeth = []
for i in range(0, RW, 20):
    teeth += [(20 + i + 10, 20 + RH + 12), (20 + i + 20, 20 + RH)]
poly = [(20, 20), (20 + RW, 20)] + list(reversed(teeth)) + [(20, 20 + RH)]
rs.d.polygon([(k(x), k(y)) for x, y in poly], fill=(255, 255, 255, 255))
cx = 20 + RW / 2
rs.text(cx, 84, "STUDENT PERKS LTD", f(MONO_B, 26), NAVY, anchor="ms")
rs.text(cx, 114, "University campus, Tanzania", f(MONO, 16), GREY, anchor="ms")
rs.text(cx, 140, "Cashier: your uni email", f(MONO, 16), GREY, anchor="ms")


def dash(y):
    rs.text(cx, y, "-" * 34, f(MONO, 18), RULE, anchor="ms")


dash(172)
items = [("GitHub Student Pack", "FREE"), ("Copilot Pro", "FREE"), ("JetBrains IDEs", "FREE"), ("Figma Education", "FREE"),
         ("Notion Education", "FREE"), ("Azure $100 credit", "FREE"), ("Microsoft 365", "FREE"), ("AWS Educate", "FREE"),
         ("Cisco NetAcad", "FREE"), ("Huawei ICT Academy", "FREE"), ("Microsoft Learn", "FREE")]
y = 210
for name, price in items:
    rs.text(44, y, name, f(MONO, 19), NAVY)
    rs.text(20 + RW - 24, y, price, f(MONO_B, 19), ORANGE, anchor="rs")
    y += 36
dash(y)
y += 44
rs.text(44, y, "SUBTOTAL", f(MONO, 19), NAVY)
rs.text(20 + RW - 24, y, "0.00", f(MONO, 19), NAVY, anchor="rs")
y += 46
rs.text(44, y, "TOTAL TZS", f(MONO_B, 28), NAVY)
rs.text(20 + RW - 24, y, "0.00", f(MONO_B, 28), NAVY, anchor="rs")
y += 36
dash(y)
y += 40
rs.text(44, y, "PAID WITH: student ID", f(MONO, 17), GREY)
rs.text(44, y + 28, "VALID UNTIL: graduation day", f(MONO, 17), GREY)
y += 60
bx = cx - 150
rnd = _random.Random(4)
while bx < cx + 150:
    w_ = rnd.choice([2, 2, 3, 5])
    rs.rect(bx, y, bx + w_, y + 54, NAVY)
    bx += w_ + rnd.choice([3, 4, 6])
rs.text(cx, y + 88, "asante, karibu tena", f(MONO, 17), GREY, anchor="ms")
rc = rc.rotate(4, resample=Image.BICUBIC, expand=True)
rx, ry = 540, 128
sh = rc.getchannel("A").filter(ImageFilter.GaussianBlur(k(10))).point(lambda v: v * 80 // 255)
s.im.paste(Image.new("RGB", rc.size, INK), (k(rx + 10), k(ry + 14)), sh)
s.im.paste(rc, (k(rx), k(ry)), rc)
s.d = ImageDraw.Draw(s.im)
# a "PAID" stamp across the receipt
stamp = Image.new("RGBA", (k(260), k(120)), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rounded_rectangle([k(6), k(6), k(254), k(114)], radius=k(14), outline=ORANGE + (220,), width=k(6))
sd.text((k(130), k(62)), "CLAIMED", font=f(BOLD, 44), fill=ORANGE + (220,), anchor="mm")
stamp = stamp.rotate(-16, resample=Image.BICUBIC, expand=True)
s.im.paste(stamp, (k(760), k(780)), stamp)
s.d = ImageDraw.Draw(s.im)
horizon(s, 8)
navy_note(s, "Small print", "Offers change. Always check each website for the latest deal.")
finish(s)
s.save(8)

# ── 9 · watch out ────────────────────────────────────────────────────────────────────────────────
s = page(9, "Watch out · Kuwa makini")
title2(s, "Free means", "free.", y=230, size=100)
s.text(W - M, 330, "Usitapeliwe", f(SIG, 66), NAVY, anchor="rs")
swash(s, W - M - 330, W - M - 10, 356, ORANGE, 5, seed=9)
rules = [("Never pay anyone to “activate” a pack", "Real student deals cost nothing. Paying a middleman = scam."),
         ("Use your real details", "Fake IDs get your account banned, and the free tools go with it."),
         ("Don't sell or share your account", "It's tied to your name and your GitHub history."),
         ("Download certificates before you graduate", "Save PDFs and add them to LinkedIn now.")]
y = 480
for j, (a, b) in enumerate(rules):
    s.d.ellipse([k(M), k(y - 34), k(M + 44), k(y + 10)], fill=ORANGE if j == 0 else NAVY)
    s.text(M + 22, y - 12, str(j + 1), f(BOLD, 24), WHITE_T, anchor="mm")
    s.text(M + 70, y, a, f(BOLD, fit(s, a, BOLD, 31, W - 2 * M - 70)), NAVY)
    s.text(M + 70, y + 40, b, f(REG, fit(s, b, REG, 23, W - 2 * M - 70)), GREY)
    if j < len(rules) - 1:
        hairline(s, M + 70, W - M, y + 74, RULE)
    y += 128
horizon(s, 9)
sticker(s, W - M - 190, wave_y(8 * W + W - M - 190) - 4, "Pay to get it? = SCAM", angle=-6, size=20)
navy_note(s, "Remember", "If someone asks you to pay for a free student deal, walk away.")
finish(s)
s.save(9)

# ── 10 · closing ─────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
s.text(M - 6, 290, "Your turn.", f(BOLD, 112), NAVY)
s.text(M, 380, "Which one are you", f(BOLD, 50), ORANGE)
s.text(M, 444, "claiming first?", f(BOLD, 50), ORANGE)
s.text(M, 540, "Niambie kwenye comments", f(SIG, 52), ORANGE)
swash(s, M + 6, M + 440, 566, ORANGE, 5, seed=10)
rows = [("Save", "and claim one this week"), ("Share", "with a classmate who's paying for tools"), ("Comment", "the perk you're claiming first")]
y = 680
for j, (a, b) in enumerate(rows):
    s.text(M, y, f"{j + 1:02d}", f(BOLD, 22), ORANGE)
    s.text(M + 56, y, a, f(BOLD, 36), NAVY)
    s.text(M + 56, y + 40, b, f(REG, 24), GREY)
    y += 108
paste_print(s, print_art("idcard", k(440)), 590, 600)
horizon(s, TOTAL)
smallcaps(s, M, BASE + 72, "Read the full post · Soma zaidi", 17, SOFT)
s.text(M, BASE + 132, POST_URL, f(BOLD, fit(s, POST_URL, BOLD, 40, W - 2 * M)), WHITE_T)
hairline(s, M, W - M, BASE + 162, (38, 60, 100))
s.text(M, BASE + 224, "Link in bio", f(SEMI, 24), SOFT)
s.text(W - M, BASE + 224, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(TOTAL)
print("ok")
