"""Carousel: Tech advice I learnt the hard way (11 slides, 1080x1350, exported at 2x).
Editorial / print direction: strong left grid, small-caps labels, hairlines, huge outlined numerals,
print-style illustrations (grain + offset ink shadow) breaking out of navy colour blocks,
hand-drawn swashes under Swahili lines, hand-placed stickers, paper grain. No portrait."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools
TOTAL = 11
M = 72                                               # page margin
RULE = (200, 206, 218)
WHITE_T = (255, 255, 255)
SOFT = (190, 202, 226)

LESSONS = [
    ("start", "Start with", "what you have", "Anza na ulichonacho",
     "I once went back to university with only a small feature phone. Don't wait for the perfect laptop. Start today.",
     ["Learn on your phone with free apps", "Use campus and library computers", "Upgrade when the work starts paying"]),
    ("skills", "Skills can't", "be stolen", "Ujuzi hauibiwi",
     "I lost my laptop, phone and certificates in one night. What I knew came home with me.",
     ["Invest in learning, not only papers", "Build projects that prove your skills", "Keep learning after class ends"]),
    ("habit", "Consistency", "beats talent", "Haba na haba hujaza kibaba",
     "Thirty minutes every day beats five hours once a week. Small steps add up faster than you think.",
     ["Pick a fixed daily learning time", "Track your streak", "Missed a day? Never miss two"]),
    ("public", "Build in", "public", "Onyesha kazi yako",
     "Nobody can hire what they can't see. Share what you learn and what you build.",
     ["Push your projects to GitHub", "Post progress, not perfection", "Write about what you learnt"]),
    ("hustle", "Solve real", "problems", "Tatua matatizo halisi",
     "Reselling Wi-Fi and repairing computers taught me more business than any class did.",
     ["Find a problem near you", "Charge fairly, deliver well", "Learn from every customer"]),
    ("people", "Your people", "matter", "Mtu ni watu",
     "Friends, teachers and customers carried me through my hardest seasons. Nobody makes it alone.",
     ["Help others generously", "Ask for help with context", "Stay in touch, not only when in need"]),
    ("health", "Protect", "your health", "Afya ni mtaji",
     "Stomach ulcers taught me early: no deadline and no code is worth your health.",
     ["Sleep, drink water, move your body", "Take real breaks from the screen", "Talk to someone when it's heavy"]),
    ("path", "Your path", "is valid", "Njia yako ni yako",
     "People said a diploma was for those who failed. It became my way into tech.",
     ["Choose what fits your goals", "Listen to advice, ignore the noise", "Compare yourself to yesterday"]),
    ("backup", "Back up", "everything", "Usiweke mayai yote kwenye kikapu kimoja",
     "Laptops get stolen and drives fail. Protect your work before you need to.",
     ["3 copies · 2 devices · 1 in the cloud", "Push your code to GitHub daily", "Turn on 2FA everywhere"]),
]
assert len(LESSONS) + 2 == TOTAL

POST_URL = "depriver.tech/blog/tech-advice-i-learnt-the-hard-way"


def page(label_left, label_right="DEPRIVER.TECH"):
    s = Slide()
    paper(s)
    smallcaps(s, M, 96, label_left, 17, ORANGE)
    smallcaps(s, W - M, 96, label_right, 17, NAVY, anchor="right")
    hairline(s, M, W - M, 118, RULE)
    return s


def navy_block(s, y0):
    s.rect(0, y0, W, H, NAVY)


def arrow(s, x, y, color=WHITE_T, w=3.4, size=12):
    s.d.line([k(x - size - 6), k(y), k(x + size - 2), k(y)], fill=color, width=k(w))
    s.d.line([k(x), k(y - size + 2), k(x + size - 2), k(y), k(x), k(y + size - 2)], fill=color, width=k(w), joint="curve")


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page("A field guide · 9 lessons")
outline_text(s, W + 40, 1130, "9", f(BOLD, 980), stroke=3, color=RULE, anchor="rs")
for i, (t, c) in enumerate([("Tech advice", NAVY), ("I learnt the", NAVY), ("hard way.", ORANGE)]):
    s.text(M - 6, 300 + i * 124, t, f(BOLD, 122), c)
s.text(M, 654, "Mambo niliyojifunza kwa njia ngumu", f(SIG, 62), ORANGE)
swash(s, M + 10, M + 560, 684, ORANGE, 6)
s.para(M, 760, "Nine lessons from my journey, from a village classroom in Kagera to writing software in Mbeya.", f(REG, 27), 480, 40, GREY)
navy_block(s, 1170)
art = print_art("rocket", k(640))
paste_print(s, art, 400, 1170 - art.height / K + 70)      # laptop sits on, and breaks into, the navy block
s.text(M, 1262, "Swipe for all 9", f(SEMI, 30), WHITE_T)
arrow(s, M + s.width("Swipe for all 9", f(SEMI, 30)) + 34, 1251)
smallcaps(s, W - M, 1262, "Kwa wote kwenye tech", 16, SOFT, anchor="right")
sticker(s, 930, 196, "Hifadhi · Save", angle=7, size=21)
finish(s)
s.save(1)

# ── 2–10 · lessons ───────────────────────────────────────────────────────────────────────────────
for i, (art_key, t1, t2, sw, body, todo) in enumerate(LESSONS):
    n = i + 2
    s = page(f"Lesson {i + 1:02d} / 09")
    outline_text(s, W - M + 20, 590, f"{i + 1:02d}", f(BOLD, 380), stroke=3, color=RULE, anchor="rs")
    art = print_art(art_key, k(680))
    paste_print(s, art, 44, 138)

    size = min(fit(s, t1, BOLD, 88, W - 2 * M), fit(s, t2, BOLD, 88, W - 2 * M))
    s.text(M - 4, 730, t1, f(BOLD, size), NAVY)
    s.text(M - 4, 730 + size * 1.02, t2, f(BOLD, size), ORANGE)
    sy = 730 + size * 1.02 + 70
    sws = fit(s, sw, SIG, 56, W - 2 * M - 40)
    s.text(M, sy, sw, f(SIG, sws), ORANGE)
    swash(s, M + 6, M + min(s.width(sw, f(SIG, sws)) * 0.9, 620), sy + 24, ORANGE, 5, seed=i)
    s.para(M, sy + 60, body, f(REG, 25), 720, 36, GREY)

    top = 1052
    navy_block(s, top)
    sticker(s, W - M - 60, top, "Methali" if sw.startswith(("Haba", "Mtu ni", "Usiweke", "Afya")) else "Kiswahili", angle=-6, size=20)
    smallcaps(s, M, top + 56, "Fanya hivi · Do this", 16, ORANGE)
    for j, t in enumerate(todo):
        y = top + 104 + j * 68
        s.text(M, y, f"{j + 1:02d}", f(BOLD, 22), ORANGE)
        s.text(M + 56, y, t, f(MED, 27), WHITE_T)
        if j < len(todo) - 1:
            hairline(s, M, W - M, y + 26, (38, 60, 100))
    arrow(s, W - M - 4, top + 50, SOFT, 3, 11)
    finish(s)
    s.save(n)

# ── 11 · closing ─────────────────────────────────────────────────────────────────────────────────
s = page("The end · Mwisho")
s.text(M - 6, 300, "Keep learning,", f(BOLD, 104), NAVY)
s.text(M - 6, 410, "keep building.", f(BOLD, 104), ORANGE)
s.text(M, 500, "Hifadhi, shiriki, tuendelee kujifunza pamoja", f(SIG, 50), ORANGE)
swash(s, M + 6, M + 600, 526, ORANGE, 5, seed=11)
rows = [("Save", "Hifadhi kwa baadaye", "Come back to it when you need it."),
        ("Share", "Mtumie rafiki yako", "Send it to someone starting out."),
        ("Comment", "Niambie somo lako", "Which lesson hit home for you?")]
y = 610
for j, (a, b, c) in enumerate(rows):
    s.text(M, y + 52, f"{j + 1:02d}", f(BOLD, 24), ORANGE)
    s.text(M + 60, y + 52, a, f(BOLD, 40), NAVY)
    s.text(M + 60 + s.width(a, f(BOLD, 40)) + 18, y + 52, b, f(SIG, 40), ORANGE)
    s.text(M + 60, y + 92, c, f(REG, 24), GREY)
    hairline(s, M, W - M, y + 122, RULE)
    y += 128
navy_block(s, 1030)
smallcaps(s, M, 1094, "Read the full post · Soma zaidi", 17, SOFT)
s.text(M, 1160, POST_URL, f(BOLD, fit(s, POST_URL, BOLD, 40, W - 2 * M)), WHITE_T)
hairline(s, M, W - M, 1196, (38, 60, 100))
s.text(M, 1262, "Questions? Ask my AI assistant", f(REG, 24), SOFT)
s.text(M + s.width("Questions? Ask my AI assistant", f(REG, 24)) + 18, 1266, "viora", f(SIG, 52), ORANGE)
smallcaps(s, W - M, 1262, "@_depriver", 18, WHITE_T, anchor="right")
finish(s)
s.save(TOTAL)
print("ok")
