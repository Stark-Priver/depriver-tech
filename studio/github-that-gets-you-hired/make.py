"""Carousel: build a GitHub profile that gets you hired (9 slides, 1080x1350, exported at 2x).
Same editorial / print direction as tech-gigs-for-students. Every step shows a small mock of the GitHub screen it
talks about (profile card, README, pinned repos, commit log, contribution graph), drawn in the brand palette."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 9
POST_URL = "depriver.tech/blog/github-that-gets-you-hired"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
import random

SHADES = [(232, 235, 242), (250, 205, 186), (242, 156, 122), (232, 96, 58), (176, 62, 30)]


def graph(s, x, y, cols, rows=7, cell=16, gap=4, seed=3, density=0.72, streak=None):
    """Contribution graph in brand orange. `streak` = (start col, end col) forced active."""
    rnd = random.Random(seed)
    for c in range(cols):
        for r in range(rows):
            v = 0
            if rnd.random() < density * (0.4 + 0.6 * c / cols):
                v = rnd.choice([1, 1, 2, 2, 3, 4])
            if streak and streak[0] <= c <= streak[1] and r not in (0, 6):
                v = max(v, rnd.choice([2, 3, 3, 4]))
            s.d.rounded_rectangle([k(x + c * (cell + gap)), k(y + r * (cell + gap)),
                                   k(x + c * (cell + gap) + cell), k(y + r * (cell + gap) + cell)], radius=k(3), fill=SHADES[v])


def avatar(s, cx, cy, r, empty=False):
    s.d.ellipse([k(cx - r), k(cy - r), k(cx + r), k(cy + r)], fill=(226, 230, 238) if empty else BLUE, outline=NAVY, width=k(3))
    if not empty:
        s.d.ellipse([k(cx - r * 0.34), k(cy - r * 0.5), k(cx + r * 0.34), k(cy + r * 0.18)], fill=NAVY)
        s.d.chord([k(cx - r * 0.66), k(cy + r * 0.25), k(cx + r * 0.66), k(cy + r * 1.4)], 180, 360, fill=NAVY)
    else:
        s.text(cx, cy + 2, "?", f(BOLD, r), GREY, anchor="mm")


def repo(s, box, name, desc, lang, lang_col, stars, demo=True):
    x0, y0, x1, y1 = box
    card(s, box, r=14)
    s.text(x0 + 24, y0 + 44, name, f(BOLD, fit(s, name, BOLD, 24, x1 - x0 - 48)), (37, 99, 235))
    s.para(x0 + 24, y0 + 80, desc, f(REG, 18), x1 - x0 - 48, 26, GREY)
    s.d.ellipse([k(x0 + 24), k(y1 - 38), k(x0 + 40), k(y1 - 22)], fill=lang_col)
    s.text(x0 + 48, y1 - 24, lang, f(MED, 17), NAVY)
    s.text(x1 - 24, y1 - 24, f"{stars} stars", f(MED, 17), GREY, anchor="rs")
    if demo:
        s.text(x0 + 48 + s.width(lang, f(MED, 17)) + 22, y1 - 24, "live demo", f(SEMI, 17), ORANGE)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For students & junior devs")
s.text(M - 6, 250, "Your GitHub", f(BOLD, 100), NAVY)
s.text(M - 6, 360, "is your CV.", f(BOLD, 100), NAVY)
s.text(M - 8, 490, "Make it hire you.", f(BOLD, 86), ORANGE)
s.text(M, 580, "Kazi yako ionekane", f(SIG, 64), NAVY)
swash(s, M + 8, M + 420, 606, ORANGE, 6)
card(s, (M, 670, W - M - 8, 990))
avatar(s, M + 80, 750, 46)
s.text(M + 150, 740, "Your Name", f(BOLD, 32), NAVY)
s.text(M + 150, 776, "@username · Software developer · Mbeya", f(REG, 21), GREY)
smallcaps(s, M + 32, 850, "214 contributions in the last year", 13, GREY)
graph(s, M + 32, 868, 40, rows=5, cell=17, gap=5, seed=11)
sticker(s, W - M - 150, 700, "Recruiters check this", angle=6, size=19, bg=NAVY)
horizon(s, 1)
cover_footer(s, "Swipe to fix yours")
finish(s)
s.save(1)

# ── 2 · 30 seconds ───────────────────────────────────────────────────────────────────────────────
s = page(2, "The truth · Ukweli")
outline_text(s, W - M + 10, 560, "30s", f(BOLD, 250), stroke=3, color=ORANGE, anchor="rs", opacity=0.7)
title2(s, "They look for", "30 seconds.", y=240, size=80)
s.para(M, 600, "When you apply, a recruiter or senior dev opens your GitHub and scans it fast. In 30 seconds they check:",
       f(REG, 26), W - 2 * M, 38, GREY)
checks = [("Who you are", "photo, name, one-line bio"), ("What you build", "pinned projects with clear READMEs"),
          ("That it works", "a live demo or screenshots"), ("That you're active", "recent, honest commits")]
y = 740
for a, b in checks:
    mark(s, M + 18, y - 10, True)
    s.text(M + 56, y, a, f(BOLD, 30), NAVY)
    s.text(M + 56 + s.width(a, f(BOLD, 30)) + 16, y, b, f(REG, fit(s, b, REG, 24, W - 2 * M - 80 - s.width(a, f(BOLD, 30)))), GREY)
    y += 66
horizon(s, 2)
navy_note(s, "So", "Make those 30 seconds easy for them.", "Rahisisha kazi yao", seed=2)
finish(s)
s.save(2)

# ── 3 · profile ──────────────────────────────────────────────────────────────────────────────────
s = page(3, "Step 01 · Fix your profile")
title2(s, "Look like a", "real developer.", y=220, size=80)
for j, ok in enumerate([False, True]):
    y0 = 400 + j * 290
    card(s, (M, y0, W - M - 8, y0 + 250))
    avatar(s, M + 90, y0 + 92, 52, empty=not ok)
    if ok:
        s.text(M + 170, y0 + 80, "Amina Juma", f(BOLD, 32), NAVY)
        s.text(M + 170, y0 + 114, "@aminajuma", f(REG, 22), GREY)
        s.text(M + 40, y0 + 190, "Web developer · Laravel & React · Building tools for small shops", f(MED, fit(s, "Web developer · Laravel & React · Building tools for small shops", MED, 23, W - 2 * M - 80)), NAVY)
        s.text(M + 40, y0 + 226, "Mbeya, Tanzania  ·  aminajuma.dev  ·  linkedin.com/in/aminajuma", f(REG, fit(s, "Mbeya, Tanzania  ·  aminajuma.dev  ·  linkedin.com/in/aminajuma", REG, 20, W - 2 * M - 80)), GREY)
    else:
        s.text(M + 170, y0 + 96, "user8823471", f(BOLD, 32), NAVY)
        s.text(M + 40, y0 + 190, "No bio · no location · no links", f(REG, 23), GREY)
    mark(s, W - M - 50, y0 + 50, ok, r=22)
sticker(s, W - M - 150, 980, "Real photo, real name", angle=-5, size=19)
horizon(s, 3)
navy_note(s, "Do this", "Photo, real name, one-line bio, location, one link.", "Jitambulishe vizuri", seed=3)
finish(s)
s.save(3)

# ── 4 · profile README ───────────────────────────────────────────────────────────────────────────
s = page(4, "Step 02 · Write a profile README")
title2(s, "Say hello", "on your profile.", y=220, size=80)
s.para(M, 400, "Create a repo with the same name as your username, add a README.md, and it shows on top of your profile.",
       f(REG, 24), W - 2 * M, 34, GREY)
card(s, (M, 490, W - M - 8, 990))
s.rect(M + 3, 493, W - M - 11, 540, (236, 239, 245))
s.text(M + 24, 526, "aminajuma / README.md", f(MONO_B, 20), NAVY)
lines = [("# Hi, I'm Amina 👋".replace(" 👋", ""), NAVY, MONO_B, 26),
         ("Web developer from Mbeya. I build simple", NAVY, MONO, 21),
         ("tools for small shops and schools.", NAVY, MONO, 21),
         ("", NAVY, MONO, 21),
         ("## What I'm building", ORANGE, MONO_B, 22),
         ("- Duka POS: sales + stock for small shops", NAVY, MONO, 21),
         ("- FPT Logbook: daily log app for trainees", NAVY, MONO, 21),
         ("## Stack", ORANGE, MONO_B, 22),
         ("Laravel · React · MySQL · Linux", NAVY, MONO, 21),
         ("## Reach me: amina@email.com", ORANGE, MONO_B, 22)]
y = 590
for t, col, fn, sz in lines:
    if t:
        s.text(M + 30, y, t, f(fn, fit(s, t, fn, sz, W - 2 * M - 70)), col)
    y += 38
horizon(s, 4)
navy_note(s, "Keep it short", "Who you are, what you build, your stack, how to reach you.", "Fupi na wazi", seed=4)
finish(s)
s.save(4)

# ── 5 · pinned repos ─────────────────────────────────────────────────────────────────────────────
s = page(5, "Step 03 · Pin your best 6")
title2(s, "Pin projects,", "not tutorials.", y=220, size=80)
s.para(M, 400, "Six real projects beat fifty half-finished folders. Real problems, real users, even small ones.",
       f(REG, 24), W - 2 * M, 34, GREY)
repos = [("duka-pos", "Sales and stock app for a real shop in Mbeya.", "PHP", (79, 93, 149), 12),
         ("fpt-logbook", "Daily logbook app for field trainees, with PDF export.", "JavaScript", (240, 200, 60), 8),
         ("school-results", "Results portal used by a secondary school.", "Python", (53, 114, 165), 5),
         ("church-site", "Website with events and live stream links.", "HTML", (227, 76, 38), 3)]
cw = (W - 2 * M - 24) / 2
for j, (nm, ds, lg, lc, st) in enumerate(repos):
    x0 = M + (j % 2) * (cw + 24)
    y0 = 490 + (j // 2) * 230
    repo(s, (x0, y0, x0 + cw - 8, y0 + 200), nm, ds, lg, lc, st)
sticker(s, W - M - 170, 960, "Not another to-do app", angle=-5, size=19, bg=NAVY)
horizon(s, 5)
navy_note(s, "Remove the noise", "Hide forks and tutorial clones you didn't change.", "Ubora kuliko wingi", seed=5)
finish(s)
s.save(5)

# ── 6 · project README ───────────────────────────────────────────────────────────────────────────
s = page(6, "Step 04 · A README for every project")
title2(s, "Explain it", "in 30 seconds.", y=220, size=80)
parts = [("What it does", "One sentence a non-developer understands."),
         ("Screenshot or GIF", "Show it working. People believe their eyes."),
         ("Live demo link", "Deploy it, even on a free tier."),
         ("Tech stack", "Laravel, React, MySQL... and why."),
         ("How to run it", "Install steps that actually work."),
         ("What you learnt", "The hard part, and how you solved it.")]
numbered(s, parts, 440, gap=104)
horizon(s, 6)
navy_note(s, "Test it", "Can a friend run your project from the README alone?", "Eleza kazi yako", seed=6)
finish(s)
s.save(6)

# ── 7 · commits ──────────────────────────────────────────────────────────────────────────────────
s = page(7, "Step 05 · Commit like a pro")
title2(s, "Small commits,", "clear messages.", y=220, size=80)
card(s, (M, 400, W / 2 - 14, 760))
card(s, (W / 2 + 6, 400, W - M - 8, 760))
for j, (hdr, ok, msgs) in enumerate([("Copy-machine log", False, ["update", "final", "final final", "fix", "asdf", "final_FINAL2"]),
                                    ("Pro log", True, ["Add stock alert on low items", "Fix VAT rounding on receipts",
                                                       "Export daily sales to PDF", "Validate phone numbers",
                                                       "Cache product list", "Write README setup steps"])]):
    x0 = M + 24 if j == 0 else W / 2 + 30
    mark(s, x0 + 14, 446, ok)
    s.text(x0 + 42, 454, hdr, f(BOLD, 24), NAVY)
    y = 512
    for m_ in msgs:
        s.text(x0, y, "• " + m_, f(MONO, fit(s, "• " + m_, MONO, 19, W / 2 - M - 60)), NAVY if ok else GREY)
        y += 40
smallcaps(s, M, 820, "Consistent beats perfect", 15, ORANGE)
graph(s, M, 842, 44, rows=5, cell=15, gap=5, seed=4, density=0.55, streak=(26, 43))
horizon(s, 7)
navy_note(s, "Don't", "Never use scripts that fake green squares. Seniors can tell.", "Kidogo kidogo kila siku", seed=7)
finish(s)
s.save(7)

# ── 8 · don'ts ───────────────────────────────────────────────────────────────────────────────────
s = page(8, "Step 06 · Avoid these")
title2(s, "Don't get", "rejected for this.", y=220, size=80)
donts = [("Passwords and API keys in code", "Use a .env file and add it to .gitignore."),
         ("Copied projects as your own", "Credit tutorials. Change and extend them."),
         ("Fifty empty repos", "Archive or delete them. Show the good ones."),
         ("No README at all", "A project nobody understands is invisible."),
         ("Client code without permission", "Office and FPT code isn't yours to publish.")]
y = 430
for a, b in donts:
    mark(s, M + 18, y - 10, False)
    s.text(M + 56, y, a, f(BOLD, fit(s, a, BOLD, 30, W - 2 * M - 60)), NAVY)
    s.text(M + 56, y + 38, b, f(REG, 23), GREY)
    if a != donts[-1][0]:
        hairline(s, M + 56, W - M, y + 64, RULE)
    y += 112
horizon(s, 8)
navy_note(s, "Leaked a key?", "Delete it from the service and make a new one now.", "Usalama kwanza", seed=8)
finish(s)
s.save(8)

# ── 9 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Drop your GitHub", "in the comments.", [("Fix", "your profile and README today"), ("Pin", "your best six projects"),
                                                   ("Comment", "your GitHub link, I'll check some")])
graph(s, 640, 690, 16, rows=7, cell=17, gap=5, seed=9, density=0.7)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
