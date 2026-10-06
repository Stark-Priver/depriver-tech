"""Carousel: Uongo au Kweli? Six tech myths students believe (8 slides, 1080x1350, exported at 2x). Each myth is a torn
slip stamped UONGO in red, the truth a navy card. Honest, not preachy: where a myth is half true, say so."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/uongo-au-kweli"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def slip(s, y, said, n, h=170):
    """Myth as a torn slip with a zigzag bottom edge."""
    x0, x1 = M, W - M - 8
    pts = [(x0, y), (x1, y), (x1, y + h)]
    x = x1
    while x > x0:
        pts += [(x - 12, y + h + 12), (max(x0, x - 24), y + h)]
        x -= 24
    pts.append((x0, y + h))
    s.d.polygon([(k(a + 8), k(b + 10)) for a, b in pts], fill=INK_SHADOW)
    s.d.polygon([(k(a), k(b)) for a, b in pts], fill=(255, 255, 255))
    s.d.line([(k(a), k(b)) for a, b in pts + [pts[0]]], fill=NAVY, width=k(3))
    smallcaps(s, x0 + 32, y + 48, f"Wanasema · Myth {n:02d}", 15, RED_NO)
    s.para(x0 + 32, y + 108, said, f(BOLD, 42), x1 - x0 - 300, 52, NAVY)


def truth(s, y, lines, label="Ukweli · The truth"):
    x0, x1 = M, W - M - 8
    h = 80 + 50 * len(lines) + 14
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + h)], radius=k(18), fill=NAVY)
    smallcaps(s, x0 + 32, y + 50, label, 15, ORANGE)
    yy = y + 104
    for ln in lines:
        s.text(x0 + 32, yy, ln, f(MED, fit(s, ln, MED, 30, x1 - x0 - 64)), WHITE_T)
        yy += 50
    return y + h


DO = ['Start with web or apps. Learn more maths when a path needs it.', 'Use the laptop you have. Try Linux or WSL to make it lighter.', 'Pick one free course this week and finish it.', 'Stay in school, and push one project to GitHub every month.', 'Learn the basics yourself. Ask AI to explain, not to do it for you.', 'Start a free beginner path on TryHackMe. Legal and fun.']

MYTHS = [
    ("Lazima uwe genius wa hesabu.", "You must be a maths genius.", "UONGO",
     ["Most web and app work is logic, patience and Googling.", "School maths is enough to start.", "Data science, AI and games need more maths, later."],
     ("Half true", "Some paths need maths. Most first jobs don't.", "Hesabu ya kawaida inatosha")),
    ("Bila MacBook huwezi ku-code.", "Without a MacBook you can't code.", "UONGO",
     ["Any laptop with 8 GB RAM and an SSD is enough.", "Linux makes old laptops fast again.", "A Mac is only required to publish iOS apps."],
     ("Truth", "The developer matters more than the laptop.", "Si laptop, ni wewe")),
    ("Umechelewa. Una miaka 25.", "It's too late, you're 25.", "UONGO",
     ["People start tech at 25, 35, even 45.", "Employers check what you can build, not your age.", "Your other experience is an advantage."],
     ("Truth", "The best time was yesterday. The next best is today.", "Hujachelewa")),
    ("Degree haina maana kwenye tech.", "A degree is useless in tech.", "NUSU",
     ["A degree opens doors: HR filters, government jobs, visas.", "But skills and projects get you hired.", "Best: finish the degree and build on the side."],
     ("Both", "Degree opens the door. Skills keep you in the room.", "Vyote viwili")),
    ("AI itachukua kazi zote za tech.", "AI will take every tech job.", "UONGO",
     ["AI writes code fast, and also makes mistakes.", "Someone must understand, check and own the result.", "People who use AI well replace people who don't."],
     ("Truth", "Learn the basics deeply, then use AI as your tool.", "AI ni chombo")),
    ("Cybersecurity ni ku-hack watu.", "Cybersecurity means hacking people.", "UONGO",
     ["It's mostly defence: protecting systems and people.", "Hacking accounts without permission is a crime", "(Cybercrimes Act, 2015). Practise on legal labs only."],
     ("Truth", "Real security pros protect. Criminals end up in court.", "Linda, usivamie")),
]

# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Tech myths · Hadithi za tech")
s.text(M - 6, 270, "Uongo", f(BOLD, 150), NAVY)
s.text(M - 6, 400, "au Kweli?", f(BOLD, 150), ORANGE)
s.text(M, 500, "Hadithi sita unazosikia kila siku", f(SIG, 54), NAVY)
swash(s, M + 8, M + 640, 526, ORANGE, 6)
s.para(M, 610, "Six things students believe about tech. Some are lies, one is half true.", f(REG, 28), 470, 42, GREY)
for i, (sw, en, verdict, _, _) in enumerate(MYTHS[:3]):
    y = 610 + i * 120
    s.d.rounded_rectangle([k(600 + 6), k(y + 8), k(W - M + 6), k(y + 92)], radius=k(12), fill=INK_SHADOW)
    s.d.rounded_rectangle([k(600), k(y), k(W - M), k(y + 84)], radius=k(12), fill=(255, 255, 255), outline=NAVY, width=k(2.5))
    s.text(626, y + 52, en, f(SEMI, fit(s, en, SEMI, 22, W - M - 640)), NAVY)
stamp(s, 820, 740, "UONGO", RED_NO, angle=-14, size=58)
stamp(s, 760, 990, "KWELI?", GREEN_OK, angle=8, size=38)
horizon(s, 1)
cover_footer(s, "Swipe, guess before you read")
finish(s)
s.save(1)

# ── 2–7 · myths ──────────────────────────────────────────────────────────────────────────────────
for i, (sw, en, verdict, lines, note) in enumerate(MYTHS):
    n = i + 2
    s = page(n, f"Hadithi {i + 1:02d} / 06", "Uongo au Kweli?")
    slip(s, 190, sw, i + 1)
    s.text(M + 32, 450, en, f(MED, 28), GREY)
    stamp(s, W - M - 150, 300, verdict, RED_NO if verdict == "UONGO" else (220, 140, 30), angle=-12, size=56)
    y = truth(s, 520, lines)
    label_box(s, (M, y + 50, W - M - 8, y + 50 + 96 + para_h(s, DO[i], 30, W - 2 * M - 78, 44)), "Fanya hivi · Do this instead", DO[i], col=GREEN_OK, size=30, lh=44)
    horizon(s, n)
    navy_note(s, note[0], note[1], note[2], seed=n)
    finish(s)
    s.save(n)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which myth did", "you believe?", [("Comment", "the number: 1, 2, 3, 4, 5 or 6"), ("Share", "with someone who needs to hear #3"),
                                             ("Add", "a myth I missed")])
stamp(s, 830, 860, "KWELI", GREEN_OK, angle=-10, size=56)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
