"""Carousel: emails that get replies, to recruiters, lecturers and clients (8 slides, 1080x1350, exported at 2x).
Ujuzi wa kazini. The device is an email window; the bad one gets red-pen marks, the good ones get green ticks."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/emails-that-get-replies"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def email(s, y, frm, subj, body, x0=M, x1=None, size=25, lh=36, attach=None):
    """Email window: navy bar, From / Subject rows, body paragraphs. Returns (bottom y, y of subject, y of from)."""
    x1 = x1 or W - M - 8
    lines = sum(wrap_lines(s, b, f(REG, size), x1 - x0 - 72) if b else 1 for b in body)
    h = 64 + 120 + 30 + lines * lh + len(body) * lh * 0.35 + (70 if attach else 0) + 20
    s.rect(x0 + 10, y + 12, x1 + 10, y + h + 12, INK_SHADOW, r=18)
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + h)], radius=k(18), fill=(255, 255, 255), outline=NAVY, width=k(3))
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + 60)], radius=k(18), fill=NAVY)
    s.rect(x0, y + 40, x1, y + 60, NAVY)
    s.text(x0 + 30, y + 40, "New message · Ujumbe mpya", f(SEMI, 20), SOFT)
    fy, sy = y + 104, y + 160
    s.text(x0 + 30, fy, "From", f(SEMI, 20), GREY)
    s.text(x0 + 130, fy, frm, f(MED, fit(s, frm, MED, 23, x1 - x0 - 160)), NAVY)
    s.rect(x0 + 24, fy + 20, x1 - 24, fy + 21.5, RULE)
    s.text(x0 + 30, sy, "Subject", f(SEMI, 20), GREY)
    s.text(x0 + 130, sy, subj, f(BOLD, fit(s, subj, BOLD, 24, x1 - x0 - 160)), NAVY)
    s.rect(x0 + 24, sy + 20, x1 - 24, sy + 21.5, RULE)
    yy = sy + 76
    for b in body:
        if b:
            yy = s.para(x0 + 36, yy, b, f(REG, size), x1 - x0 - 72, lh, NAVY) + lh * 0.35
        else:
            yy += lh * 0.6
    if attach:
        s.d.rounded_rectangle([k(x0 + 36), k(yy - 10), k(x0 + 36 + s.width(attach, f(SEMI, 21)) + 70), k(yy + 40)], radius=k(10),
                              fill=(253, 236, 230), outline=ORANGE, width=k(2))
        s.text(x0 + 56, yy + 22, "PDF  " + attach, f(SEMI, 21), ORANGE)
    return y + h, sy, fy


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Skills uni skips · Ujuzi wa kazini")
s.text(M - 6, 250, "No reply?", f(BOLD, 110), NAVY)
s.text(M - 6, 360, "Fix the email.", f(BOLD, 96), ORANGE)
s.text(M, 450, "Barua pepe inayojibiwa", f(SIG, 58), NAVY)
swash(s, M + 8, M + 500, 476, ORANGE, 6)
y, sy, fy = email(s, 560, "cutieboy99@gmail.com", "hi", ["habari naomba kazi yoyote nina cv"], x1=W - M - 8)
red_ring(s, M + 116, sy - 34, M + 190, sy + 12)
red_ring(s, M + 116, fy - 34, M + 420, fy + 12)
red_note(s, 640, y + 80, "Itapuuzwa!", 56)
horizon(s, 1)
cover_footer(s, "Swipe for templates")
finish(s)
s.save(1)

# ── 2 · what's wrong ─────────────────────────────────────────────────────────────────────────────
s = page(2, "What's wrong · Kosa liko wapi", "Ujuzi wa kazini")
title2(s, "Why this email", "gets ignored.", y=220, size=86)
tick_fill(s, [("Unprofessional address", "cutieboy99 doesn't get interviews. Use your name."),
              ("Empty subject: “hi”", "Recruiters get hundreds. Say what it is."),
              ("No name, no role, no details", "Which job? Who are you? What can you do?"),
              ("“Kazi yoyote”", "Sounds desperate. Ask for a specific role."),
              ("CV mentioned, not attached", "Attach a PDF with a clear name.")], 420, 1000, size=30, sub=25, ok=False)
horizon(s, 2)
navy_note(s, "Truth", "They decide in about 10 seconds. Make it easy.", "Sekunde kumi tu", seed=2)
finish(s)
s.save(2)

# ── 3 · anatomy ──────────────────────────────────────────────────────────────────────────────────
s = page(3, "Anatomy · Muundo", "Ujuzi wa kazini")
title2(s, "Six parts of", "a good email.", y=220, size=86)
flow(s, [("Clear subject", "Internship application: Backend (Asha Juma)"), ("Greeting with a name", "“Dear Ms Mushi,” if you know it"),
         ("Who you are, in one line", "Third-year BSc CS student at MUST"), ("What you want", "One specific request"),
         ("Why you / details", "Two or three facts, a link"), ("Thanks + signature", "Name, phone, LinkedIn or GitHub")],
     410, h=82, gap=22, size=27)
horizon(s, 3)
navy_note(s, "Length", "If it doesn't fit on a phone screen, it's too long.", "Fupi na wazi", seed=3)
finish(s)
s.save(3)

# ── 4 · to a company ─────────────────────────────────────────────────────────────────────────────
s = page(4, "To a company · Kwa kampuni", "Ujuzi wa kazini")
title2(s, "Applying for", "an internship.", y=210, size=80)
email(s, 380, "asha.juma@gmail.com", "Internship application: Backend developer (Asha Juma)",
      ["Dear Ms Mushi,", "I'm a third-year Computer Science student at MUST, applying for your backend internship from June to August.",
       "I've built a shop stock API in Laravel (link below) and I'm comfortable with SQL and Git.",
       "My CV is attached. Thank you for your time.", "Asha Juma · 07XX XXX XXX · github.com/ashajuma"],
      size=25, lh=35, attach="Asha_Juma_CV.pdf")
horizon(s, 4)
navy_note(s, "Attach", "Name the file Firstname_Lastname_CV.pdf, never cv_final2.pdf.", "Jina la faili lieleweke", seed=4)
finish(s)
s.save(4)

# ── 5 · to a lecturer ────────────────────────────────────────────────────────────────────────────
s = page(5, "To a lecturer · Kwa mhadhiri", "Ujuzi wa kazini")
title2(s, "Asking a lecturer", "a question.", y=210, size=80)
email(s, 380, "asha.juma@students.must.ac.tz", "CS 2201: question about Assignment 2, part B",
      ["Dear Dr Mwakyusa,", "I'm Asha Juma, CS 2201, Group B.", "In Assignment 2 part B, should the API return all orders, or only today's orders? I've read the brief and the slides from week 5.",
       "Thank you.", "Asha Juma, Reg. No. 2024-04-1234"], size=25, lh=35)
horizon(s, 5)
navy_note(s, "Respect", "Show you tried first. Ask one clear question.", "Uliza kwa adabu", seed=5)
finish(s)
s.save(5)

# ── 6 · to a client ──────────────────────────────────────────────────────────────────────────────
s = page(6, "To a client · Kwa mteja", "Ujuzi wa kazini")
title2(s, "Following up", "with a client.", y=210, size=80)
email(s, 380, "asha@ashadev.co.tz", "Quotation: Duka la Mama Neema website",
      ["Dear Mama Neema,", "Thank you for meeting me on Tuesday. As promised, the quotation is attached: 5 pages, mobile friendly, ready in 3 weeks.",
       "With a 50% deposit I can start on Monday. Happy to answer any questions.", "Asha Juma · 07XX XXX XXX"],
      size=25, lh=35, attach="Quotation_Duka_Neema.pdf")
horizon(s, 6)
navy_note(s, "Always", "End with a clear next step: a date, an action.", "Hatua inayofuata", seed=6)
finish(s)
s.save(6)

# ── 7 · rules ────────────────────────────────────────────────────────────────────────────────────
s = page(7, "Rules · Kanuni", "Ujuzi wa kazini")
title2(s, "Small habits,", "big difference.", y=220, size=86)
tick_fill(s, [("Professional address", "firstname.lastname@gmail.com is free."), ("Read it out loud before sending", "Typos jump out."),
              ("Follow up once", "After 5 to 7 working days, short and polite."), ("Reply within a day", "Even “Nimepokea, nitajibu kesho.”"),
              ("Formal by default", "Match their tone once they reply.")], 420, 1000, size=30, sub=25)
horizon(s, 7)
navy_note(s, "Mobile", "Most people read email on their phone. Short paragraphs win.", "Aya fupi", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Who do you need", "to email this week?", [("Save", "these three templates"), ("Share", "with a friend applying for FPT"),
                                                     ("Comment", "“template” and I'll help with yours")])
stamp(s, 840, 860, "IMEJIBIWA", GREEN_OK, angle=-10, size=44)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
