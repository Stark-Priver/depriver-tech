"""Carousel: how to study programming for exams (8 slides, 1080x1350, exported at 2x). Timed for mid-November exams.
The device is an exam paper: ruled sheet, handwritten code, red-pen marks and a trace table."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/study-programming-for-exams"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def exam_sheet(s, box, q, code, mark=None, ticks=(), lh=44):
    """Ruled exam answer sheet with a question, handwritten-style mono code and red-pen marks."""
    x0, y0, x1, y1 = box
    paper_doc(s, box, rule=True)
    smallcaps(s, x0 + 100, y0 + 60, "Exam answer sheet · CS 1102", 13, GREY)
    s.para(x0 + 100, y0 + 108, q, f(SEMI, 22), x1 - x0 - 150, 30, NAVY)
    yy = y0 + 108 + wrap_lines(s, q, f(SEMI, 22), x1 - x0 - 150) * 30 + 26
    for i, ln in enumerate(code):
        s.text(x0 + 100, yy, ln, f(MONO, 22), (30, 50, 110))
        if i in ticks:
            mark_x = x0 + 110 + s.width(ln, f(MONO, 22)) + 16
            s.d.line([k(mark_x), k(yy - 10), k(mark_x + 8), k(yy - 2), k(mark_x + 24), k(yy - 22)], fill=RED_NO, width=k(4), joint="curve")
        yy += lh
    if mark:
        red_ring(s, x1 - 150, y1 - 120, x1 - 30, y1 - 36)
        s.text(x1 - 90, y1 - 74, mark, f(SIG, 44), RED_NO, anchor="mm")


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Exam season · Msimu wa mitihani")
s.text(M - 6, 250, "Programming", f(BOLD, 96), NAVY)
s.text(M - 6, 350, "exam?", f(BOLD, 96), NAVY)
s.text(M - 8, 470, "Don't memorise.", f(BOLD, 84), ORANGE)
s.text(M, 560, "Usikariri, elewa", f(SIG, 60), NAVY)
swash(s, M + 8, M + 420, 586, ORANGE, 6)
s.para(M, 670, "How to prepare when the exam asks you to write and trace code on paper.", f(REG, 27), 430, 40, GREY)
exam_sheet(s, (540, 560, W - M, 1000), "Q3. Return the largest number in a list.",
           ["def largest(nums):", "  big = nums[0]", "  for n in nums:", "    if n > big:", "      big = n", "  return big"], mark="9/10", ticks=(1, 5), lh=38)
horizon(s, 1)
cover_footer(s, "Swipe for the study plan")
finish(s)
s.save(1)

# ── 2 · why memorising fails ─────────────────────────────────────────────────────────────────────
s = page(2, "The trap · Mtego")
title2(s, "Memorising", "fails here.", y=220, size=88)
s.para(M, 410, "You memorised “largest number in a list”. The exam asks for the smallest, or the second largest. Same idea, different code.",
       f(MED, 30), W - 2 * M, 44, NAVY)
exam_sheet(s, (M, 590, W - M - 8, 960), "Q3. Return the SMALLEST number in a list.",
           ["def largest(nums):", "  big = nums[0]", "  ...  (memorised answer)"])
for yy in (745, 789, 833):
    strike(s, M + 96, M + 470, yy)
red_note(s, 600, 820, "Hukuelewa swali!", 46)
horizon(s, 2)
navy_note(s, "Truth", "Lecturers change one detail on purpose. Understanding survives that.", "Elewa, usikariri", seed=2)
finish(s)
s.save(2)

# ── 3 · practise like the exam ───────────────────────────────────────────────────────────────────
s = page(3, "Practise · Fanya mazoezi")
title2(s, "Practise the way", "you'll be tested.", y=220, size=80)
tick_fill(s, [("Write code by hand", "On paper, no autocomplete, no red underlines to save you."),
              ("Time yourself", "If a question is worth 10 marks, give it about 15 minutes."),
              ("Then type it and run it", "The computer marks your paper answer honestly."),
              ("Explain it out loud", "If you can't explain a line, you don't own it yet.")], 440, 990, size=34, sub=28)
horizon(s, 3)
navy_note(s, "Tip", "Keep one notebook only for hand-written code practice.", "Mkono kwanza, kompyuta baadaye", seed=3)
finish(s)
s.save(3)

# ── 4 · trace tables ─────────────────────────────────────────────────────────────────────────────
s = page(4, "Trace tables · Fuatilia code")
title2(s, "Be the computer.", "Trace it.", y=220, size=84)
code_window(s, 380, ["total = 0", "for i in range(1, 4):", "    total = total + i", "print(total)"], file="swali_2.py", size=25, lh=40)
table(s, M, 650, ["Step", "i", "total"], [["Start", "-", "0"], ["Loop 1", "1", "1"], ["Loop 2", "2", "3"], ["Loop 3", "3", "6"]],
      [330, 230, W - 2 * M - 8 - 560], size=26, rh=64, hl_rows=(3,))
horizon(s, 4)
navy_note(s, "Answer", "It prints 6. range(1, 4) stops before 4.", "Andika kila hatua", seed=4)
finish(s)
s.save(4)

# ── 5 · past papers ──────────────────────────────────────────────────────────────────────────────
s = page(5, "Past papers · Mitihani iliyopita")
title2(s, "Past papers", "are gold.", y=220, size=92)
flow(s, [("Get 3 years of past papers", "Class reps, seniors, the library."), ("Solve one without notes", "Timed, like the real exam."),
         ("Mark it honestly", "Run your code. Compare with seniors."), ("Redo only what you got wrong", "Two days later, from scratch.")],
     420, h=100, gap=36, size=29)
horizon(s, 5)
navy_note(s, "Pattern", "Topics repeat. After three papers you'll see what comes every year.", "Maswali hujirudia", seed=5)
finish(s)
s.save(5)

# ── 6 · study together ───────────────────────────────────────────────────────────────────────────
s = page(6, "Study group · Kusoma pamoja")
title2(s, "Teach it", "to a friend.", y=220, size=92)
s.para(M, 420, "Explaining forces you to understand. Each person picks one topic and teaches it in 10 minutes.", f(MED, 30), W - 2 * M, 44, NAVY)
tick_fill(s, [("Small group: 3 to 4 people", "Bigger groups turn into chatting."), ("One topic each", "Loops, arrays, functions, OOP: 10 minutes each."),
              ("Swap and mark past papers", "You learn fast from other people's mistakes."), ("Phones away for 50 minutes", "Then a 10-minute break.")], 580, 1000, size=31, sub=26)
horizon(s, 6)
navy_note(s, "Rule", "If nobody can explain it, ask the lecturer this week, not on exam day.", "Uliza mapema", seed=6)
finish(s)
s.save(6)

# ── 7 · exam day ─────────────────────────────────────────────────────────────────────────────────
s = page(7, "Exam day · Siku ya mtihani")
title2(s, "In the exam", "room.", y=220, size=92)
numbered(s, [("Read every question first", "Then start with the one you know best."), ("Plan before you write", "Three lines of steps, in plain words."),
             ("Write clean, readable code", "Good names. Lecturers mark what they can read."), ("Stuck? Write the logic anyway", "Steps and comments can still earn marks."),
             ("Check the edges", "Empty list? Zero? Negative numbers?")], 430, gap=112)
horizon(s, 7)
navy_note(s, "Sleep", "A rested brain debugs better than a tired one.", "Lala vizuri", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which exam is", "your hardest?", [("Save", "for your revision week"), ("Share", "with your study group"),
                                              ("Comment", "the course code, I'll help where I can")])
stamp(s, 840, 860, "PASS", GREEN_OK, angle=-10, size=60)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
