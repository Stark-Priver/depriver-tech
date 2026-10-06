"""Carousel: your 2027 tech roadmap (8 slides, 1080x1350, exported at 2x). Timed for the new year. The device is a
winding road with four quarter flags (Q1–Q4); each quarter slide highlights its flag."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/tech-roadmap-2027"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs

QUARTERS = [("Q1", "Jan–Mar", "Foundations"), ("Q2", "Apr–Jun", "Specialise"), ("Q3", "Jul–Sep", "Experience"), ("Q4", "Oct–Dec", "Show & apply")]


def road(s, y, h=220, active=None, x0=M, x1=None):
    """Winding road across the width with four flags; active flag is orange, others navy."""
    x1 = x1 or W - M
    pts = []
    for i in range(41):
        t = i / 40
        import math
        pts.append((x0 + (x1 - x0) * t, y + h / 2 + math.sin(t * math.pi * 2.2) * h * 0.32))
    s.d.line([(k(a), k(b + 8)) for a, b in pts], fill=INK_SHADOW, width=k(46), joint="curve")
    s.d.line([(k(a), k(b)) for a, b in pts], fill=NAVY, width=k(46), joint="curve")
    for i in range(0, 40, 2):
        s.d.line([(k(pts[i][0]), k(pts[i][1])), (k(pts[i + 1][0]), k(pts[i + 1][1]))], fill=(255, 255, 255), width=k(4))
    for q in range(4):
        px, py = pts[5 + q * 10]
        col = ORANGE if active is None or active == q else (150, 158, 175)
        s.d.line([k(px), k(py - 10), k(px), k(py - 100)], fill=NAVY, width=k(5))
        s.d.polygon([(k(px), k(py - 100)), (k(px + 64), k(py - 82)), (k(px), k(py - 64))], fill=col)
        s.text(px + 8, py - 76, QUARTERS[q][0], f(BOLD, 18), WHITE_T)


def quarter_slide(n, q, t1, t2, items, note):
    code, months, theme = QUARTERS[q]
    s = page(n, f"{code} · {months} · {theme}", "Roadmap 2027")
    road(s, 140, h=200, active=q)
    title2(s, t1, t2, y=440, size=80)
    tick_fill(s, items, 640, 1000, size=30, sub=25)
    horizon(s, n)
    navy_note(s, *note, seed=n)
    finish(s)
    s.save(n)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "New year · Mwaka mpya")
s.text(M - 6, 260, "Your 2027", f(BOLD, 110), NAVY)
s.text(M - 6, 375, "tech roadmap.", f(BOLD, 104), ORANGE)
s.text(M, 470, "Mwaka mpya, mpango mpya", f(SIG, 58), NAVY)
swash(s, M + 8, M + 540, 496, ORANGE, 6)
s.para(M, 570, "Four quarters, one clear goal each. Screenshot it and check it every month.", f(REG, 28), W - 2 * M, 42, GREY)
road(s, 700, h=260)
horizon(s, 1)
cover_footer(s, "Swipe for the plan")
finish(s)
s.save(1)

# ── 2 · look back ────────────────────────────────────────────────────────────────────────────────
s = page(2, "Look back first · Tathmini 2026", "Roadmap 2027")
title2(s, "Before 2027,", "look at 2026.", y=220, size=88)
paper_doc(s, (M, 400, W - M - 8, 1000), title="Three honest questions")
y = 530
for lab, q in [("1", "What did I learn and actually build in 2026?"), ("2", "What stopped me? (time, laptop, data, focus)"),
               ("3", "What ONE thing would change my 2027?")]:
    s.d.ellipse([k(M + 36), k(y - 34), k(M + 84), k(y + 14)], fill=ORANGE)
    s.text(M + 60, y - 10, lab, f(BOLD, 24), WHITE_T, anchor="mm")
    s.para(M + 110, y, q, f(SEMI, 30), W - 2 * M - 170, 40, NAVY)
    s.rect(M + 110, y + 70, W - M - 60, y + 71.5, RULE)
    s.rect(M + 110, y + 120, W - M - 60, y + 121.5, RULE)
    y += 150
horizon(s, 2)
navy_note(s, "Write it", "On paper. Ten minutes. No judgement.", "Andika ukweli", seed=2)
finish(s)
s.save(2)

quarter_slide(3, 0, "Q1: build your", "foundations.", [("One language, deeply", "Not five. Finish one course and 20 exercises."),
              ("Git every day", "Every exercise goes to GitHub."), ("One small project a month", "Calculator, to-do, a site for someone.")],
              ("Goal", "By March: 3 projects on GitHub you can explain.", "Msingi imara"))
quarter_slide(4, 1, "Q2: pick", "your path.", [("Choose a direction", "Backend, frontend, mobile, data, security, design."),
              ("Learn its main framework", "Laravel, React, Flutter, Power BI…"), ("Apply early for FPT / internships", "Most deadlines come before June.")],
              ("Goal", "By June: one real project in your chosen path.", "Chagua njia"))
quarter_slide(5, 2, "Q3: get real", "experience.", [("FPT, internship or freelance", "Real users, real deadlines, real feedback."),
              ("Contribute to open source", "Docs, small fixes, translations count."), ("Update LinkedIn monthly", "Post what you built and learned.")],
              ("Goal", "By September: one thing you did for someone else.", "Uzoefu halisi"))
quarter_slide(6, 3, "Q4: show it,", "apply.", [("Polish your portfolio", "Three best projects, clear READMEs, live links."),
              ("CV and interviews", "Apply widely, practise with friends."), ("Teach someone younger", "Teaching locks in what you know.")],
              ("Goal", "By December: applications sent, portfolio live.", "Onyesha kazi"))

# ── 7 · keep it alive ────────────────────────────────────────────────────────────────────────────
s = page(7, "Keep it alive · Endeleza", "Roadmap 2027")
title2(s, "Plans die in", "February.", y=220, size=88)
table(s, M, 410, ["Month", "Built", "Learned"], [["Jan", "", ""], ["Feb", "", ""], ["Mar", "", ""], ["…", "", ""]],
      [200, 380, W - 2 * M - 8 - 580], size=26, rh=70)
tick_list(s, [("Fill one row on the last day of every month", None), ("Find an accountability partner", None)], 830, size=28)
horizon(s, 7)
navy_note(s, "Small", "One row a month is enough to stay on track.", "Kidogo kidogo", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What's your ONE", "goal for 2027?", [("Comment", "your goal, in one line"), ("Tag", "your accountability partner"),
                                                ("Save", "and check it every month")])
stamp(s, 840, 860, "2027", GREEN_OK, angle=-10, size=70)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
