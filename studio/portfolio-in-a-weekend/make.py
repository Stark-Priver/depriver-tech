"""Carousel: build your portfolio website in one weekend (8 slides, 1080x1350, exported at 2x). Same editorial / print
direction as coding-on-a-data-budget. The device is a weekend timetable (ratiba): time blocks for Saturday and Sunday,
from picking a template to sharing a live link."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/portfolio-in-a-weekend"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing


def timetable(s, y, blocks, h=126):
    """Time blocks: time chip on the left rail, task card on the right."""
    s.rect(M + 92, y - 20, M + 96, y + len(blocks) * h - 40, RULE)
    for i, (t_, a, b) in enumerate(blocks):
        yy = y + i * h
        s.d.rounded_rectangle([k(M), k(yy - 6), k(M + 150), k(yy + 46)], radius=k(26), fill=ORANGE if i % 2 == 0 else NAVY)
        s.text(M + 75, yy + 20, t_, f(BOLD, 26), WHITE_T, anchor="mm")
        card(s, (M + 180, yy - 20, W - M - 8, yy + h - 36), r=14)
        s.text(M + 206, yy + 22, a, f(BOLD, fit(s, a, BOLD, 29, W - 2 * M - 230)), NAVY)
        s.text(M + 206, yy + 58, b, f(REG, fit(s, b, REG, 22, W - 2 * M - 230)), GREY)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For students & junior devs")
s.text(M - 6, 250, "Your portfolio", f(BOLD, 100), NAVY)
s.text(M - 6, 356, "site, live by", f(BOLD, 100), NAVY)
s.text(M - 8, 486, "Sunday night.", f(BOLD, 110), ORANGE)
s.text(M, 576, "Wikendi moja tu", f(SIG, 62), NAVY)
swash(s, M + 8, M + 360, 602, ORANGE, 6)
timetable(s, 700, [("Sat", "Build it", "template, about, projects"), ("Sun", "Ship it", "mobile check, deploy, share")], h=140)
horizon(s, 1)
cover_footer(s, "Swipe for the timetable")
finish(s)
s.save(1)

# ── 2 · prep ─────────────────────────────────────────────────────────────────────────────────────
s = page(2, "Friday night · Maandalizi")
title2(s, "Prepare these", "on Friday.", y=220, size=84)
prep = [("3 projects", "Your best, with a one-line description each."), ("Screenshots", "Clean ones, on real data, not lorem ipsum."),
        ("A clear photo", "Face, good light, plain background."), ("Your story", "Three sentences: who, what you build, what's next."),
        ("Links", "GitHub, LinkedIn, CV as PDF, email.")]
numbered(s, prep, 430, gap=112)
horizon(s, 2)
navy_note(s, "Truth", "Content is the hard part. Code is the easy part.", "Andaa maudhui kwanza", seed=2)
finish(s)
s.save(2)

# ── 3 · saturday ─────────────────────────────────────────────────────────────────────────────────
s = page(3, "Saturday · Jumamosi")
title2(s, "Saturday:", "build it.", y=220, size=88)
timetable(s, 420, [("09:00", "Pick a simple template", "One page. HTML/CSS or a starter you understand."),
                   ("11:00", "Hero + about", "Name, role, photo, three-sentence story."),
                   ("14:00", "Projects section", "Screenshot, one line, tech used, links for each."),
                   ("17:00", "Contact section", "Email, GitHub, LinkedIn, CV download.")])
horizon(s, 3)
navy_note(s, "Rule", "Done is better than perfect. Polish comes later.", "Maliza kwanza", seed=3)
finish(s)
s.save(3)

# ── 4 · sunday ───────────────────────────────────────────────────────────────────────────────────
s = page(4, "Sunday · Jumapili")
title2(s, "Sunday:", "ship it.", y=220, size=88)
timetable(s, 420, [("09:00", "Check it on a phone", "Most visitors will open it on mobile."),
                   ("11:00", "Fix and proofread", "Typos, broken links, slow images."),
                   ("14:00", "Deploy for free", "GitHub Pages, Netlify or Vercel."),
                   ("17:00", "Share the link", "Bio, LinkedIn, CV, WhatsApp status.")])
horizon(s, 4)
navy_note(s, "Then", "Add each new project the day you finish it.", "Endelea kuongeza", seed=4)
finish(s)
s.save(4)

# ── 5 · free hosting ─────────────────────────────────────────────────────────────────────────────
s = page(5, "Free hosting · Bure")
title2(s, "Three free", "ways to go live.", y=220, size=84)
hosts = [("GitHub Pages", "Push your HTML to a repo, turn on Pages.", "yourname.github.io"),
         ("Netlify", "Drag and drop your folder, or connect GitHub.", "yourname.netlify.app"),
         ("Vercel", "Best for React and Next.js projects.", "yourname.vercel.app")]
y = 410
for a, b, c in hosts:
    card(s, (M, y, W - M - 8, y + 170), r=14)
    s.text(M + 30, y + 58, a, f(BOLD, 36), NAVY)
    s.text(M + 30, y + 100, b, f(REG, 24), GREY)
    s.text(M + 30, y + 140, c, f(SEMI, 24), ORANGE)
    y += 196
horizon(s, 5)
navy_note(s, "Later", "A custom domain (.com or .co.tz) looks pro, but free is fine to start.", "Anza bure", seed=5)
finish(s)
s.save(5)

# ── 6 · what goes on it ──────────────────────────────────────────────────────────────────────────
s = page(6, "What goes on it · Ndani yake")
title2(s, "Keep it to", "five sections.", y=220, size=84)
secs = [("Hero", "Name, role, one line, photo"), ("About", "Your three-sentence story"), ("Projects", "3–6, best first, with links"),
        ("Skills", "Only what you've used"), ("Contact", "Email, GitHub, LinkedIn, CV")]
numbered(s, secs, 440, gap=110, ts=34, bs=25)
horizon(s, 6)
navy_note(s, "Skip", "Skill percentage bars. “HTML 90%” means nothing.", "Rahisi ni bora", seed=6)
finish(s)
s.save(6)

# ── 7 · mistakes ─────────────────────────────────────────────────────────────────────────────────
s = page(7, "Avoid these · Epuka")
title2(s, "Don't let these", "kill it.", y=220, size=84)
bad = [("Lorem ipsum left in", "Looks unfinished. Read every word."), ("Links that go nowhere", "Click every button before you share."),
       ("Huge images", "Compress them. Slow sites lose visitors."), ("Projects with no proof", "Add a screenshot and a live link."),
       ("Never updated", "A 2-year-old portfolio says you stopped.")]
y = 430
for a, b in bad:
    mark(s, M + 18, y - 10, False)
    s.text(M + 56, y, a, f(BOLD, 31), NAVY)
    s.text(M + 56, y + 40, b, f(REG, 24), GREY)
    y += 116
horizon(s, 7)
navy_note(s, "Test", "Send it to two friends. Watch where they get confused.", "Waulize wenzako", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Built it?", "Drop your link.", [("Save", "for this weekend"), ("Share", "with your coding buddy"),
                                            ("Comment", "your portfolio link, I'll check some")])
s.d.rounded_rectangle([k(620), k(740), k(W - M), k(800)], radius=k(30), fill=GREEN_OK)
s.text(620 + (W - M - 620) / 2, 771, "Live by Sunday", f(BOLD, 26), WHITE_T, anchor="mm")
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
