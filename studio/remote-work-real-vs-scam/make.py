"""Carousel: remote jobs, real or scam? (8 slides, 1080x1350, exported at 2x). Usalama. The device is a fake job advert
covered in red-pen rings and UTAPELI stamps, then what a real remote job process looks like."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/remote-work-real-vs-scam"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs

AD = [("REMOTE JOB!! Work from home", 34), ("Earn $50/hour. No experience needed.", 27), ("Only 10 places left, apply TODAY", 25),
      ("Registration fee: TZS 30,000", 27), ("Contact HR on WhatsApp: +XX XXX", 25)]


def job_ad(s, box, rings=True):
    x0, y0, x1, y1 = box
    paper_doc(s, box)
    y = y0 + 90
    pos = []
    for t_, sz in AD:
        fs = fit(s, t_, BOLD if sz > 30 else SEMI, sz, x1 - x0 - 70)
        s.text(x0 + 36, y, t_, f(BOLD if sz > 30 else SEMI, fs), NAVY if sz > 30 else (40, 50, 70))
        pos.append((y, s.width(t_, f(BOLD if sz > 30 else SEMI, fs))))
        y += sz * 2.1
    if rings:
        for i in (1, 3, 4):
            yy, ww = pos[i]
            red_ring(s, x0 + 22, yy - 40, x0 + 50 + ww, yy + 14, w=3)
    return pos


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Stay safe · Usalama")
s.text(M - 6, 250, "$50 an hour,", f(BOLD, 96), NAVY)
s.text(M - 6, 350, "from home?", f(BOLD, 96), NAVY)
s.text(M - 6, 450, "Read this first.", f(BOLD, 72), ORANGE)
s.text(M, 535, "Kazi halisi au utapeli?", f(SIG, 56), NAVY)
swash(s, M + 8, M + 470, 561, ORANGE, 6)
job_ad(s, (M, 620, W - M - 8, 1000))
stamp(s, 860, 700, "UTAPELI", RED_NO, angle=-12, size=50)
horizon(s, 1)
cover_footer(s, "Swipe, spot the signs")
finish(s)
s.save(1)

# ── 2 · red flags ────────────────────────────────────────────────────────────────────────────────
s = page(2, "Red flags · Dalili za utapeli", "Usalama")
title2(s, "Six red flags", "in one advert.", y=220, size=86)
tick_fill(s, [("They ask YOU to pay", "Registration, training, equipment. Real employers pay you."), ("Huge pay, no skills needed", "If it sounds too good, it is."),
              ("Only WhatsApp or Telegram", "No company website, no real email."), ("Rush: “apply TODAY”", "Pressure stops you thinking."),
              ("No interview", "Hired after one chat message."), ("They want your ID and bank details first", "Before any contract.")],
          410, 1010, size=29, sub=24, ok=False)
horizon(s, 2)
navy_note(s, "Rule", "Any job that asks you to pay first is a scam. Every time.", "Kazi haiombi pesa", seed=2)
finish(s)
s.save(2)

# ── 3 · common scams ─────────────────────────────────────────────────────────────────────────────
s = page(3, "Common scams · Utapeli wa kawaida", "Usalama")
title2(s, "Scams that target", "students.", y=220, size=86)
for i, (a, b) in enumerate([("Registration fee", "Pay to “secure” the job, then they vanish."),
                             ("Task scams", "Like videos or rate apps, small payouts, then “pay to unlock” bigger tasks."),
                             ("Fake equipment", "“Buy your laptop from our supplier, we refund you.” They don't."),
                             ("Data harvesting", "A fake form to collect your ID, NIDA and bank details.")]):
    y = 420 + i * 150
    card(s, (M, y, W - M - 8, y + 128), r=16)
    s.rect(M + 2, y + 2, M + 12, y + 126, RED_NO)
    s.text(M + 40, y + 50, a, f(BOLD, 29), NAVY)
    s.para(M + 40, y + 92, b, f(REG, 23), W - 2 * M - 80, 30, GREY)
horizon(s, 3)
navy_note(s, "Task scams", "Early payouts are bait. The big “unlock” payment is the trap.", "Chambo kidogo, mtego mkubwa", seed=3)
finish(s)
s.save(3)

# ── 4 · real jobs ────────────────────────────────────────────────────────────────────────────────
s = page(4, "Real jobs · Kazi halisi", "Usalama")
title2(s, "What a real remote", "job looks like.", y=220, size=82)
flow(s, [("A real company", "Website, LinkedIn page, real employees"), ("A clear role", "Skills needed, tasks, pay range"),
         ("Interviews", "Video calls, maybe a small technical test"), ("A written contract", "Pay, schedule, notice period"),
         ("They pay you", "You never pay them")], 410, h=88, gap=28, size=28, colors=[GREEN_OK, NAVY])
horizon(s, 4)
navy_note(s, "Honest", "Real remote jobs need real skills. Build them first.", "Ujuzi kwanza", seed=4)
finish(s)
s.save(4)

# ── 5 · where ────────────────────────────────────────────────────────────────────────────────────
s = page(5, "Where to look · Wapi", "Usalama")
title2(s, "Where real", "remote work is.", y=220, size=86)
tick_fill(s, [("Company careers pages", "Apply directly on the company's own website."), ("LinkedIn jobs", "Check the company page and the recruiter's profile."),
              ("Known remote job boards", "e.g. We Work Remotely, Remote OK. Still check each company."),
              ("Freelance platforms", "e.g. Upwork, Fiverr: payment goes through the platform."), ("Referrals", "People you've worked with. The strongest route.")],
          410, 1010, size=29, sub=24)
horizon(s, 5)
navy_note(s, "Never", "Move a freelance client off the platform before you've been paid.", "Usitoke nje ya platform", seed=5)
finish(s)
s.save(5)

# ── 6 · verify ───────────────────────────────────────────────────────────────────────────────────
s = page(6, "Verify · Thibitisha", "Usalama")
title2(s, "Check before", "you send anything.", y=220, size=84)
numbered(s, [("Google the company + “scam”", "Read what others say."), ("Check the email domain", "@company.com, not @gmail.com for a big firm."),
             ("Find employees on LinkedIn", "Real companies have real people."), ("Ask for a video call", "Scammers avoid showing their face."),
             ("Ask a mentor or senior", "Two minutes of advice can save your money.")], 430, gap=112)
horizon(s, 6)
navy_note(s, "Already paid?", "Stop, keep the evidence, report it. Warn others.", "Ripoti na onya wengine", seed=6)
finish(s)
s.save(6)

# ── 7 · getting paid ─────────────────────────────────────────────────────────────────────────────
s = page(7, "Getting paid · Kulipwa", "Usalama")
title2(s, "Agree on pay", "before you start.", y=220, size=86)
tick_fill(s, [("How, when, how much", "Written in the contract or the platform."), ("Check the method works in Tanzania", "Before you sign, not after a month of work."),
              ("Start small", "First payment arrives? Then commit fully."), ("Keep records", "Invoices, messages, payment references. Taxes too.")],
          420, 990, size=31, sub=26)
horizon(s, 7)
navy_note(s, "Rule", "Work done without agreed payment terms is a gift.", "Makubaliano kwanza", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Seen a fake job", "advert lately?", [("Comment", "the red flag you spotted"), ("Share", "in your class WhatsApp group"),
                                                ("Save", "the six red flags")])
stamp(s, 840, 860, "UTAPELI", RED_NO, angle=-10, size=52)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
