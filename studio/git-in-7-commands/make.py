"""Carousel: Git in 7 commands (8 slides, 1080x1350, exported at 2x). Ujuzi wa kazini. The device is a commit timeline
(save points on a line) next to a terminal; each command gets a numbered chip #1–#7."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/git-in-7-commands"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def timeline(s, y, commits, x0=M + 20, x1=None, active=None):
    """Horizontal commit line: dots with short labels below, alternating up/down."""
    x1 = x1 or W - M - 20
    s.rect(x0, y - 3, x1, y + 3, NAVY)
    gap = (x1 - x0) / max(1, len(commits) - 1)
    for i, lab in enumerate(commits):
        cx = x0 + i * gap
        cur = active is None or i == active
        s.d.ellipse([k(cx - 18), k(y - 18), k(cx + 18), k(y + 18)], fill=ORANGE if cur else (255, 255, 255), outline=NAVY, width=k(4))
        ty = y + 56 if i % 2 == 0 else y - 34
        s.text(cx, ty, lab, f(SEMI, fit(s, lab, SEMI, 20, gap * 1.8)), NAVY, anchor="ms")


def cmd_head(s, y, items):
    for c, m, n in items:
        ww = s.width(c, f(MONO_B, 30)) + 44
        s.d.rounded_rectangle([k(M), k(y - 40), k(M + ww), k(y + 16)], radius=k(12), fill=TERM_BG)
        s.text(M + 22, y - 2, c, f(MONO_B, 30), WHITE_T)
        s.text(M + ww + 24, y - 2, m, f(SEMI, fit(s, m, SEMI, 28, W - 2 * M - ww - 90)), NAVY)
        s.text(W - M, y - 2, f"#{n}", f(BOLD, 24), ORANGE, anchor="rs")
        y += 84
    return y


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Skills uni skips · Ujuzi wa kazini")
s.text(M - 6, 260, "Git in", f(BOLD, 120), NAVY)
s.text(M - 6, 380, "7 commands.", f(BOLD, 110), ORANGE)
s.text(M, 470, "Hifadhi kila hatua", f(SIG, 60), NAVY)
swash(s, M + 8, M + 420, 496, ORANGE, 6)
timeline(s, 640, ["init", "login form", "fix bug", "sales page", "deploy"])
terminal(s, 760, ["$ git add .", "$ git commit -m \"Add sales page\"", "$ git push"], title="terminal", size=25, lh=42)
horizon(s, 1)
cover_footer(s, "Swipe, never lose code again")
finish(s)
s.save(1)

# ── 2 · why ──────────────────────────────────────────────────────────────────────────────────────
s = page(2, "Why Git · Kwa nini", "Ujuzi wa kazini")
title2(s, "Save points", "for your code.", y=220, size=88)
tick_fill(s, [("Go back in time", "Broke something? Return to the last working version."), ("No more final_FINAL2.zip", "One folder, full history."),
              ("Work in a team", "Everyone's changes merge together."), ("Your GitHub is your CV", "Recruiters look at your commits.")],
          420, 990, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Like", "Save points in a game. Die? Restart from the last save.", "Kama game", seed=2)
finish(s)
s.save(2)

# ── 3 · start ────────────────────────────────────────────────────────────────────────────────────
s = page(3, "Start · Anza", "Ujuzi wa kazini")
title2(s, "Start tracking", "a project.", y=220, size=88)
y = cmd_head(s, 440, [("git init", "start Git in this folder", 1), ("git status", "what changed?", 2)])
terminal(s, y + 10, ["$ git status", "On branch main", "Changes not staged:", "!  modified: index.html", "Untracked: style.css"], title="duka-app", size=24, lh=40)
horizon(s, 3)
navy_note(s, "Habit", "Run git status all the time. It never changes anything.", "status ni salama", seed=3)
finish(s)
s.save(3)

# ── 4 · save ─────────────────────────────────────────────────────────────────────────────────────
s = page(4, "Save · Hifadhi", "Ujuzi wa kazini")
title2(s, "Save a", "checkpoint.", y=220, size=92)
y = cmd_head(s, 440, [("git add .", "choose what to save", 3), ("git commit -m", "save it with a message", 4)])
for j, (msg, ok) in enumerate([("update", False), ("stuff", False), ("Add login form validation", True), ("Fix total when cart is empty", True)]):
    yy = y + 40 + j * 70
    mark(s, M + 18, yy - 10, ok)
    s.text(M + 56, yy, f'-m "{msg}"', f(MONO_B, 27), NAVY if ok else GREY)
horizon(s, 4)
navy_note(s, "Good message", "Say what the commit DOES, in a few words.", "Ujumbe unaoeleweka", seed=4)
finish(s)
s.save(4)

# ── 5 · history ──────────────────────────────────────────────────────────────────────────────────
s = page(5, "History · Historia", "Ujuzi wa kazini")
title2(s, "See your", "history.", y=220, size=92)
y = cmd_head(s, 440, [("git log --oneline", "every save, newest first", 5)])
terminal(s, y + 10, ["$ git log --oneline", "a1f08d6 Add sales page", "9c2e4b1 Fix total when cart is empty", "77d0e3a Add login form validation",
                     "1b3f9aa Initial commit"], title="duka-app", size=24, lh=40)
horizon(s, 5)
navy_note(s, "Group projects", "This list shows who did what. Proof of your work.", "Historia haidanganyi", seed=5)
finish(s)
s.save(5)

# ── 6 · share ────────────────────────────────────────────────────────────────────────────────────
s = page(6, "Share · Shiriki", "Ujuzi wa kazini")
title2(s, "Send it to", "GitHub.", y=220, size=92)
y = cmd_head(s, 440, [("git push", "upload your commits", 6), ("git pull", "download your team's commits", 7)])
terminal(s, y + 10, ["# first time only:", "$ git remote add origin <your repo URL>", "$ git push -u origin main"], title="duka-app", size=24, lh=40)
horizon(s, 6)
navy_note(s, "Then", "Your code is backed up, and your profile gets a green square.", "Backup + CV", seed=6)
finish(s)
s.save(6)

# ── 7 · daily routine ────────────────────────────────────────────────────────────────────────────
s = page(7, "Every day · Kila siku", "Ujuzi wa kazini")
title2(s, "The daily", "routine.", y=220, size=92)
flow(s, [("git pull", "Get the latest from your team"), ("Write code", "One small piece at a time"), ("git status", "Check what changed"),
         ("git add + git commit", "Save with a clear message"), ("git push", "Share and back up")], 410, h=88, gap=28, size=28)
horizon(s, 7)
navy_note(s, "Rule", "Commit small and often. Many saves beat one huge one.", "Hifadhi mara kwa mara", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What's your worst", "“lost code” story?", [("Comment", "your story"), ("Save", "your Git cheat sheet"),
                                                     ("Share", "with your group project team")])
timeline(s, 870, ["init", "", "", "push"], x0=620, x1=W - M - 20)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
