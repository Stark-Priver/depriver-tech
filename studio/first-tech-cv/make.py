"""Carousel: your first tech CV (8 slides, 1080x1350, exported at 2x). Same editorial / print direction as
best-laptop-for-tech. The device is a lecturer's red pen: a CV page marked up with strikes, circles and handwritten
notes, then the clean version and the rules behind each fix."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/first-tech-cv"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
PEN = (205, 38, 38)


def note(s, x, y, text, size=40, angle=-4):
    """Handwritten red-pen note."""
    fnt = f(SIG, size)
    w, h = s.width(text, fnt) + 20, size * 1.6
    lay = Image.new("RGBA", (k(w), k(h)), (0, 0, 0, 0))
    ImageDraw.Draw(lay).text((k(10), k(h * 0.72)), text, font=fnt, fill=PEN + (255,), anchor="ls")
    lay = lay.rotate(angle, resample=Image.BICUBIC, expand=True)
    s.im.paste(lay, (k(x), k(y)), lay)
    s.d = ImageDraw.Draw(s.im)


def strike(s, x0, x1, y):
    s.d.line([k(x0), k(y + 2), k(x1), k(y - 3)], fill=PEN, width=k(4))


def ring(s, box):
    x0, y0, x1, y1 = box
    s.d.ellipse([k(x0), k(y0), k(x1), k(y1)], outline=PEN, width=k(4))


def cv_page(s, box, rows, gap=38):
    """A CV sheet: name bar, then grey text lines; rows = [(label, line text)]. Returns row baselines."""
    x0, y0, x1, y1 = box
    card(s, box, r=8)
    ys = []
    y = y0 + 60
    for lab, txt in rows:
        if lab:
            smallcaps(s, x0 + 30, y, lab, 13, ORANGE)
            y += 34
        s.text(x0 + 30, y, txt, f(MED, fit(s, txt, MED, 22, x1 - x0 - 60)), NAVY if lab is None else (70, 78, 95))
        ys.append(y)
        y += gap
    return ys


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For students & fresh graduates")
s.text(M - 6, 250, "Your CV is", f(BOLD, 104), NAVY)
s.text(M - 6, 360, "one page.", f(BOLD, 104), NAVY)
s.text(M - 8, 490, "Make it count.", f(BOLD, 104), ORANGE)
s.text(M, 580, "CV ya kwanza, ifanye vizuri", f(SIG, 58), NAVY)
swash(s, M + 8, M + 540, 606, ORANGE, 6)
s.para(M, 690, "A lecturer's red pen on a student CV, and how to fix every mark.", f(REG, 27), 400, 40, GREY)
ys = cv_page(s, (520, 650, W - M - 8, 1010), [(None, "CURRICULUM VITAE"), ("Personal", "DOB · Religion · Marital status"),
                                               ("Objective", "To get a job in a reputable company"), ("Skills", "MS Word, Internet, Hard working")])
strike(s, 548, 900, ys[1] - 8)
ring(s, (540, ys[2] - 40, 1000, ys[2] + 12))
note(s, 640, 920, "Projects ziko wapi?", 40)
horizon(s, 1)
cover_footer(s, "Swipe for the red pen")
finish(s)
s.save(1)

# ── 2 · the red pen ──────────────────────────────────────────────────────────────────────────────
s = page(2, "The red pen · Kalamu nyekundu")
title2(s, "What the", "red pen sees.", y=220, size=84)
rows = [(None, "JOHN P. MWAKALINGA  —  CV"), ("Personal details", "Born 2003 · Christian · Single · Box 123"),
        ("Objective", "To work in a reputable company"),
        ("Skills", "MS Office, Internet, Hard working, Team player"),
        ("Education", "CSEE 2019, ACSEE 2021, Diploma 2024"), ("Projects", "(none)")]
ys = cv_page(s, (M, 370, W - M - 8, 990), rows, gap=58)
strike(s, M + 26, M + 560, ys[1] - 8)
note(s, M + 610, ys[1] - 56, "si lazima", 40)
ring(s, (M + 14, ys[2] - 40, M + 440, ys[2] + 14))
note(s, M + 470, ys[2] - 50, "kila mtu anasema hivi", 36)
strike(s, M + 26, M + 300, ys[3] - 8)
note(s, M + 560, ys[3] - 50, "skills za tech?", 40)
ring(s, (M + 14, ys[5] - 40, M + 140, ys[5] + 14))
note(s, M + 180, ys[5] - 40, "hapa ndipo pa muhimu!", 42)
horizon(s, 2)
navy_note(s, "The fix", "Less about you on paper, more proof of what you can do.", "Onyesha, usiseme tu", seed=2)
finish(s)
s.save(2)

# ── 3 · the order ────────────────────────────────────────────────────────────────────────────────
s = page(3, "The order · Mpangilio")
title2(s, "Seven sections,", "this order.", y=220, size=84)
order = [("Header", "Name, phone, email, location, GitHub, LinkedIn"), ("Summary", "Two lines: who you are and what you build"),
         ("Skills", "Languages, frameworks, tools you've really used"), ("Projects", "Your strongest proof, with links"),
         ("Experience", "FPT, internships, gigs, volunteering"), ("Education", "Most recent first, with GPA if good"),
         ("Referees", "Two or three, with their permission")]
numbered(s, order, 430, gap=86, ts=30, bs=22)
horizon(s, 3)
navy_note(s, "Why projects early?", "As a student, projects are your experience.", "Kazi zako ndizo uzoefu", seed=3)
finish(s)
s.save(3)

# ── 4 · header & summary ─────────────────────────────────────────────────────────────────────────
s = page(4, "Header & summary · Kichwa")
title2(s, "Easy to call,", "easy to remember.", y=220, size=80)
card(s, (M, 400, W - M - 8, 760), r=10)
s.text(M + 34, 470, "Amina Juma", f(BOLD, 48), NAVY)
s.text(M + 34, 512, "Junior Web Developer", f(SEMI, 26), ORANGE)
s.text(M + 34, 560, "Mbeya · 07XX XXX XXX · amina.juma@gmail.com", f(MED, 22), (70, 78, 95))
s.text(M + 34, 594, "github.com/aminajuma · linkedin.com/in/aminajuma", f(MED, 22), (70, 78, 95))
hairline(s, M + 34, W - M - 40, 624, RULE)
s.para(M + 34, 670, "Computer Science diploma graduate who builds web apps for small businesses with Laravel and React. "
       "Shipped a POS used daily by a shop in Mbeya.", f(REG, 23), W - 2 * M - 80, 33, NAVY)
for ok, t_ in [(True, "Professional email: name.surname@, not boy_mtundu99@"), (False, "No photo needed unless they ask for one"),
               (False, "No DOB, religion or marital status")]:
    pass
y = 830
for ok, t_ in [(True, "Professional email: name.surname, not boy_mtundu99"), (True, "Summary: what you build, not what you want")]:
    mark(s, M + 18, y - 10, ok)
    s.text(M + 56, y, t_, f(SEMI, fit(s, t_, SEMI, 27, W - 2 * M - 60)), NAVY)
    y += 64
horizon(s, 4)
navy_note(s, "Example only", "Use your real details. Never copy someone's CV.", "Kuwa wewe", seed=4)
finish(s)
s.save(4)

# ── 5 · projects with impact ─────────────────────────────────────────────────────────────────────
s = page(5, "Projects · Miradi")
title2(s, "Show impact,", "not just tasks.", y=220, size=84)
card(s, (M, 400, W - M - 8, 520), r=12)
mark(s, M + 40, 450, False)
s.text(M + 76, 460, "“Did a website for a shop.”", f(SEMI, 30), (70, 78, 95))
strike(s, M + 76, M + 500, 450)
card(s, (M, 560, W - M - 8, 790), r=12)
mark(s, M + 40, 610, True)
s.para(M + 76, 620, "“Built a sales and stock app for a shop in Mbeya with Laravel and MySQL. "
       "Used daily by 3 staff; stock errors dropped in the first month.”", f(SEMI, 27), W - 2 * M - 120, 38, NAVY)
smallcaps(s, M, 860, "The formula", 15, ORANGE)
s.text(M, 912, "Built [what] for [who] using [tools], so that [result].", f(BOLD, fit(s, "Built [what] for [who] using [tools], so that [result].", BOLD, 30, W - 2 * M)), NAVY)
s.text(M, 960, "Add the link: GitHub or live demo.", f(REG, 25), GREY)
horizon(s, 5)
navy_note(s, "Tip", "Use real numbers only. Never invent results.", "Ukweli tu", seed=5)
finish(s)
s.save(5)

# ── 6 · FPT counts ───────────────────────────────────────────────────────────────────────────────
s = page(6, "Experience · Uzoefu")
title2(s, "Your FPT", "is experience.", y=230, size=90)
card(s, (M, 420, W - M - 8, 780), r=12)
s.text(M + 34, 480, "IT Trainee (Field Practical Training)", f(BOLD, 28), NAVY)
s.text(M + 34, 516, "Company name, Mbeya · Jun – Aug 2026", f(REG, 22), GREY)
y = 576
for b in ["Set up and maintained 20+ office computers and printers", "Configured the office Wi-Fi and fixed network faults",
          "Built an Excel tracker the team used for equipment"]:
    s.d.ellipse([k(M + 34), k(y - 15), k(M + 46), k(y - 3)], fill=ORANGE)
    s.text(M + 62, y, b, f(MED, fit(s, b, MED, 24, W - 2 * M - 110)), NAVY)
    y += 56
s.text(M, 860, "Start each line with a verb: Built, Configured, Fixed, Led.", f(SEMI, fit(s, "Start each line with a verb: Built, Configured, Fixed, Led.", SEMI, 28, W - 2 * M)), NAVY)
s.text(M, 912, "Gigs and volunteering count too.", f(REG, 25), GREY)
horizon(s, 6)
navy_note(s, "Example", "Write what YOU did, from your logbook. Keep it true.", "Logbook ni hazina", seed=6)
finish(s)
s.save(6)

# ── 7 · final checks ─────────────────────────────────────────────────────────────────────────────
s = page(7, "Final checks · Kabla ya kutuma")
title2(s, "Before you", "hit send.", y=230, size=92)
checks = [("One page", "Two only with real work experience."), ("Save as PDF", "Word files break on other computers."),
          ("Name the file", "Amina-Juma-CV.pdf, not CV final(2).pdf"), ("No typos", "Read it out loud, then ask a friend."),
          ("Referees agreed", "Ask your FPT supervisor or lecturer first."), ("Tailor it", "Match the skills to each job advert.")]
y = 430
for a, b in checks:
    s.d.rounded_rectangle([k(M), k(y - 30), k(M + 34), k(y + 4)], radius=k(7), outline=NAVY, width=k(3))
    s.d.line([k(M + 7), k(y - 13), k(M + 15), k(y - 5), k(M + 28), k(y - 22)], fill=GREEN_OK, width=k(4), joint="curve")
    s.text(M + 56, y, a, f(BOLD, 30), NAVY)
    s.text(M + 56, y + 38, b, f(REG, 23), GREY)
    y += 98
horizon(s, 7)
navy_note(s, "Remember", "A CV gets the interview. You get the job.", "Hatua ya kwanza", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What's the hardest", "part of your CV?", [("Save", "for application season"), ("Share", "with a classmate job hunting"),
                                                    ("Comment", "the section you struggle with")])
note(s, 640, 720, "Safi sana!", 70, angle=-8)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
