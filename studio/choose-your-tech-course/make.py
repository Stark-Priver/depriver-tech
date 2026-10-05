"""Carousel: finished Form Four or Form Six? Choosing a tech course and university in Tanzania
(10 slides, 1080x1350, exported at 2x). Same editorial / print direction as darasani-vs-kazini.
University programmes and entry requirements come from the TCU Bachelor's Degree Admission Guidebook
2026/2027 (for holders of secondary school qualifications)."""
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
POST_URL = "depriver.tech/blog/choose-your-tech-course"
BASE = 1060

# ── print illustrations (600x420 art board, navy outlines, no faces) ─────────────────────────────
ART.update({
    "cover": svg(GROUND + f'''
      <path d="M90 330 h300 l34 40 H56z" fill="#c9d4ea" {ST}/>
      <rect x="110" y="150" width="260" height="180" rx="16" fill="#fff" {ST}/>
      <rect x="128" y="168" width="224" height="144" rx="8" fill="#0b1e3f"/>
      <path d="M152 200 h60 M152 226 h120 M170 252 h80 M152 278 h50" stroke="#a9c4f5" stroke-width="8" stroke-linecap="round"/>
      <path d="M152 200 h24" stroke="#e8603a" stroke-width="8" stroke-linecap="round"/>
      <g transform="translate(240 120)"><path d="M-120 0 L0-52 L120 0 L0 52z" fill="#0b1e3f" {ST}/>
        <path d="M-70 22 v44 c0 20 140 20 140 0 v-44" fill="#26406c" {ST}/>
        <path d="M100 8 v70" stroke="#ffc857" stroke-width="7" stroke-linecap="round"/><circle cx="100" cy="84" r="10" fill="#ffc857" {ST} stroke-width="4"/></g>
      <g transform="translate(480 250)"><path d="M0 130 V-90" {ST} stroke-width="12"/>
        <path d="M6-100 h90 l24 24 -24 24 h-90z" fill="#e8603a" {ST} stroke-width="5"/>
        <text x="52" y="-68" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="20" fill="#fff">DEGREE</text>
        <path d="M-6-30 h-90 l-24 24 24 24 h90z" fill="#fff" {ST} stroke-width="5"/>
        <text x="-52" y="2" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="20" fill="#0b1e3f">DIPLOMA</text></g>'''),

    "roads": svg(GROUND + f'''
      <path d="M300 410 C300 300 140 260 90 120" fill="none" stroke="#c9d4ea" stroke-width="64" stroke-linecap="round"/>
      <path d="M300 410 C300 300 460 260 510 120" fill="none" stroke="#c9d4ea" stroke-width="64" stroke-linecap="round"/>
      <path d="M300 410 C300 300 140 260 90 120 M300 410 C300 300 460 260 510 120" fill="none" stroke="#fff" stroke-width="6" stroke-dasharray="16 20" stroke-linecap="round"/>
      <g transform="translate(90 96)"><circle r="44" fill="#fff" {ST}/><text y="10" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="28" fill="#0b1e3f">F4</text></g>
      <g transform="translate(510 96)"><circle r="44" fill="#e8603a" {ST}/><text y="10" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="28" fill="#fff">F6</text></g>
      <g transform="translate(300 250)"><path d="M0-70 L60-36 V20 C60 54 30 72 0 82 C-30 72-60 54-60 20 V-36z" fill="#ffc857" {ST}/>
        <path d="M-24 6 l18 18 l32-36" fill="none" stroke="#0b1e3f" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>'''),

    "research": svg(GROUND + f'''
      <rect x="70" y="60" width="300" height="320" rx="18" fill="#fff" {ST}/>
      <rect x="160" y="40" width="120" height="44" rx="12" fill="#0b1e3f" {ST}/>
      {"".join(f'<rect x="100" y="{120 + i * 60}" width="34" height="34" rx="8" fill="{"#e8603a" if i < 3 else "#fff"}" {ST} stroke-width="5"/><path d="M152 {137 + i * 60} h{170 - (i % 2) * 50}" stroke="#c9d4ea" stroke-width="12" stroke-linecap="round"/>' for i in range(4))}
      {"".join(f'<path d="M108 {136 + i * 60} l8 8 l14-16" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>' for i in range(3))}
      <g transform="translate(430 240)"><circle r="92" fill="#fff" fill-opacity=".6" {ST} stroke-width="10"/>
        <path d="M-50 20 v-50 l50-30 l50 30 v50z" fill="#a9c4f5" {ST} stroke-width="5"/>
        <path d="M-20 20 v-30 h40 v30" fill="#fff" {ST} stroke-width="5"/>
        <path d="M66 66 l70 70" stroke="#0b1e3f" stroke-width="26" stroke-linecap="round"/></g>'''),
})

ICON = {  # small course icons, 120x120
    "cs": '<rect x="14" y="22" width="92" height="70" rx="10" fill="#fff" {ST}/><path d="M42 46 l-14 12 14 12 M78 46 l14 12 -14 12 M66 40 l-12 36" fill="none" {ST}/><path d="M40 104 h40" {ST}/>',
    "se": '<rect x="14" y="16" width="56" height="44" rx="8" fill="#a9c4f5" {ST}/><rect x="50" y="44" width="56" height="44" rx="8" fill="#fff" {ST}/><rect x="24" y="74" width="34" height="34" rx="8" fill="#e8603a" {ST}/><path d="M64 62 h28 M64 74 h18" {ST} stroke-width="5"/>',
    "it": '<rect x="18" y="14" width="84" height="26" rx="6" fill="#fff" {ST}/><rect x="18" y="48" width="84" height="26" rx="6" fill="#a9c4f5" {ST}/><rect x="18" y="82" width="84" height="26" rx="6" fill="#fff" {ST}/><circle cx="34" cy="27" r="5" fill="#3ddc84"/><circle cx="34" cy="61" r="5" fill="#3ddc84"/><circle cx="34" cy="95" r="5" fill="#e8603a"/>',
    "data": '<path d="M16 104 h90" {ST}/><rect x="22" y="64" width="18" height="40" fill="#a9c4f5" {ST} stroke-width="5"/><rect x="50" y="40" width="18" height="64" fill="#e8603a" {ST} stroke-width="5"/><rect x="78" y="20" width="18" height="84" fill="#ffc857" {ST} stroke-width="5"/>',
    "cyber": '<path d="M60 10 L100 26 V58 C100 84 80 100 60 110 C40 100 20 84 20 58 V26z" fill="#e8603a" {ST}/><rect x="44" y="54" width="32" height="26" rx="5" fill="#fff" {ST} stroke-width="5"/><path d="M50 54 v-8 a10 10 0 0 1 20 0 v8" fill="none" {ST} stroke-width="5"/>',
    "ce": '<rect x="28" y="28" width="64" height="64" rx="8" fill="#0b1e3f" {ST}/><rect x="44" y="44" width="32" height="32" rx="4" fill="#ffc857"/>' + "".join(f'<path d="M{40 + i * 20} 28 v-14 M{40 + i * 20} 92 v14 M28 {40 + i * 20} h-14 M92 {40 + i * 20} h14" {{ST}} stroke-width="5"/>' for i in range(3)),
    "net": '<circle cx="60" cy="60" r="16" fill="#e8603a" {ST}/>' + "".join(f'<path d="M60 60 L{x} {y}" {{ST}} stroke-width="5"/><circle cx="{x}" cy="{y}" r="12" fill="#a9c4f5" {{ST}} stroke-width="5"/>' for x, y in [(18, 20), (102, 20), (18, 100), (102, 100)]),
    "bis": '<rect x="18" y="40" width="84" height="64" rx="10" fill="#fff" {ST}/><path d="M44 40 v-12 h32 v12" fill="none" {ST}/><path d="M34 88 l18-18 l14 10 l22-24" fill="none" stroke="#e8603a" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>',
}


def icon(key, size):
    body = ICON[key].replace("{ST}", ST)
    return svg_image(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120">{body}</svg>', k(size))


COURSES = [
    [("cs", "Computer Science", "How software works: algorithms, data, programming.", "you love solving puzzles"),
     ("se", "Software Engineering", "Building, testing and shipping real apps in teams.", "you want to build products"),
     ("it", "Information Technology", "Systems, databases and networks that run organisations.", "you like making tech work"),
     ("data", "Data Science & AI", "Statistics, data analysis and machine learning.", "you're strong in maths")],
    [("cyber", "Cyber Security", "Protecting systems, networks and data from attacks.", "you think like a detective"),
     ("ce", "Computer Engineering", "Hardware meets software: circuits and embedded systems.", "you open up gadgets"),
     ("net", "Networks & Telecom", "How data travels: networks, mobile and the internet.", "you want to keep us online"),
     ("bis", "Business IT", "Information systems that help companies run.", "you like tech and business")],
]

UNIS = [
    [("UDSM", "University of Dar es Salaam", "Dar es Salaam", "Computer Science · Computer Eng. & IT · Telecom Eng.", "udsm.ac.tz"),
     ("UDOM", "University of Dodoma", "Dodoma", "Computer Science · Software Eng. · Cyber Security · AI Eng.", "udom.ac.tz"),
     ("MUST", "Mbeya University of Science and Technology", "Mbeya", "Computer Science · Software Eng. · Data Science Eng.", "must.ac.tz"),
     ("DIT", "Dar es Salaam Institute of Technology", "Dar es Salaam", "Computer Eng. · Electronics & Telecom Eng.", "dit.ac.tz"),
     ("ATC", "Arusha Technical College", "Arusha", "Computer Science · Information Technology", "atc.ac.tz")],
    [("ARU", "Ardhi University", "Dar es Salaam", "Data Science & AI · Computer Systems & Networks", "aru.ac.tz"),
     ("MU", "Mzumbe University", "Morogoro", "IT & Systems · Applied Statistics", "mzumbe.ac.tz"),
     ("IFM", "Institute of Finance Management", "Dar es Salaam", "Computer Science · Cyber Security · IT", "ifm.ac.tz"),
     ("NIT", "National Institute of Transport", "Dar es Salaam", "Computer Science · Information Technology", "nit.ac.tz"),
     ("IAA", "Institute of Accountancy Arusha", "Arusha", "Computer Science · IT · Cyber Security", "iaa.ac.tz")],
]


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


def card(s, box, r=18):
    """Print-style card: white, navy outline, offset ink block behind."""
    x0, y0, x1, y1 = box
    s.rect(x0 + 8, y0 + 10, x1 + 8, y1 + 10, (205, 211, 224), r=r)
    s.d.rounded_rectangle([k(x0), k(y0), k(x1), k(y1)], radius=k(r), fill=(255, 255, 255), outline=NAVY, width=k(3))


def navy_note(s, label, line, sw=None, seed=0):
    smallcaps(s, M, BASE + 74, label, 16, ORANGE)
    s.text(M, BASE + 130, line, f(SEMI, fit(s, line, SEMI, 31, W - 2 * M)), WHITE_T)
    if sw:
        sws = fit(s, sw, SIG, 54, W - 2 * M - 40)
        s.text(M, BASE + 214, sw, f(SIG, sws), ORANGE)
        swash(s, M + 6, M + min(s.width(sw, f(SIG, sws)) * 0.9, 620), BASE + 238, ORANGE, 5, seed=seed)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For Form Four & Form Six leavers")
s.text(M - 6, 250, "Finished school?", f(BOLD, 96), NAVY)
s.text(M - 8, 380, "Now choose", f(BOLD, 138), ORANGE)
s.text(M - 8, 500, "your tech path.", f(BOLD, 112), ORANGE)
s.text(M, 600, "Chagua njia yako", f(SIG, 64), NAVY)
swash(s, M + 8, M + 420, 628, ORANGE, 6)
s.para(M, 710, "Tech courses explained, where to study them in Tanzania, and how to choose wisely.",
       f(REG, 27), 380, 40, GREY)
paste_print(s, print_art("cover", k(560)), 470, 600)
horizon(s, 1)
s.text(M, 1262, "Swipe to plan your next move", f(SEMI, 30), WHITE_T)
arrow(s, M + s.width("Swipe to plan your next move", f(SEMI, 30)) + 34, 1251)
s.text(W - M, 1262, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(1)

# ── 2 · two roads ────────────────────────────────────────────────────────────────────────────────
s = page(2, "Step 01 · Know your road")
paste_print(s, print_art("roads", k(520)), 280, 120)
s.text(M - 4, 520, "Two roads,", f(BOLD, 88), NAVY)
s.text(M - 4, 610, "same destination.", f(BOLD, 88), ORANGE)
col, top = 540, 700
smallcaps(s, M, top, "After Form Four", 16, GREY)
smallcaps(s, col + 40, top, "After Form Six", 16, ORANGE)
s.rect(col, top - 22, col + 2, top + 280, RULE)
y = s.para(M, top + 50, "Ordinary Diploma (NTA 4–6) at a college. Check NACTVET for courses.", f(MED, 25), col - M - 30, 36, NAVY)
s.para(M, y + 14, "Good GPA? Join a degree later through equivalent entry, or start working.", f(REG, 24), col - M - 30, 34, GREY)
y = s.para(col + 40, top + 50, "Bachelor's degree, usually 3 years (4 for engineering).", f(MED, 25), W - M - col - 40, 36, NAVY)
s.para(col + 40, y + 14, "Your A-Level subject combination decides which courses you can join. Check the TCU guidebook.", f(REG, 24), W - M - col - 40, 34, GREY)
horizon(s, 2)
sticker(s, W - M - 160, wave_y(W + W - M - 160) - 4, "Both work", angle=-6, size=20)
navy_note(s, "Truth", "A diploma is not a failure. A degree is not a guarantee.", "Njia zote zinafika", seed=1)
finish(s)
s.save(2)

# ── 3–4 · courses ────────────────────────────────────────────────────────────────────────────────
notes = [("Don't judge a course by its name", "Read the modules before you apply.", "Soma maudhui ya kozi"),
         ("Not sure yet?", "Computer Science keeps the most doors open.", "Ukiwa na shaka, anza na msingi")]
for p, group in enumerate(COURSES):
    n = p + 3
    s = page(n, f"Step 02 · Pick a course ({p + 1}/2)")
    s.text(M - 4, 220, "Which course" if p == 0 else "More courses", f(BOLD, 76), NAVY)
    s.text(M - 4, 300, "fits you?" if p == 0 else "to consider.", f(BOLD, 76), ORANGE)
    cw, ch, gap, y0 = (W - 2 * M - 30) / 2, 330, 30, 350
    for j, (ic, name, learn, pick) in enumerate(group):
        x0 = M + (j % 2) * (cw + gap)
        yy = y0 + (j // 2) * (ch + gap)
        card(s, (x0, yy, x0 + cw - 8, yy + ch))
        im = icon(ic, 78)
        s.im.paste(im, (k(x0 + 26), k(yy + 24)), im)
        s.text(x0 + 26, yy + 150, name, f(BOLD, fit(s, name, BOLD, 30, cw - 60)), NAVY)
        s.para(x0 + 26, yy + 192, learn, f(REG, 21), cw - 60, 30, GREY)
        s.text(x0 + 26, yy + ch - 26, "Pick it if " + pick, f(MED, fit(s, "Pick it if " + pick, MED, 20, cw - 60)), ORANGE)
    horizon(s, n)
    navy_note(s, notes[p][0], notes[p][1], notes[p][2], seed=n)
    finish(s)
    s.save(n)

# ── 5–6 · universities ───────────────────────────────────────────────────────────────────────────
for p, group in enumerate(UNIS):
    n = p + 5
    s = page(n, f"Step 03 · Where to study ({p + 1}/2)", "TCU guidebook 2026/27")
    t1, t2 = ("Universities", "to know.") if p == 0 else ("More places", "to study.")
    ts = min(72, fit(s, t1 + " " + t2, BOLD, 72, W - 2 * M))
    s.text(M - 4, 210, t1, f(BOLD, ts), NAVY)
    s.text(M - 4 + s.width(t1, f(BOLD, ts)) + 20, 210, t2, f(BOLD, ts), ORANGE)
    y = 330
    for j, (abbr, name, city, courses, site) in enumerate(group):
        s.text(M, y + 4, abbr, f(BOLD, fit(s, abbr, BOLD, 34, 150)), ORANGE if j % 2 == 0 else NAVY)
        cw_ = smallcaps(s, W - M, y - 6, city, 14, GREY, anchor="right")
        s.text(M + 180, y - 4, name, f(SEMI, fit(s, name, SEMI, 25, W - 2 * M - 180 - cw_ - 20)), NAVY)
        s.text(W - M, y + 32, site, f(SEMI, 19), ORANGE, anchor="rs")
        sw_ = s.width(site, f(SEMI, 19))
        s.text(M + 180, y + 32, courses, f(REG, fit(s, courses, REG, 21, W - 2 * M - 180 - sw_ - 24)), GREY)
        if j < len(group) - 1:
            hairline(s, M, W - M, y + 74, RULE)
        y += 136
    horizon(s, n)
    if p == 0:
        navy_note(s, "Want to know more?", "Visit each website for courses, fees and how to apply.", "Tembelea tovuti zao", seed=n)
    else:
        navy_note(s, "Not the full list", "Full list: tcu.go.tz (degrees) · nactvet.go.tz (diplomas)", "Orodha kamili iko TCU na NACTVET", seed=n)
    finish(s)
    s.save(n)

# ── 7 · entry requirements ───────────────────────────────────────────────────────────────────────
s = page(7, "Step 04 · Check the entry rules")
s.text(M - 4, 230, "Maths opens", f(BOLD, 92), NAVY)
s.text(M - 4, 330, "most doors.", f(BOLD, 92), ORANGE)
s.para(M, 400, "Two principal passes at A-Level, but which subjects? Real examples:", f(REG, 26), 820, 38, GREY)
reqs = [("UDSM", "Computer Science", "Advanced Maths + Physics or Computer Science"),
        ("UDOM", "Software Engineering", "Maths + Physics or Computer Science"),
        ("MUST", "Computer Science", "Adv. Maths + Physics or Chemistry, plus D in O-Level Maths & English"),
        ("ARU", "Data Science & AI", "Maths + one of Physics, Geography, Chemistry, Computer Science, Economics...")]
y = 500
for abbr, course, rule in reqs:
    card(s, (M, y, W - M - 8, y + 110), r=14)
    s.text(M + 26, y + 46, abbr, f(BOLD, 28), ORANGE)
    s.text(M + 150, y + 46, course, f(SEMI, 27), NAVY)
    s.text(M + 26, y + 88, rule, f(REG, fit(s, rule, REG, 21, W - 2 * M - 70)), GREY)
    y += 128
horizon(s, 7)
navy_note(s, "Do this", "Download the TCU guidebook and match your combination.", "Hesabu ni ufunguo", seed=7)
finish(s)
s.save(7)

# ── 8 · research checklist ───────────────────────────────────────────────────────────────────────
s = page(8, "Step 05 · Research before you apply")
paste_print(s, print_art("research", k(380)), 640, 130)
s.text(M - 4, 230, "Research", f(BOLD, 92), NAVY)
s.text(M - 4, 330, "the place.", f(BOLD, 92), ORANGE)
s.text(M, 410, "Chunguza kabla ya kuchagua", f(SIG, 50), ORANGE)
swash(s, M + 6, M + 480, 436, ORANGE, 5, seed=8)
checks = [("Is it accredited?", "TCU or NACTVET lists"),
          ("Read the curriculum", "not just the course name"),
          ("Labs and computers", "enough for every student?"),
          ("Field practical", "links with real companies"),
          ("Where do alumni work?", "look them up on LinkedIn"),
          ("Fees, HESLB loan, rent", "the real total cost"),
          ("Talk to current students", "they'll tell you the truth")]
y = 520
for j, (a, b) in enumerate(checks):
    s.d.rounded_rectangle([k(M), k(y - 30), k(M + 34), k(y + 4)], radius=k(7), outline=NAVY, width=k(3))
    s.text(M + 56, y, a, f(SEMI, 30), NAVY)
    bx = M + 56 + s.width(a, f(SEMI, 30)) + 18
    s.text(bx, y + 4, b, f(SIG, fit(s, b, SIG, 38, W - M - bx)), ORANGE)
    if j < len(checks) - 1:
        hairline(s, M, W - M, y + 26, RULE)
    y += 70
horizon(s, 8)
navy_note(s, "Remember", "You're choosing 3 years of your life. Spend 3 days researching.")
finish(s)
s.save(8)

# ── 9 · your choice ──────────────────────────────────────────────────────────────────────────────
s = page(9, "Step 06 · Make your own choice")
paste_print(s, print_art("path", k(420)), 600, 128)
s.text(M, 300, "My story", f(SIG, 72), ORANGE)
swash(s, M + 6, M + 250, 326, ORANGE, 5, seed=4)
y = 490
for line, col_ in [("Division I in Form Four.", NAVY), ("Everyone expected A-Level.", NAVY),
                   ("I chose a Computer", ORANGE), ("Science diploma at MUST.", ORANGE)]:
    s.text(M - 4, y, line, f(BOLD, 52), col_)
    y += 66
s.para(M, y + 30, "Teachers, parents and relatives said it was the wrong choice. Some called it a college “for failed students.” "
       "I got hired as a software engineer before I even graduated.", f(REG, 25), W - 2 * M, 36, GREY)
s.para(M, y + 180, "Don't choose for prestige, or because your friends did. Choose the path where you'll actually learn.",
       f(SEMI, 28), W - 2 * M, 40, NAVY)
horizon(s, 9)
sticker(s, W - M - 170, wave_y(8 * W + W - M - 170) - 4, "Your life, your call", angle=-6, size=19)
navy_note(s, "The lesson", "Your path doesn't have to look like everyone else's.", "Uamuzi ni wako, si wa watu", seed=9)
finish(s)
s.save(9)

# ── 10 · closing ─────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
s.text(M - 6, 290, "Your turn.", f(BOLD, 112), NAVY)
s.text(M, 380, "Which course, and", f(BOLD, 50), ORANGE)
s.text(M, 444, "which university?", f(BOLD, 50), ORANGE)
s.text(M, 540, "Niambie kwenye comments", f(SIG, 52), ORANGE)
swash(s, M + 6, M + 440, 566, ORANGE, 5, seed=10)
rows = [("Save", "for application season"), ("Share", "with a Form Four or Six leaver"), ("Comment", "your course and university")]
y = 680
for j, (a, b) in enumerate(rows):
    s.text(M, y, f"{j + 1:02d}", f(BOLD, 22), ORANGE)
    s.text(M + 56, y, a, f(BOLD, 36), NAVY)
    s.text(M + 56, y + 40, b, f(REG, 24), GREY)
    y += 108
paste_print(s, print_art("cover", k(420)), 600, 640)
horizon(s, TOTAL)
smallcaps(s, M, BASE + 72, "Read the full post · Soma zaidi", 17, SOFT)
s.text(M, BASE + 132, POST_URL, f(BOLD, fit(s, POST_URL, BOLD, 40, W - 2 * M)), WHITE_T)
hairline(s, M, W - M, BASE + 162, (38, 60, 100))
s.text(M, BASE + 224, "Link in bio", f(SEMI, 24), SOFT)
s.text(W - M, BASE + 224, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(TOTAL)
print("ok")
