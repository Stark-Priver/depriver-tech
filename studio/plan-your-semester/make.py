"""Carousel: plan your semester (8 slides, 1080x1350, exported at 2x). Timed for the start of semester 2. The device is a
15-week semester strip with markers for tests, assignments and exams, plus a weekly timetable grid."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/plan-your-semester"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs

MARKS = {4: ("A1", ORANGE), 6: ("CAT", RED_NO), 8: ("A2", ORANGE), 10: ("CAT", RED_NO), 12: ("FYP", NAVY), 15: ("EXAM", RED_NO)}


def semester(s, y, h=110, weeks=15, marks=MARKS):
    cw = (W - 2 * M) / weeks
    for i in range(weeks):
        x0 = M + i * cw
        m = marks.get(i + 1)
        s.d.rounded_rectangle([k(x0 + 2), k(y), k(x0 + cw - 2), k(y + h)], radius=k(8), fill=(255, 255, 255) if not m else m[1],
                              outline=NAVY if m else (214, 219, 230), width=k(2))
        s.text(x0 + cw / 2, y + 30, f"W{i + 1}", f(BOLD, 15), WHITE_T if m else GREY, anchor="mm")
        if m:
            s.text(x0 + cw / 2, y + h - 30, m[0], f(BOLD, 13), WHITE_T, anchor="mm")


def week_grid(s, y, rows, h=64):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    cw = (W - 2 * M - 120) / 7
    for i, d in enumerate(days):
        s.text(M + 120 + i * cw + cw / 2, y - 14, d, f(BOLD, 18), NAVY, anchor="ms")
    cols = {"Class": NAVY, "Study": ORANGE, "Project": GREEN_OK, "Rest": (190, 198, 214), "": (244, 245, 248)}
    for r, (lab, cells) in enumerate(rows):
        yy = y + r * (h + 8)
        s.text(M, yy + h / 2 + 8, lab, f(SEMI, 20), GREY)
        for i, c in enumerate(cells):
            x0 = M + 120 + i * cw
            s.d.rounded_rectangle([k(x0 + 3), k(yy), k(x0 + cw - 3), k(yy + h)], radius=k(8), fill=cols[c])
            if c:
                s.text(x0 + cw / 2, yy + h / 2, c, f(SEMI, 15), WHITE_T if c != "Rest" else NAVY, anchor="mm")
    return y + len(rows) * (h + 8)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Semester 2 · Muhula wa pili")
s.text(M - 6, 260, "15 weeks.", f(BOLD, 120), NAVY)
s.text(M - 6, 370, "Plan them now.", f(BOLD, 100), ORANGE)
s.text(M, 460, "Panga muhula wako", f(SIG, 60), NAVY)
swash(s, M + 8, M + 420, 486, ORANGE, 6)
s.para(M, 570, "One hour of planning in week 1 saves you from the week-14 panic.", f(REG, 28), W - 2 * M, 42, GREY)
semester(s, 700)
x = M
for lab, col in [("Assignment", ORANGE), ("Test (CAT)", RED_NO), ("Project", NAVY)]:
    s.d.rounded_rectangle([k(x), k(860), k(x + 26), k(886)], radius=k(6), fill=col)
    s.text(x + 36, 882, lab, f(SEMI, 21), NAVY)
    x += 60 + s.width(lab, f(SEMI, 21)) + 20
horizon(s, 1)
cover_footer(s, "Swipe, plan in one hour")
finish(s)
s.save(1)

# ── 2 · collect dates ────────────────────────────────────────────────────────────────────────────
s = page(2, "Step 1 · Hatua ya kwanza", "Panga muhula")
title2(s, "Put every date", "in one place.", y=220, size=86)
tick_fill(s, [("Collect every course outline", "Week 1, from lecturers or the class rep."), ("Copy every deadline", "Assignments, tests, presentations, exams."),
              ("One calendar for all of it", "Google Calendar on your phone, with reminders."), ("Reminder 1 week before", "Not the night before.")],
          420, 990, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Why", "You can't plan for a deadline you forgot exists.", "Kalenda moja", seed=2)
finish(s)
s.save(2)

# ── 3 · weekly rhythm ────────────────────────────────────────────────────────────────────────────
s = page(3, "Your week · Wiki yako", "Panga muhula")
title2(s, "Give every week", "a rhythm.", y=220, size=86)
week_grid(s, 430, [("Morning", ["Class", "Class", "Class", "Class", "Class", "Project", "Rest"]),
                   ("Afternoon", ["Study", "Class", "Study", "Class", "Study", "Project", "Rest"]),
                   ("Evening", ["Study", "Study", "Project", "Study", "Rest", "Rest", "Study"])], h=110)
s.para(M, 860, "An example. Block study time like it's a class you can't skip.", f(MED, 28), W - 2 * M, 40, NAVY)
horizon(s, 3)
navy_note(s, "Sunday evening", "15 minutes to plan the week ahead.", "Jumapili jioni", seed=3)
finish(s)
s.save(3)

# ── 4 · side project ─────────────────────────────────────────────────────────────────────────────
s = page(4, "Side project · Mradi binafsi", "Panga muhula")
title2(s, "Keep one project", "alive.", y=220, size=88)
tick_fill(s, [("2 to 3 hours a week", "Small, steady, every week. Weekends work well."), ("Link it to a course", "Database course? Build the database for your project."),
              ("Push to GitHub weekly", "Your profile shows a whole semester of work."), ("Finish small", "One feature done beats ten half-done.")],
          420, 990, size=31, sub=26)
horizon(s, 4)
navy_note(s, "Result", "By the end of the semester you have a portfolio piece, not just grades.", "Alama + portfolio", seed=4)
finish(s)
s.save(4)

# ── 5 · no last minute ───────────────────────────────────────────────────────────────────────────
s = page(5, "No last minute · Bila dakika za mwisho", "Panga muhula")
title2(s, "Start assignments", "the day you get them.", y=220, size=80)
flow(s, [("Day 1: read it and ask questions", "While the lecturer still remembers it"), ("Split it into 3 parts", "Plan, build, write up"),
         ("Do one part a week", "Small sessions, not one all-nighter"), ("Finish 2 days early", "Time to check, print and submit calmly")],
     420, h=100, gap=36, size=29)
horizon(s, 5)
navy_note(s, "Truth", "Assignments take the same time either way. Early is just calmer.", "Mapema ni amani", seed=5)
finish(s)
s.save(5)

# ── 6 · health ───────────────────────────────────────────────────────────────────────────────────
s = page(6, "Your body too · Afya", "Panga muhula")
title2(s, "Your brain needs", "fuel and sleep.", y=220, size=84)
tick_fill(s, [("7 hours of sleep", "Most bugs and bad marks come from tired brains."), ("Real meals", "Not just chips and energy drinks."),
              ("Move a little every day", "A walk, football, the gym."), ("Phone limits while studying", "Notifications off for 50-minute blocks.")],
          420, 990, size=31, sub=26)
horizon(s, 6)
navy_note(s, "Remember", "Struggling? Talk to someone. Every campus has support.", "Usibebe peke yako", seed=6)
finish(s)
s.save(6)

# ── 7 · weekly check ─────────────────────────────────────────────────────────────────────────────
s = page(7, "Weekly check · Tathmini ya wiki", "Panga muhula")
title2(s, "15 minutes", "every Sunday.", y=220, size=90)
paper_doc(s, (M, 400, W - M - 8, 1000), title="Sunday check · Week __")
y = 530
for q in ["What's due in the next 2 weeks?", "What did I finish this week?", "What's my ONE priority for next week?", "Project: what will I push to GitHub?"]:
    s.d.rounded_rectangle([k(M + 36), k(y - 26), k(M + 64), k(y + 2)], radius=k(6), outline=NAVY, width=k(3))
    s.text(M + 84, y, q, f(SEMI, 28), NAVY)
    s.rect(M + 84, y + 50, W - M - 60, y + 51.5, RULE)
    y += 110
horizon(s, 7)
navy_note(s, "Habit", "Same time every week. It becomes automatic.", "Kila Jumapili", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What's your goal", "this semester?", [("Comment", "your goal: a grade, a project, a habit"), ("Save", "the Sunday checklist"),
                                                 ("Share", "with your study group")])
stamp(s, 840, 860, "TAYARI", GREEN_OK, angle=-10, size=56)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
