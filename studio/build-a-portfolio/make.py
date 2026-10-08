"""Carousel: build a portfolio from zero, what to put inside it and how to present each project (12 slides, 1080x1350,
exported at 2x). Complements portfolio-in-a-weekend (the site) and github-that-gets-you-hired (the profile): a project
ladder (stairs), ideas by track, pick three, an annotated case-study page, weak vs strong write-ups, where it lives."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 12
POST_URL = "depriver.tech/blog/build-a-portfolio"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # paper docs, tables, flows, tick lists

ART.update({
    "folio": svg(GROUND + f'''
      <rect x="80" y="60" width="440" height="310" rx="18" fill="#fff" {ST}/>
      <path d="M80 110 h440" {ST}/>
      <circle cx="112" cy="86" r="8" fill="#c43434"/><circle cx="140" cy="86" r="8" fill="#f0b43c"/><circle cx="168" cy="86" r="8" fill="#22a05a"/>
      <rect x="200" y="76" width="280" height="22" rx="11" fill="#e6ecf7"/>
      <rect x="108" y="134" width="120" height="96" rx="10" fill="#e8603a" {ST} stroke-width="4"/>
      <rect x="240" y="134" width="120" height="96" rx="10" fill="#a9c4f5" {ST} stroke-width="4"/>
      <rect x="372" y="134" width="120" height="96" rx="10" fill="#0b1e3f" {ST} stroke-width="4"/>
      <path d="M108 262 h90 M240 262 h70 M372 262 h96 M108 292 h60 M240 292 h96 M372 292 h50" stroke="#c9d4ea" stroke-width="10" stroke-linecap="round"/>
      <rect x="108" y="318" width="110" height="30" rx="15" fill="#0b1e3f"/>
      <text x="163" y="339" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="16" fill="#fff">Live demo</text>
      <path d="M168 168 l10 20 22 3 -16 15 4 22 -20 -11 -20 11 4 -22 -16 -15 22 -3z" fill="#fff" stroke="#0b1e3f" stroke-width="3" stroke-linejoin="round"/>'''),
})


def badge(s, x, y, n, col=ORANGE, r=19):
    s.d.ellipse([k(x - r), k(y - r), k(x + r), k(y + r)], fill=col)
    s.text(x, y, str(n), f(BOLD, 20), WHITE_T, anchor="mm")


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Beginners · Portfolio")
s.text(M - 6, 250, "Build a", f(BOLD, 112), NAVY)
s.text(M - 6, 366, "portfolio that", f(BOLD, 96), NAVY)
s.text(M - 8, 496, "hires you.", f(BOLD, 128), ORANGE)
s.text(M, 586, "Kazi yako ijieleze", f(SIG, 58), NAVY)
swash(s, M + 8, M + 420, 612, ORANGE, 6)
s.para(M, 700, "From zero projects to three that prove what you can do.", f(REG, 27), 420, 40, GREY)
paste_print(s, print_art("folio", k(520)), 500, 640)
sticker(s, W - M - 160, 660, "Even with no experience", angle=-5, size=18, bg=NAVY)
horizon(s, 1)
cover_footer(s, "Swipe, start building proof")
finish(s)
s.save(1)

# ── 2 · cv vs portfolio ──────────────────────────────────────────────────────────────────────────
s = page(2, "The idea · Dhana")
title2(s, "A CV claims.", "A portfolio proves.", y=220, size=84)
mid = W / 2
for j, (lab, col, big, ex, ok) in enumerate([("CV", RED_NO, "“I know React.”", "Anyone can write this line.", False),
                                             ("Portfolio", GREEN_OK, "“Here's a booking app I built in React.”", "Live link. Code. Screenshots.", True)]):
    x0 = M if j == 0 else mid + 14
    x1 = mid - 14 if j == 0 else W - M - 8
    card(s, (x0, 400, x1, 720))
    s.rect(x0 + 2, 402, x1 - 2, 412, col)
    smallcaps(s, x0 + 30, 462, lab, 16, col)
    yy = s.para(x0 + 30, 520, big, f(BOLD, 30), x1 - x0 - 60, 40, NAVY)
    mark(s, x0 + 46, yy + 36, ok)
    s.para(x0 + 80, yy + 46, ex, f(REG, 23), x1 - x0 - 110, 32, GREY)
s.para(M, 800, "Recruiters, clients and FPT supervisors trust what they can click. A portfolio is a small collection of your best work, "
       "each piece explained: what it is, why you built it and how.", f(REG, 27), W - 2 * M, 40, NAVY)
horizon(s, 2)
navy_note(s, "In short", "Don't tell them you can build. Show them.", "Usiseme, onyesha", seed=2)
finish(s)
s.save(2)

# ── 3 · project ladder ───────────────────────────────────────────────────────────────────────────
s = page(3, "No projects yet? · Huna project?")
title2(s, "Climb the", "project ladder.", y=220, size=88)
steps = [("Level 1 · Clone", "Copy a known app's look. Great practice, not your star."),
         ("Level 2 · For you", "A tool you really use: budget, timetable, notes."),
         ("Level 3 · For others", "Solve a real problem for a shop, club or church."),
         ("Level 4 · Real work", "A client, a hackathon or a team project.")]
sw = (W - 2 * M - 8) / 4
for i, (a, b) in enumerate(steps):
    x0, top = M + i * sw, 760 - i * 110
    hot = i == 3
    s.rect(x0 + 8, top + 10, x0 + sw + 8, 1000, (205, 211, 224))
    s.d.rectangle([k(x0), k(top), k(x0 + sw), k(1000)], fill=ORANGE if hot else (NAVY if i == 2 else (255, 255, 255)), outline=NAVY, width=k(3))
    fg, sub = (WHITE_T, WHITE_T if hot else SOFT) if i >= 2 else (NAVY, GREY)
    lab, name = a.split(" · ")
    smallcaps(s, x0 + 18, top + 40, lab, 13, WHITE_T if hot else (ORANGE if i < 3 else WHITE_T))
    s.text(x0 + 18, top + 82, name, f(BOLD, fit(s, name, BOLD, 28, sw - 30)), fg)
    s.para(x0 + 18, top + 118, b, f(REG, 19), sw - 34, 26, sub)
horizon(s, 3)
navy_note(s, "Aim", "Your portfolio's star should come from level 3 or 4.", "Panda ngazi moja moja", seed=3)
finish(s)
s.save(3)

# ── 4 · ideas by track ───────────────────────────────────────────────────────────────────────────
s = page(4, "Project ideas · Mawazo")
title2(s, "Ideas you can", "start this week.", y=220, size=86)
table(s, M, 400, ["Track", "Project idea"],
      [["Web", "Booking site for a local salon or lodge"], ["Mobile", "Group contributions (michango) tracker"],
       ["Data", "Dashboard of crop prices from public data"], ["UI/UX", "Redesign an app screen you use every day"],
       ["IT / Network", "Write-up: set up a small office network"]],
      [250, 678], size=26, rh=82)
s.para(M, 935, "Twist any idea with a local problem and it stops looking like a tutorial.", f(REG, 23), W - 2 * M, 32, GREY)
horizon(s, 4)
navy_note(s, "Best ideas", "Come from problems you see every day.", "Tatizo ni wazo", seed=4)
finish(s)
s.save(4)

# ── 5 · pick three ───────────────────────────────────────────────────────────────────────────────
s = page(5, "Quality · Ubora")
title2(s, "Three great,", "not ten okay.", y=220, size=90)
for j, (lab, txt) in enumerate([("01 · The star", "Your best, most finished project. Live, polished, explained."),
                                ("02 · The problem solver", "Something real people use, even if it's five friends."),
                                ("03 · The range", "Shows another skill: an API, a design, some data work.")]):
    label_box(s, (M, 400 + j * 195, W - M - 8, 570 + j * 195), lab, txt, col=ORANGE if j == 0 else NAVY, size=28)
horizon(s, 5)
navy_note(s, "Rule", "If a project needs an excuse, leave it out.", "Bora kuliko bora tu", seed=5)
finish(s)
s.save(5)

# ── 6 · case study anatomy ───────────────────────────────────────────────────────────────────────
s = page(6, "Each project · Kila project")
title2(s, "Every project is", "a mini story.", y=220, size=84)
ty = paper_doc(s, (M, 380, W - M - 8, 1000))
sticker(s, W - M - 120, 392, "Example", angle=6, size=17)
rows = [("Title + one line", "Saluni Booking: book a hair appointment in 30 seconds."),
        ("Screenshots or a 60-sec demo", "Three screens and a short screen recording."),
        ("The problem", "Customers waited for hours; the owner used a paper diary."),
        ("What I built + tools", "Booking page and SMS reminders · React, Firebase"),
        ("Result + what I learned", "Used every week by the salon · handling double bookings."),
        ("Links", "Live demo  ·  Code on GitHub")]
y = ty - 6
for i, (a, b) in enumerate(rows):
    badge(s, M + 48, y + 2, i + 1)
    smallcaps(s, M + 84, y + 10, a, 14, ORANGE)
    s.text(M + 84, y + 50, b, f(SEMI if i == 5 else MED, fit(s, b, MED, 25, W - 2 * M - 130)), NAVY if i != 5 else (37, 99, 235))
    if i < 5:
        hairline(s, M + 84, W - M - 44, y + 74, RULE)
    y += 90
horizon(s, 6)
navy_note(s, "Why", "A reviewer understands it in 30 seconds, without asking you.", "Eleza kwa ufupi", seed=6)
finish(s)
s.save(6)

# ── 7 · write it well ────────────────────────────────────────────────────────────────────────────
s = page(7, "Writing it · Uandishi")
title2(s, "Same project.", "Better story.", y=220, size=88)
label_box(s, (M, 390, W - M - 8, 500), "Weak", "A to-do app built with React.", col=RED_NO, size=26)
label_box(s, (M, 530, W - M - 8, 730), "Strong", "A deadline tracker for my study group of 14. It reminds everyone a day before each "
          "assignment. Built with React and Firebase.", col=GREEN_OK, size=26)
smallcaps(s, M, 790, "The formula", 15, ORANGE)
for i, (a, b) in enumerate([("Who it's for", "a real person or group"), ("The problem", "what was hard before"),
                            ("How you built it", "tools and your role"), ("A number", "users, time saved, results")]):
    x = M if i % 2 == 0 else mid + 10
    yy = 856 + (i // 2) * 100
    badge(s, x + 18, yy - 8, i + 1, r=17)
    s.text(x + 48, yy, a, f(BOLD, 27), NAVY)
    s.text(x + 48, yy + 32, b, f(REG, 21), GREY)
horizon(s, 7)
navy_note(s, "Tip", "Write it in plain words. A non-techie should get it too.", "Lugha rahisi", seed=7)
finish(s)
s.save(7)

# ── 8 · where it lives ───────────────────────────────────────────────────────────────────────────
s = page(8, "Where it lives · Iweke wapi")
title2(s, "Put it where", "they'll look.", y=220, size=88)
numbered(s, [("GitHub", "The code, with a clear README for every project."),
             ("A simple personal site", "One link for everything: you, projects, contact."),
             ("LinkedIn Featured", "Pin your best project to the top of your profile."),
             ("Behance or Dribbble", "If you're a designer, this is your gallery."),
             ("A one-page PDF", "For WhatsApp and email, when a link isn't enough.")], 420, gap=108, ts=31, bs=23)
horizon(s, 8)
navy_note(s, "Start", "GitHub + one link is enough on day one.", "Anza na ulicho nacho", seed=8)
finish(s)
s.save(8)

# ── 9 · proof boosters ───────────────────────────────────────────────────────────────────────────
s = page(9, "Make it believable · Ushahidi")
title2(s, "Proof that", "it's real.", y=220, size=92)
tick_fill(s, [("A live demo link", "Free hosting: GitHub Pages, Netlify, Vercel."),
              ("A 60-second video", "A screen recording with your voice explaining it."),
              ("Real numbers", "“14 users”, “cut booking time from 1 hour to 5 minutes.”"),
              ("Kind words", "A message from someone who used it, with permission."),
              ("Clean code + README", "Someone will open your GitHub. Make it easy."),
              ("Your face and name", "People hire people, not usernames.")], 410, 990, size=28, sub=22, max_gap=64)
horizon(s, 9)
navy_note(s, "Truth", "Never invent numbers. Small and true beats big and fake.", "Ukweli ni heshima", seed=9)
finish(s)
s.save(9)

# ── 10 · mistakes ────────────────────────────────────────────────────────────────────────────────
s = page(10, "Avoid these · Epuka")
title2(s, "Portfolio", "killers.", y=220, size=96)
tick_fill(s, [("A tutorial clone as your star", "Everyone has the same weather app."),
              ("Broken links and dead demos", "Click every link before you share."),
              ("15 unfinished projects", "Three finished ones say more."),
              ("No explanation", "A screenshot alone tells them nothing."),
              ("Private repos and lorem ipsum", "If they can't see it, it doesn't count.")], 410, 990, size=28, sub=22, ok=False, max_gap=48)
horizon(s, 10)
navy_note(s, "Check", "Open it on your phone, like a recruiter would.", "Kagua kabla ya kutuma", seed=10)
finish(s)
s.save(10)

# ── 11 · keep it alive ───────────────────────────────────────────────────────────────────────────
s = page(11, "Keep it alive · Endelea")
title2(s, "A portfolio is", "never finished.", y=220, size=86)
flow(s, [("Every month: improve one thing", "A feature, a better screenshot, a clearer README."),
         ("Swap, don't stack", "A better project replaces your weakest one."),
         ("Share each new project", "A short LinkedIn post or WhatsApp status."),
         ("Ask for feedback", "A senior developer, a lecturer, a friend in tech.")], 410, h=104, gap=34, size=30)
horizon(s, 11)
navy_note(s, "Remember", "Your portfolio grows as you grow.", "Kidogo kidogo", seed=11)
finish(s)
s.save(11)

# ── 12 · closing ─────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Drop your portfolio", "link, I'll look.", [("Comment", "your link or your project idea"), ("Save", "the case-study template"),
                                                     ("Share", "with a friend who says “I have no projects”")])
paste_print(s, print_art("folio", k(380)), 640, 650)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
