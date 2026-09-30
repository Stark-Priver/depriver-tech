"""'Things I wish I knew earlier' — junior dev tips carousel for Privatus Cosmas (7 slides, 1080x1350).
Reuses the design system (fonts, colours, Slide helpers) from the intro carousel so the series matches."""
import os

import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers

TOTAL = 7


class JSlide(Slide):
    def counter(self, n):
        self.text(W - 60, 70, f"{n:02d} / {TOTAL:02d}", f(MED, 18), GREY, anchor="rs")

    def save(self, n):
        out = self.im
        out.save(f"{OUT}slide-{n}.png", optimize=True)
        out.save(f"{OUT}slide-{n}.jpg", quality=95)

    def fit(self, lines, font_name, max_size, maxw):
        """Largest size <= max_size at which every line fits maxw."""
        size = max_size
        while size > 40 and any(self.width(t, f(font_name, size)) > maxw for t in lines):
            size -= 2
        return size

    def check(self, x, y, r=15):
        self.d.ellipse([k(x - r), k(y - r), k(x + r), k(y + r)], fill=ORANGE)
        self.d.line([k(x - 7), k(y), k(x - 2), k(y + 6), k(x + 8), k(y - 6)], fill=(255, 255, 255), width=k(3.4),
                    joint="curve")


# ── 1 · hook ─────────────────────────────────────────────
s = JSlide()
s.rect(0, 830, 560, 872, BLUE)
s.rect(0, 872, 560, H, NAVY)
s.photo(470, 780, fade="left")
s.text(96, 330, "Junior developer or new to tech?", f(MED, 30), NAVY)
lines = ["Things I", "Wish I Knew", "Earlier"]
size = s.fit(lines, BOLD, 112, 570)
for i, (t, c) in enumerate(zip(lines, (NAVY, ORANGE, NAVY))):
    s.text(90, 470 + i * size * 1.24, t, f(BOLD, size), c)
s.rect(210, 1128, 380, 1170, ORANGE)
s.text(96, 1060, "Privatus", f(SIG, 112), (255, 255, 255))
s.text(170, 1170, "Cosmas", f(SIG, 112), (255, 255, 255))
s.swipe(640, 1150)
s.counter(1)
s.save(1)

# ── 2–6 · tips ───────────────────────────────────────────
tips = [
    ("Fundamentals", "beat frameworks",
     "Frameworks change every year. How the web works, data structures, Git, SQL and debugging never go out of date.",
     ["Build one project with no framework", "Learn Git beyond add, commit, push", "Write raw SQL before using an ORM"]),
    ("Read more code", "than you write",
     "Most of the job is understanding code that already exists. Reading good codebases is the fastest way to level up.",
     ["Read one open-source repo a week", "Trace a feature from UI to database", "Review your teammates’ pull requests"]),
    ("Ask better", "questions",
     "Being stuck for hours is not a badge of honour. Try first, then ask clearly, so people can actually help you.",
     ["Share what you already tried", "Include the exact error and context", "Timebox it: 30–60 minutes, then ask"]),
    ("Ship first,", "then improve",
     "Done and working beats perfect and unfinished. Real users will teach you more than any tutorial.",
     ["Break work into small pull requests", "Deploy early, even to a test server", "Treat feedback as data, not failure"]),
    ("Grow beyond", "the code",
     "Communication, writing and understanding the problem make you valuable. Syntax is only part of the job.",
     ["Write clear commits, docs and updates", "Understand the ‘why’ before coding", "Learn in public and share what you learn"]),
]
for i, (l1, l2, body, todo) in enumerate(tips):
    n = i + 2
    s = JSlide()
    s.text(86, 300, f"{i + 1:02d}", f(BOLD, 150), ORANGE)
    size = s.fit([l1, l2], BOLD, 92, 900)
    s.text(90, 480, l1, f(BOLD, size), NAVY)
    s.text(90, 480 + size * 1.18, l2, f(BOLD, size), ORANGE)
    s.para(94, 480 + size * 1.18 + 76, body, f(REG, 28), 880, 42, GREY)
    cx0, cy0, cx1, cy1 = 70, 880, W - 70, 1250
    s.rect(cx0, cy0, cx1, cy1, NAVY, r=34)
    s.text(cx0 + 56, cy0 + 72, "DO THIS", f(SEMI, 18), BLUE)
    s.rect(cx0 + 56, cy0 + 90, cx0 + 116, cy0 + 95, ORANGE)
    for j, t in enumerate(todo):
        yy = cy0 + 162 + j * 70
        s.check(cx0 + 72, yy - 10)
        s.text(cx0 + 106, yy, t, f(MED, 29), (255, 255, 255))
    s.swipe(W - 70 - 214, 228)
    s.counter(n)
    s.save(n)

# ── 7 · save + connect ──────────────────────────────────
s = JSlide()
s.photo(520, 760, fade="left")
s.text(90, 230, "Save This", f(BOLD, 112), NAVY)
s.text(90, 355, "For Later", f(BOLD, 112), ORANGE)
y = s.para(94, 440, "Which tip hit home? Tell me in the comments, and share this with someone starting their tech journey.",
           f(REG, 27), 470, 40, GREY)
s.bullets(96, y + 50, ["Fundamentals first", "Read code daily", "Ask with context", "Ship, then improve",
                       "Grow beyond code"], lh=48, title_font=f(SEMI, 27))
cx0, cy0, cx1, cy1 = 70, 950, 700, 1270
s.rect(cx0, cy0, cx1, cy1, NAVY, r=30)
s.text(cx0 + 50, cy0 + 72, "Let’s connect", f(BOLD, 38), (255, 255, 255))
s.rect(cx0 + 50, cy0 + 96, cx0 + 130, cy0 + 102, ORANGE)
rows = [("Phone", "+255 752 747 681"), ("Website", "depriver.tech"), ("Instagram", "@_depriver")]
for i, (lab, val) in enumerate(rows):
    yy = cy0 + 150 + i * 56
    s.text(cx0 + 50, yy, lab.upper(), f(MED, 15), BLUE)
    s.text(cx0 + 230, yy + 1, val, f(SEMI, 27), (255, 255, 255))
s.counter(7)
s.save(7)
print("ok")
