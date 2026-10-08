"""Carousel: freelance like a pro, best practices from niche to getting paid (12 slides, 1080x1350, exported at 2x).
One client job walked through seven stages, each stage slide carrying a progress track under the header; devices are an
amateur-vs-pro ledger, package cards, a signed agreement, chat bubbles for updates and scope creep, and a stamped invoice."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 14
POST_URL = "depriver.tech/blog/freelance-like-a-pro"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # paper docs, stamps, tracks, tick lists

ART.update({
    "briefcase": svg(GROUND + f'''
      <rect x="120" y="150" width="300" height="220" rx="22" fill="#0b1e3f" {ST}/>
      <path d="M215 150 v-34 a14 14 0 0 1 14 -14 h82 a14 14 0 0 1 14 14 v34" fill="none" {ST} stroke-width="10"/>
      <path d="M120 236 h300" stroke="#a9c4f5" stroke-width="8"/>
      <rect x="250" y="220" width="40" height="34" rx="6" fill="#e8603a" {ST} stroke-width="4"/>
      <g transform="translate(360 70) rotate(9)"><path d="M0 0 h150 l30 30 v210 h-180z" fill="#fff" {ST}/>
        <text x="20" y="48" font-family="Poppins" font-weight="700" font-size="24" fill="#0b1e3f">INVOICE</text>
        <path d="M20 80 h120 M20 112 h90 M20 144 h130 M20 176 h70" stroke="#c9d4ea" stroke-width="9" stroke-linecap="round"/>
        <g transform="translate(92 196) rotate(-14)"><rect x="-62" y="-26" width="124" height="52" rx="8" fill="none" stroke="#22a05a" stroke-width="6"/>
        <text x="0" y="12" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="30" fill="#22a05a">PAID</text></g></g>'''),
})

STAGES = ["Niche", "Clients", "Brief", "Agreement", "Updates", "Scope", "Payment"]


def stage_page(n, i, label_right="Freelance like a pro"):
    """Stage slide: header + progress track (stage i of 7) with the stage names under the dots."""
    s = page(n, f"Stage {i:02d} / 07 · {STAGES[i - 1]}", label_right)
    track(s, i, len(STAGES), y=168)
    x0, x1 = M + 20, W - M - 20
    gap = (x1 - x0) / (len(STAGES) - 1)
    for j, lab in enumerate(STAGES):
        s.text(x0 + j * gap, 214, lab, f(SEMI if j == i - 1 else MED, 15), ORANGE if j == i - 1 else GREY, anchor="ms")
    return s


def stage_title(s, a, b, size=80):
    title2(s, a, b, y=310, size=size)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Beginners · Kazi huru")
s.text(M - 6, 250, "Freelance", f(BOLD, 116), NAVY)
s.text(M - 6, 370, "like a", f(BOLD, 116), NAVY)
s.text(M - 8, 500, "pro.", f(BOLD, 150), ORANGE)
s.text(M, 590, "Kazi safi, malipo safi", f(SIG, 58), NAVY)
swash(s, M + 8, M + 470, 616, ORANGE, 6)
s.para(M, 700, "From zero to your first paid client, then every job done like a professional.", f(REG, 27), 420, 40, GREY)
paste_print(s, print_art("briefcase", k(540)), 470, 600)
sticker(s, W - M - 150, 560, "From zero", angle=-6, size=22, bg=NAVY)
horizon(s, 1)
cover_footer(s, "Swipe, run it like a business")
finish(s)
s.save(1)

# ── 2 · starting from zero ───────────────────────────────────────────────────────────────────────
s = page(2, "Starting from zero · Unaanza sifuri")
title2(s, "No clients?", "No problem.", y=220, size=90)
y = tick_list(s, [("One skill people pay for", "You don't need ten. One you can do well enough."),
                  ("Good enough beats perfect", "If you can build it with a tutorial's help, you can be paid for it."),
                  ("A laptop, data and a phone", "WhatsApp Business is free and looks professional."),
                  ("No experience? Make some.", "Practice projects count as experience. Next slide.")], 410, size=29, sub=22, gap=20)
smallcaps(s, M, y + 26, "Beginner-friendly services", 15, ORANGE)
chip_row(s, ["Simple websites", "Posters & logos", "Laptop fixes", "Excel & data entry", "Social media pages", "Computer lessons"], M, y + 48, size=21)
horizon(s, 2)
navy_note(s, "Truth", "Nobody starts with clients. Everyone starts with practice.", "Kila mtaalamu alianza", seed=2)
finish(s)
s.save(2)

# ── 3 · first 30 days ────────────────────────────────────────────────────────────────────────────
s = page(3, "Your first month · Mwezi wa kwanza")
title2(s, "Your first", "30 days.", y=220, size=92)
flow(s, [("Week 1 · Pick your offer", "One skill, one type of client, one sentence."),
         ("Week 2 · Build 3 samples", "A site for a family shop, a poster for a local event."),
         ("Week 3 · Show up", "Portfolio page, WhatsApp Business, tell 20 people."),
         ("Week 4 · First paid job", "Small, at a beginner price, with a deposit.")], 410, h=104, gap=34, size=30)
horizon(s, 3)
navy_note(s, "Beginner price", "Lower than the pros is fine. Free is not.", "Usijiuze bure", seed=3)
finish(s)
s.save(3)

# ── 4 · amateur vs pro ───────────────────────────────────────────────────────────────────────────
s = page(4, "The difference · Tofauti")
title2(s, "Same skills.", "Different results.", y=220, size=86)
mid = W / 2 + 10
smallcaps(s, M, 420, "Amateur", 16, RED_NO)
smallcaps(s, mid, 420, "Professional", 16, GREEN_OK)
hairline(s, M, W - M, 440, NAVY, 3)
rows = [("“Toa chochote”", "A written quote"), ("Starts, no deposit", "50% deposit first"), ("Silent for 2 weeks", "A weekly update"),
        ("WhatsApp promises", "A signed agreement"), ("“Almost done” forever", "Dated milestones"), ("Vanishes after delivery", "Handover + follow-up")]
y = 500
for a, b in rows:
    mark(s, M + 16, y - 10, False, r=15)
    s.text(M + 48, y, a, f(MED, fit(s, a, MED, 27, mid - M - 70)), GREY)
    mark(s, mid + 16, y - 10, True, r=15)
    s.text(mid + 48, y, b, f(BOLD, fit(s, b, BOLD, 27, W - M - mid - 50)), NAVY)
    hairline(s, M, W - M, y + 30, RULE)
    y += 82
horizon(s, 4)
navy_note(s, "The truth", "Clients pay for trust, not just for code.", "Uaminifu ni mtaji", seed=4)
finish(s)
s.save(4)

# ── 5 · niche + packages ─────────────────────────────────────────────────────────────────────────
s = stage_page(5, 1)
stage_title(s, "Pick a lane.", "Package it.")
label_box(s, (M, 470, mid - 20, 610), "Too wide", "“I do websites, logos, apps, anything.”", col=RED_NO, size=24)
label_box(s, (mid, 470, W - M - 8, 610), "Clear", "“I build booking sites for hotels and lodges.”", col=GREEN_OK, size=24)
pw = (W - 2 * M - 8 - 40) / 3
packs = [("Basic", ["1-page site", "Contact form", "1 revision"]), ("Standard", ["5 pages", "Booking form", "2 revisions"]),
         ("Premium", ["Payments + admin", "Training", "3 months support"])]
for j, (name, items) in enumerate(packs):
    x0 = M + j * (pw + 20)
    hot = j == 1
    card(s, (x0, 650, x0 + pw, 975), r=16, fill=NAVY if hot else (255, 255, 255))
    s.text(x0 + 26, 712, name, f(BOLD, 34), WHITE_T if hot else NAVY)
    if hot:
        sticker(s, x0 + pw - 70, 650, "Popular", angle=6, size=15)
    hairline(s, x0 + 26, x0 + pw - 26, 742, (60, 84, 128) if hot else RULE)
    for q, it in enumerate(items):
        s.text(x0 + 26, 800 + q * 56, "· " + it, f(MED, fit(s, "· " + it, MED, 24, pw - 40)), SOFT if hot else GREY)
horizon(s, 5)
navy_note(s, "Why", "Specialists get trusted faster, and packages make choosing easy.", "Chagua njia moja", seed=5)
finish(s)
s.save(5)

# ── 6 · profile + where clients are ──────────────────────────────────────────────────────────────
s = stage_page(6, 2)
stage_title(s, "Look hireable.", "Then go find them.")
y = tick_list(s, [("A one-line offer", "Who you help, and how."), ("3 real projects", "With the result: more bookings, faster sales."),
                  ("Proof", "Client messages and reviews, shared with permission."), ("Easy contact", "WhatsApp Business, email, one link.")],
              470, size=28, sub=22, gap=18)
smallcaps(s, M, y + 30, "Where clients are", 15, ORANGE)
chip_row(s, ["Friends & family", "Shops near you", "Past classmates", "LinkedIn", "WhatsApp status", "Upwork", "Fiverr"], M, y + 52, size=21)
horizon(s, 6)
navy_note(s, "Start", "Local first: the businesses you pass every day need you.", "Anza na waliokuzunguka", seed=6)
finish(s)
s.save(6)

# ── 7 · the brief ────────────────────────────────────────────────────────────────────────────────
s = stage_page(7, 3)
stage_title(s, "Ask before", "you quote.", size=84)
numbered(s, [("What problem should this solve?", "More customers? Less paperwork?"), ("Who will use it?", "Customers, staff, or both."),
             ("What does “done” look like?", "Write it down together."), ("When do you need it?", "And why that date."),
             ("What budget do you have in mind?", "Ask it plainly. It saves both of you time."),
             ("Who makes the final decision?", "Talk to that person.")], 480, gap=86, ts=28, bs=21)
horizon(s, 7)
navy_note(s, "Rule", "Never quote on the first WhatsApp message.", "Uliza kwanza, bei baadaye", seed=7)
finish(s)
s.save(7)

# ── 8 · the agreement ────────────────────────────────────────────────────────────────────────────
s = stage_page(8, 4)
stage_title(s, "Put it on", "paper.", size=84)
ty = paper_doc(s, (M, 460, W - M - 8, 990), "Project agreement · Lodge booking site")
terms = [("Scope", "5 pages, booking form, mobile-friendly"), ("Not included", "Logo, photos, online payments"),
         ("Timeline", "3 weeks, 3 dated milestones"), ("Payment", "50% deposit · 25% · 25% at handover"),
         ("Revisions", "2 rounds; extra changes are quoted"), ("Ownership", "Transfers after full payment")]
y = ty + 50
for a, b in terms:
    smallcaps(s, M + 36, y, a, 14, ORANGE)
    s.text(M + 250, y + 2, b, f(SEMI, fit(s, b, SEMI, 25, W - 2 * M - 300)), NAVY)
    hairline(s, M + 36, W - M - 44, y + 24, RULE)
    y += 66
stamp(s, W - M - 160, 940, "SIGNED", col=GREEN_OK, angle=-10, size=44)
horizon(s, 8)
navy_note(s, "Even for friends", "Especially for friends. A page now saves the friendship later.", "Maandishi hayadanganyi", seed=8)
finish(s)
s.save(8)

# ── 9 · updates ──────────────────────────────────────────────────────────────────────────────────
s = stage_page(9, 5)
stage_title(s, "Never go", "silent.", size=84)
y = chat(s, M + 80, 460, W - 2 * M - 88, "Done: home and rooms pages (link below). Next: the booking form. "
         "Need from you: room photos by Tuesday.", "You · Friday update", mine=True, size=25, lh=36)
y = tick_list(s, [("Reply within 24 hours", None), ("Show progress with a live link", None), ("Bad news early, before the deadline", None)],
              y + 80, size=28)
label_box(s, (M, 840, W - M - 8, 985), "Free tools that help", "Google Drive for files · Trello for tasks · GitHub for code · WhatsApp Business labels for clients", size=24)
horizon(s, 9)
navy_note(s, "Truth", "Clients forgive delays. They don't forgive silence.", "Mawasiliano ni sehemu ya kazi", seed=9)
finish(s)
s.save(9)

# ── 10 · scope creep ──────────────────────────────────────────────────────────────────────────────
s = stage_page(10, 6)
stage_title(s, "“Can you just", "add one thing?”", size=80)
y = chat(s, M, 460, 620, "Can you just add an online shop too? It's small.", "Client", mine=False, size=25, lh=36)
y = chat(s, M + 200, y + 34, W - 2 * M - 208, "Sawa, nitaongeza tu.", "Amateur", mine=True, size=25, lh=36, tag="Free work", tag_ok=False)
chat(s, M + 200, y + 40, W - 2 * M - 208, "Happy to! It's outside our agreement, so it's 5 extra days and an extra fee. Shall I send a quote?",
     "Professional", mine=True, size=25, lh=36, tag="Pro move")
horizon(s, 10)
navy_note(s, "Rule", "New idea = new quote. Kindly, every time.", "Kazi mpya, bei mpya", seed=10)
finish(s)
s.save(10)

# ── 11 · delivery + payment ───────────────────────────────────────────────────────────────────────
s = stage_page(11, 7)
stage_title(s, "Deliver it.", "Get paid.", size=84)
ty = paper_doc(s, (M, 450, W - M - 8, 735), "Invoice #014 · Lodge booking site", fold=False)
for j, (a, st, col) in enumerate([("Deposit · 50%", "PAID", GREEN_OK), ("Design approved · 25%", "PAID", GREEN_OK),
                                  ("Final handover · 25%", "DUE", RED_NO)]):
    yy = ty + 40 + j * 50
    s.text(M + 36, yy, a, f(SEMI, 25), NAVY)
    s.text(W - M - 50, yy, st, f(BOLD, 24), col, anchor="rs")
tick_list(s, [("Logins and passwords handed over", None), ("Code on their GitHub or drive", None), ("A short how-to video", None),
              ("Final files after the final payment", None)], 810, size=27)
horizon(s, 11)
navy_note(s, "Invoice", "Number, date, what was done, and your M-Pesa or bank details.", "Lipwa kwa heshima", seed=11)
finish(s)
s.save(11)

# ── 12 · run it like a business ──────────────────────────────────────────────────────────────────
s = page(12, "Beyond one job · Biashara")
title2(s, "Run it like", "a business.", y=220, size=90)
tick_fill(s, [("Separate your money", "A business M-Pesa line or bank account."), ("Record every payment", "Client, amount, date. A spreadsheet is enough."),
              ("Save part of every payment", "For tax, slow months and new tools."), ("Get a TIN as you grow", "Register with TRA so companies can pay you."),
              ("Ask for reviews and referrals", "Happy clients bring the next ones."), ("Offer monthly support", "Updates and hosting = steady income.")],
          410, 990, size=28, sub=22, max_gap=40)
horizon(s, 12)
navy_note(s, "Mindset", "You're not doing favours. You're running a business.", "Wewe ni kampuni", seed=12)
finish(s)
s.save(12)

# ── 13 · red flags ───────────────────────────────────────────────────────────────────────────────
s = page(13, "Red flags · Epuka")
title2(s, "Walk away", "from these.", y=220, size=92)
tick_fill(s, [("Refuses any deposit", "Serious clients pay to start."), ("“Do it for exposure”", "Exposure doesn't pay rent."),
              ("Asks you to pay to get the job", "That's a scam. Always."), ("A free “test” that is the whole project", "Small paid test, or nothing."),
              ("Overpays, then asks for a refund", "The first payment will bounce.")], 410, 990, size=28, sub=22, ok=False, max_gap=48)
horizon(s, 13)
navy_note(s, "Rule", "If it feels wrong, walk away politely.", "Usitapeliwe", seed=13)
finish(s)
s.save(13)

# ── 14 · closing ─────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What's your worst", "client story?", [("Comment", "your story (no names)"), ("Save", "the agreement checklist"),
                                                ("Share", "with a friend starting freelancing")])
paste_print(s, print_art("briefcase", k(400)), 620, 640)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
