"""Carousel: how to price your first freelance job in TZS (8 slides, 1080x1350, exported at 2x). Ujuzi wa kazini. The
device is a quotation paper (Nukuu ya bei). All numbers are clearly labelled examples, never market rates."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/price-your-first-freelance-job"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def quote(s, box, rows, total, note=True):
    """Quotation sheet: header, item rows with amounts, total line."""
    x0, y0, x1, y1 = box
    paper_doc(s, box)
    s.text(x0 + 36, y0 + 70, "NUKUU YA BEI", f(BOLD, 30), NAVY)
    s.text(x0 + 36, y0 + 104, "Quotation · Mfano / example", f(MED, 19), GREY)
    y = y0 + 160
    for a, b in rows:
        s.text(x0 + 36, y, a, f(MED, 22), NAVY)
        s.text(x1 - 36, y, b, f(MONO, 22), NAVY, anchor="rs")
        s.rect(x0 + 36, y + 14, x1 - 36, y + 15.5, RULE)
        y += 48
    s.rect(x0 + 36, y - 10, x1 - 36, y - 6, NAVY)
    s.text(x0 + 36, y + 34, "JUMLA", f(BOLD, 26), NAVY)
    s.text(x1 - 36, y + 34, total, f(MONO_B, 26), ORANGE, anchor="rs")
    return y + 34


ROWS = [("Design (2 pages)", "120,000"), ("Build + mobile layout", "300,000"), ("Domain + hosting", "client"), ("Training, 1 hour", "30,000")]

# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Freelancing · Kazi huru")
s.text(M - 6, 250, "“Bei gani?”", f(BOLD, 110), ORANGE)
s.text(M - 6, 360, "Price your first", f(BOLD, 72), NAVY)
s.text(M - 6, 440, "freelance job.", f(BOLD, 72), NAVY)
s.text(M, 530, "Usijiuze bure", f(SIG, 60), NAVY)
swash(s, M + 8, M + 340, 556, ORANGE, 6)
s.para(M, 640, "A simple method in TZS, what to put in writing, and how to get paid. Numbers here are examples only.", f(REG, 27), 430, 40, GREY)
quote(s, (560, 560, W - M, 1010), ROWS, "450,000")
horizon(s, 1)
cover_footer(s, "Swipe for the method")
finish(s)
s.save(1)

# ── 2 · the mistake ──────────────────────────────────────────────────────────────────────────────
s = page(2, "The mistake · Kosa la kwanza", "Ujuzi wa kazini")
title2(s, "“Toa chochote”", "is not a price.", y=220, size=84)
for i, (who, txt, mine) in enumerate([("Client", "Tovuti ya biashara ni bei gani?", False), ("You", "Aah... toa chochote tu bro", True),
                                      ("Client", "Sawa, elfu hamsini. Na app pia iwe ndani, na logo, na...", False)]):
    chat(s, M if not mine else W - M - 8 - 560, 410 + i * 170, 560, txt, who, mine=mine, size=25, lh=34)
horizon(s, 2)
navy_note(s, "Result", "Weeks of work, no clear scope, and a price that can't pay your data.", "Weka bei, weka mipaka", seed=2)
finish(s)
s.save(2)

# ── 3 · the method ───────────────────────────────────────────────────────────────────────────────
s = page(3, "The method · Njia", "Ujuzi wa kazini")
title2(s, "Hours × rate", "+ costs + buffer.", y=220, size=86)
y = table(s, M, 420, ["Part", "Mfano · Example"], [["Your hours", "30 hours"], ["× your hourly rate", "× TZS 12,000"],
                                                    ["= Your time", "360,000"], ["+ Costs (data, transport)", "30,000"],
                                                    ["+ Buffer 15% (surprises)", "60,000"], ["= Quote", "≈ 450,000"]],
          [520, W - 2 * M - 8 - 520], size=26, rh=72, hl_rows=(5,))
s.text(M, y + 50, "Example numbers only. Your rate depends on skill, client and city.", f(REG, 23), GREY)
horizon(s, 3)
navy_note(s, "Your rate", "Ask seniors what they charge. Start a bit lower, raise it every project.", "Panda taratibu", seed=3)
finish(s)
s.save(3)

# ── 4 · costs ────────────────────────────────────────────────────────────────────────────────────
s = page(4, "Hidden costs · Gharama zilizojificha", "Ujuzi wa kazini")
title2(s, "Costs students", "forget.", y=220, size=88)
tick_fill(s, [("Domain and hosting", "Better: the client pays and owns them directly."), ("Meetings and travel", "Bajaji to the client three times adds up."),
              ("Data bundles", "Uploads, calls, research."), ("Paid themes, plugins, SMS credits", "List them, or ask the client to buy them."),
              ("Support after launch", "Agree on a period, e.g. 2 weeks free fixes.")], 410, 1000, size=31, sub=26)
horizon(s, 4)
navy_note(s, "Rule", "If it costs you money, it's in the quote.", "Kila gharama iandikwe", seed=4)
finish(s)
s.save(4)

# ── 5 · scope ────────────────────────────────────────────────────────────────────────────────────
s = page(5, "Scope · Mipaka ya kazi", "Ujuzi wa kazini")
title2(s, "Write what's", "included.", y=220, size=88)
half = (W - 2 * M - 30) / 2
for j, (head, items, ok) in enumerate([("Included", ["5 pages", "Contact form", "Mobile layout", "2 rounds of changes"], True),
                                        ("Not included", ["Online payments", "A mobile app", "Writing all the text", "Monthly updates"], False)]):
    x0 = M + j * (half + 30)
    card(s, (x0, 410, x0 + half - 8, 900), r=18)
    smallcaps(s, x0 + 30, 466, head, 16, GREEN_OK if ok else RED_NO)
    y = 540
    for it in items:
        mark(s, x0 + 46, y - 10, ok, r=15)
        s.text(x0 + 76, y, it, f(SEMI, fit(s, it, SEMI, 27, half - 110)), NAVY)
        y += 86
horizon(s, 5)
navy_note(s, "Extra request?", "“Sawa, hiyo ni kazi mpya. Nitakutumia nukuu yake.”", "Kazi mpya, bei mpya", seed=5)
finish(s)
s.save(5)

# ── 6 · getting paid ─────────────────────────────────────────────────────────────────────────────
s = page(6, "Getting paid · Kulipwa", "Ujuzi wa kazini")
title2(s, "Deposit first,", "always.", y=220, size=92)
flow(s, [("50% deposit to start", "No deposit, no start. Clients who pay are serious."), ("Show progress", "A link they can click, every week."),
         ("50% before handover", "Before final files, logins or going live."), ("Receipt for every payment", "Mobile money reference plus a simple receipt.")],
     420, h=100, gap=34, size=29)
horizon(s, 6)
navy_note(s, "Bigger jobs", "Split into milestones: design, build, launch. Paid at each.", "Hatua kwa hatua", seed=6)
finish(s)
s.save(6)

# ── 7 · the quote ────────────────────────────────────────────────────────────────────────────────
s = page(7, "Send a real quote · Nukuu", "Ujuzi wa kazini")
title2(s, "Send it on", "paper (or PDF).", y=220, size=86)
quote(s, (M, 400, W - M - 8, 1000), ROWS + [("Deposit 50% to start", "225,000"), ("Valid for", "14 days")], "450,000")
horizon(s, 7)
navy_note(s, "Why", "A written quote looks professional and protects both of you.", "Andika, usiongee tu", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "How did you price", "your first job?", [("Comment", "your story (no shame)"), ("Save", "before your next client"),
                                                   ("Share", "with a friend who works for “chochote”")])
stamp(s, 840, 860, "IMELIPWA", GREEN_OK, angle=-10, size=48)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
