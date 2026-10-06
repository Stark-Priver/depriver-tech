"""Carousel: make your FPT (field practical training) count, eight weeks, eight moves
(10 slides, 1080x1350, exported at 2x). Same editorial / print direction as free-tools-for-students (panorama paper,
navy wave, seam badges, print art, swashes, stickers). The carousel reads like an FPT logbook: every slide is one
week, signed off with a supervisor's stamp."""
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
LINE_BLUE = (190, 208, 240)
MARGIN_RED = (232, 96, 58)
POST_URL = "depriver.tech/blog/make-your-fpt-count"
BASE = 1060

# ── print illustrations (600x420 art board, navy outlines, no faces) ─────────────────────────────
RULED = lambda x, y, w, n, gap=26: "".join(f'<path d="M{x} {y + i * gap} h{w}" stroke="#a9c4f5" stroke-width="3"/>' for i in range(n))

ART.update({
    # open logbook with a stamp and a pen
    "logbook": svg(GROUND + f'''
      <path d="M300 92 C240 70 120 66 60 84 V360 C120 342 240 346 300 368z" fill="#fff" {ST}/>
      <path d="M300 92 C360 70 480 66 540 84 V360 C480 342 360 346 300 368z" fill="#fff" {ST}/>
      <path d="M300 92 V368" {ST} stroke-width="4"/>
      {RULED(84, 130, 190, 8)}{RULED(326, 130, 190, 8)}
      <path d="M110 112 V340" stroke="#e8603a" stroke-width="3" opacity=".7"/>
      <text x="90" y="124" font-family="Poppins" font-weight="700" font-size="16" fill="#0b1e3f">WEEK 01</text>
      <path d="M124 152 h120 M124 178 h90 M124 204 h130 M124 230 h70" stroke="#0b1e3f" stroke-width="5" stroke-linecap="round" opacity=".55"/>
      <g transform="rotate(-14 430 250)"><circle cx="430" cy="250" r="66" fill="none" stroke="#e8603a" stroke-width="7"/>
        <circle cx="430" cy="250" r="52" fill="none" stroke="#e8603a" stroke-width="3"/>
        <text x="430" y="242" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="22" fill="#e8603a">SIGNED</text>
        <text x="430" y="270" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="14" fill="#e8603a">SUPERVISOR</text></g>
      <g transform="translate(520 120) rotate(38)"><rect x="-12" y="-120" width="24" height="170" rx="6" fill="#0b1e3f" {ST} stroke-width="5"/>
        <rect x="-12" y="-120" width="24" height="34" rx="6" fill="#e8603a" {ST} stroke-width="5"/>
        <path d="M-12 50 L0 80 L12 50z" fill="#ffc857" {ST} stroke-width="5"/></g>'''),

    # trainee badge on a lanyard and a clock showing 7:55
    "badge": svg(GROUND + f'''
      <path d="M150 20 L230 150 M330 20 L250 150" stroke="#e8603a" stroke-width="16" stroke-linecap="round"/>
      <rect x="226" y="140" width="28" height="30" rx="6" fill="#0b1e3f"/>
      <rect x="140" y="166" width="200" height="220" rx="18" fill="#fff" {ST}/>
      <path d="M140 228 V184 a18 18 0 0 1 18-18 h164 a18 18 0 0 1 18 18 V228z" fill="#0b1e3f" {ST}/>
      <text x="240" y="206" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="22" fill="#fff" letter-spacing="3">TRAINEE</text>
      <circle cx="240" cy="276" r="30" fill="#a9c4f5" {ST} stroke-width="5"/>
      <path d="M186 332 h108 M200 356 h80" stroke="#c9d4ea" stroke-width="11" stroke-linecap="round"/>
      <g transform="translate(470 230)"><circle r="92" fill="#fff" {ST}/><circle r="76" fill="none" stroke="#c9d4ea" stroke-width="4"/>
        {"".join(f'<path d="M0 -70 v12" transform="rotate({a})" {ST} stroke-width="5"/>' for a in range(0, 360, 30))}
        <path d="M0 0 L-6 -50" {ST} stroke-width="8"/><path d="M0 0 L-24 -54" transform="rotate(30)" stroke="#e8603a" stroke-width="5" stroke-linecap="round"/>
        <path d="M0 0 L46 -10" transform="rotate(-140)" {ST} stroke-width="10"/><circle r="9" fill="#0b1e3f"/></g>'''),

    # notebook with a question bubble
    "ask": svg(GROUND + f'''
      <g transform="rotate(-6 200 250)"><rect x="80" y="110" width="250" height="270" rx="12" fill="#fff" {ST}/>
        <path d="M80 110 h36 v270 h-36" fill="#e8603a" {ST}/>
        {RULED(140, 160, 160, 8)}
        <path d="M148 174 h100 M148 200 h130 M148 226 h80" stroke="#0b1e3f" stroke-width="5" stroke-linecap="round" opacity=".55"/></g>
      <g transform="translate(440 160)"><path d="M-110 -80 h220 a24 24 0 0 1 24 24 v110 a24 24 0 0 1 -24 24 h-140 l-40 40 v-40 h-40 a24 24 0 0 1 -24 -24 v-110 a24 24 0 0 1 24 -24z" fill="#0b1e3f" {ST}/>
        <text x="0" y="14" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="36" fill="#fff">What's next?</text></g>'''),

    # toolbox with tool chips
    "toolbox": svg(GROUND + f'''
      <path d="M210 150 v-40 a14 14 0 0 1 14-14 h152 a14 14 0 0 1 14 14 v40" fill="none" {ST} stroke-width="12"/>
      <rect x="110" y="150" width="380" height="220" rx="20" fill="#e8603a" {ST}/>
      <path d="M110 220 h380" {ST}/>
      <rect x="270" y="204" width="60" height="34" rx="8" fill="#ffc857" {ST} stroke-width="5"/>
      <g transform="rotate(-18 170 120)"><rect x="120" y="90" width="110" height="46" rx="23" fill="#fff" {ST} stroke-width="5"/>
        <text x="175" y="121" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="20" fill="#0b1e3f">git</text></g>
      <g transform="rotate(12 450 110)"><rect x="390" y="86" width="130" height="46" rx="23" fill="#a9c4f5" {ST} stroke-width="5"/>
        <text x="455" y="117" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="20" fill="#0b1e3f">linux</text></g>
      <g transform="rotate(-4 300 60)"><rect x="236" y="34" width="140" height="46" rx="23" fill="#0b1e3f" {ST} stroke-width="5"/>
        <text x="306" y="65" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="20" fill="#fff">SQL</text></g>'''),

    # people network: badges joined by lines
    "network": svg(GROUND + f'''
      <path d="M300 210 L130 110 M300 210 L470 110 M300 210 L120 320 M300 210 L480 320 M130 110 L470 110" stroke="#0b1e3f" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
      {"".join(f'<g transform="translate({x} {y})"><circle r="{r}" fill="{c}" {ST}/><circle cy="-{r * 0.22}" r="{r * 0.3}" fill="#0b1e3f"/><path d="M-{r * 0.55} {r * 0.62} c0-{r * 0.6} {r * 1.1}-{r * 0.6} {r * 1.1} 0" fill="#0b1e3f"/></g>' for x, y, r, c in [(300, 210, 78, "#e8603a"), (130, 110, 52, "#fff"), (470, 110, 52, "#a9c4f5"), (120, 320, 50, "#a9c4f5"), (480, 320, 50, "#fff")])}'''),

    # portfolio folder with screenshots
    "folder": svg(GROUND + f'''
      <path d="M80 120 h150 l30 30 h260 v220 H80z" fill="#0b1e3f" {ST}/>
      <g transform="rotate(-8 230 200)"><rect x="140" y="100" width="200" height="140" rx="10" fill="#fff" {ST} stroke-width="5"/>
        <rect x="156" y="116" width="168" height="80" rx="6" fill="#a9c4f5"/><path d="M160 186 l40-40 l30 26 l40-46 l50 60z" fill="#fff" opacity=".9"/>
        <path d="M156 216 h100" stroke="#c9d4ea" stroke-width="9" stroke-linecap="round"/></g>
      <g transform="rotate(7 380 200)"><rect x="290" y="96" width="200" height="140" rx="10" fill="#fff" {ST} stroke-width="5"/>
        <path d="M310 124 h120 M310 150 h150 M310 176 h90 M310 202 h130" stroke="#c9d4ea" stroke-width="9" stroke-linecap="round"/>
        <path d="M310 124 h50" stroke="#e8603a" stroke-width="9" stroke-linecap="round"/></g>
      <path d="M60 200 h460 l-30 170 H90z" fill="#26406c" {ST}/>
      <text x="290" y="300" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="34" fill="#fff" letter-spacing="3">PROOF</text>'''),

    # envelope with a wax seal and a letter peeking out
    "letter": svg(GROUND + f'''
      <g transform="rotate(-5 300 230)">
        <rect x="160" y="60" width="280" height="220" rx="8" fill="#fff" {ST}/>
        <text x="186" y="108" font-family="Poppins" font-weight="700" font-size="18" fill="#0b1e3f">TO WHOM IT MAY CONCERN</text>
        <path d="M186 140 h220 M186 166 h190 M186 192 h210" stroke="#c9d4ea" stroke-width="9" stroke-linecap="round"/>
        <rect x="100" y="190" width="400" height="190" rx="12" fill="#a9c4f5" {ST}/>
        <path d="M100 196 L300 300 L500 196" fill="none" {ST}/>
        <circle cx="300" cy="300" r="40" fill="#e8603a" {ST}/>
        <path d="M284 300 l12 12 l22-24" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>'''),
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


def stamp(s, cx, cy, week, angle=-12, color=ORANGE):
    """Round supervisor stamp: WEEK / 0n / SIGNED, slightly faded like real ink."""
    R = 74
    lay = Image.new("RGBA", (k(2 * R + 20), k(2 * R + 20)), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    c, ink = k(R + 10), color + (215,)
    ld.ellipse([c - k(R), c - k(R), c + k(R), c + k(R)], outline=ink, width=k(6))
    ld.ellipse([c - k(R - 12), c - k(R - 12), c + k(R - 12), c + k(R - 12)], outline=ink, width=k(2.5))
    ld.text((c, c - k(30)), "WEEK", font=f(BOLD, 16), fill=ink, anchor="mm")
    ld.text((c, c + k(4)), f"{week:02d}", font=f(BOLD, 46), fill=ink, anchor="mm")
    ld.text((c, c + k(38)), "SIGNED", font=f(BOLD, 15), fill=ink, anchor="mm")
    worn = Image.effect_noise(lay.size, 90).point(lambda v: 255 if v > 70 else 120)
    lay.putalpha(ImageChops.multiply(lay.getchannel("A"), worn))
    lay = lay.rotate(angle, resample=Image.BICUBIC, expand=True)
    s.im.paste(lay, (k(cx) - lay.width // 2, k(cy) - lay.height // 2), lay)
    s.d = ImageDraw.Draw(s.im)


def ruled_card(s, box, r=16, margin=96, fill=(255, 255, 255), gap=46):
    """A logbook page: white card, blue rules, red margin line, offset ink block behind."""
    x0, y0, x1, y1 = box
    s.rect(x0 + 8, y0 + 10, x1 + 8, y1 + 10, (205, 211, 224), r=r)
    s.d.rounded_rectangle([k(x0), k(y0), k(x1), k(y1)], radius=k(r), fill=fill, outline=NAVY, width=k(3))
    y = y0 + 58
    while y < y1 - 14:
        s.rect(x0 + 3, y, x1 - 3, y + 1.5, LINE_BLUE)
        y += gap
    if margin:
        s.rect(x0 + margin, y0 + 3, x0 + margin + 2, y1 - 3, MARGIN_RED)


def points(s, items, y, x=M, num=True, maxw=W - 2 * M, gap=118, ts=32, bs=23):
    for j, (a, b) in enumerate(items):
        if num:
            s.d.ellipse([k(x), k(y - 34), k(x + 44), k(y + 10)], fill=ORANGE if j % 2 == 0 else NAVY)
            s.text(x + 22, y - 12, str(j + 1), f(BOLD, 24), WHITE_T, anchor="mm")
        s.text(x + 70, y, a, f(BOLD, fit(s, a, BOLD, ts, maxw - 70)), NAVY)
        s.text(x + 70, y + 40, b, f(REG, fit(s, b, REG, bs, maxw - 70)), GREY)
        if j < len(items) - 1:
            hairline(s, x + 70, x + maxw, y + 72, RULE)
        y += gap
    return y


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For students on field practical training")
s.text(M - 6, 250, "FPT is not", f(BOLD, 92), NAVY)
s.text(M - 6, 350, "a holiday.", f(BOLD, 92), NAVY)
s.text(M - 6, 466, "Make it", f(BOLD, 110), ORANGE)
s.text(M - 10, 590, "count.", f(BOLD, 150), ORANGE)
s.text(M, 690, "Mafunzo si likizo", f(SIG, 64), NAVY)
swash(s, M + 8, M + 400, 716, ORANGE, 6)
s.para(M, 800, "Eight weeks that can turn into a reference, real experience and even a job offer.",
       f(REG, 27), 440, 40, GREY)
paste_print(s, print_art("logbook", k(560)), 480, 560)
sticker(s, W - M - 160, 1000, "8 weeks · 8 moves", angle=-5, size=22, bg=NAVY)
horizon(s, 1)
s.text(M, 1262, "Swipe through your logbook", f(SEMI, 30), WHITE_T)
arrow(s, M + s.width("Swipe through your logbook", f(SEMI, 30)) + 34, 1251)
s.text(W - M, 1262, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(1)

# ── 2 · week 01 · show up like staff ─────────────────────────────────────────────────────────────
s = page(2, "Week 01 · Show up like staff")
title2(s, "Act like you", "work there.", y=230, size=84)
paste_print(s, print_art("badge", k(400)), 620, 300)
points(s, [("Arrive before time", "7:55 beats 8:05, every single day."),
           ("Dress like the team", "Look at what staff wear and match it."),
           ("Phone in your bag", "Scrolling at your desk is the first thing they notice."),
           ("Say yes to small tasks", "Carrying cables today, real tickets tomorrow.")], 470, maxw=560, gap=134)
stamp(s, W - M - 70, 940, 1, angle=10)
horizon(s, 2)
navy_note(s, "Truth", "They judge how you work before what you know.", "Nidhamu kwanza", seed=2)
finish(s)
s.save(2)

# ── 3 · week 02 · logbook ────────────────────────────────────────────────────────────────────────
s = page(3, "Week 02 · Write the logbook daily")
title2(s, "Your logbook", "is a CV draft.", y=230, size=84)
# bad entry
ruled_card(s, (M, 390, W - M - 8, 560))
smallcaps(s, M + 20, 436, "Day 12", 14, GREY)
s.text(M + 122, 436, "Before", f(BOLD, 20), MARGIN_RED)
s.text(M + 122, 520, "Observed.", f(SIG, 60), NAVY)
s.d.line([k(M + 112), k(500), k(M + 380), k(492)], fill=MARGIN_RED, width=k(5))
sticker(s, W - M - 150, 500, "Says nothing", angle=-6, size=20, bg=NAVY)
# good entry
ruled_card(s, (M, 600, W - M - 8, 960), gap=70)
smallcaps(s, M + 20, 646, "Day 12", 14, GREY)
s.text(M + 122, 646, "After", f(BOLD, 20), ORANGE)
rows = [("Did", "Set up 6 office PCs and fixed the HR printer on the network."),
        ("Tools", "Windows installer, MikroTik Winbox, a LAN cable tester."),
        ("Learnt", "How DHCP reservations give a printer a fixed IP."),
        ("Next", "Ask my supervisor to show me the VLAN setup.")]
y = 718
for a, b in rows:
    s.text(M + 20, y, a, f(BOLD, 21), ORANGE)
    s.text(M + 122, y, b, f(MED, fit(s, b, MED, 24, W - 2 * M - 160)), NAVY)
    y += 70
stamp(s, W - M - 80, 640, 2, angle=-10)
horizon(s, 3)
navy_note(s, "Do this", "Write it every evening. Get it signed every week.", "Andika kila siku", seed=3)
finish(s)
s.save(3)

# ── 4 · week 03 · ask for work ───────────────────────────────────────────────────────────────────
s = page(4, "Week 03 · Ask for real work")
title2(s, "Don't wait.", "Ask for work.", y=230, size=84)
paste_print(s, print_art("ask", k(420)), 600, 290)
points(s, [("Finished a task?", "Go back and ask: what's next?"),
           ("Carry a notebook", "Write every new word, tool and command."),
           ("Ask why, not only how", "Why it's built this way teaches more than how."),
           ("Offer to help seniors", "Small help now, bigger tasks later.")], 500, maxw=W - 2 * M, gap=126)
stamp(s, W - M - 90, 860, 3, angle=8)
horizon(s, 4)
navy_note(s, "Remember", "Nobody hands trainees work. The ones who ask get it.", "Uliza, usiogope", seed=4)
finish(s)
s.save(4)

# ── 5 · week 04 · learn their tools ──────────────────────────────────────────────────────────────
s = page(5, "Week 04 · Learn their tools")
title2(s, "Copy their", "stack at home.", y=230, size=84)
paste_print(s, print_art("toolbox", k(330)), 700, 150)
s.para(M, 430, "Every office runs on tools you never saw in class. Write each one down, then practise it at home.",
       f(REG, 26), 540, 38, GREY)
chips = ["Git", "Linux servers", "MikroTik", "SQL databases", "Excel", "Laravel", "React", "ERP systems",
         "POS systems", "Active Directory", "Docker", "Figma"]
x, y = M, 640
for j, c in enumerate(chips):
    fnt = f(SEMI, 25)
    w_ = s.width(c, fnt) + 48
    if x + w_ > W - M:
        x, y = M, y + 78
    hero = j in (0, 3, 6)
    s.rect(x + 4, y + 6, x + w_ + 4, y + 62, (205, 211, 224), r=29)
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + 56)], radius=k(28), fill=NAVY if hero else (255, 255, 255),
                          outline=NAVY, width=k(2.5))
    s.text(x + w_ / 2, y + 29, c, fnt, WHITE_T if hero else NAVY, anchor="mm")
    x += w_ + 16
s.text(M, y + 140, "Pick one. Learn it well enough to teach it.", f(SEMI, 30), NAVY)
stamp(s, W - M - 80, y + 120, 4, angle=-8)
horizon(s, 5)
navy_note(s, "Do this", "Rebuild a small version of their system on your laptop.", "Jifunze kwa macho", seed=5)
finish(s)
s.save(5)

# ── 6 · week 05 · people ─────────────────────────────────────────────────────────────────────────
s = page(6, "Week 05 · Meet the people")
title2(s, "Your network", "starts here.", y=230, size=84)
paste_print(s, print_art("network", k(400)), 620, 300)
points(s, [("Your supervisor", "Your first reference. Make their job easy."),
           ("The seniors", "Ask one career question every week."),
           ("Other trainees", "Today's classmates, tomorrow's colleagues."),
           ("Clients you meet", "Be polite. They remember the helpful trainee.")], 470, maxw=560, gap=134)
stamp(s, W - M - 80, 920, 5, angle=-6)
horizon(s, 6)
navy_note(s, "Do this", "Save their numbers and connect on LinkedIn before you leave.", "Watu ni mtaji", seed=6)
finish(s)
s.save(6)

# ── 7 · week 06 · proof ──────────────────────────────────────────────────────────────────────────
s = page(7, "Week 06 · Collect proof")
title2(s, "Leave with", "proof.", y=230, size=92)
paste_print(s, print_art("folder", k(420)), 590, 140)
s.text(M, 470, "Ushahidi ni muhimu", f(SIG, 54), NAVY)
swash(s, M + 6, M + 380, 496, ORANGE, 5, seed=7)
ruled_card(s, (M, 560, W - M - 8, 900), margin=160)
smallcaps(s, M + 20, 606, "Write it up", 14, GREY)
s.text(M + 186, 606, "One short case study", f(BOLD, 21), ORANGE)
rows = [("Problem", "What wasn't working, in one line."),
        ("What I did", "The steps and the tools you used."),
        ("Result", "Faster, fixed, saved time or money."),
        ("Proof", "Screenshots, with private data hidden.")]
y = 698
for a, b in rows:
    s.text(M + 20, y, a, f(BOLD, 21), ORANGE)
    s.text(M + 186, y, b, f(MED, fit(s, b, MED, 25, W - 2 * M - 220)), NAVY)
    y += 46
stamp(s, W - M - 90, 900, 6, angle=12)
horizon(s, 7)
navy_note(s, "Always", "Ask before you share anything from the office. Hide client data.", "Siri za ofisi ni siri", seed=7)
finish(s)
s.save(7)

# ── 8 · week 07 · recommendation letter ──────────────────────────────────────────────────────────
s = page(8, "Week 07 · Get the letter")
title2(s, "Ask for the", "letter early.", y=230, size=84)
paste_print(s, print_art("letter", k(400)), 620, 300)
points(s, [("Ask two weeks before", "Not on your last day, when everyone's busy."),
           ("Hand them a summary", "One page: what you did, tools, results."),
           ("Leave your contacts", "Phone, email, LinkedIn, so they can find you."),
           ("Say thank you", "In person, then a short message after.")], 470, maxw=560, gap=134)
stamp(s, W - M - 80, 930, 7, angle=-10)
horizon(s, 8)
navy_note(s, "Bonus", "Ask: “If a vacancy opens, can I apply?”", "Shukrani ni mlango", seed=8)
finish(s)
s.save(8)

# ── 9 · week 08 · don't ──────────────────────────────────────────────────────────────────────────
s = page(9, "Week 08 · Don't do these")
title2(s, "Don't ruin", "your name.", y=230, size=84)
s.text(W - M, 330, "Usiharibu jina", f(SIG, 56), NAVY, anchor="rs")
swash(s, W - M - 320, W - M - 10, 354, ORANGE, 5, seed=9)
ruled_card(s, (M, 400, W - M - 8, 960), gap=80)
smallcaps(s, M + 20, 446, "Never", 14, MARGIN_RED)
donts = ["Copy a friend's logbook", "Disappear for days without telling anyone", "Share office passwords or client data",
         "Post their systems on social media", "Spend the day on your phone", "Complain loudly that FPT isn't paid"]
y = 528
for d_ in donts:
    fnt = f(SEMI, fit(s, d_, SEMI, 30, W - 2 * M - 160))
    s.text(M + 122, y, d_, fnt, NAVY)
    s.d.line([k(M + 114), k(y - 11), k(M + 130 + s.width(d_, fnt)), k(y - 13)], fill=MARGIN_RED, width=k(4))
    s.d.line([k(M + 34), k(y - 24), k(M + 58), k(y)], fill=MARGIN_RED, width=k(4))
    s.d.line([k(M + 58), k(y - 24), k(M + 34), k(y)], fill=MARGIN_RED, width=k(4))
    y += 80
stamp(s, W - M - 90, 900, 8, angle=8)
horizon(s, 9)
navy_note(s, "Remember", "Tech in Tanzania is small. Your name travels.")
finish(s)
s.save(9)

# ── 10 · closing ─────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
s.text(M, 220, "My first FPT was at MUST in 2024.", f(SEMI, 30), NAVY)
s.text(M, 262, "It shaped how I work today.", f(SEMI, 30), GREY)
hairline(s, M, W - M, 300, RULE)
s.text(M - 6, 420, "Your turn.", f(BOLD, 112), NAVY)
s.text(M, 504, "What has FPT taught", f(BOLD, 48), ORANGE)
s.text(M, 566, "you so far?", f(BOLD, 48), ORANGE)
s.text(M, 650, "Niambie kwenye comments", f(SIG, 52), ORANGE)
swash(s, M + 6, M + 440, 676, ORANGE, 5, seed=10)
rows = [("Save", "and read it every Monday of FPT"), ("Share", "with a classmate on field"), ("Comment", "your best FPT lesson")]
y = 770
for j, (a, b) in enumerate(rows):
    s.text(M, y, f"{j + 1:02d}", f(BOLD, 22), ORANGE)
    s.text(M + 56, y, a, f(BOLD, 34), NAVY)
    s.text(M + 56, y + 38, b, f(REG, 23), GREY)
    y += 96
paste_print(s, print_art("logbook", k(420)), 600, 680)
horizon(s, TOTAL)
smallcaps(s, M, BASE + 72, "Read the full post · Soma zaidi", 17, SOFT)
s.text(M, BASE + 132, POST_URL, f(BOLD, fit(s, POST_URL, BOLD, 40, W - 2 * M)), WHITE_T)
hairline(s, M, W - M, BASE + 162, (38, 60, 100))
s.text(M, BASE + 224, "Link in bio", f(SEMI, 24), SOFT)
s.text(W - M, BASE + 224, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(TOTAL)
print("ok")
