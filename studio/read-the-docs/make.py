"""Carousel: learn to read documentation (8 slides, 1080x1350, exported at 2x). Ujuzi wa kazini. The device is a docs page
mock with a sidebar (Quickstart, Guides, API reference, Examples, Changelog) and an annotated function reference."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/read-the-docs"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs

SECTIONS = ["Quickstart", "Guides", "API reference", "Examples", "Changelog"]


def docs_page(s, box, active=None, title="Getting started", lines=6):
    """Docs website mock: top bar with search, left sidebar with sections, content lines."""
    x0, y0, x1, y1 = box
    s.rect(x0 + 10, y0 + 12, x1 + 10, y1 + 12, INK_SHADOW, r=18)
    s.d.rounded_rectangle([k(x0), k(y0), k(x1), k(y1)], radius=k(18), fill=(255, 255, 255), outline=NAVY, width=k(3))
    s.d.rounded_rectangle([k(x0), k(y0), k(x1), k(y0 + 64)], radius=k(18), fill=NAVY)
    s.rect(x0, y0 + 44, x1, y0 + 64, NAVY)
    s.text(x0 + 26, y0 + 42, "docs", f(BOLD, 22), WHITE_T)
    s.d.rounded_rectangle([k(x1 - 250), k(y0 + 14), k(x1 - 20), k(y0 + 50)], radius=k(18), fill=(38, 58, 96))
    s.text(x1 - 230, y0 + 39, "Search  Ctrl+K", f(MED, 17), SOFT)
    sw = (x1 - x0) * 0.32
    s.rect(x0 + 3, y0 + 64, x0 + sw, y1 - 3, (244, 245, 248))
    for i, sec in enumerate(SECTIONS):
        yy = y0 + 110 + i * 50
        if sec == active:
            s.d.rounded_rectangle([k(x0 + 12), k(yy - 28), k(x0 + sw - 12), k(yy + 12)], radius=k(10), fill=ORANGE)
        s.text(x0 + 26, yy, sec, f(SEMI, fit(s, sec, SEMI, 19, sw - 40)), WHITE_T if sec == active else NAVY)
    cx = x0 + sw + 30
    s.text(cx, y0 + 120, title, f(BOLD, fit(s, title, BOLD, 28, x1 - cx - 30)), NAVY)
    for i in range(lines):
        yy = y0 + 160 + i * 34
        if yy > y1 - 30:
            break
        s.d.rounded_rectangle([k(cx), k(yy), k(x1 - 30 - (i % 3) * 60), k(yy + 12)], radius=k(6), fill=(214, 220, 232))
    return sw


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Skills uni skips · Ujuzi wa kazini")
s.text(M - 6, 250, "Read the", f(BOLD, 110), NAVY)
s.text(M - 6, 360, "docs.", f(BOLD, 110), ORANGE)
s.text(M, 450, "Soma maelekezo rasmi", f(SIG, 58), NAVY)
swash(s, M + 8, M + 470, 476, ORANGE, 6)
s.para(M, 560, "The skill that separates people who copy tutorials from people who build anything.", f(REG, 28), W - 2 * M, 42, GREY)
docs_page(s, (M, 680, W - M - 8, 1000), active="Quickstart")
horizon(s, 1)
cover_footer(s, "Swipe, learn to read them")
finish(s)
s.save(1)

# ── 2 · why ──────────────────────────────────────────────────────────────────────────────────────
s = page(2, "Why docs · Kwa nini", "Ujuzi wa kazini")
title2(s, "Tutorials age.", "Docs don't.", y=220, size=88)
tick_fill(s, [("Written by the people who built it", "The official, correct way."), ("Updated with every version", "A 2021 video may show code that no longer works."),
              ("Cheaper on your bundle", "Text costs almost nothing compared with video."), ("A real job skill", "At work, nobody makes a tutorial for your problem.")],
          420, 990, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Balance", "Videos for your first steps. Docs for everything after.", "Video kuanza, docs kukua", seed=2)
finish(s)
s.save(2)

# ── 3 · map ──────────────────────────────────────────────────────────────────────────────────────
s = page(3, "The map · Ramani", "Ujuzi wa kazini")
title2(s, "Every docs site", "has the same map.", y=220, size=84)
table(s, M, 410, ["Section", "Use it to"], [["Quickstart", "Get it running in 10 minutes"], ["Guides", "Learn one topic step by step"],
                                            ["API reference", "Look up exact functions and options"], ["Examples", "Copy working code, then adapt"],
                                            ["Changelog", "See what changed between versions"]],
      [330, W - 2 * M - 8 - 330], size=26, rh=86)
horizon(s, 3)
navy_note(s, "Start", "Always do the Quickstart first, even if it looks too easy.", "Anza na Quickstart", seed=3)
finish(s)
s.save(3)

# ── 4 · how to read ──────────────────────────────────────────────────────────────────────────────
s = page(4, "How to read · Jinsi ya kusoma", "Ujuzi wa kazini")
title2(s, "Don't read it", "like a novel.", y=220, size=88)
numbered(s, [("Know your question first", "“How do I send a POST request with JSON?”"), ("Use the search box", "Ctrl+K or Ctrl+F for the exact word."),
             ("Read the example first", "Then read the explanation around it."), ("Run it yourself", "Change one thing, see what happens."),
             ("Bookmark what you use often", "Your own little map.")], 430, gap=112)
horizon(s, 4)
navy_note(s, "Truth", "Seniors don't remember everything. They know where to look.", "Wanajua wapi pa kutafuta", seed=4)
finish(s)
s.save(4)

# ── 5 · a function reference ─────────────────────────────────────────────────────────────────────
s = page(5, "Reference · Kumbukumbu", "Ujuzi wa kazini")
title2(s, "How to read a", "function entry.", y=220, size=84)
y = code_window(s, 390, ["str.split(sep=None, maxsplit=-1)", "", "# Returns a list of the words in the string,", "# using sep as the separator.",
                         "", '"a,b,c".split(",")  # ["a", "b", "c"]'], file="docs.python.org", lang="Python", size=24, lh=40)
for i, (lab, txt) in enumerate([("Name", "what you call"), ("Parameters", "what you pass"), ("Returns", "what you get back"), ("Example", "copy, run, change")]):
    xx = M + (i % 2) * 470
    yy = y + 70 + (i // 2) * 80
    s.d.ellipse([k(xx), k(yy - 30), k(xx + 40), k(yy + 10)], fill=ORANGE if i % 2 == 0 else NAVY)
    s.text(xx + 20, yy - 10, str(i + 1), f(BOLD, 20), WHITE_T, anchor="mm")
    s.text(xx + 56, yy, lab, f(BOLD, 27), NAVY)
    s.text(xx + 56 + s.width(lab, f(BOLD, 27)) + 12, yy, txt, f(REG, 22), GREY)
horizon(s, 5)
navy_note(s, "Defaults", "sep=None means you can skip it. That's what = shows.", "Soma thamani za msingi", seed=5)
finish(s)
s.save(5)

# ── 6 · versions ─────────────────────────────────────────────────────────────────────────────────
s = page(6, "Versions · Matoleo", "Ujuzi wa kazini")
title2(s, "Match the docs", "to your version.", y=220, size=84)
tick_fill(s, [("Check your version", "python --version, php -v, or package.json."), ("Pick the same version in the docs", "Most sites have a version menu at the top."),
              ("Read the changelog when upgrading", "Look for “breaking changes” and “deprecated”."),
              ("Old tutorial broken?", "Search the changelog for the function name.")], 420, 990, size=31, sub=26)
horizon(s, 6)
navy_note(s, "Common bug", "Half of “the tutorial doesn't work” is a version mismatch.", "Toleo sahihi", seed=6)
finish(s)
s.save(6)

# ── 7 · challenge ────────────────────────────────────────────────────────────────────────────────
s = page(7, "Challenge · Changamoto", "Ujuzi wa kazini")
title2(s, "One week,", "docs only.", y=220, size=92)
docs_page(s, (M, 400, W - M - 8, 760), active="Quickstart", title="Your first app", lines=8)
tick_list(s, [("Pick one tool: Laravel, React, Flask, Flutter", None), ("Do its Quickstart with no YouTube", None),
              ("Build one tiny thing from the Guides", None)], 840, size=28)
horizon(s, 7)
navy_note(s, "Then", "Post what you built and which page helped most.", "Onyesha ulichojifunza", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which docs do", "you read most?", [("Comment", "your favourite docs site"), ("Save", "the map on slide 3"),
                                              ("Share", "with someone stuck in tutorial hell")])
stamp(s, 840, 860, "NIMESOMA", GREEN_OK, angle=-10, size=46)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
