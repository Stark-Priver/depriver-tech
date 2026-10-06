"""Carousel: coding on a data bundle budget (8 slides, 1080x1350, exported at 2x). Same editorial / print direction as
linkedin-for-students. The device is a data meter (like a phone's bundle bar) that drains on the leaks and stays full
on the habits that save MBs."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/coding-on-a-data-budget"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing


def meter(s, x, y, w, level, label, h=56):
    """Bundle bar: navy track, fill coloured by level (green > orange > red), label inside."""
    col = GREEN_OK if level > 0.5 else ORANGE if level > 0.2 else RED_NO
    s.rect(x + 6, y + 8, x + w + 6, y + h + 8, (205, 211, 224), r=h / 2)
    s.d.rounded_rectangle([k(x), k(y), k(x + w), k(y + h)], radius=k(h / 2), fill=(255, 255, 255), outline=NAVY, width=k(3))
    fw = max(h, (w - 8) * level)
    s.d.rounded_rectangle([k(x + 4), k(y + 4), k(x + 4 + fw), k(y + h - 4)], radius=k((h - 8) / 2), fill=col)
    s.text(x + w, y - 14, label, f(BOLD, 24), col, anchor="rs")


def tips_slide(n, label, t1, t2, tips, note, level):
    s = page(n, label)
    title2(s, t1, t2, y=220, size=84)
    meter(s, M, 390, W - 2 * M, level, f"Bundle {int(level * 100)}%")
    y = 540
    for a, b in tips:
        mark(s, M + 18, y - 10, True)
        s.text(M + 56, y, a, f(BOLD, fit(s, a, BOLD, 34, W - 2 * M - 60)), NAVY)
        s.para(M + 56, y + 44, b, f(REG, 27), W - 2 * M - 60, 38, GREY)
        y += 150
    horizon(s, n)
    navy_note(s, *note, seed=n)
    finish(s)
    s.save(n)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For students on bundles")
s.text(M - 6, 250, "Your bundle", f(BOLD, 104), NAVY)
s.text(M - 6, 360, "ended.", f(BOLD, 104), NAVY)
s.text(M - 8, 480, "Your learning", f(BOLD, 96), ORANGE)
s.text(M - 8, 580, "shouldn't.", f(BOLD, 96), ORANGE)
s.text(M, 670, "Okoa MB, endelea kujifunza", f(SIG, 58), NAVY)
swash(s, M + 8, M + 540, 696, ORANGE, 6)
meter(s, M, 780, W - 2 * M, 0.08, "Bundle 8%")
s.text(M, 900, "Ujumbe: kifurushi chako kinakaribia kuisha.", f(MED, 26), RED_NO)
horizon(s, 1)
cover_footer(s, "Swipe to save your MBs")
finish(s)
s.save(1)

# ── 2 · where it goes ────────────────────────────────────────────────────────────────────────────
s = page(2, "Where it goes · MB zinaenda wapi")
title2(s, "What eats", "your bundle.", y=220, size=84)
eaters = [("Video tutorials (HD)", 0.95), ("Auto-updates (Windows, apps)", 0.8), ("npm / pip installs, again and again", 0.6),
          ("Social media scrolling", 0.55), ("Reading docs and articles", 0.08)]
y = 420
for a, lv in eaters:
    s.text(M, y, a, f(SEMI, 28), NAVY)
    s.d.rounded_rectangle([k(M), k(y + 18), k(W - M), k(y + 46)], radius=k(14), fill=(226, 230, 238))
    col = RED_NO if lv > 0.7 else ORANGE if lv > 0.3 else GREEN_OK
    s.d.rounded_rectangle([k(M), k(y + 18), k(M + (W - 2 * M) * lv), k(y + 46)], radius=k(14), fill=col)
    y += 112
s.text(M, 980, "Illustration: video costs far more than reading.", f(REG, 22), GREY)
horizon(s, 2)
navy_note(s, "So", "Read more, stream less. Text is almost free.", "Soma zaidi, tazama kidogo", seed=2)
finish(s)
s.save(2)

tips_slide(3, "Learn offline · Bila internet", "Learn without", "a connection.",
           [("DevDocs offline", "Open devdocs.io, enable offline docs for your languages, read them anywhere."),
            ("Save articles and PDFs", "Download tutorials and books on Wi-Fi, read them on the daladala."),
            ("Practise locally", "Python, PHP and Node run on your laptop with no internet at all.")],
           ("Truth", "Most coding needs zero internet. Only looking things up does.", "Code haihitaji bando"), 0.85)
tips_slide(4, "Download smart · Pakua kwa akili", "Download when", "it's cheap.",
           [("Campus and office Wi-Fi", "Plan big downloads for where Wi-Fi is free."),
            ("Night bundles", "Schedule big downloads when night bundles are cheaper."),
            ("Lower video quality", "360p or 480p is enough to follow a coding tutorial.")],
           ("Plan it", "Keep a list of things to download next time you're on Wi-Fi.", "Panga upakuaji"), 0.7)
tips_slide(5, "Developer tricks · Mbinu", "Tools that", "save MBs.",
           [("Git works offline", "Commit all day without internet. Push once when you're connected."),
            ("Reuse packages", "Keep node_modules and pip caches. Copy them by flash drive, don't re-download."),
            ("One project template", "Start new projects from a saved template, not fresh installs.")],
           ("Pro tip", "Share a flash drive of installers with your class.", "Tushirikiane"), 0.75)
tips_slide(6, "Stop the leaks · Ziba mianya", "Stop silent", "data leaks.",
           [("Set Wi-Fi/hotspot as metered", "Windows then pauses big updates on that connection."),
            ("Turn off auto-updates", "Update apps when you're on free Wi-Fi."),
            ("Check data usage", "Phone settings show which app ate your bundle.")],
           ("Do this today", "Mark your hotspot as metered. Two minutes, big savings.", "Linda kifurushi"), 0.9)

# ── 7 · weekly plan ──────────────────────────────────────────────────────────────────────────────
s = page(7, "A bundle plan · Mpango")
title2(s, "One bundle,", "one week of learning.", y=220, size=80)
plan = [("On Wi-Fi", "Download docs, videos, packages, updates"), ("On the bus", "Read saved articles and PDFs"),
        ("At home", "Code offline, commit with Git"), ("Online, 10 min", "Search errors, push code, ask questions")]
y = 450
for a, b in plan:
    s.d.rounded_rectangle([k(M), k(y - 44), k(M + 250), k(y + 16)], radius=k(14), fill=NAVY)
    s.text(M + 125, y - 14, a, f(BOLD, 24), WHITE_T, anchor="mm")
    s.para(M + 280, y - 4, b, f(SEMI, 27), W - 2 * M - 290, 36, NAVY)
    y += 130
horizon(s, 7)
navy_note(s, "Remember", "No bundle is not a reason to stop. It's a reason to plan.", "Panga, usisimame", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What's your best", "MB-saving trick?", [("Save", "before your next bundle ends"), ("Share", "with the friend always asking for hotspot"),
                                                  ("Comment", "your best data trick")])
meter(s, 600, 760, 400, 0.92, "92%", h=60)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
