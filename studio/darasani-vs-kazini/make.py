"""Carousel: Darasani vs Kazini, what school teaches you about tech vs what the real world expects
(9 slides, 1080x1350, exported at 2x). Same editorial / print direction as techtember (panorama paper,
navy wave, seam badges, outlined numerals, print art, swashes, stickers). Each round splits into
school (left) vs work (right), then one lesson and one thing to do while you're still a student."""
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
POST_URL = "depriver.tech/blog/darasani-vs-kazini"

# ── print illustrations (600x420 art board, navy outlines, no faces) ─────────────────────────────
# Every round: the school object on the left, the work object on the right, a dashed divider between.
HAND = 'font-family="Mr Dafoe" fill="#0b1e3f"'
MONO = 'font-family="Liberation Mono" font-weight="700"'
SPLIT = '<path d="M300 40 V380" stroke="#0b1e3f" stroke-width="4" stroke-dasharray="4 14" stroke-linecap="round" opacity=".45"/>'


def sheet(x, y, w, h, angle=-5):
    """Ruled exam paper with a red margin line."""
    lines = "".join(f'<path d="M{x + 14} {y + 50 + i * 30} h{w - 28}" stroke="#a9c4f5" stroke-width="3"/>' for i in range(int((h - 60) / 30)))
    return (f'<g transform="rotate({angle} {x + w / 2} {y + h / 2})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#fff" {ST}/>'
            f'{lines}<path d="M{x + 40} {y + 6} V{y + h - 6}" stroke="#e8603a" stroke-width="3" opacity=".7"/>')


def pencil(x, y, angle=35):
    return (f'<g transform="translate({x} {y}) rotate({angle})"><rect x="-12" y="-110" width="24" height="150" fill="#ffc857" {ST} stroke-width="5"/>'
            f'<rect x="-12" y="-128" width="24" height="22" rx="4" fill="#e8603a" {ST} stroke-width="5"/>'
            f'<path d="M-12 40 L0 72 L12 40z" fill="#f3dcb4" {ST} stroke-width="5"/><path d="M-4 62 L0 72 L4 62z" fill="#0b1e3f"/></g>')


def screen(x, y, w, h, body):
    """Laptop: dark screen with `body` drawn inside, sitting on a keyboard base."""
    return (f'<path d="M{x - 26} {y + h} h{w + 52} l22 30 H{x - 48}z" fill="#c9d4ea" {ST}/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#fff" {ST}/>'
            f'<rect x="{x + 14}" y="{y + 14}" width="{w - 28}" height="{h - 28}" rx="6" fill="#0b1e3f"/>{body}')


ART.update({
    "cover": svg(GROUND + f'''
      {sheet(40, 60, 230, 300, -7)}
        <text x="96" y="140" {HAND} font-size="30">for(i=0; i&lt;n; i++)</text>
        <text x="110" y="200" {HAND} font-size="30">print(i)</text>
        <text x="96" y="260" {HAND} font-size="30">x = 5</text>
        <ellipse cx="162" cy="252" rx="22" ry="18" fill="none" stroke="#e8603a" stroke-width="4"/>
        <text x="190" y="330" font-family="Mr Dafoe" font-size="46" fill="#e8603a">-2</text></g>
      {pencil(250, 300, 28)}
      {screen(340, 110, 230, 170, '''
        <path d="M374 150 h40 M374 176 h90 M392 202 h70 M392 228 h50" stroke="#a9c4f5" stroke-width="8" stroke-linecap="round"/>
        <path d="M374 150 h18 M392 228 h20" stroke="#e8603a" stroke-width="8" stroke-linecap="round"/>
        <rect x="488" y="232" width="56" height="20" rx="10" fill="#3ddc84"/>''')}
      <g transform="translate(300 214)"><circle r="44" fill="#e8603a" {ST}/>
        <text x="0" y="14" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="38" fill="#fff">VS</text></g>'''),

    "paper": svg(GROUND + SPLIT + f'''
      {sheet(40, 50, 220, 300, -4)}
        <text x="92" y="128" {HAND} font-size="30">int total = 0</text>
        <text x="92" y="188" {HAND} font-size="30">total += x</text>
        <circle cx="236" cy="180" r="16" fill="none" stroke="#e8603a" stroke-width="4"/>
        <text x="92" y="248" {HAND} font-size="30">return total;</text>
        <text x="160" y="320" font-family="Mr Dafoe" font-size="50" fill="#e8603a">-2</text></g>
      {pencil(262, 320, 30)}
      {screen(340, 90, 220, 190, '''
        <path d="M370 130 h60 M370 160 h120 M386 190 h90 M370 220 h70" stroke="#a9c4f5" stroke-width="8" stroke-linecap="round"/>
        <path d="M386 200 q8 6 16 0 t16 0 t16 0 t16 0 t16 0" fill="none" stroke="#e8603a" stroke-width="4"/>''')}
      <g transform="translate(470 92) rotate(4)"><rect x="-80" y="-22" width="160" height="44" rx="12" fill="#ffc857" {ST} stroke-width="5"/>
        <text x="0" y="9" text-anchor="middle" {MONO} font-size="20" fill="#0b1e3f">';' expected</text></g>'''),

    "memory": svg(GROUND + SPLIT + f'''
      <g transform="rotate(-6 150 220)">{"".join(f'<rect x="{50 + i * 10}" y="{90 + i * 14}" width="200" height="130" rx="10" fill="{c}" {ST} stroke-width="5"/>' for i, c in enumerate(["#e7ecf6", "#fff", "#fff"]))}
        <text x="92" y="168" font-family="Poppins" font-weight="700" font-size="22" fill="#e8603a">DEFINE:</text>
        <path d="M92 192 h150 M92 218 h110" stroke="#c9d4ea" stroke-width="9" stroke-linecap="round"/></g>
      <g transform="translate(120 320)"><circle r="44" fill="#fff" {ST}/><path d="M0-26 V0 L18 12" fill="none" {ST} stroke-width="6"/>
        <path d="M-14-50 h28" {ST} stroke-width="8"/></g>
      <rect x="330" y="70" width="240" height="270" rx="16" fill="#fff" {ST}/>
      <path d="M330 120 V86 a16 16 0 0 1 16-16 h208 a16 16 0 0 1 16 16 v34z" fill="#0b1e3f" {ST}/>
      <rect x="352" y="140" width="196" height="40" rx="20" fill="#e7ecf6" {ST} stroke-width="4"/>
      <circle cx="378" cy="160" r="9" fill="none" {ST} stroke-width="4"/><path d="M385 167 l8 8" {ST} stroke-width="4"/>
      <text x="402" y="168" {MONO} font-size="18" fill="#0b1e3f">how to...</text>
      <path d="M356 214 h170 M356 244 h130 M356 274 h150 M356 304 h90" stroke="#c9d4ea" stroke-width="10" stroke-linecap="round"/>
      <path d="M356 214 h60" stroke="#a9c4f5" stroke-width="10" stroke-linecap="round"/>
      <g transform="translate(540 330)"><circle r="40" fill="#e8603a" {ST}/>
        <text x="0" y="12" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="34" fill="#fff">?!</text></g>'''),

    "git": svg(GROUND + SPLIT + f'''
      <g transform="rotate(-18 150 220)">
        <rect x="70" y="170" width="190" height="96" rx="18" fill="#e8603a" {ST}/>
        <rect x="20" y="188" width="56" height="60" rx="6" fill="#c9d4ea" {ST}/>
        <path d="M34 206 h12 M34 230 h12" stroke="#0b1e3f" stroke-width="6"/>
        <circle cx="236" cy="218" r="10" fill="#fff" {ST} stroke-width="4"/></g>
      <g transform="translate(140 108) rotate(-4)"><rect x="-108" y="-26" width="216" height="52" rx="8" fill="#fff" {ST} stroke-width="5"/>
        <text x="0" y="8" text-anchor="middle" {MONO} font-size="19" fill="#0b1e3f">final_FINAL2.zip</text></g>
      <path d="M150 300 c0 40 20 50 40 70" fill="none" {ST} stroke-width="4" stroke-dasharray="6 10"/>
      <path d="M360 330 V80 M360 270 C360 230 470 230 470 190 V150 C470 110 360 120 360 90" fill="none" stroke="#a9c4f5" stroke-width="12" stroke-linecap="round"/>
      {"".join(f'<circle cx="{x}" cy="{y}" r="18" fill="{c}" {ST} stroke-width="5"/>' for x, y, c in [(360, 320, "#fff"), (360, 250, "#fff"), (470, 190, "#ffc857"), (470, 150, "#ffc857"), (360, 160, "#fff"), (360, 90, "#e8603a")])}
      <g transform="translate(510 300)"><rect x="-58" y="-34" width="116" height="68" rx="14" fill="#fff" {ST} stroke-width="5"/>
        <text x="-28" y="10" font-family="Poppins" font-weight="700" font-size="26" fill="#0b1e3f">PR</text>
        <circle cx="30" cy="0" r="16" fill="#3ddc84" {ST} stroke-width="4"/><path d="M22 0 l6 6 l10-12" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/></g>'''),

    "users": svg(GROUND + SPLIT + f'''
      <g transform="rotate(-6 150 220)"><rect x="70" y="70" width="160" height="270" rx="22" fill="#c9d4ea" {ST}/>
        <rect x="90" y="92" width="120" height="56" rx="8" fill="#e7ecf6" {ST} stroke-width="4"/>
        <text x="198" y="132" text-anchor="end" {MONO} font-size="28" fill="#0b1e3f">2+2</text>
        {"".join(f'<rect x="{90 + c * 42}" y="{166 + r * 42}" width="32" height="32" rx="8" fill="{"#e8603a" if c == 2 else "#fff"}" {ST} stroke-width="4"/>' for r in range(4) for c in range(3))}</g>
      <rect x="380" y="70" width="140" height="280" rx="24" fill="#0b1e3f" {ST}/>
      <rect x="394" y="100" width="112" height="220" rx="10" fill="#e7ecf6"/>
      <text x="450" y="150" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="20" fill="#0b1e3f">TSh 25,000</text>
      <circle cx="450" cy="210" r="32" fill="#3ddc84" {ST} stroke-width="5"/>
      <path d="M434 210 l12 12 l20-24" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
      <rect x="410" y="268" width="80" height="28" rx="10" fill="#e8603a"/>
      {"".join(f"""<g transform="translate({x} {y})"><path d="M-30 48 a30 28 0 0 1 60 0z" fill="{shirt}" {ST} stroke-width="5"/>
        <circle r="24" fill="{skin}" {ST} stroke-width="5"/><path d="M-23 -6 a24 24 0 0 1 46 0 a20 15 0 0 0-46 0z" fill="#0b1e3f"/></g>"""
        for x, y, skin, shirt in [(560, 120, "#8d5524", "#ffc857"), (560, 250, "#6b3e1d", "#a9c4f5"), (342, 300, "#a0673a", "#e8603a")])}'''),

    "deploy": svg(GROUND + SPLIT + f'''
      {sheet(50, 50, 210, 310, -3)}
        {"".join(f'<rect x="{96}" y="{84 + i * 36}" width="130" height="28" rx="4" fill="{"#ffc857" if i == 3 else "#fff"}" {ST} stroke-width="4"/><text x="161" y="{104 + i * 36}" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="16" fill="#0b1e3f">{7 - i}</text>' for i in range(7))}
        <text x="100" y="346" {HAND} font-size="30">OSI model</text></g>
      <rect x="350" y="110" width="170" height="250" rx="14" fill="#0b1e3f" {ST}/>
      {"".join(f'<rect x="366" y="{128 + i * 58}" width="138" height="42" rx="6" fill="#26406c" {ST} stroke-width="4"/><circle cx="386" cy="{149 + i * 58}" r="7" fill="{c}"/><path d="M406 {149 + i * 58} h80" stroke="#a9c4f5" stroke-width="6" stroke-linecap="round" opacity=".7"/>' for i, c in enumerate(["#3ddc84", "#3ddc84", "#e8603a", "#3ddc84"]))}
      <path d="M560 42 a36 36 0 1 0 30 52 a28 28 0 1 1-30-52z" fill="#ffc857" {ST} stroke-width="5"/>
      <text x="508" y="70" font-family="Poppins" font-weight="700" font-size="20" fill="#0b1e3f">3am</text>
      <g transform="translate(540 300)"><path d="M0-44 L44 34 H-44z" fill="#e8603a" {ST} stroke-width="5"/>
        <path d="M0-14 v22" stroke="#fff" stroke-width="8" stroke-linecap="round"/><circle cy="22" r="5" fill="#fff"/></g>'''),

    "proof": svg(GROUND + SPLIT + f'''
      <g transform="rotate(-5 150 210)"><rect x="40" y="80" width="230" height="170" rx="8" fill="#fff" {ST}/>
        <rect x="54" y="94" width="202" height="142" rx="4" fill="none" stroke="#ffc857" stroke-width="5"/>
        <text x="155" y="140" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="22" fill="#0b1e3f">CERTIFICATE</text>
        <path d="M90 170 h130 M110 196 h90" stroke="#c9d4ea" stroke-width="8" stroke-linecap="round"/></g>
      <g transform="translate(220 270)"><path d="M-20 20 L-30 80 L0 64 L30 80 L20 20z" fill="#e8603a" {ST} stroke-width="5"/>
        <circle r="38" fill="#ffc857" {ST}/><text x="0" y="9" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="22" fill="#0b1e3f">GPA</text></g>
      <rect x="330" y="70" width="240" height="280" rx="16" fill="#fff" {ST}/>
      <path d="M330 120 V86 a16 16 0 0 1 16-16 h208 a16 16 0 0 1 16 16 v34z" fill="#0b1e3f" {ST}/>
      <circle cx="356" cy="95" r="7" fill="#fff"/><circle cx="378" cy="95" r="7" fill="#fff"/><circle cx="400" cy="95" r="7" fill="#fff"/>
      <circle cx="380" cy="168" r="26" fill="#a9c4f5" {ST} stroke-width="5"/><path d="M420 160 h120 M420 184 h80" stroke="#c9d4ea" stroke-width="9" stroke-linecap="round"/>
      {"".join(f'<rect x="{352 + c * 28}" y="{222 + r * 28}" width="22" height="22" rx="4" fill="{["#e7ecf6", "#a8e6c1", "#3ddc84", "#2f9e5e"][(r * 5 + c * 3 + r * c) % 4]}"/>' for r in range(4) for c in range(7))}'''),

    "house": svg(GROUND + f'''
      <rect x="70" y="300" width="460" height="64" rx="6" fill="#c9d4ea" {ST}/>
      <text x="300" y="344" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="28" fill="#0b1e3f" letter-spacing="6">MSINGI</text>
      <path d="M120 300 V180 L300 70 L480 180 V300" fill="none" stroke="#e8603a" stroke-width="8" stroke-dasharray="20 14" stroke-linecap="round"/>
      {"".join(f'<rect x="{130 + c * 72}" y="{250 - r * 40}" width="66" height="34" rx="4" fill="#fff" {ST} stroke-width="5"/>' for r, cols in enumerate([5, 5, 3]) for c in range(cols) if not (r == 2 and c == 2))}
      <g transform="translate(470 120) rotate(-20)"><rect x="-40" y="-12" width="80" height="24" rx="4" fill="#ffc857" {ST} stroke-width="5"/>
        <rect x="-6" y="12" width="12" height="70" rx="4" fill="#e8603a" {ST} stroke-width="5"/></g>'''),
})

ROUNDS = [
    ("paper", "Code on paper", "vs. code on screen.",
     "Java on paper in the exam. One missing ; and the marks are gone.",
     "An editor, a linter, autocomplete. You run the code fifty times a day.",
     "Mantiki kwanza, sintaksia baadaye", "Type your paper code on a computer the same day."),
    ("memory", "Memorise it", "vs. find it.",
     "Exams reward cramming definitions word for word.",
     "Nobody memorises everything. Seniors search, read docs and ask all day.",
     "Hakuna anayekariri kila kitu", "Practise reading official docs, not only notes."),
    ("git", "Group work", "vs. teamwork.",
     "One person does the whole group work. The rest just add their names.",
     "Everyone ships. Git and code review show exactly who did what.",
     "Kazi ya kikundi, si ya mtu mmoja", "Do your part, and put it on GitHub from day one."),
    ("users", "Toy projects", "vs. real users.",
     "A calculator. A student system. Your lecturer is the only user.",
     "Real people, real money, slow networks and every edge case you forgot.",
     "Mteja hasomi code yako", "Build one thing a real person uses, every semester."),
    ("deploy", "Diagrams", "vs. production.",
     "Draw the OSI model and the waterfall SDLC for marks.",
     "Servers, domains, deploys, and something breaking at 3 a.m.",
     "Kwangu inafanya kazi, haitoshi", "Deploy your project online, even on a free tier."),
    ("proof", "Grades", "vs. GitHub.",
     "GPA and certificates are the scoreboard.",
     "“Show me what you've built.” I got hired while still a student.",
     "Vitendo vinaongea zaidi", "Keep three projects you can demo in two minutes."),
]
assert len(ROUNDS) + 3 == TOTAL
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


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "School vs real-world tech")
s.text(M - 6, 250, "I learnt to code", f(BOLD, 92), NAVY)
s.text(M - 8, 380, "on paper.", f(BOLD, 150), ORANGE)
s.text(M - 4, 462, "Then I got a real job.", f(BOLD, 60), NAVY)
s.text(M, 556, "Darasani vs Kazini", f(SIG, 64), ORANGE)
swash(s, M + 8, M + 440, 584, ORANGE, 6)
s.para(M, 670, "6 differences between school and real-world tech, and what to do while you're still a student.",
       f(REG, 27), 360, 40, GREY)
paste_print(s, print_art("cover", k(600)), 440, 560)
horizon(s, 1)
sticker(s, 800, 540, "from student to software engineer", angle=-5, size=19)
s.text(M, 1262, "Swipe for round 1", f(SEMI, 30), WHITE_T)
arrow(s, M + s.width("Swipe for round 1", f(SEMI, 30)) + 34, 1251)
s.text(W - M, 1262, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(1)

# ── 2–7 · rounds ─────────────────────────────────────────────────────────────────────────────────
COL = 520
for i, (art_key, t1, t2, school, work, sw, tip) in enumerate(ROUNDS):
    n = i + 2
    s = page(n, f"Round {i + 1:02d} / 06", "Darasani vs Kazini")
    outline_text(s, W - M + 20, 560, f"{i + 1:02d}", f(BOLD, 360), stroke=3, color=RULE, anchor="rs")
    paste_print(s, print_art(art_key, k(620)), 40, 136)

    size = min(fit(s, t1, BOLD, 80, W - 2 * M), fit(s, t2, BOLD, 80, W - 2 * M))
    s.text(M - 4, 660, t1, f(BOLD, size), NAVY)
    s.text(M - 4, 660 + size * 1.02, t2, f(BOLD, size), ORANGE)

    top = 660 + size * 1.02 + 70
    smallcaps(s, M, top, "Darasani · School", 16, GREY)
    smallcaps(s, COL + 40, top, "Kazini · Real world", 16, ORANGE)
    s.rect(COL, top - 22, COL + 2, top + 150, RULE)
    s.para(M, top + 46, school, f(REG, 25), COL - M - 30, 36, GREY)
    s.para(COL + 40, top + 46, work, f(MED, 25), W - M - COL - 40, 36, NAVY)

    horizon(s, n)
    sticker(s, W - M - 130, wave_y((n - 1) * W + W - M - 130) - 4, "Somo", angle=-6, size=20)
    smallcaps(s, M, BASE + 74, "Still in school? Do this", 16, ORANGE)
    s.text(M, BASE + 130, tip, f(SEMI, fit(s, tip, SEMI, 31, W - 2 * M)), WHITE_T)
    sws = fit(s, sw, SIG, 54, W - 2 * M - 40)
    s.text(M, BASE + 214, sw, f(SIG, sws), ORANGE)
    swash(s, M + 6, M + min(s.width(sw, f(SIG, sws)) * 0.9, 620), BASE + 238, ORANGE, 5, seed=i)
    finish(s)
    s.save(n)

# ── 8 · advice ───────────────────────────────────────────────────────────────────────────────────
s = page(8, "Advice for students · Ushauri")
s.text(M - 6, 250, "Still in school?", f(BOLD, 96), NAVY)
s.text(M - 6, 350, "Start now.", f(BOLD, 96), ORANGE)
s.para(M, 420, "School isn't useless. Paper code trains your logic. Just don't stop there.", f(REG, 26), 760, 38, GREY)
items = [("Type up your paper code", "same day"),
         ("Ship a real project", "every semester"),
         ("Live on GitHub", "commit, push, repeat"),
         ("Use AI as a tutor", "not a copy machine"),
         ("Treat field practical", "like a real job"),
         ("Respect the fundamentals", "DSA, logic, maths")]
y = 560
for j, (a, b) in enumerate(items):
    s.text(M, y, f"{j + 1:02d}", f(BOLD, 22), ORANGE)
    s.text(M + 56, y, a, f(SEMI, 32), NAVY)
    bx = M + 56 + s.width(a, f(SEMI, 32)) + 18
    s.text(bx, y + 4, b, f(SIG, fit(s, b, SIG, 40, W - M - bx)), ORANGE)
    if j < len(items) - 1:
        hairline(s, M, W - M, y + 30, RULE)
    y += 76
horizon(s, 8)
smallcaps(s, M, BASE + 74, "The short version", 17, SOFT)
s.text(M, BASE + 140, "Learn it in class. Prove it in projects.", f(SEMI, fit(s, "Learn it in class. Prove it in projects.", SEMI, 36, W - 2 * M)), WHITE_T)
s.text(W - M, BASE + 224, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
sticker(s, 880, 170, "Save this one", angle=6, size=20)
finish(s)
s.save(8)

# ── 9 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
s.text(M, 230, "Shule inakupa msingi,", f(SIG, fit(s, "Shule inakupa msingi,", SIG, 84, W - 2 * M)), NAVY)
s.text(M, 330, "nyumba unajenga wewe.", f(SIG, fit(s, "nyumba unajenga wewe.", SIG, 84, W - 2 * M)), ORANGE)
swash(s, M + 6, M + 600, 362, ORANGE, 6, seed=9)
s.text(M, 430, "School lays the foundation. You build the house.", f(MED, 27), GREY)
s.text(M - 4, 540, "Your turn.", f(BOLD, 84), NAVY)
s.para(M, 600, "What did school teach you that work never asked for?", f(SEMI, 34), 470, 46, ORANGE)
s.text(M, 790, "Niambie kwenye comments", f(SIG, 46), ORANGE)
paste_print(s, print_art("house", k(540)), 500, 600)
horizon(s, TOTAL)
smallcaps(s, M, BASE + 72, "Read the full post · Soma zaidi", 17, SOFT)
s.text(M, BASE + 132, POST_URL, f(BOLD, fit(s, POST_URL, BOLD, 40, W - 2 * M)), WHITE_T)
hairline(s, M, W - M, BASE + 162, (38, 60, 100))
s.text(M, BASE + 224, "Link in bio", f(SEMI, 24), SOFT)
s.text(W - M, BASE + 224, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(TOTAL)
print("ok")
