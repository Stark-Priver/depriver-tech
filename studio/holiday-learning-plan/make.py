"""Carousel: a 4-week holiday learning plan (8 slides, 1080x1350, exported at 2x). Timed for the December break. The
device is a weekly planner strip (seven day cells), with rest days for Christmas and New Year."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/holiday-learning-plan"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
REST = (150, 158, 175)


def week_strip(s, y, tasks, col, h=150, label=None):
    """Seven day cells; a task of None is a rest day (grey)."""
    cw = (W - 2 * M) / 7
    if label:
        smallcaps(s, M, y - 18, label, 15, col)
    for i, t_ in enumerate(tasks):
        x0 = M + i * cw
        box = [k(x0 + 3), k(y + 3), k(x0 + cw - 3), k(y + h - 3)]
        s.d.rounded_rectangle(box, radius=k(12), fill=(255, 255, 255) if t_ else (238, 241, 246), outline=NAVY if t_ else (214, 219, 230), width=k(2))
        s.text(x0 + 14, y + 34, DAYS[i], f(BOLD, 18), col if t_ else REST)
        if t_:
            s.para(x0 + 14, y + 70, t_, f(MED, 17), cw - 26, 23, NAVY)
        else:
            s.text(x0 + 14, y + 80, "Rest", f(SIG, 30), REST)


def week_slide(n, label, t1, t2, col, tasks, goal, note, res):
    s = page(n, label, "Mpango wa likizo")
    title2(s, t1, t2, y=220, size=86)
    week_strip(s, 440, tasks, col, h=190)
    label_box(s, (M, 690, W - M - 8, 870), "Goal by Sunday · Lengo", goal, col=col, size=30, lh=42)
    smallcaps(s, M, 930, "Free help · Bure", 15, col)
    chip_row(s, res, M, 950, size=21)
    horizon(s, n)
    navy_note(s, *note, seed=n)
    finish(s)
    s.save(n)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "December break · Likizo")
s.text(M - 6, 250, "4 weeks off.", f(BOLD, 104), NAVY)
s.text(M - 6, 360, "Make them count.", f(BOLD, 96), ORANGE)
s.text(M, 450, "Likizo yenye malengo", f(SIG, 60), NAVY)
swash(s, M + 8, M + 460, 476, ORANGE, 6)
s.para(M, 560, "One hour a day for four weeks. Rest days included, because it's still a holiday.", f(REG, 28), W - 2 * M, 42, GREY)
for i, (lab, col) in enumerate([("Week 1 · Basics", NAVY), ("Week 2 · Small builds", ORANGE), ("Week 3 · Real project", NAVY), ("Week 4 · Show it", GREEN_OK)]):
    y = 680 + i * 84
    s.d.rounded_rectangle([k(M), k(y), k(M + 300), k(y + 60)], radius=k(30), fill=col)
    s.text(M + 150, y + 31, lab, f(BOLD, 22), WHITE_T, anchor="mm")
    for d in range(7):
        x0 = M + 330 + d * 82
        rest = (i == 1 and d == 4) or (i == 2 and d == 4) or d == 6
        s.d.rounded_rectangle([k(x0), k(y + 4), k(x0 + 70), k(y + 56)], radius=k(10), fill=(238, 241, 246) if rest else (255, 255, 255),
                              outline=(214, 219, 230) if rest else col, width=k(2))
horizon(s, 1)
cover_footer(s, "Swipe for the plan")
finish(s)
s.save(1)

# ── 2 · the rule ─────────────────────────────────────────────────────────────────────────────────
s = page(2, "The rule · Kanuni", "Mpango wa likizo")
title2(s, "1 hour a day", "beats 10 on Sunday.", y=220, size=82)
bars(s, [("1 hour × 24 days", 0.85, GREEN_OK), ("“I'll do a big session on Sunday”", 0.3, RED_NO), ("Watching tutorials only", 0.15, RED_NO)], 440, gap=120)
s.text(M, 820, "Illustration: what usually sticks after 4 weeks.", f(REG, 22), GREY)
tick_list(s, [("Same time every day, e.g. 8 to 9 a.m.", None), ("Phone in another room", None)], 900, size=28)
horizon(s, 2)
navy_note(s, "And rest", "Family, church, friends, sleep. A rested brain learns faster.", "Pumzika pia", seed=2)
finish(s)
s.save(2)

week_slide(3, "Week 1 · Wiki ya kwanza", "Week 1:", "the basics.", NAVY,
           ["Pick ONE language", "Variables & types", "If / else", "Loops", "Functions", "Practise 10 small problems", None],
           "Write a program that asks your name and age and prints a greeting.", ("Tip", "Don't switch languages this week. Finish what you start.", "Lugha moja tu"), ["freeCodeCamp", "W3Schools", "Python.org tutorial", "MDN"])
week_slide(4, "Week 2 · Wiki ya pili", "Week 2:", "small builds.", ORANGE,
           ["Calculator", "Tip / VAT calculator", "To-do list", "Fix bugs, clean code", None, "Quiz game", None],
           "Three tiny programs that work, saved on GitHub.", ("Christmas", "Rest on Christmas. Code can wait one day.", "Krismasi njema"), ["GitHub (free)", "Exercism", "VS Code"])
week_slide(5, "Week 3 · Wiki ya tatu", "Week 3: one", "real project.", NAVY,
           ["Choose a real user", "Plan the screens", "Build part 1", "Build part 2", None, "Ask the user to test", None],
           "A small site or app for someone real: a shop, church, school club or your family business.", ("New Year", "Rest on 1 January, then finish strong.", "Heri ya mwaka mpya"), ["Figma (free)", "Paper sketches", "Your user"])
week_slide(6, "Week 4 · Wiki ya nne", "Week 4:", "show it.", GREEN_OK,
           ["Fix what the user found", "Deploy it free", "Write a good README", "Screenshots + demo video", "Update your CV", "Post it on LinkedIn", None],
           "A live link, a README and a post. Proof of four weeks of work.", ("Remember", "Unshown work is invisible work.", "Onyesha ulichojenga"), ["Vercel / Netlify", "GitHub Pages", "LinkedIn"])

# ── 7 · the full plan ────────────────────────────────────────────────────────────────────────────
s = page(7, "The whole plan · Mpango mzima", "Mpango wa likizo")
title2(s, "Screenshot", "this plan.", y=220, size=92)
for i, (lab, col, tasks) in enumerate([
        ("Week 1 · Basics", NAVY, ["Pick", "Types", "If", "Loops", "Func", "Practise", None]),
        ("Week 2 · Small builds", ORANGE, ["Calc", "VAT", "To-do", "Fix", None, "Quiz", None]),
        ("Week 3 · Real project", NAVY, ["User", "Plan", "Build", "Build", None, "Test", None]),
        ("Week 4 · Show it", GREEN_OK, ["Fix", "Deploy", "README", "Video", "CV", "Post", None])]):
    week_strip(s, 420 + i * 150, tasks, col, h=110, label=lab)
horizon(s, 7)
navy_note(s, "Your move", "Set it as your lock screen for December.", "Anza kesho", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What will you", "learn this break?", [("Comment", "your language or project"), ("Tag", "a study partner for December"),
                                                 ("Save", "and check it every Sunday")])
stamp(s, 840, 860, "TAYARI", GREEN_OK, angle=-10, size=56)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
