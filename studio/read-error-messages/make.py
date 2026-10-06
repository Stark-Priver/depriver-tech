"""Carousel: read the error message, it's telling you (8 slides, 1080x1350, exported at 2x). Ujuzi wa kazini. The device is
a terminal traceback with labelled parts, read from the bottom up."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/read-error-messages"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs

TB = ["$ python sales.py", "Traceback (most recent call last):", '  File "sales.py", line 12, in <module>',
      "    total = total + sale[\"amount\"]", "!TypeError: unsupported operand type(s)", "!for +: 'int' and 'str'"]


def tag(s, x, y, n, text, col=ORANGE):
    s.d.ellipse([k(x - 20), k(y - 20), k(x + 20), k(y + 20)], fill=col)
    s.text(x, y, str(n), f(BOLD, 20), WHITE_T, anchor="mm")
    s.text(x + 34, y + 9, text, f(BOLD, 27), NAVY)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Skills uni skips · Ujuzi wa kazini")
s.text(M - 6, 250, "Read the error.", f(BOLD, 96), NAVY)
s.text(M - 6, 350, "It's telling you.", f(BOLD, 96), ORANGE)
s.text(M, 440, "Kosa linakuambia kitu", f(SIG, 58), NAVY)
swash(s, M + 8, M + 470, 466, ORANGE, 6)
terminal(s, 540, TB, title="terminal", size=23, lh=40)
s.text(M, 950, "Most beginners see red text and panic.", f(SEMI, 27), NAVY)
s.text(M, 990, "Seniors read it. Here's how.", f(SEMI, 27), GREY)
horizon(s, 1)
cover_footer(s, "Swipe, stop panicking")
finish(s)
s.save(1)

# ── 2 · anatomy ──────────────────────────────────────────────────────────────────────────────────
s = page(2, "Anatomy · Muundo wa kosa", "Ujuzi wa kazini")
title2(s, "Three parts.", "Every time.", y=220, size=92)
y = terminal(s, 370, TB[1:], title="terminal", size=23, lh=40)
tag(s, M + 20, y + 70, 1, "Where:  sales.py, line 12")
tag(s, M + 20, y + 140, 2, "What:  TypeError (wrong type)", NAVY)
tag(s, M + 20, y + 210, 3, "Why:  adding a number and text")
horizon(s, 2)
navy_note(s, "The fix", "sale[\"amount\"] is text. Use int(sale[\"amount\"]).", "Soma sehemu tatu", seed=2)
finish(s)
s.save(2)

# ── 3 · bottom up ────────────────────────────────────────────────────────────────────────────────
s = page(3, "Read bottom-up · Soma kutoka chini", "Ujuzi wa kazini")
title2(s, "Start from the", "last line.", y=220, size=88)
tick_fill(s, [("The last line is the real message", "Error type and reason. Read it slowly, word by word."),
              ("Then find YOUR file in the trace", "Skip lines from libraries. Find your file and line number."),
              ("Go to that exact line", "Check the values there with a print() or the debugger."),
              ("The bug may be one line earlier", "A missing bracket often shows up on the next line.")], 420, 990, size=31, sub=26)
horizon(s, 3)
navy_note(s, "Habit", "Read the message out loud before you change any code.", "Soma kabla ya kubadilisha", seed=3)
finish(s)
s.save(3)

# ── 4 · common errors ────────────────────────────────────────────────────────────────────────────
s = page(4, "Common errors · Makosa ya kawaida", "Ujuzi wa kazini")
title2(s, "Learn these", "six by heart.", y=220, size=88)
table(s, M, 400, ["Error", "Usually means"], [["SyntaxError", "Typo: bracket, colon, quote"], ["NameError", "Name misspelt or not defined"],
                                               ["TypeError", "Wrong type: text vs number"], ["IndexError", "List position doesn't exist"],
                                               ["KeyError", "Dictionary key doesn't exist"], ["404 / 500", "Page missing / server crashed"]],
      [330, W - 2 * M - 8 - 330], size=26, rh=78)
horizon(s, 4)
navy_note(s, "Other languages", "JavaScript, PHP and Java have the same ideas with different names.", "Wazo ni lile lile", seed=4)
finish(s)
s.save(4)

# ── 5 · search it ────────────────────────────────────────────────────────────────────────────────
s = page(5, "Search it right · Tafuta vizuri", "Ujuzi wa kazini")
title2(s, "Google like", "a developer.", y=220, size=88)
for j, (lab, q, ok) in enumerate([("Weak search", "my code is not working python help", False),
                                  ("Strong search", "python TypeError unsupported operand int and str", True)]):
    y = 420 + j * 190
    card(s, (M, y, W - M - 8, y + 140), r=40)
    mark(s, M + 50, y + 70, ok, r=20)
    smallcaps(s, M + 90, y + 50, lab, 14, GREEN_OK if ok else RED_NO)
    s.text(M + 90, y + 100, q, f(MONO, fit(s, q, MONO, 26, W - 2 * M - 130)), NAVY)
tick_list(s, [("Copy the exact error type and message", None), ("Remove your own names and file paths", None),
              ("Add the language or framework", None)], 850, size=28)
horizon(s, 5)
navy_note(s, "And AI?", "Paste the error and ask it to EXPLAIN, then fix it yourself.", "Uliza ufafanuzi", seed=5)
finish(s)
s.save(5)

# ── 6 · isolate ──────────────────────────────────────────────────────────────────────────────────
s = page(6, "Isolate it · Tenga tatizo", "Ujuzi wa kazini")
title2(s, "Still stuck?", "Shrink the problem.", y=220, size=84)
flow(s, [("Print the values", "What is sale really? print(type(sale))"), ("Comment out half the code", "Still broken? The bug is in the other half."),
         ("Make the smallest example", "5 lines that show the same error."), ("Explain it to a rubber duck", "Saying it out loud often reveals it.")],
     420, h=100, gap=34, size=29)
horizon(s, 6)
navy_note(s, "Truth", "Half of all bugs are found while writing the question.", "Andika tatizo", seed=6)
finish(s)
s.save(6)

# ── 7 · ask for help ─────────────────────────────────────────────────────────────────────────────
s = page(7, "Ask well · Uliza vizuri", "Ujuzi wa kazini")
title2(s, "Ask for help", "the right way.", y=220, size=88)
paper_doc(s, (M, 410, W - M - 8, 1000), title="My question · Swali langu")
y = 520
for lab, txt in [("1 · Goal", "Add up today's sales from sales.csv"), ("2 · Expected", "A total like 245000"),
                 ("3 · Got", "TypeError: unsupported operand… (full error below)"), ("4 · Tried", "Printed sale[\"amount\"]: it's '5000' (text)"),
                 ("5 · Code", "The 6 smallest lines that show the problem")]:
    smallcaps(s, M + 36, y, lab, 14, ORANGE)
    s.text(M + 36, y + 40, txt, f(MED, fit(s, txt, MED, 26, W - 2 * M - 90)), NAVY)
    y += 92
horizon(s, 7)
navy_note(s, "Never send", "“Guys code yangu haifanyi kazi” with a blurry photo.", "Screenshot, si picha ya skrini", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What error haunts", "you the most?", [("Comment", "the error, I'll explain it"), ("Save", "for your next red screen"),
                                                ("Share", "with the friend who panics")])
stamp(s, 840, 860, "IMETATULIWA", GREEN_OK, angle=-10, size=36)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
