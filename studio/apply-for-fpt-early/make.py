"""Carousel: apply for field practical training (FPT) early (8 slides, 1080x1350, exported at 2x). Timed for March. The
device is an application checklist on paper plus a March-to-June timeline. Pairs with make-your-fpt-count."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/apply-for-fpt-early"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs

DOCS = ["CV (1 page, PDF)", "Cover letter / email", "University introduction letter", "Latest results (transcript)", "GitHub or portfolio link", "Copy of student ID"]


def checklist(s, box, items, done=()):
    x0, y0, x1, y1 = box
    paper_doc(s, box, title="FPT application · Ombi")
    y = y0 + 150
    gap = (y1 - y0 - 190) / max(1, len(items) - 1)
    for i, it in enumerate(items):
        s.d.rounded_rectangle([k(x0 + 36), k(y - 28), k(x0 + 66), k(y + 2)], radius=k(6), fill=(255, 255, 255), outline=NAVY, width=k(3))
        if i in done:
            s.d.line([k(x0 + 40), k(y - 14), k(x0 + 50), k(y - 4), k(x0 + 70), k(y - 34)], fill=GREEN_OK, width=k(5), joint="curve")
        s.text(x0 + 86, y, it, f(SEMI, fit(s, it, SEMI, 26, x1 - x0 - 120)), NAVY)
        y += gap


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "FPT season · Msimu wa FPT")
s.text(M - 6, 250, "Apply for FPT", f(BOLD, 96), NAVY)
s.text(M - 6, 350, "in March.", f(BOLD, 96), ORANGE)
s.text(M - 6, 430, "Not in June.", f(BOLD, 60), NAVY)
s.text(M, 515, "Omba mapema", f(SIG, 60), NAVY)
swash(s, M + 8, M + 330, 541, ORANGE, 6)
s.para(M, 620, "The best places fill early. Here's the documents list, where to apply and a month-by-month plan.", f(REG, 27), 430, 40, GREY)
checklist(s, (540, 560, W - M, 1010), [d.split(" (")[0] for d in DOCS[:5]], done=(0, 2, 4))
horizon(s, 1)
cover_footer(s, "Swipe, start this week")
finish(s)
s.save(1)

# ── 2 · why early ────────────────────────────────────────────────────────────────────────────────
s = page(2, "Why early · Kwa nini mapema", "Omba FPT")
title2(s, "Early students", "get the good places.", y=220, size=82)
tick_fill(s, [("Popular companies fill up", "Banks, telcos and software houses take limited students."), ("Some have deadlines", "Miss it and you wait a whole year."),
              ("Supervisors plan ahead", "They choose people who asked early and clearly."), ("Time to try again", "A “no” in March still leaves time for plan B.")],
          420, 990, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Remember", "A great FPT can become your first job.", "FPT ni mlango wa kazi", seed=2)
finish(s)
s.save(2)

# ── 3 · documents ────────────────────────────────────────────────────────────────────────────────
s = page(3, "Documents · Nyaraka", "Omba FPT")
title2(s, "Prepare your", "documents now.", y=220, size=86)
checklist(s, (M, 400, W - M - 8, 1000), DOCS)
horizon(s, 3)
navy_note(s, "Tip", "Scan everything into one folder on your phone and email.", "Folder moja", seed=3)
finish(s)
s.save(3)

# ── 4 · where ────────────────────────────────────────────────────────────────────────────────────
s = page(4, "Where · Wapi", "Omba FPT")
title2(s, "Where tech", "students go.", y=220, size=88)
places = [("Banks & fintech", "IT, systems, security"), ("Telecoms", "Networks, apps, data"), ("Software houses", "Real projects, fast learning"),
          ("Government agencies", "Systems, networks, support"), ("Hospitals & NGOs", "IT support, data systems"), ("Startups", "Do a bit of everything")]
cw = (W - 2 * M - 24) / 2
for i, (a, b) in enumerate(places):
    xx, yy = M + (i % 2) * (cw + 24), 410 + (i // 2) * 190
    card(s, (xx, yy, xx + cw - 8, yy + 160), r=16)
    s.text(xx + 28, yy + 62, f"{i + 1:02d}", f(BOLD, 24), ORANGE)
    s.text(xx + 80, yy + 62, a, f(BOLD, fit(s, a, BOLD, 28, cw - 110)), NAVY)
    s.para(xx + 28, yy + 112, b, f(REG, 23), cw - 60, 31, GREY)
horizon(s, 4)
navy_note(s, "Ask too", "Your department's placement office and last year's students.", "Uliza waliotangulia", seed=4)
finish(s)
s.save(4)

# ── 5 · how to approach ──────────────────────────────────────────────────────────────────────────
s = page(5, "How · Jinsi ya kuomba", "Omba FPT")
title2(s, "Email, visit,", "follow up.", y=220, size=88)
flow(s, [("Email a clear application", "Subject, who you are, dates, CV attached"), ("Visit with printed documents", "Ask for HR or the IT manager, politely"),
         ("Follow up after a week", "Short, friendly, once"), ("Get the acceptance in writing", "Your university will need the letter")],
     420, h=100, gap=36, size=29)
horizon(s, 5)
navy_note(s, "Templates", "Our “emails that get replies” post has a ready FPT email.", "Tumia template", seed=5)
finish(s)
s.save(5)

# ── 6 · timeline ─────────────────────────────────────────────────────────────────────────────────
s = page(6, "Timeline · Ratiba", "Omba FPT")
title2(s, "Month by", "month.", y=220, size=92)
table(s, M, 410, ["Month", "Do this"], [["March", "List 10 places, prepare documents"], ["April", "Send all applications"],
                                        ["May", "Follow up, visit, plan B"], ["June", "Confirm, get the letter"], ["FPT", "Learn, build, keep a logbook"]],
      [240, W - 2 * M - 8 - 240], size=27, rh=86)
horizon(s, 6)
navy_note(s, "Check", "Your own university's dates may differ. Ask your coordinator.", "Thibitisha tarehe", seed=6)
finish(s)
s.save(6)

# ── 7 · plan B ───────────────────────────────────────────────────────────────────────────────────
s = page(7, "No reply? · Hakuna jibu?", "Omba FPT")
title2(s, "No reply?", "Plan B.", y=220, size=92)
tick_fill(s, [("Ask lecturers and alumni", "Many placements come through people, not emails."), ("Try smaller companies", "Less competition, more real work."),
              ("Offer a clear skill", "“I can help with your website or IT support.”"), ("Build something anyway", "A real project for a local business counts as experience.")],
          420, 990, size=31, sub=26)
horizon(s, 7)
navy_note(s, "Truth", "Ten applications with no answer is normal. Keep going.", "Usikate tamaa", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Where do you want", "to do FPT?", [("Comment", "your dream place"), ("Tag", "your classmates applying"),
                                              ("Read", "“Make your FPT count” on the blog")])
stamp(s, 840, 860, "IMEKUBALIWA", GREEN_OK, angle=-10, size=38)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
