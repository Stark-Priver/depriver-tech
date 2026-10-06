"""Carousel: your first hackathon (8 slides, 1080x1350, exported at 2x). Timed for DevFest / hackathon season.
The device is an event badge on a lanyard and a 48-hour clock timeline."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/your-first-hackathon"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def badge(s, x, y, w=360, role="HACKER", name="Jina: Wewe", team="Team: Mvua"):
    h = w * 1.25
    cx = x + w / 2
    q = w / 360
    s.d.line([k(cx - 60 * q), k(y - 140 * q), k(cx - 16 * q), k(y + 4)], fill=NAVY, width=k(14 * q))
    s.d.line([k(cx + 60 * q), k(y - 140 * q), k(cx + 16 * q), k(y + 4)], fill=NAVY, width=k(14 * q))
    card(s, (x, y, x + w, y + h), r=22 * q)
    s.d.rounded_rectangle([k(x), k(y), k(x + w), k(y + 150 * q)], radius=k(22 * q), fill=ORANGE)
    s.rect(x, y + 120 * q, x + w, y + 150 * q, ORANGE)
    s.d.rounded_rectangle([k(cx - 36 * q), k(y + 20 * q), k(cx + 36 * q), k(y + 34 * q)], radius=k(7 * q), fill=(255, 255, 255))
    s.text(cx, y + 100 * q, role, f(BOLD, 46 * q), WHITE_T, anchor="ms")
    s.text(cx, y + 210 * q, name, f(BOLD, 30 * q), NAVY, anchor="ms")
    s.text(cx, y + 255 * q, team, f(MED, 24 * q), GREY, anchor="ms")
    s.text(cx, y + 330 * q, "48h", f(BOLD, 64 * q), ORANGE, anchor="ms")
    s.text(cx, y + 372 * q, "build · pitch · learn", f(SEMI, 20 * q), NAVY, anchor="ms")


def clock(s, cx, cy, r, hours_done=20):
    """48-hour dial: navy ring, orange arc for hours done."""
    s.d.ellipse([k(cx - r + 6), k(cy - r + 8), k(cx + r + 6), k(cy + r + 8)], fill=INK_SHADOW)
    s.d.ellipse([k(cx - r), k(cy - r), k(cx + r), k(cy + r)], fill=(255, 255, 255), outline=NAVY, width=k(5))
    s.d.arc([k(cx - r + 16), k(cy - r + 16), k(cx + r - 16), k(cy + r - 16)], -90, -90 + 360 * hours_done / 48, fill=ORANGE, width=k(18))
    s.text(cx, cy - 4, f"{hours_done}h", f(BOLD, r * 0.42), NAVY, anchor="mm")
    s.text(cx, cy + r * 0.34, "of 48", f(SEMI, r * 0.16), GREY, anchor="mm")


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Hackathon season · Msimu wa hackathon")
s.text(M - 6, 260, "Your first", f(BOLD, 100), NAVY)
s.text(M - 6, 368, "hackathon.", f(BOLD, 100), ORANGE)
s.text(M, 460, "Usiogope, jaribu", f(SIG, 60), NAVY)
swash(s, M + 8, M + 400, 486, ORANGE, 6)
s.para(M, 570, "48 hours, a team, one idea. What to expect, how to prepare, and how to pitch.", f(REG, 28), 470, 42, GREY)
chip_row(s, ["No experience needed", "Free food", "New friends"], M, 760, size=21, maxx=560)
badge(s, 680, 470, 320)
horizon(s, 1)
cover_footer(s, "Swipe, get ready")
finish(s)
s.save(1)

# ── 2 · what it is ───────────────────────────────────────────────────────────────────────────────
s = page(2, "What is it · Ni nini")
title2(s, "A weekend to", "build something.", y=220, size=84)
s.para(M, 410, "Teams of 2 to 5 build a working prototype in 24 to 48 hours, then present it to judges. Prizes are nice. The real win is what you learn and who you meet.",
       f(MED, 30), W - 2 * M, 44, NAVY)
smallcaps(s, M, 640, "Where to find them", 15, ORANGE)
tick_fill(s, [("Google DevFests and GDG events", "Developer communities in many cities"), ("University and innovation hub hackathons", "Watch your department notice board"),
              ("Online hackathons", "Devpost and MLH list many, open worldwide")], 700, 1000, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Truth", "Beginners are welcome. Organisers want you there.", "Wanakukaribisha", seed=2)
finish(s)
s.save(2)

# ── 3 · before ───────────────────────────────────────────────────────────────────────────────────
s = page(3, "Before · Kabla")
title2(s, "Prepare the", "week before.", y=220, size=88)
tick_fill(s, [("Build a mixed team", "A builder, a designer, a presenter. Not five backend developers."),
              ("Set up your tools", "Git, your framework, a starter template. Don't install on the day."),
              ("Learn one quick deploy", "Vercel, Render or similar, so your demo has a link."),
              ("Pack well", "Charger, extension cable, water, a jacket for the AC.")], 410, 1000, size=31, sub=26)
horizon(s, 3)
navy_note(s, "Sleep", "Arrive rested. Tired teams make bad decisions.", "Pumzika kwanza", seed=3)
finish(s)
s.save(3)

# ── 4 · 48 hours ─────────────────────────────────────────────────────────────────────────────────
s = page(4, "The 48 hours · Masaa 48")
title2(s, "How the hours", "really go.", y=220, size=88)
plan = [("0–2h", "Pick the problem and one core feature"), ("2–4h", "Sketch screens, split tasks, set up Git"),
        ("4–30h", "Build. Merge often. Demo-able every few hours"), ("30–40h", "Freeze features. Fix bugs, polish the demo"),
        ("40–46h", "Slides and pitch practice, three times"), ("48h", "Present. Breathe. Celebrate")]
y = 420
for i, (t_, a) in enumerate(plan):
    s.d.rounded_rectangle([k(M), k(y - 40), k(M + 170), k(y + 14)], radius=k(27), fill=ORANGE if i % 2 == 0 else NAVY)
    s.text(M + 85, y - 13, t_, f(BOLD, 24), WHITE_T, anchor="mm")
    s.text(M + 200, y - 2, a, f(SEMI, fit(s, a, SEMI, 27, W - 2 * M - 210)), NAVY)
    y += 104
horizon(s, 4)
navy_note(s, "Golden rule", "Stop adding features at hour 30. A working demo beats a big idea.", "Demo inayofanya kazi", seed=4)
finish(s)
s.save(4)

# ── 5 · the idea ─────────────────────────────────────────────────────────────────────────────────
s = page(5, "The idea · Wazo")
title2(s, "Small problem,", "clear demo.", y=220, size=88)
tick_fill(s, [("A real problem you've seen", "Queues at the clinic, lost bus tickets, shop debts in a notebook."),
              ("One feature, done well", "Judges remember one thing that works, not ten that don't."),
              ("Fits the theme", "Read the judging criteria before choosing."),
              ("Easy to show in 2 minutes", "If you can't demo it, simplify it.")], 410, 1000, size=31, sub=26)
clock(s, 900, 900, 80, 2)
horizon(s, 5)
navy_note(s, "Local wins", "Tanzanian problems make memorable projects.", "Tatizo la kwetu", seed=5)
finish(s)
s.save(5)

# ── 6 · the pitch ────────────────────────────────────────────────────────────────────────────────
s = page(6, "The pitch · Kuwasilisha")
title2(s, "3 minutes", "that decide it.", y=220, size=88)
flow(s, [("The problem", "One real person, one real pain. 30 seconds."), ("The demo", "Live, the main flow only. 90 seconds."),
         ("Why it matters", "Who it helps and how many. 30 seconds."), ("What's next", "What you'd build with more time. 30 seconds.")],
     420, h=100, gap=34, size=30)
horizon(s, 6)
navy_note(s, "Plan B", "Record a demo video in case the Wi-Fi dies.", "Daima kuwa na video", seed=6)
finish(s)
s.save(6)

# ── 7 · don'ts ───────────────────────────────────────────────────────────────────────────────────
s = page(7, "Avoid · Epuka")
title2(s, "Mistakes first", "timers make.", y=220, size=88)
tick_fill(s, [("Building too much", "Half-finished features look worse than none."), ("Skipping all sleep", "Take short naps in turns."),
              ("Leaving the pitch to the end", "Practise from hour 40, not minute 47."), ("Fighting over the idea for hours", "Vote in 20 minutes and move on.")], 410, 1000, size=31, sub=26, ok=False)
horizon(s, 7)
navy_note(s, "Remember", "Losing your first hackathon is normal. Not going is the only fail.", "Kushiriki ni kushinda", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Have you done a", "hackathon yet?", [("Tag", "the friends for your team"), ("Share", "the next hackathon you find"),
                                                ("Comment", "“niko tayari” if you'll join one")])
clock(s, 850, 860, 120, 48)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
