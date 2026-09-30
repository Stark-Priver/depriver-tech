"""'Coding basics for beginners' carousel for Privatus Cosmas (12 slides, 1080x1350).
Beginner languages, core concepts with code, tech-life tools, tips & tricks.
Reuses the design system (fonts, colours, Slide helpers) from the intro carousel so the series matches."""
import re

import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers

TOTAL = 12
MONO = FONTS + "LiberationMono-Regular.ttf"
MONO_B = FONTS + "LiberationMono-Bold.ttf"
WHITE_T = (255, 255, 255)
SOFT = (196, 208, 232)       # light text on navy
MUTED = (122, 140, 176)      # comments on navy
GREEN = (152, 214, 160)      # strings
KEYWORDS = {"if", "else", "elif", "for", "in", "while", "def", "return", "True", "False", "print"}


def mono(size, bold=False):
    return ImageFont.truetype(MONO_B if bold else MONO, int(size * K))


class BSlide(Slide):
    def counter(self, n):
        self.text(W - 60, 70, f"{n:02d} / {TOTAL:02d}", f(MED, 18), GREY, anchor="rs")

    def save(self, n):
        self.im.save(f"{OUT}slide-{n}.jpg", quality=95)

    def fit(self, lines, font_name, max_size, maxw):
        size = max_size
        while size > 40 and any(self.width(t, f(font_name, size)) > maxw for t in lines):
            size -= 2
        return size

    def check(self, x, y, r=15, fill=ORANGE):
        self.d.ellipse([k(x - r), k(y - r), k(x + r), k(y + r)], fill=fill)
        self.d.line([k(x - 7), k(y), k(x - 2), k(y + 6), k(x + 8), k(y - 6)], fill=WHITE_T, width=k(3.4),
                    joint="curve")

    def header(self, label, l1, l2, max_size=96):
        self.text(90, 190, label, f(SEMI, 20), ORANGE)
        self.rect(90, 208, 150, 213, ORANGE)
        size = self.fit([l1, l2], BOLD, max_size, 900)
        self.text(88, 210 + size * 1.12, l1, f(BOLD, size), NAVY)
        self.text(88, 210 + size * 2.3, l2, f(BOLD, size), ORANGE)
        return 210 + size * 2.3

    def pill(self, x, y, t, fill=NAVY, fg=WHITE_T, size=24):
        font = f(SEMI, size)
        w = self.width(t, font) + 44
        self.rect(x, y, x + w, y + size * 2.2, fill, r=size * 1.1)
        self.text(x + 22, y + size * 1.1 + 1, t, font, fg, anchor="lm")
        return x + w

    def code(self, x0, y0, x1, lines, size=27, lh=46):
        """Navy editor card with light syntax highlighting. Returns bottom y."""
        y1 = y0 + 96 + len(lines) * lh + 24
        self.rect(x0, y0, x1, y1, NAVY, r=30)
        for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
            cx = x0 + 44 + i * 30
            self.d.ellipse([k(cx - 8), k(y0 + 38), k(cx + 8), k(y0 + 54)], fill=c)
        self.text(x1 - 40, y0 + 53, "PYTHON", f(MED, 15), MUTED, anchor="rs")
        fn, fb = mono(size), mono(size, True)
        cw = self.width("M", fn)
        for i, line in enumerate(lines):
            y = y0 + 110 + i * lh
            col = 0
            for tok in re.findall(r'#.*|f?"[^"]*"|\w+|\s+|.', line):
                if tok.startswith("#"):
                    c, ft = MUTED, fn
                elif tok.startswith('"') or tok.startswith('f"'):
                    c, ft = GREEN, fn
                elif tok in KEYWORDS:
                    c, ft = ORANGE, fb
                elif tok.replace(".", "").isdigit():
                    c, ft = BLUE, fn
                else:
                    c, ft = WHITE_T, fn
                self.text(x0 + 44 + col * cw, y, tok, ft, c)
                col += len(tok)
        return y1


# ── 1 · hook ─────────────────────────────────────────────
s = BSlide()
s.rect(0, 830, 560, 872, BLUE)
s.rect(0, 872, 560, H, NAVY)
s.photo(470, 780, fade="left")
s.text(96, 330, "New to programming? Start here.", f(MED, 30), NAVY)
lines = ["Coding", "Basics Made", "Simple"]
size = s.fit(lines, BOLD, 112, 570)
for i, (t, c) in enumerate(zip(lines, (NAVY, ORANGE, NAVY))):
    s.text(90, 470 + i * size * 1.24, t, f(BOLD, size), c)
s.rect(210, 1128, 380, 1170, ORANGE)
s.text(96, 1060, "Privatus", f(SIG, 112), WHITE_T)
s.text(170, 1170, "Cosmas", f(SIG, 112), WHITE_T)
s.swipe(640, 1150)
s.counter(1)
s.save(1)

# ── 2 · beginner languages ──────────────────────────────
s = BSlide()
s.header("STEP 1 · CHOOSE A LANGUAGE", "Best Beginner", "Languages", 92)
s.swipe(W - 70 - 214, 110)
langs = [
    ("Python", "AI, data, automation, backend", "Reads almost like plain English."),
    ("JavaScript", "Websites & web apps", "Runs in every browser. Instant results."),
    ("HTML & CSS", "Structure & style of web pages", "See your work on screen in minutes."),
    ("SQL", "Databases & data analysis", "Every business stores data. High demand."),
    ("Java", "Android, banking, big systems", "Teaches strong coding discipline."),
    ("Dart", "Mobile apps with Flutter", "One codebase for Android & iOS."),
]
gx0, gy0, gap = 70, 500, 18
cw_, ch_ = (W - 140 - gap) / 2, 244
cols = [NAVY, CHAR, (20, 52, 102), NAVY, CHAR, (20, 52, 102)]
for i, (name, best, why) in enumerate(langs):
    cx, cy = gx0 + (i % 2) * (cw_ + gap), gy0 + (i // 2) * (ch_ + gap)
    s.rect(cx, cy, cx + cw_, cy + ch_, cols[i], r=26)
    s.text(cx + 34, cy + 66, name, f(BOLD, 38), WHITE_T)
    s.rect(cx + 34, cy + 84, cx + 84, cy + 89, ORANGE)
    s.text(cx + 34, cy + 128, "BEST FOR", f(SEMI, 15), BLUE)
    s.text(cx + 34, cy + 160, best, f(MED, 21), WHITE_T)
    s.para(cx + 34, cy + 206, why, f(REG, 19), cw_ - 60, 28, SOFT)
s.counter(2)
s.save(2)

# ── 3 · pick by goal ────────────────────────────────────
s = BSlide()
s.header("STEP 2 · MATCH IT TO YOUR GOAL", "Pick by", "Your Goal", 104)
s.swipe(W - 70 - 214, 110)
goals = [("Websites", ["HTML & CSS", "JavaScript"]),
         ("Data & AI", ["Python", "SQL"]),
         ("Mobile apps", ["Dart / Flutter", "Kotlin"]),
         ("Automation", ["Python", "Bash"]),
         ("Games", ["C#", "Unity"])]
y = 500
for g, chips in goals:
    s.text(90, y + 38, g, f(BOLD, 34), NAVY)
    x = 420
    s.d.line([k(330), k(y + 27), k(390), k(y + 27)], fill=ORANGE, width=k(4))
    s.d.line([k(378), k(y + 17), k(390), k(y + 27), k(378), k(y + 37)], fill=ORANGE, width=k(4), joint="curve")
    for j, c in enumerate(chips):
        x = s.pill(x, y + 3, c, fill=ORANGE if j == 0 else NAVY) + 14
    s.rect(90, y + 84, W - 90, y + 86, (226, 228, 233))
    y += 106
cx0, cy0, cx1, cy1 = 70, 1060, W - 70, 1270
s.rect(cx0, cy0, cx1, cy1, NAVY, r=30)
s.text(cx0 + 50, cy0 + 62, "GOLDEN RULE", f(SEMI, 18), BLUE)
s.rect(cx0 + 50, cy0 + 80, cx0 + 110, cy0 + 85, ORANGE)
s.para(cx0 + 50, cy0 + 132, "Pick ONE language and stick with it for 3 months. The concepts transfer to every other language.",
       f(MED, 27), cx1 - cx0 - 100, 40, WHITE_T)
s.counter(3)
s.save(3)

# ── 4–8 · core concepts ─────────────────────────────────
concepts = [
    ("Variables &", "Data Types",
     "A variable is a labelled box that stores a value. The data type says what kind of value is inside.",
     ['name = "Asha"         # text (string)',
      'age = 21              # whole number (int)',
      'price = 4500.50       # decimal (float)',
      'is_student = True     # yes/no (boolean)'],
     ["Store and reuse information anywhere", "Name things clearly: total_price, not tp"]),
    ("Conditions", "(if / else)",
     "Conditions let your program make decisions: do this when something is true, otherwise do that.",
     ['if age >= 18:',
      '    print("You can vote")',
      'else:',
      '    print("Not yet, keep growing")'],
     ["Your app reacts to different situations", "Handle the edge cases: empty, zero, wrong input"]),
    ("Loops", "(for / while)",
     "Loops repeat work for you. Instead of writing the same line 100 times, write it once and loop.",
     ['fruits = ["mango", "banana", "avocado"]',
      'for fruit in fruits:',
      '    print(fruit)',
      '',
      'for i in range(3):     # 0, 1, 2',
      '    print("Hi", i)'],
     ["Process thousands of items in seconds", "Always make sure the loop can stop"]),
    ("Functions", "Reuse Your Code",
     "A function is a named block of code that does one job. Write it once, call it whenever you need it.",
     ['def greet(name):',
      '    return f"Hello, {name}!"',
      '',
      'print(greet("Asha"))  # Hello, Asha!'],
     ["No repeated code, fewer bugs, easy testing", "One function, one job, a clear verb name"]),
    ("Data", "Structures",
     "Ways to organise many values together. Lists keep things in order; dictionaries pair keys with values.",
     ['scores = [90, 75, 88]               # list',
      'user = {"name": "Asha", "age": 21}  # dict',
      'print(scores[0])     # 90',
      'print(user["name"])  # Asha'],
     ["Model real data: users, products, orders", "Lists start counting at 0, not 1"]),
]
for i, (l1, l2, body, snippet, why) in enumerate(concepts):
    n = i + 4
    s = BSlide()
    bottom = s.header(f"CORE CONCEPT {i + 1:02d} / 05", l1, l2, 92)
    s.swipe(W - 70 - 214, 110)
    y = s.para(92, bottom + 76, body, f(REG, 29), 900, 43, GREY)
    yb = s.code(70, y + 20, W - 70, snippet, size=29, lh=50 if len(snippet) > 4 else 56)
    s.text(90, yb + 80, "WHY IT MATTERS", f(SEMI, 19), ORANGE)
    s.rect(90, yb + 97, 150, yb + 102, ORANGE)
    for j, t in enumerate(why):
        yy = yb + 160 + j * 66
        s.check(106, yy - 10)
        s.text(140, yy, t, f(MED, 29), INK)
    s.counter(n)
    s.save(n)

# ── 9 · tech-life essentials ────────────────────────────
s = BSlide()
s.header("BEYOND THE LANGUAGE", "Tech Life", "Essentials", 100)
s.swipe(W - 70 - 214, 110)
tools = [
    ("Git & GitHub", "Save versions, undo mistakes, work in a team, show your portfolio."),
    ("The Terminal", "Run tools, install packages and move faster than clicking."),
    ("VS Code", "Free editor with extensions, themes and a built-in debugger."),
    ("Debugging", "Read the error, add prints or breakpoints, fix one thing at a time."),
    ("Docs & Search", "Official docs first. Learn to search the exact error message."),
    ("AI Assistants", "Great to explain code. Understand it before you paste it."),
]
gx0, gy0, gap = 70, 500, 18
cw_, ch_ = (W - 140 - gap) / 2, 244
for i, (name, what) in enumerate(tools):
    cx, cy = gx0 + (i % 2) * (cw_ + gap), gy0 + (i // 2) * (ch_ + gap)
    dark = (i // 2 + i % 2) % 2 == 0
    s.rect(cx, cy, cx + cw_, cy + ch_, NAVY if dark else (236, 239, 246), r=26)
    s.text(cx + 34, cy + 56, f"{i + 1:02d}", f(BOLD, 22), ORANGE)
    s.text(cx + 34, cy + 106, name, f(BOLD, 34), WHITE_T if dark else NAVY)
    s.para(cx + 34, cy + 152, what, f(REG, 20), cw_ - 64, 30, SOFT if dark else GREY)
s.counter(9)
s.save(9)

# ── 10 · learning tips ──────────────────────────────────
s = BSlide()
s.header("TIPS & TRICKS · LEARNING", "Learn Faster,", "Not Harder", 96)
s.swipe(W - 70 - 214, 110)
tips = [
    ("30 minutes daily", "beats 5 hours once a week. Consistency wins."),
    ("Type the code yourself", "Copy-paste teaches your clipboard, not you."),
    ("Read the error message", "Start from the last line. It usually tells you exactly what broke."),
    ("Build tiny projects", "Calculator, to-do list, portfolio site. Then make them better."),
    ("Rubber duck it", "Explain your code out loud, line by line. The bug often shows itself."),
]
y = 530
for t, b in tips:
    s.check(106, y - 10)
    s.text(140, y, t, f(SEMI, 30), NAVY)
    y = s.para(140, y + 44, b, f(REG, 25), 840, 36, GREY) + 44
s.counter(10)
s.save(10)

# ── 11 · shortcuts ──────────────────────────────────────
s = BSlide()
s.header("TIPS & TRICKS · VS CODE", "Shortcuts That", "Save Hours", 92)
s.swipe(W - 70 - 214, 110)
keys = [(["Ctrl", "P"], "Open any file by name"),
        (["Ctrl", "Shift", "P"], "Command palette: find any action"),
        (["Ctrl", "/"], "Comment / uncomment a line"),
        (["Ctrl", "D"], "Select the next same word, edit all"),
        (["Alt", "Up / Down"], "Move the current line up or down"),
        (["Tab"], "Autocomplete commands in the terminal")]
y = 500
for combo, what in keys:
    x = 90
    for j, key in enumerate(combo):
        if j:
            s.text(x + 10, y + 36, "+", f(SEMI, 26), GREY, anchor="lm")
            x += 40
        font = f(SEMI, 24)
        w = s.width(key, font) + 40
        s.rect(x, y + 6, x + w, y + 70, (208, 214, 226), r=12)
        s.rect(x, y, x + w, y + 62, WHITE_T, r=12)
        s.d.rounded_rectangle([k(x), k(y), k(x + w), k(y + 62)], radius=k(12), outline=(208, 214, 226), width=k(2))
        s.text(x + w / 2, y + 32, key, font, NAVY, anchor="mm")
        x += w
    s.text(470, y + 36, what, f(MED, 25), INK, anchor="lm")
    y += 104
s.text(90, y + 40, "Mac? Use Cmd instead of Ctrl.", f(REG, 22), GREY)
s.counter(11)
s.save(11)

# ── 12 · recap + connect ────────────────────────────────
s = BSlide()
s.photo(520, 760, fade="left")
s.text(90, 230, "Save This", f(BOLD, 112), NAVY)
s.text(90, 355, "Roadmap", f(BOLD, 112), ORANGE)
y = s.para(94, 440, "Share it with a friend starting their tech journey. Which language are you learning? Tell me below.",
           f(REG, 27), 470, 40, GREY)
s.bullets(96, y + 50, ["Pick one language", "Master the 5 core concepts", "Learn Git & the terminal",
                       "Build something every week"], lh=48, title_font=f(SEMI, 27))
cx0, cy0, cx1, cy1 = 70, 950, 700, 1270
s.rect(cx0, cy0, cx1, cy1, NAVY, r=30)
s.text(cx0 + 50, cy0 + 72, "Let’s connect", f(BOLD, 38), WHITE_T)
s.rect(cx0 + 50, cy0 + 96, cx0 + 130, cy0 + 102, ORANGE)
rows = [("Phone", "+255 752 747 681"), ("Website", "depriver.tech"), ("Instagram", "@_depriver")]
for i, (lab, val) in enumerate(rows):
    yy = cy0 + 150 + i * 56
    s.text(cx0 + 50, yy, lab.upper(), f(MED, 15), BLUE)
    s.text(cx0 + 230, yy + 1, val, f(SEMI, 27), WHITE_T)
s.counter(12)
s.save(12)
print("ok")
