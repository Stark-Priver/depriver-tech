"""Carousel: "Itachukua siku 2": how to estimate your time (8 slides, 1080x1350, exported at 2x). Ujuzi wa kazini. The
device is a plan-vs-reality bar chart (Gantt style): the short orange plan bar and the long red real one."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/estimate-your-time"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def gantt(s, y, rows, days=14, x0=M + 230, x1=None, rh=70):
    """Rows: (label, start, length, colour). Day grid with numbers."""
    x1 = x1 or W - M
    dw = (x1 - x0) / days
    for d in range(days + 1):
        s.rect(x0 + d * dw, y - 10, x0 + d * dw + 1.5, y + rh * len(rows), RULE)
        if d < days:
            s.text(x0 + d * dw + dw / 2, y - 22, str(d + 1), f(MED, 15), GREY, anchor="ms")
    for i, (lab, st, ln, col) in enumerate(rows):
        yy = y + i * rh
        s.text(M, yy + rh / 2 + 10, lab, f(SEMI, fit(s, lab, SEMI, 25, 220)), NAVY)
        s.d.rounded_rectangle([k(x0 + st * dw + 3), k(yy + 14), k(x0 + (st + ln) * dw - 3), k(yy + rh - 14)], radius=k(12), fill=col)
    return y + rh * len(rows)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Skills uni skips · Ujuzi wa kazini")
s.text(M - 6, 260, "“Itachukua", f(BOLD, 104), NAVY)
s.text(M - 6, 370, "siku 2.”", f(BOLD, 104), ORANGE)
s.text(M, 460, "(It took two weeks.)", f(SIG, 58), NAVY)
swash(s, M + 8, M + 470, 486, ORANGE, 6)
gantt(s, 620, [("Plan", 0, 2, ORANGE), ("Reality", 0, 13, RED_NO)], rh=90)
s.para(M, 880, "How to estimate tasks honestly, and what to say when you're late.", f(REG, 28), W - 2 * M, 42, GREY)
horizon(s, 1)
cover_footer(s, "Swipe, plan like a pro")
finish(s)
s.save(1)

# ── 2 · why ──────────────────────────────────────────────────────────────────────────────────────
s = page(2, "Why it fails · Kwa nini inashindwa", "Ujuzi wa kazini")
title2(s, "Why estimates", "always slip.", y=220, size=88)
tick_fill(s, [("You only count the coding", "Not testing, fixing, meetings or deploying."), ("Unknowns hide inside", "A new library, a strange bug, missing data."),
              ("Interruptions", "Classes, family, power cuts, no bundle."), ("Optimism", "We imagine the day where everything works first time.")],
          420, 990, size=31, sub=26, ok=False)
horizon(s, 2)
navy_note(s, "Truth", "Even seniors get it wrong. They just plan for it.", "Hata wakubwa hukosea", seed=2)
finish(s)
s.save(2)

# ── 3 · break it down ────────────────────────────────────────────────────────────────────────────
s = page(3, "Break it down · Gawanya", "Ujuzi wa kazini")
title2(s, "Big task?", "Cut it small.", y=220, size=92)
table(s, M, 410, ["Feature: login", "Hours"], [["Login form (screen)", "3"], ["API endpoint + validation", "4"], ["Password hashing + sessions", "3"],
                                               ["Error messages", "2"], ["Total", "12"]],
      [600, W - 2 * M - 8 - 600], size=27, rh=80, hl_rows=(4,))
horizon(s, 3)
navy_note(s, "Rule", "If a task is bigger than one day, split it again.", "Kazi ndogo ndogo", seed=3)
finish(s)
s.save(3)

# ── 4 · hidden work ──────────────────────────────────────────────────────────────────────────────
s = page(4, "Hidden work · Kazi iliyojificha", "Ujuzi wa kazini")
title2(s, "Add the work", "nobody sees.", y=220, size=88)
gantt(s, 440, [("Build", 0, 3, NAVY), ("Test", 3, 1, ORANGE), ("Fix bugs", 4, 2, ORANGE), ("Review", 6, 1, ORANGE), ("Deploy", 7, 1, ORANGE),
               ("Docs", 8, 1, ORANGE)], days=10, rh=82)
horizon(s, 4)
navy_note(s, "Look", "Building was 3 days. The real job took 9.", "Si code peke yake", seed=4)
finish(s)
s.save(4)

# ── 5 · buffer ───────────────────────────────────────────────────────────────────────────────────
s = page(5, "Buffer · Akiba ya muda", "Ujuzi wa kazini")
title2(s, "Give a range,", "not a number.", y=220, size=88)
table(s, M, 410, ["Situation", "Multiply by"], [["Done it before", "× 1.3"], ["Similar, some new parts", "× 1.5"], ["Brand new tech for you", "× 2"],
                                                 ["Depends on other people", "× 2 or more"]],
      [600, W - 2 * M - 8 - 600], size=27, rh=86)
s.text(M, 900, "Say “3 to 5 days”, not “3 days”.", f(BOLD, 34), ORANGE)
horizon(s, 5)
navy_note(s, "Rule of thumb", "Under-promise, over-deliver. Never the opposite.", "Ahidi kidogo, toa zaidi", seed=5)
finish(s)
s.save(5)

# ── 6 · track ────────────────────────────────────────────────────────────────────────────────────
s = page(6, "Track it · Fuatilia", "Ujuzi wa kazini")
title2(s, "Learn from", "your own numbers.", y=220, size=86)
table(s, M, 410, ["Task", "Guess", "Real"], [["Login screen", "3h", "5h"], ["Sales report", "4h", "9h"], ["Deploy", "1h", "3h"], ["Your ratio", "", "≈ × 2"]],
      [440, 230, W - 2 * M - 8 - 670], size=27, rh=84, hl_rows=(3,))
s.para(M, 860, "After a few weeks you'll know your own ratio. Use it for every new estimate.", f(MED, 29), W - 2 * M, 42, NAVY)
horizon(s, 6)
navy_note(s, "Easy", "A simple sheet with three columns is enough.", "Daftari linatosha", seed=6)
finish(s)
s.save(6)

# ── 7 · communicate ──────────────────────────────────────────────────────────────────────────────
s = page(7, "Speak early · Sema mapema", "Ujuzi wa kazini")
title2(s, "Late? Say it", "early.", y=220, size=92)
chat(s, M, 420, 760, "Habari boss, login itachelewa: password reset ilikuwa ngumu kuliko nilivyofikiri. Nitamaliza Alhamisi badala ya leo. Nimeshamaliza fomu na API.",
     "You", mine=True, size=26, lh=36)
tick_list(s, [("What's late, and why (one line)", None), ("The new date", None), ("What IS done already", None)], 780, size=29)
horizon(s, 7)
navy_note(s, "Never", "Surprising people on the deadline day.", "Usisubiri dakika ya mwisho", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What took you way", "longer than planned?", [("Comment", "your “siku 2” story"), ("Save", "for your next project"),
                                                       ("Share", "with your group project team")])
stamp(s, 840, 860, "KWA WAKATI", GREEN_OK, angle=-10, size=40)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
