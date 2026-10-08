"""Carousel: the best first programming language + framework for a beginner, and where to start (12 slides, 1080x1350,
exported at 2x). Explains the concept first (language = bricks, framework = a house frame already standing), then picks
by goal, the routes, when you're ready for a framework, a 12-week plan and free places to start."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 12
POST_URL = "depriver.tech/blog/first-language-and-framework"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # flow, table, tick lists, code windows

BRICK = 'fill="#e8603a"'
ART.update({
    "bricks": svg(GROUND + "".join(
        f'<rect x="{110 + c * 96 + (48 if r % 2 else 0)}" y="{300 - r * 52}" width="88" height="44" rx="5" {BRICK} {ST}/>'
        for r in range(4) for c in range(4 if r % 2 else 4) if 110 + c * 96 + (48 if r % 2 else 0) < 470) + f'''
      <path d="M430 120 l70 -50 l26 26 l-60 64z" fill="#c9d4ea" {ST}/>
      <path d="M436 150 l-34 40" {ST} fill="none"/>
      <text x="300" y="80" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="34" fill="#0b1e3f">if · for · def</text>'''),
    "frame": svg(GROUND + f'''
      <path d="M90 380 h420" {ST} fill="none"/>
      <path d="M120 380 V190 M480 380 V190 M300 380 V190 M210 380 V190 M390 380 V190" stroke="#c9a46a" stroke-width="16" stroke-linecap="round"/>
      <path d="M120 380 V190 M480 380 V190 M300 380 V190 M210 380 V190 M390 380 V190" {ST} fill="none" stroke-width="4"/>
      <path d="M100 196 L300 60 L500 196" fill="none" stroke="#0b1e3f" stroke-width="14" stroke-linejoin="round" stroke-linecap="round"/>
      <path d="M120 286 h360 M120 196 h360" stroke="#0b1e3f" stroke-width="8" stroke-linecap="round"/>
      <rect x="226" y="300" width="148" height="80" rx="6" fill="#e8603a" {ST}/>
      <text x="300" y="350" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="26" fill="#fff">your app</text>
      <rect x="138" y="214" width="56" height="54" rx="4" fill="#a9c4f5" {ST} stroke-width="4"/>
      <rect x="406" y="214" width="56" height="54" rx="4" fill="#a9c4f5" {ST} stroke-width="4"/>'''),
})


def concept_card(s, box, art, label, big, text):
    x0, y0, x1, y1 = box
    card(s, box)
    paste_print(s, print_art(art, k(x1 - x0 - 60)), x0 + 30, y0 + 18, offset=(6, 8))
    ty = y0 + 18 + (x1 - x0 - 60) * 0.7 + 30
    smallcaps(s, x0 + 30, ty, label, 15, ORANGE)
    ty = s.para(x0 + 30, ty + 52, big, f(BOLD, 32), x1 - x0 - 60, 40, NAVY)
    s.para(x0 + 30, ty + 18, text, f(REG, 23), x1 - x0 - 60, 33, GREY)


def route_card(s, y, h, label, steps, why, build):
    card(s, (M, y, W - M - 8, y + h), r=16)
    s.rect(M + 2, y + 2, M + 12, y + h - 2, ORANGE)
    smallcaps(s, M + 36, y + 44, label, 15, ORANGE)
    x = M + 36
    for i, st in enumerate(steps):
        ww = s.width(st, f(BOLD, 30)) + 40
        s.d.rounded_rectangle([k(x), k(y + 60), k(x + ww), k(y + 106)], radius=k(23), fill=NAVY if i < len(steps) - 1 else ORANGE)
        s.text(x + ww / 2, y + 83, st, f(BOLD, 30), WHITE_T, anchor="mm")
        x += ww
        if i < len(steps) - 1:
            arrow(s, x + 26, y + 83, NAVY, 3.4, 11)
            x += 56
    s.text(M + 36, y + 146, why, f(SEMI, fit(s, why, SEMI, 25, W - 2 * M - 70)), NAVY)
    s.text(M + 36, y + 180, "Build first: " + build, f(REG, fit(s, "Build first: " + build, REG, 23, W - 2 * M - 70)), GREY)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Beginners · Wanaoanza")
s.text(M - 6, 250, "Your first", f(BOLD, 108), NAVY)
s.text(M - 6, 366, "language +", f(BOLD, 108), NAVY)
s.text(M - 8, 498, "framework.", f(BOLD, 128), ORANGE)
s.text(M, 588, "Anza hapa, bila kuchanganyikiwa", f(SIG, 54), NAVY)
swash(s, M + 8, M + 560, 612, ORANGE, 6)
s.para(M, 700, "What they are, which to pick for your goal, and exactly where to start for free.", f(REG, 27), 440, 40, GREY)
paste_print(s, print_art("frame", k(500)), 520, 620)
sticker(s, W - M - 170, 680, "Python? JavaScript? Flutter?", angle=-5, size=19, bg=NAVY)
horizon(s, 1)
cover_footer(s, "Swipe, start the right way")
finish(s)
s.save(1)

# ── 2 · the concept ──────────────────────────────────────────────────────────────────────────────
s = page(2, "The concept · Dhana")
title2(s, "Language vs", "framework.", y=220, size=88)
mid = W / 2
concept_card(s, (M, 380, mid - 14, 990), "bricks", "Language · Lugha", "The words and grammar.",
             "How you give the computer instructions. Python, JavaScript, Dart, PHP.")
concept_card(s, (mid + 14, 380, W - M - 8, 990), "frame", "Framework", "A ready-made structure.",
             "Code someone already wrote for common jobs. Django, React, Flutter, Laravel.")
horizon(s, 2)
navy_note(s, "Think of it like", "Language = bricks. Framework = a house frame already standing.", "Lugha kwanza, framework baadaye", seed=2)
finish(s)
s.save(2)

# ── 3 · what a framework does ────────────────────────────────────────────────────────────────────
s = page(3, "Why frameworks exist · Kwa nini")
title2(s, "Building a", "shop website?", y=220, size=88)
half = (W - 2 * M) / 2 - 10
smallcaps(s, M, 410, "Language only: you write", 15, RED_NO)
tick_list(s, ["Login & passwords", "Links between pages", "Database code", "Security", "Forms & checks"], 470, x=M, size=28, ok=False, maxw=half)
smallcaps(s, mid + 10, 410, "With a framework: ready", 15, GREEN_OK)
tick_list(s, ["Login & passwords", "Links between pages", "Database code", "Security", "Forms & checks"], 470, x=mid + 10, size=28, maxw=half)
card(s, (M, 790, W - M - 8, 950), r=16)
s.para(M + 30, 850, "So you spend your time on the shop itself: products, cart, M-Pesa. Not on rebuilding what everyone needs.",
       f(SEMI, 27), W - 2 * M - 70, 38, NAVY)
horizon(s, 3)
navy_note(s, "But remember", "A framework is still the language. Weak Python = lost in Django.", "Msingi ndio kila kitu", seed=3)
finish(s)
s.save(3)

# ── 4 · pick by goal ─────────────────────────────────────────────────────────────────────────────
s = page(4, "Pick by goal · Chagua kwa lengo")
title2(s, "What do you", "want to build?", y=220, size=86)
table(s, M, 400, ["I want to build", "Language", "Framework"],
      [["Websites", "JavaScript", "React"], ["Backend & APIs", "Python", "Django / FastAPI"], ["Mobile apps", "Dart", "Flutter"],
       ["Data & AI", "Python", "pandas, scikit-learn"], ["Business systems", "PHP", "Laravel"]],
      [330, 250, 348], size=27, rh=80)
s.para(M, 935, "Websites start with HTML & CSS first. They are not programming languages, but every web route needs them.",
       f(REG, 23), W - 2 * M, 32, GREY)
horizon(s, 4)
navy_note(s, "Golden rule", "One goal. One language. One framework. Three months.", "Kimoja kwa wakati", seed=4)
finish(s)
s.save(4)

# ── 5 · my pick ──────────────────────────────────────────────────────────────────────────────────
s = page(5, "Not sure? · Huna uhakika?")
title2(s, "Still not sure?", "Start with Python.", y=220, size=84)
y = tick_list(s, [("Reads almost like English", None), ("One language: web, data, AI, automation", None),
                  ("Thousands of free courses", None)], 420, size=29)
code_window(s, y + 10, ['name = input("Jina lako? ")', 'print("Karibu, " + name)', "for i in range(3):",
                        '    print("Ninajifunza Python!")'], file="hello.py", size=25, lh=44)
horizon(s, 5)
navy_note(s, "Prefer websites?", "Pick JavaScript. It runs in every browser, even on your phone.", "Zote mbili ni nzuri", seed=5)
finish(s)
s.save(5)

# ── 6 · the web route ────────────────────────────────────────────────────────────────────────────
s = page(6, "Route 01 · The web")
title2(s, "The web route,", "step by step.", y=220, size=84)
flow(s, [("HTML", "The structure: headings, text, images"), ("CSS", "The style: colours, layout, phone screens"),
         ("JavaScript", "The language: buttons, logic, data"), ("React", "The framework: big apps in small pieces"),
         ("Git + deploy", "Put it online for free")], 400, h=94, gap=28, size=30)
horizon(s, 6)
navy_note(s, "Build", "A portfolio site first, then a to-do app in React.", "Jenga huku ukijifunza", seed=6)
finish(s)
s.save(6)

# ── 7 · other routes ─────────────────────────────────────────────────────────────────────────────
s = page(7, "More routes · Njia nyingine")
title2(s, "Other routes", "that work.", y=220, size=88)
route_card(s, 370, 196, "Mobile apps", ["Dart", "Flutter"], "One codebase for Android and iPhone.", "an expense tracker")
route_card(s, 576, 196, "Backend & data", ["Python", "Django"], "Login, admin panel and database come ready.", "a school library system")
route_card(s, 782, 196, "Business systems", ["PHP", "Laravel"], "Cheap hosting everywhere, many local jobs.", "a duka stock system")
horizon(s, 7)
navy_note(s, "Pattern", "Language first, then its framework. Never the other way.", "Hatua kwa hatua", seed=7)
finish(s)
s.save(7)

# ── 8 · ready for a framework ────────────────────────────────────────────────────────────────────
s = page(8, "Checklist · Uko tayari?")
title2(s, "Ready for a", "framework?", y=220, size=90)
tick_fill(s, [("Variables & data types", "Text, numbers, true/false, without looking them up."),
              ("If/else and loops", "Written by you, not copied."),
              ("Functions", "That take inputs and return a result."),
              ("Lists & dictionaries", "Arrays and objects in JavaScript."),
              ("Read an error", "And find the line that broke."),
              ("A small app, no tutorial", "A calculator, a quiz, a shopping list.")], 410, 990, size=29, sub=23, max_gap=64)
horizon(s, 8)
navy_note(s, "Usually", "4 to 8 weeks of daily practice in the language first.", "Usiruke hatua", seed=8)
finish(s)
s.save(8)

# ── 9 · where to start: the plan ─────────────────────────────────────────────────────────────────
s = page(9, "Where to start · Anzia hapa")
title2(s, "Your first", "12 weeks.", y=220, size=92)
flow(s, [("Week 1–2 · Set up", "Install VS Code + your language. Print \"Hello\"."),
         ("Week 3–5 · The basics", "Variables, if/else, loops, functions, lists."),
         ("Week 6 · First project", "Build something small with no tutorial."),
         ("Week 7–10 · The framework", "Its official tutorial, then your own version."),
         ("Week 11–12 · Ship it", "Deploy it, push to GitHub, share the link.")], 400, h=94, gap=28, size=29)
horizon(s, 9)
navy_note(s, "Daily", "One hour a day beats seven hours on Sunday.", "Kidogo kidogo", seed=9)
finish(s)
s.save(9)

# ── 10 · free resources ──────────────────────────────────────────────────────────────────────────
s = page(10, "Free resources · Bure kabisa")
title2(s, "Where to learn,", "for free.", y=220, size=86)
numbered(s, [("Python", "CS50P by Harvard (free) · the python.org tutorial"),
             ("Web: HTML, CSS, JavaScript", "freeCodeCamp · The Odin Project · MDN docs"),
             ("React", "react.dev, the official \"Learn\" section"),
             ("Flutter", "docs.flutter.dev codelabs"),
             ("Django", "The Django Girls tutorial"),
             ("Laravel", "Laravel Bootcamp")], 420, gap=96, ts=30, bs=23)
horizon(s, 10)
navy_note(s, "One more", "Watch in Swahili or English, but always type the code yourself.", "Andika mwenyewe", seed=10)
finish(s)
s.save(10)

# ── 11 · mistakes ────────────────────────────────────────────────────────────────────────────────
s = page(11, "Avoid these · Epuka")
title2(s, "Beginner", "mistakes.", y=220, size=96)
tick_fill(s, [("Switching languages every week", "You restart at zero every time."),
              ("React before JavaScript", "You'll copy code you can't understand."),
              ("Tutorial hell", "Watching 50 videos, building nothing."),
              ("Arguing about the \"best\" language", "Companies hire people who build."),
              ("Pasting AI code you can't explain", "Use AI as a tutor, not a copy machine.")], 410, 990, size=29, sub=23, ok=False, max_gap=44)
horizon(s, 11)
navy_note(s, "Truth", "The best language is the one you finish a project in.", "Maliza unachoanza", seed=11)
finish(s)
s.save(11)

# ── 12 · closing ─────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which language + framework", "are you picking?", [("Comment", "your pick and your goal"), ("Save", "the 12-week plan"),
                                                           ("Share", "with a friend starting tech")])
paste_print(s, print_art("bricks", k(360)), 660, 680)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
