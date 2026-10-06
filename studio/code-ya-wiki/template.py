"""Code ya Wiki (code of the week, spot the bug): shared 6-slide template. Each episode lives in
studio/code-ya-wiki-NN/make.py, sets EP and execs this file. The device is a code editor window; the answer slide circles
the bug in red, the fix slide marks the changed line green. Slides: the puzzle, a hint (expected vs got), the bug, the
fix, the lesson, your turn. Keep code lines under ~44 characters.
EP keys: num, lang, file, question, goal, code [lines], bug_lines [indexes], expected, got, hint, why, fixed [lines],
fix_lines [indexes], lesson, avoid [3], sw."""
import re
TOTAL = 6
POST_URL = f"depriver.tech/blog/code-ya-wiki-{EP['num']:02d}"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing

KEYWORDS = {"def", "return", "for", "in", "if", "else", "elif", "while", "print", "range", "len", "const", "let", "function",
            "UPDATE", "SET", "WHERE", "SELECT", "FROM", "AND", "OR", "INSERT", "INTO", "VALUES", "or", "and", "not", "echo",
            "await", "async", "Number", "true", "false", "True", "False", "null", "None", "new", "prepare", "execute"}
CODE_GREEN = (22, 128, 70)
CODE_BLUE = (37, 99, 235)
HL_RED = (252, 226, 222)
HL_GREEN = (219, 242, 227)


def code_line(s, x, y, line, size):
    """One line of code with simple colouring: keywords, strings, numbers, comments."""
    fnt, fb = f(MONO, size), f(MONO_B, size)
    for tok in re.findall(r"#.*$|--.*$|//.*$|\"[^\"]*\"|'[^']*'|\$?\w+|\s+|.", line):
        if tok.startswith(("#", "//", "--")):
            col, ft = GREY, fnt
        elif tok[0] in "\"'":
            col, ft = CODE_GREEN, fnt
        elif tok.isdigit():
            col, ft = CODE_BLUE, fnt
        elif tok in KEYWORDS:
            col, ft = ORANGE, fb
        else:
            col, ft = NAVY, fnt
        s.text(x, y, tok, ft, col)
        x += s.width(tok, ft)


def editor(s, y, lines, hl=(), hl_col=HL_RED, size=27, lh=46, circle=False, x0=M, x1=W - M - 8):
    """Editor window: navy title bar with dots and file name, line numbers, highlighted lines. Returns bottom y."""
    h = 70 + 30 + lh * len(lines) + 20
    s.rect(x0 + 10, y + 12, x1 + 10, y + h + 12, (205, 211, 224), r=20)
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + h)], radius=k(20), fill=(255, 255, 255), outline=NAVY, width=k(3))
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + 64)], radius=k(20), fill=NAVY)
    s.rect(x0, y + 40, x1, y + 64, NAVY)
    for i, c in enumerate([RED_NO, (240, 180, 60), GREEN_OK]):
        s.d.ellipse([k(x0 + 26 + i * 30), k(y + 22), k(x0 + 46 + i * 30), k(y + 42)], fill=c)
    s.text(x0 + 130, y + 40, EP["file"], f(MONO, 21), SOFT)
    s.text(x1 - 24, y + 40, EP["lang"], f(SEMI, 19), ORANGE, anchor="rs")
    yy = y + 64 + 30
    for i, ln in enumerate(lines):
        if i in hl:
            s.rect(x0 + 3, yy - 4, x1 - 3, yy + lh - 6, hl_col)
        s.text(x0 + 44, yy + lh * 0.62, str(i + 1), f(MONO, size - 4), (150, 158, 175), anchor="rs")
        code_line(s, x0 + 64, yy + lh * 0.66, ln, size)
        yy += lh
    if circle and hl:
        a, b = min(hl), max(hl)
        cy0, cy1 = y + 94 + a * lh - 9, y + 94 + (b + 1) * lh - 1
        wmax = max(s.width(lines[i], f(MONO, size)) for i in hl)
        cx1 = min(x1 - 6, x0 + 64 + wmax + 30)
        for d in (0, 3):
            s.d.ellipse([k(x0 + 46 - d), k(cy0 - d), k(cx1 + d), k(cy1 + d)], outline=RED_NO, width=k(4))
    return y + h


def ep_tag(s, x, y, size=22):
    t = f"Code ya Wiki #{EP['num']:02d}"
    w_ = s.width(t, f(BOLD, size)) + 40
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + size * 2.1)], radius=k(size), fill=ORANGE)
    s.text(x + w_ / 2, y + size * 1.08, t, f(BOLD, size), WHITE_T, anchor="mm")


def out_box(s, x0, x1, y, label, value, good):
    card(s, (x0, y, x1, y + 130), r=16)
    s.rect(x0 + 2, y + 2, x0 + 12, y + 128, GREEN_OK if good else RED_NO)
    smallcaps(s, x0 + 36, y + 46, label, 14, GREEN_OK if good else RED_NO)
    s.text(x0 + 36, y + 100, value, f(MONO_B, fit(s, value, MONO_B, 30, x1 - x0 - 60)), NAVY)


if "SKIP_SLIDES" not in globals():
    # ── 1 · the puzzle ───────────────────────────────────────────────────────────────────────────
    s = page(1, "Spot the bug · Tafuta kosa")
    ep_tag(s, M, 165)
    s.text(M - 6, 330, "Kosa liko wapi?", f(BOLD, 96), NAVY)
    s.text(M - 4, 410, EP["question"], f(BOLD, fit(s, EP["question"], BOLD, 46, W - 2 * M)), ORANGE)
    s.para(M, 470, "Goal: " + EP["goal"], f(MED, 26), W - 2 * M, 38, GREY)
    editor(s, 560, EP["code"])
    horizon(s, 1)
    cover_footer(s, "Guess first, then swipe")
    finish(s)
    s.save(1)

    # ── 2 · hint ─────────────────────────────────────────────────────────────────────────────────
    s = page(2, "Dokezo · Hint", f"Code ya Wiki #{EP['num']:02d}")
    title2(s, "It runs.", "But it's wrong.", y=230, size=92)
    half = (W - 2 * M - 30) / 2
    out_box(s, M, M + half, 420, "Expected · Tulitarajia", EP["expected"], True)
    out_box(s, M + half + 30, W - M - 8, 420, "Got · Tulipata", EP["got"], False)
    smallcaps(s, M, 660, "Hint · Dokezo", 15, ORANGE)
    s.para(M, 720, EP["hint"], f(SEMI, 36), W - 2 * M, 52, NAVY)
    s.text(M, 960, "Comment your answer before you swipe.", f(MED, 26), GREY)
    horizon(s, 2)
    navy_note(s, "Rule", "Code that runs is not the same as code that's right.", "Kufanya kazi si kuwa sahihi", seed=2)
    finish(s)
    s.save(2)

    # ── 3 · the bug ──────────────────────────────────────────────────────────────────────────────
    s = page(3, "Jibu · The bug", f"Code ya Wiki #{EP['num']:02d}")
    title2(s, "Found it.", "Line " + ", ".join(str(i + 1) for i in EP["bug_lines"]) + ".", y=220, size=92)
    y = editor(s, 380, EP["code"], hl=EP["bug_lines"], circle=True)
    s.para(M, y + 70, EP["why"], f(MED, 29), W - 2 * M, 42, NAVY)
    horizon(s, 3)
    navy_note(s, "Why it happens", EP["lesson"], seed=3)
    finish(s)
    s.save(3)

    # ── 4 · the fix ──────────────────────────────────────────────────────────────────────────────
    s = page(4, "Imerekebishwa · The fix", f"Code ya Wiki #{EP['num']:02d}")
    title2(s, "The fix:", "small and safe.", y=220, size=92)
    y = editor(s, 380, EP["fixed"], hl=EP["fix_lines"], hl_col=HL_GREEN)
    out_box(s, M, W - M - 8, y + 50, "Now · Sasa", EP["expected"], True)
    horizon(s, 4)
    navy_note(s, "Test it", "Run it again with the same input and compare.", "Jaribu tena", seed=4)
    finish(s)
    s.save(4)

    # ── 5 · the lesson ───────────────────────────────────────────────────────────────────────────
    s = page(5, "Somo · The lesson", f"Code ya Wiki #{EP['num']:02d}")
    title2(s, "Never get", "caught again.", y=220, size=92)
    y = 450
    for a, b in EP["avoid"]:
        mark(s, M + 18, y - 10, True)
        s.text(M + 56, y, a, f(BOLD, fit(s, a, BOLD, 34, W - 2 * M - 60)), NAVY)
        s.para(M + 56, y + 46, b, f(REG, 27), W - 2 * M - 60, 38, GREY)
        y += 170
    horizon(s, 5)
    navy_note(s, "Remember", EP["lesson"], EP["sw"], seed=5)
    finish(s)
    s.save(5)

    # ── 6 · your turn ────────────────────────────────────────────────────────────────────────────
    s = page(TOTAL, "The end · Mwisho", f"Code ya Wiki #{EP['num']:02d}")
    closing(s, "Did you find it", "before slide 3?", [("Comment", "“nimepata” or “nimekwama”"), ("Share", "with the classmate who always debugs"),
                                                   ("Send me", "a bug for the next Code ya Wiki")])
    horizon(s, TOTAL)
    closing_footer(s)
    finish(s)
    s.save(TOTAL)
    print("ok")
