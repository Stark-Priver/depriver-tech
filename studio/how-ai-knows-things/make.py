"""Carousel: how AI "knows" things, Inavyofanya kazi #5 (8 slides, 1080x1350, exported at 2x). The device is a
next-word prediction: a sentence with a blank and probability bars (clearly marked as an illustration)."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/how-ai-knows-things"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def prompt_line(s, y, before, blank_w=200, size=40):
    s.text(M, y, before, f(BOLD, size), NAVY)
    x = M + s.width(before, f(BOLD, size)) + 14
    s.d.rounded_rectangle([k(x), k(y - size * 0.95), k(x + blank_w), k(y + 10)], radius=k(10), fill=(253, 236, 230), outline=ORANGE, width=k(3))
    s.text(x + blank_w / 2, y - size * 0.4, "?", f(BOLD, size), ORANGE, anchor="mm")


def word_bars(s, y, items, w=None):
    w = w or W - 2 * M
    for word, p in items:
        s.text(M, y, word, f(SEMI, 28), NAVY)
        s.text(W - M, y, f"{int(p * 100)}%", f(BOLD, 26), ORANGE if p == items[0][1] else GREY, anchor="rs")
        s.d.rounded_rectangle([k(M), k(y + 16), k(M + w), k(y + 42)], radius=k(13), fill=PALE)
        s.d.rounded_rectangle([k(M), k(y + 16), k(M + max(26, w * p)), k(y + 42)], radius=k(13), fill=ORANGE if p == items[0][1] else (150, 158, 175))
        y += 86
    return y


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "How it works · Inavyofanya kazi #05")
s.text(M - 6, 250, "How does AI", f(BOLD, 100), NAVY)
s.text(M - 6, 356, "“know” things?", f(BOLD, 100), ORANGE)
s.text(M, 448, "Inabashiri neno linalofuata", f(SIG, 56), NAVY)
swash(s, M + 8, M + 520, 474, ORANGE, 6)
prompt_line(s, 590, "Mji mkuu wa Tanzania ni", 230, 40)
word_bars(s, 660, [("Dodoma", 0.86), ("Dar es Salaam", 0.11), ("Arusha", 0.02)])
s.text(M, 940, "Illustration, not real model numbers.", f(REG, 22), GREY)
horizon(s, 1)
cover_footer(s, "Swipe, look inside")
finish(s)
s.save(1)

# ── 2 · training ─────────────────────────────────────────────────────────────────────────────────
s = page(2, "Training · Mafunzo", "Inavyofanya kazi")
title2(s, "It read a huge", "amount of text.", y=220, size=86)
tick_fill(s, [("Trained on huge amounts of text", "Books, websites, code, conversations."),
              ("It learns patterns, not a list of facts", "Which words tend to follow which, and in what situations."),
              ("Then it's tuned to be helpful", "People rate answers so it learns to follow instructions.")], 420, 900, size=31, sub=27)
horizon(s, 2)
navy_note(s, "So", "It doesn't look facts up in a table. It predicts.", "Inabashiri, haikumbuki", seed=2)
finish(s)
s.save(2)

# ── 3 · next word ────────────────────────────────────────────────────────────────────────────────
s = page(3, "Next word · Neno linalofuata", "Inavyofanya kazi")
title2(s, "One word", "at a time.", y=220, size=90)
prompt_line(s, 450, "Habari za", 220, 44)
word_bars(s, 520, [("asubuhi", 0.48), ("leo", 0.27), ("jioni", 0.19), ("kazi", 0.06)])
s.para(M, 900, "It picks a word, adds it, then predicts the next one again. Hundreds of times, very fast.", f(MED, 28), W - 2 * M, 40, NAVY)
horizon(s, 3)
navy_note(s, "Illustration", "Real models choose from tens of thousands of options.", "Neno kwa neno", seed=3)
finish(s)
s.save(3)

# ── 4 · tokens ───────────────────────────────────────────────────────────────────────────────────
s = page(4, "Tokens · Vipande", "Inavyofanya kazi")
title2(s, "It reads in", "pieces (tokens).", y=220, size=88)
for row, (label, parts) in enumerate([("English", ["Good", " morning"]), ("Kiswahili", ["Hab", "ari", " za", " asub", "uhi"])]):
    y = 450 + row * 190
    smallcaps(s, M, y, label, 15, ORANGE)
    x = M
    for i, p in enumerate(parts):
        ww = s.width(p, f(MONO_B, 32)) + 36
        s.d.rounded_rectangle([k(x), k(y + 24), k(x + ww), k(y + 100)], radius=k(12), fill=[NAVY, ORANGE, (37, 99, 235), GREEN_OK, (150, 90, 200)][i % 5])
        s.text(x + ww / 2, y + 62, p, f(MONO_B, 32), WHITE_T, anchor="mm")
        x += ww + 8
s.para(M, 880, "Illustration. Many models split Swahili into more pieces than English, because they saw less Swahili text.", f(MED, 27), W - 2 * M, 40, NAVY)
horizon(s, 4)
navy_note(s, "That's why", "AI is often weaker in Kiswahili. Better Swahili data fixes that.", "Kiswahili kinahitaji data", seed=4)
finish(s)
s.save(4)

# ── 5 · making things up ─────────────────────────────────────────────────────────────────────────
s = page(5, "Hallucinations · Kubuni", "Inavyofanya kazi")
title2(s, "Why it sometimes", "makes things up.", y=220, size=84)
chat(s, M, 420, 700, "Nipe vitabu 3 vya historia ya Tanzania na waandishi wao.", "You", mine=True, size=25, lh=34)
chat(s, M + 120, 570, 760, "1. “Tanzania: Safari ya Uhuru” by J. Mwakasege (1987)…", "AI", mine=False, size=25, lh=34, tag="Huenda si kweli", tag_ok=False)
s.para(M, 790, "It writes what a real answer would LOOK like. If it doesn't know, it can still produce a confident, fake title.", f(MED, 29), W - 2 * M, 42, NAVY)
horizon(s, 5)
navy_note(s, "Rule", "Confident is not the same as correct.", "Kujiamini si ukweli", seed=5)
finish(s)
s.save(5)

# ── 6 · cutoff and context ───────────────────────────────────────────────────────────────────────
s = page(6, "Limits · Mipaka", "Inavyofanya kazi")
title2(s, "What it knows,", "and when.", y=220, size=88)
tick_fill(s, [("A training cutoff date", "It may not know recent news, prices or new versions."),
              ("Some tools can search", "Then it reads web pages, but can still misread them."),
              ("It only sees what you give it", "Paste your code or document and it can use that."),
              ("It doesn't remember you by default", "Unless the app has a memory feature turned on.")], 420, 990, size=31, sub=26)
horizon(s, 6)
navy_note(s, "Tip", "For anything recent, check the official source.", "Thibitisha habari mpya", seed=6)
finish(s)
s.save(6)

# ── 7 · use it well ──────────────────────────────────────────────────────────────────────────────
s = page(7, "Use it well · Itumie vizuri", "Inavyofanya kazi")
title2(s, "Use it like a", "smart assistant.", y=220, size=86)
numbered(s, [("Give context", "Who you are, what you're building, what you tried."), ("Ask it to explain", "Understanding beats copying, especially for exams."),
             ("Check facts and code", "Run the code. Verify names, dates, sources."), ("Ask for sources, then open them", "A link you didn't click proves nothing."),
             ("Keep private data out", "No passwords, IDs or client secrets.")], 430, gap=112)
horizon(s, 7)
navy_note(s, "Remember", "You are responsible for what you submit, not the AI.", "Jukumu ni lako", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Has AI ever lied", "to you?", [("Comment", "the funniest wrong answer"), ("Save", "the 5 rules on slide 7"),
                                          ("Share", "with a friend who trusts it blindly")])
stamp(s, 840, 860, "THIBITISHA", RED_NO, angle=-10, size=42)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
