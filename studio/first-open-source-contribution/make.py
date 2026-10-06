"""Carousel: your first open source contribution (8 slides, 1080x1350, exported at 2x). Ujuzi wa kazini. The device is a
GitHub-style pull request card ending in a green "Merged" badge."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/first-open-source-contribution"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs

PURPLE = (110, 64, 201)


def pr_card(s, y, title, num, status="Merged", body=None, x0=M, x1=None, files="1 file changed · +3 −1"):
    x1 = x1 or W - M - 8
    h = 220 + (wrap_lines(s, body, f(REG, 24), x1 - x0 - 72) * 34 + 20 if body else 0)
    card(s, (x0, y, x1, y + h), r=18)
    col = PURPLE if status == "Merged" else GREEN_OK
    w_ = s.width(status, f(BOLD, 21)) + 44
    s.d.rounded_rectangle([k(x0 + 30), k(y + 30), k(x0 + 30 + w_), k(y + 72)], radius=k(21), fill=col)
    s.text(x0 + 30 + w_ / 2, y + 51, status, f(BOLD, 21), WHITE_T, anchor="mm")
    s.text(x0 + 46 + w_, y + 60, f"#{num}", f(SEMI, 22), GREY)
    s.para(x0 + 30, y + 124, title, f(BOLD, 30), x1 - x0 - 60, 38, NAVY)
    yy = y + 124 + wrap_lines(s, title, f(BOLD, 30), x1 - x0 - 60) * 38
    if body:
        yy = s.para(x0 + 36, yy + 10, body, f(REG, 24), x1 - x0 - 72, 34, GREY)
    s.text(x0 + 30, y + h - 26, files, f(MONO, 20), GREY)
    return y + h


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Skills uni skips · Ujuzi wa kazini")
s.text(M - 6, 250, "Your first", f(BOLD, 100), NAVY)
s.text(M - 6, 352, "open source", f(BOLD, 100), ORANGE)
s.text(M - 6, 454, "contribution.", f(BOLD, 100), ORANGE)
s.text(M, 540, "Changia dunia", f(SIG, 60), NAVY)
swash(s, M + 8, M + 340, 566, ORANGE, 6)
pr_card(s, 650, "Add Kiswahili translation for the settings page", 1284, files="1 file changed · +42 −0")
stamp(s, 860, 940, "MERGED", PURPLE, angle=-10, size=44)
horizon(s, 1)
cover_footer(s, "Swipe, make your first PR")
finish(s)
s.save(1)

# ── 2 · what and why ─────────────────────────────────────────────────────────────────────────────
s = page(2, "Why · Kwa nini", "Ujuzi wa kazini")
title2(s, "Real code,", "real reviewers.", y=220, size=90)
s.para(M, 400, "Open source projects share their code publicly. Anyone can suggest improvements through a pull request.", f(MED, 30), W - 2 * M, 44, NAVY)
tick_fill(s, [("Learn from real codebases", "Bigger and better than any class project."), ("Get reviewed by experienced developers", "Free mentoring, in public."),
              ("A portfolio that proves teamwork", "Recruiters can click and see it.")], 560, 990, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Truth", "Many senior developers started with a tiny typo fix.", "Anza kidogo", seed=2)
finish(s)
s.save(2)

# ── 3 · not only code ────────────────────────────────────────────────────────────────────────────
s = page(3, "Not only code · Si code tu", "Ujuzi wa kazini")
title2(s, "Ways to help", "without being senior.", y=220, size=82)
ways = [("Docs", "Fix unclear README steps"), ("Kiswahili", "Translate the app's text"), ("Bug reports", "Clear steps to reproduce"),
        ("Tests", "Add a missing test"), ("Design", "Icons, screenshots, UX notes"), ("Small fixes", "“good first issue” labels")]
cw = (W - 2 * M - 24) / 2
for i, (a, b) in enumerate(ways):
    xx, yy = M + (i % 2) * (cw + 24), 410 + (i // 2) * 190
    card(s, (xx, yy, xx + cw - 8, yy + 160), r=16)
    s.text(xx + 28, yy + 62, f"{i + 1:02d}", f(BOLD, 24), ORANGE)
    s.text(xx + 80, yy + 62, a, f(BOLD, 29), NAVY)
    s.para(xx + 28, yy + 112, b, f(REG, 23), cw - 60, 31, GREY)
horizon(s, 3)
navy_note(s, "Our edge", "Many apps need Kiswahili. That's a contribution only we can make well.", "Kiswahili ni nguvu yetu", seed=3)
finish(s)
s.save(3)

# ── 4 · find a project ───────────────────────────────────────────────────────────────────────────
s = page(4, "Find one · Tafuta mradi", "Ujuzi wa kazini")
title2(s, "Start with tools", "you already use.", y=220, size=84)
tick_fill(s, [("A library from your own project", "You already know what it does."), ("Search the “good first issue” label", "On GitHub, filter issues by that label."),
              ("Translation platforms", "Many projects translate via Weblate or Crowdin. Look for Swahili (sw)."),
              ("Check it's alive", "Recent commits, maintainers replying to issues.")], 420, 990, size=31, sub=26)
horizon(s, 4)
navy_note(s, "Read first", "CONTRIBUTING.md tells you exactly how they want help.", "Soma maelekezo", seed=4)
finish(s)
s.save(4)

# ── 5 · the flow ─────────────────────────────────────────────────────────────────────────────────
s = page(5, "The flow · Hatua", "Ujuzi wa kazini")
title2(s, "From fork to", "pull request.", y=220, size=86)
flow(s, [("Fork", "Your own copy on GitHub"), ("Clone + new branch", "git checkout -b fix-readme"), ("Make one small change", "Test it locally"),
         ("Commit + push", "Clear message"), ("Open a pull request", "Explain what and why")], 410, h=88, gap=28, size=28)
horizon(s, 5)
navy_note(s, "Practise", "Git in 7 commands covers everything you need here.", "Tumia Git", seed=5)
finish(s)
s.save(5)

# ── 6 · a good PR ────────────────────────────────────────────────────────────────────────────────
s = page(6, "A good PR · PR nzuri", "Ujuzi wa kazini")
title2(s, "Write a PR", "people want to merge.", y=220, size=84)
pr_card(s, 410, "Fix install steps for Windows in README", 512, status="Open",
        body="The guide says `make install`, which doesn't work on Windows. I added the PowerShell command and tested it on Windows 11. Fixes #498.",
        files="1 file changed · +6 −2")
tick_list(s, [("Clear title: what it does", None), ("Why, and how you tested it", None), ("Link the issue it fixes", None)], 840, size=28)
horizon(s, 6)
navy_note(s, "Small wins", "Small, focused PRs get reviewed and merged faster.", "Ndogo na wazi", seed=6)
finish(s)
s.save(6)

# ── 7 · etiquette ────────────────────────────────────────────────────────────────────────────────
s = page(7, "Etiquette · Adabu", "Ujuzi wa kazini")
title2(s, "Be the contributor", "they remember.", y=220, size=82)
tick_fill(s, [("Ask before big changes", "Comment on the issue first."), ("Accept feedback calmly", "Review comments are help, not insults."),
              ("Be patient", "Maintainers are often volunteers."), ("No spam PRs", "Changing one word just to get a PR hurts the project.")],
          420, 990, size=31, sub=26)
horizon(s, 7)
navy_note(s, "Reputation", "Your GitHub history is public forever. Make it good.", "Heshima ni mtaji", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which project will", "you help first?", [("Comment", "the project, I'll suggest a first issue"), ("Save", "the 5-step flow"),
                                                    ("Share", "with a friend ready to grow")])
stamp(s, 840, 860, "MERGED", PURPLE, angle=-10, size=50)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
