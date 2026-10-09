"""Carousel: Python from beginner to professional (16 slides, 1080x1350, exported at 2x). Six levels (setup → professional)
with real code at each level, every area where Python is used (two 10-tile slides), specialisation paths, projects per
level and free resources. Content is shared with the PDF guide in studio/python-roadmap-guide via data.py."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = globals().get("TOTAL_OVERRIDE", 16)
POST_URL = "depriver.tech/blog/python-roadmap"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # code windows, terminals, tables, flows
exec(open(os.path.join(HERE, "data.py")).read())         # AREAS, LEVELS, PATHS, RESOURCES, the logo art

def level_tag(s, lv, y=150):
    """Level ribbon under the header: six small boxes, the current one orange."""
    gap, x = 10, M
    wd = (W - 2 * M - gap * 5) / 6
    for i, (lab, name, _, _) in enumerate(LEVELS):
        cur = i == lv
        done = i < lv
        s.d.rounded_rectangle([k(x), k(y), k(x + wd), k(y + 40)], radius=k(8), fill=ORANGE if cur else (NAVY if done else (255, 255, 255)),
                              outline=NAVY, width=k(2.5))
        s.text(x + wd / 2, y + 20, name, f(SEMI if cur else MED, 16), WHITE_T if (cur or done) else NAVY, anchor="mm")
        x += wd + gap


def area_tiles(s, items, start, y0=390, rows=5, h=104, gap=14):
    cw = (W - 2 * M - 8 - 18) / 2
    for i, (name, _, libs, _) in enumerate(items):
        col, row = i // rows, i % rows
        x0, yy = M + col * (cw + 18), y0 + row * (h + gap)
        card(s, (x0, yy, x0 + cw, yy + h), r=14)
        s.text(x0 + 26, yy + 46, f"{start + i:02d}", f(BOLD, 20), ORANGE)
        s.text(x0 + 70, yy + 46, name, f(BOLD, fit(s, name, BOLD, 27, cw - 90)), NAVY)
        s.text(x0 + 70, yy + 82, libs, f(MONO, fit(s, libs, MONO, 18, cw - 90, smallest=12)), GREY)


if __name__ == "__main__" or globals().get("RUN_CAROUSEL", True):
    # ── 1 · cover ────────────────────────────────────────────────────────────────────────────────
    s = page(1, "Python roadmap · Ramani")
    s.text(M - 6, 250, "Python:", f(BOLD, 120), NAVY)
    s.text(M - 6, 368, "beginner to", f(BOLD, 104), NAVY)
    s.text(M - 8, 496, "professional.", f(BOLD, 116), ORANGE)
    s.text(M, 586, "Ramani kamili, hatua kwa hatua", f(SIG, 54), NAVY)
    swash(s, M + 8, M + 560, 612, ORANGE, 6)
    s.para(M, 700, "Six levels, real code, every area Python is used in, and a free PDF guide.", f(REG, 27), 440, 40, GREY)
    paste_print(s, print_art("python", k(440)), 560, 650)
    sticker(s, W - M - 170, 660, "Free book: Python Daily", angle=-5, size=20, bg=NAVY)
    horizon(s, 1)
    cover_footer(s, "Swipe, save this roadmap")
    finish(s)
    s.save(1)

    # ── 2 · why python ───────────────────────────────────────────────────────────────────────────
    s = page(2, "Why Python · Kwa nini")
    title2(s, "Why start", "with Python?", y=220, size=90)
    y = tick_list(s, [("Reads almost like English", "So you learn logic, not symbols."),
                      ("One language, many careers", "Web, data, AI, automation, security and more."),
                      ("Huge free community", "Every error you meet, someone has solved.")], 410, size=29, sub=23, gap=16)
    code_window(s, y + 10, ['jina = "Asha"', 'print(f"Habari, {jina}!")'], file="hello.py", size=26, lh=46)
    horizon(s, 2)
    navy_note(s, "Truth", "Python is one of the most used languages in the world.", "Lugha ya kila fani", seed=2)
    finish(s)
    s.save(2)

    # ── 3 · roadmap overview ─────────────────────────────────────────────────────────────────────
    s = page(3, "The roadmap · Ramani")
    title2(s, "Six levels,", "one at a time.", y=220, size=90)
    flow(s, [(f"{lab} · {name}  ({when})", focus) for lab, name, when, focus in LEVELS], 390, h=86, gap=20, size=27)
    horizon(s, 3)
    navy_note(s, "Pace", "Rough times at 1–2 hours a day. Slower is fine; stopping isn't.", "Polepole ndio mwendo", seed=3)
    finish(s)
    s.save(3)

    # ── 4 · level 0 ──────────────────────────────────────────────────────────────────────────────
    s = page(4, "Level 0 · Set up", "Day 1")
    level_tag(s, 0)
    title2(s, "Set up in", "one evening.", y=300, size=84)
    y = tick_list(s, [("Install Python from python.org", "On Windows, tick “Add python.exe to PATH”."),
                      ("Install VS Code + the Python extension", None), ("Run your first file", None)], 470, size=27, sub=22, gap=10)
    terminal(s, y + 10, ["$ python --version", "Python 3.13.0", "$ python hello.py", "Habari, Asha!"], title="terminal", size=25, lh=40)
    horizon(s, 4)
    navy_note(s, "On a phone only?", "Start on Google Colab or Replit in the browser.", "Anza na ulicho nacho", seed=4)
    finish(s)
    s.save(4)

    # ── 5 · level 1: logic ───────────────────────────────────────────────────────────────────────
    s = page(5, "Level 1 · Basics", "Weeks 1–6")
    level_tag(s, 1)
    title2(s, "The basics:", "logic.", y=300, size=88)
    chip_row(s, ["variables", "int · float · str · bool", "input / print", "if / elif / else", "for · while", "functions"], M, 440, size=21)
    code_window(s, 560, ["marks = [78, 45, 90, 62]", "for m in marks:", "    if m >= 50:", '        print(m, "Pass")', "    else:",
                         '        print(m, "Fail")'], file="results.py", size=25, lh=40)
    horizon(s, 5)
    navy_note(s, "Practice", "Type every example yourself. Then change it and break it.", "Andika mwenyewe", seed=5)
    finish(s)
    s.save(5)

    # ── 6 · level 1: data structures ─────────────────────────────────────────────────────────────
    s = page(6, "Level 1 · Basics", "Weeks 1–6")
    level_tag(s, 1)
    title2(s, "The basics:", "data structures.", y=300, size=84)
    table(s, M, 430, ["Type", "Looks like", "Use it for"], [["list", "[78, 90, 62]", "Ordered items"], ["dict", '{"name": "Asha"}', "Named values"],
                                                         ["tuple", "(-6.8, 39.2)", "Fixed values"], ["set", '{"A", "B"}', "No duplicates"]],
          [180, 380, 368], size=25, rh=64)
    code_window(s, 770, ['student = {"name": "Asha", "marks": [78, 90]}', 'avg = sum(student["marks"]) / 2', 'print(student["name"], avg)'],
                file="student.py", size=23, lh=38)
    horizon(s, 6)
    navy_note(s, "Then", "Add try/except for errors, and reading/writing files.", "Msingi imara", seed=6)
    finish(s)
    s.save(6)

    # ── 7 · level 2 ──────────────────────────────────────────────────────────────────────────────
    s = page(7, "Level 2 · Intermediate", "Months 2–3")
    level_tag(s, 2)
    title2(s, "Use other", "people's code.", y=300, size=86)
    chip_row(s, ["modules & import", "pip", "virtual environments", "classes (OOP)", "JSON & CSV", "APIs", "Git & GitHub"], M, 440, size=21)
    code_window(s, 590, ["import requests", "", 'res = requests.get("https://api.github.com/users/octocat")', "data = res.json()",
                         'print(data["name"], data["public_repos"])'], file="api.py", size=22, lh=40)
    horizon(s, 7)
    navy_note(s, "Milestone", "You can build small tools that talk to the internet.", "Sasa unajenga", seed=7)
    finish(s)
    s.save(7)

    # ── 8 · level 3 ──────────────────────────────────────────────────────────────────────────────
    s = page(8, "Level 3 · Advanced", "Months 4–6")
    level_tag(s, 3)
    title2(s, "Write code", "others can trust.", y=300, size=84)
    chip_row(s, ["type hints", "pytest", "PEP 8 + ruff", "decorators", "generators", "SQL + sqlite3", "async basics"], M, 440, size=21)
    code_window(s, 590, ["def average(marks: list[float]) -> float:", "    return sum(marks) / len(marks)", "",
                         "def test_average():", "    assert average([50, 100]) == 75"], file="test_marks.py", size=24, lh=40, hl=(3, 4))
    horizon(s, 8)
    navy_note(s, "Why", "Tested, readable code is what companies pay for.", "Ubora ni kazi", seed=8)
    finish(s)
    s.save(8)

    # ── 9–10 · where python is used ──────────────────────────────────────────────────────────────
    for p in range(2):
        n = 9 + p
        s = page(n, f"Where Python is used · {p + 1}/2", "20 areas")
        title2(s, "Where Python" if p == 0 else "And even", "is used." if p == 0 else "more places.", y=220, size=88)
        area_tiles(s, AREAS[p * 10:(p + 1) * 10], p * 10 + 1)
        horizon(s, n)
        navy_note(s, *[("Big names", "Instagram, Spotify and Netflix all use Python.", "Python iko kila mahali"),
                       ("Your move", "Pick the area that excites you. That's Level 4.", "Chagua unachopenda")][p], seed=n)
        finish(s)
        s.save(n)

    # ── 11 · level 4 ─────────────────────────────────────────────────────────────────────────────
    s = page(11, "Level 4 · Specialise", "Months 6–9")
    level_tag(s, 4)
    title2(s, "Pick one path.", "Go deep.", y=300, size=86)
    table(s, M, 420, ["Path", "Learn in this order"], [[a, b] for a, b, _ in PATHS], [230, 698], size=23, rh=78)
    horizon(s, 11)
    navy_note(s, "Rule", "One path for six months beats six paths for one month.", "Njia moja kwanza", seed=11)
    finish(s)
    s.save(11)

    # ── 12 · level 5 ─────────────────────────────────────────────────────────────────────────────
    s = page(12, "Level 5 · Professional", "Month 9+")
    level_tag(s, 5)
    title2(s, "Work like", "a professional.", y=300, size=86)
    tick_fill(s, [("Git every day", "Branches, pull requests, clear commits."), ("Tests and code reviews", "Give and take feedback."),
                  ("Docker + deploy", "Your code runs on servers, not only your laptop."), ("Docs and READMEs", "Others can use what you build."),
                  ("Problem solving for interviews", "Data structures and algorithms practice."), ("Real users", "Freelance, open source or a team project.")],
              450, 990, size=27, sub=21, max_gap=30)
    horizon(s, 12)
    navy_note(s, "Truth", "Professional means reliable, not knowing everything.", "Kuaminika ni ujuzi", seed=12)
    finish(s)
    s.save(12)

    # ── 13 · projects per level ──────────────────────────────────────────────────────────────────
    s = page(13, "Build as you learn · Jenga")
    title2(s, "One project", "per level.", y=220, size=90)
    table(s, M, 400, ["Level", "Build this"], [["Basics", "Grade calculator, number-guessing game"], ["Intermediate", "Weather app using a free API"],
                                               ["Advanced", "Expense tracker with SQLite + tests"], ["Specialise", "A serious project in your path"],
                                               ["Professional", "Something real people use, deployed"]], [250, 678], size=25, rh=86)
    horizon(s, 13)
    navy_note(s, "Remember", "Projects teach what tutorials can't.", "Jenga ukijifunza", seed=13)
    finish(s)
    s.save(13)

    # ── 14 · resources ───────────────────────────────────────────────────────────────────────────
    s = page(14, "Free resources · Bure")
    title2(s, "Learn it", "for free.", y=220, size=92)
    numbered(s, RESOURCES, 420, gap=96, ts=29, bs=22)
    horizon(s, 14)
    navy_note(s, "Plus", "Python Daily, the free book: every level in detail.", "Pakua bure", seed=14)
    finish(s)
    s.save(14)

    # ── 15 · habits ──────────────────────────────────────────────────────────────────────────────
    s = page(15, "How to win · Siri")
    title2(s, "Habits that", "get you there.", y=220, size=90)
    tick_fill(s, [("Code a little every day", "One hour daily beats a weekend marathon."), ("Read the error, bottom line first", "It usually tells you the fix."),
                  ("Build before you feel ready", "You'll never feel ready. Build anyway."), ("Use AI as a tutor", "Ask it to explain, not to do your work."),
                  ("Learn in public", "Share progress on LinkedIn or your status.")], 410, 990, size=28, sub=22, max_gap=48)
    horizon(s, 15)
    navy_note(s, "Avoid", "Jumping to Django or AI before the basics.", "Usiruke hatua", seed=15)
    finish(s)
    s.save(15)

    # ── 16 · closing ─────────────────────────────────────────────────────────────────────────────
    s = page(TOTAL, "The end · Mwisho")
    closing(s, "Which level are", "you on right now?", [("Comment", "your level and your area"), ("Download", "the free book, Python Daily"),
                                                      ("Share", "with someone learning Python")])
    paste_print(s, print_art("python", k(340)), 680, 660)
    horizon(s, TOTAL)
    closing_footer(s)
    finish(s)
    s.save(TOTAL)
    print("ok")
