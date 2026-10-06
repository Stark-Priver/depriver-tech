"""Carousel: LinkedIn for students (8 slides, 1080x1350, exported at 2x). Same editorial / print direction as
first-tech-interview. The device is a generic profile mock (no platform branding), shown before and after, then one
section per slide: headline, about, experience, featured, and a weekly routine."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/linkedin-for-students"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing


def avatar(s, cx, cy, r, empty=False):
    s.d.ellipse([k(cx - r - 5), k(cy - r - 5), k(cx + r + 5), k(cy + r + 5)], fill=(255, 255, 255))
    s.d.ellipse([k(cx - r), k(cy - r), k(cx + r), k(cy + r)], fill=(226, 230, 238) if empty else BLUE, outline=NAVY, width=k(3))
    if empty:
        s.text(cx, cy + 2, "?", f(BOLD, r), GREY, anchor="mm")
    else:
        s.d.ellipse([k(cx - r * 0.34), k(cy - r * 0.5), k(cx + r * 0.34), k(cy + r * 0.18)], fill=NAVY)
        s.d.chord([k(cx - r * 0.66), k(cy + r * 0.25), k(cx + r * 0.66), k(cy + r * 1.4)], 180, 360, fill=NAVY)


def profile(s, box, good):
    x0, y0, x1, y1 = box
    card(s, box, r=16)
    if good:
        s.d.rounded_rectangle([k(x0 + 3), k(y0 + 3), k(x1 - 3), k(y0 + 110)], radius=k(14), fill=NAVY)
        s.text(x0 + 30, y0 + 70, "I build web apps for small businesses", f(SEMI, 24), SOFT)
    else:
        s.d.rounded_rectangle([k(x0 + 3), k(y0 + 3), k(x1 - 3), k(y0 + 110)], radius=k(14), fill=(214, 219, 230))
    avatar(s, x0 + 100, y0 + 130, 58, empty=not good)
    nm = "Amina Juma" if good else "amina j."
    s.text(x0 + 34, y0 + 240, nm, f(BOLD, 34), NAVY)
    hl = "Junior Web Developer · Laravel & React · CS graduate, MUST" if good else "Student at university"
    s.text(x0 + 34, y0 + 280, hl, f(MED, fit(s, hl, MED, 23, x1 - x0 - 70)), NAVY if good else GREY)
    s.text(x0 + 34, y0 + 314, "Mbeya, Tanzania · 214 connections" if good else "12 connections", f(REG, 20), GREY)
    mark(s, x1 - 40, y0 + 150, good, r=22)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For students & fresh graduates")
s.text(M - 6, 250, "Recruiters are", f(BOLD, 96), NAVY)
s.text(M - 6, 352, "searching.", f(BOLD, 96), NAVY)
s.text(M - 8, 470, "Can they find you?", f(BOLD, 84), ORANGE)
s.text(M, 560, "LinkedIn kwa wanafunzi", f(SIG, 58), NAVY)
swash(s, M + 8, M + 470, 586, ORANGE, 6)
profile(s, (M + 60, 650, W - M - 8, 990), True)
horizon(s, 1)
cover_footer(s, "Swipe to fix your profile")
finish(s)
s.save(1)

# ── 2 · before / after ───────────────────────────────────────────────────────────────────────────
s = page(2, "Before & after · Kabla na baada")
title2(s, "Same student,", "different chances.", y=200, size=70)
profile(s, (M, 310, W - M - 8, 650), False)
profile(s, (M, 680, W - M - 8, 1020), True)
horizon(s, 2)
navy_note(s, "Start with", "A clear photo of your face and a headline that says what you do.", "Picha na kichwa", seed=2)
finish(s)
s.save(2)

# ── 3 · headline ─────────────────────────────────────────────────────────────────────────────────
s = page(3, "Headline · Kichwa cha habari")
title2(s, "Your headline", "is your hook.", y=230, size=88)
smallcaps(s, M, 420, "The formula", 15, ORANGE)
s.text(M, 480, "Role · main skills · proof", f(BOLD, 44), NAVY)
y = 590
for ok, t_ in [(False, "Student at university"), (False, "Looking for opportunities"),
               (True, "Junior Web Developer · Laravel & React · Built a POS for a Mbeya shop"),
               (True, "IT Support · Networks & hardware · FPT at a regional hospital")]:
    mark(s, M + 18, y - 10, ok)
    s.text(M + 56, y, t_, f(SEMI, fit(s, t_, SEMI, 28, W - 2 * M - 60)), NAVY if ok else GREY)
    y += 80
horizon(s, 3)
navy_note(s, "Tip", "Use the words recruiters search for: the job title you want.", "Andika unachofanya", seed=3)
finish(s)
s.save(3)

# ── 4 · about ────────────────────────────────────────────────────────────────────────────────────
s = page(4, "About · Kuhusu wewe")
title2(s, "Write About", "like a human.", y=230, size=88)
card(s, (M, 400, W - M - 8, 800), r=14)
smallcaps(s, M + 34, 450, "Example", 14, ORANGE)
s.para(M + 34, 500, "I'm a Computer Science graduate from MUST who loves building simple tools for small businesses. "
       "During my field training I set up office networks and built an equipment tracker. "
       "Right now I'm learning Docker and looking for a junior developer role. Let's connect.", f(REG, 26), W - 2 * M - 80, 38, NAVY)
for i, t_ in enumerate(["Who you are", "What you've done", "What you want next"]):
    x = M + i * 310
    s.d.rounded_rectangle([k(x), k(850), k(x + 290), k(900)], radius=k(25), fill=NAVY if i % 2 == 0 else (255, 255, 255), outline=NAVY, width=k(2.5))
    s.text(x + 145, 876, t_, f(SEMI, 22), WHITE_T if i % 2 == 0 else NAVY, anchor="mm")
horizon(s, 4)
navy_note(s, "Keep it short", "Three to five sentences. First person. No buzzwords.", "Kuwa wewe", seed=4)
finish(s)
s.save(4)

# ── 5 · experience & featured ────────────────────────────────────────────────────────────────────
s = page(5, "Experience & featured · Uzoefu")
title2(s, "Fill it with", "proof.", y=230, size=92)
items = [("FPT counts as experience", "Add it like a job: role, company, months, what you did."),
         ("Featured section", "Pin your best project, your GitHub and your CV."),
         ("Skills", "Add 5–10 real skills, then take a skill quiz if offered."),
         ("Recommendations", "Ask your FPT supervisor for a two-line recommendation."),
         ("Certificates", "Cisco, Microsoft Learn, Huawei: add them all.")]
numbered(s, items, 440, gap=112)
horizon(s, 5)
navy_note(s, "Honest only", "Never list skills you can't talk about in an interview.", "Ukweli ni heshima", seed=5)
finish(s)
s.save(5)

# ── 6 · weekly routine ───────────────────────────────────────────────────────────────────────────
s = page(6, "Weekly routine · Kila wiki")
title2(s, "20 minutes", "a week.", y=230, size=96)
days = [("Mon", "Connect with 5 people in your field, with a short note"), ("Wed", "Comment something useful on 3 posts"),
        ("Fri", "Post one thing you learnt or built this week")]
y = 440
for d_, t_ in days:
    s.d.rounded_rectangle([k(M), k(y - 46), k(M + 110), k(y + 18)], radius=k(14), fill=ORANGE)
    s.text(M + 55, y - 14, d_, f(BOLD, 28), WHITE_T, anchor="mm")
    s.para(M + 140, y - 6, t_, f(SEMI, 30), W - 2 * M - 150, 40, NAVY)
    y += 150
s.text(M, 930, "Connect with alumni from your university first.", f(MED, 27), GREY)
horizon(s, 6)
navy_note(s, "Remember", "People hire people they know. Let them know you.", "Julikana", seed=6)
finish(s)
s.save(6)

# ── 7 · don'ts ───────────────────────────────────────────────────────────────────────────────────
s = page(7, "Avoid these · Epuka")
title2(s, "Don't do", "this.", y=230, size=96)
bad = [("No photo, or a group photo", "Just your face, clear and smiling."), ("Copying someone's About", "Recruiters notice. Write yours."),
       ("Begging posts", "“Please hire me” posts rarely work. Show work instead."), ("Fake titles", "“CEO” of a company with no product hurts trust."),
       ("Disappearing for a year", "A small post a week keeps you visible.")]
y = 440
for a, b in bad:
    mark(s, M + 18, y - 10, False)
    s.text(M + 56, y, a, f(BOLD, 31), NAVY)
    s.text(M + 56, y + 40, b, f(REG, 24), GREY)
    y += 116
horizon(s, 7)
navy_note(s, "Rule", "Let your work speak. Your profile just introduces it.", "Kazi iongee", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Drop your profile", "link below.", [("Fix", "your photo and headline today"), ("Share", "with a classmate who has 12 connections"),
                                              ("Comment", "your LinkedIn link, let's connect")])
avatar(s, 860, 800, 90)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
