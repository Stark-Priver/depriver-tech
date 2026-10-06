"""Shared layout for the editorial carousels (page frame, navy horizon, notes, titles, cards, closing slide, posters).
Executed after base.py and kit.py by studio/<slug>/make.py, which sets TOTAL and POST_URL first."""
M = 72
RULE = (200, 206, 218)
WHITE_T = (255, 255, 255)
SOFT = (190, 202, 226)
BASE = 1060
MONO, MONO_B = "LiberationMono-Regular.ttf", "LiberationMono-Bold.ttf"
GREEN_OK = (34, 160, 90)
RED_NO = (196, 52, 52)


def page(n, label_left, label_right="depriver.tech"):
    s = Slide()
    panorama_paper(s, n, TOTAL)
    smallcaps(s, M, 96, label_left, 17, ORANGE)
    s.text(W - M, 96, label_right, f(SEMI, 20), NAVY, anchor="rs")
    hairline(s, M, W - M, 118, RULE)
    return s


def horizon(s, n):
    navy_wave(s, n, BASE)
    seam_nodes(s, n, TOTAL, BASE)


def arrow(s, x, y, color=WHITE_T, w=3.4, size=12):
    s.d.line([k(x - size - 6), k(y), k(x + size - 2), k(y)], fill=color, width=k(w))
    s.d.line([k(x), k(y - size + 2), k(x + size - 2), k(y), k(x), k(y + size - 2)], fill=color, width=k(w), joint="curve")


def navy_note(s, label, line, sw=None, seed=0):
    smallcaps(s, M, BASE + 74, label, 16, ORANGE)
    s.text(M, BASE + 130, line, f(SEMI, fit(s, line, SEMI, 31, W - 2 * M)), WHITE_T)
    if sw:
        sws = fit(s, sw, SIG, 54, W - 2 * M - 40)
        s.text(M, BASE + 214, sw, f(SIG, sws), ORANGE)
        swash(s, M + 6, M + min(s.width(sw, f(SIG, sws)) * 0.9, 620), BASE + 238, ORANGE, 5, seed=seed)


def title2(s, a, b, y=230, size=84):
    s.text(M - 4, y, a, f(BOLD, fit(s, a, BOLD, size, W - 2 * M)), NAVY)
    s.text(M - 4, y + size * 1.08, b, f(BOLD, fit(s, b, BOLD, size, W - 2 * M)), ORANGE)


def card(s, box, r=18, fill=(255, 255, 255)):
    """Print-style card: navy outline, offset ink block behind."""
    x0, y0, x1, y1 = box
    s.rect(x0 + 8, y0 + 10, x1 + 8, y1 + 10, (205, 211, 224), r=r)
    s.d.rounded_rectangle([k(x0), k(y0), k(x1), k(y1)], radius=k(r), fill=fill, outline=NAVY, width=k(3))


def mark(s, x, y, ok, r=17):
    """Round tick (ok) or cross badge centred at x, y."""
    s.d.ellipse([k(x - r), k(y - r), k(x + r), k(y + r)], fill=GREEN_OK if ok else RED_NO)
    if ok:
        s.d.line([k(x - 8), k(y), k(x - 2), k(y + 7), k(x + 9), k(y - 7)], fill=WHITE_T, width=k(4), joint="curve")
    else:
        s.d.line([k(x - 7), k(y - 7), k(x + 7), k(y + 7)], fill=WHITE_T, width=k(4))
        s.d.line([k(x + 7), k(y - 7), k(x - 7), k(y + 7)], fill=WHITE_T, width=k(4))


def numbered(s, items, y, x=M, maxw=None, gap=104, ts=31, bs=23):
    """Big orange numbers, bold line, grey line, hairlines between."""
    maxw = maxw or W - M - x
    for j, (a, b) in enumerate(items):
        s.text(x, y, f"{j + 1:02d}", f(BOLD, 30), ORANGE)
        s.text(x + 70, y, a, f(BOLD, fit(s, a, BOLD, ts, maxw - 70)), NAVY)
        s.text(x + 70, y + 38, b, f(REG, fit(s, b, REG, bs, maxw - 70)), GREY)
        if j < len(items) - 1:
            hairline(s, x + 70, x + maxw, y + 62, RULE)
        y += gap
    return y


def cover_footer(s, swipe):
    s.text(M, 1262, swipe, f(SEMI, 30), WHITE_T)
    arrow(s, M + s.width(swipe, f(SEMI, 30)) + 34, 1251)
    s.text(W - M, 1262, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")


def closing(s, q1, q2, rows, seed=10):
    s.text(M - 6, 290, "Your turn.", f(BOLD, 112), NAVY)
    s.text(M, 380, q1, f(BOLD, 50), ORANGE)
    s.text(M, 444, q2, f(BOLD, 50), ORANGE)
    s.text(M, 540, "Niambie kwenye comments", f(SIG, 52), ORANGE)
    swash(s, M + 6, M + 440, 566, ORANGE, 5, seed=seed)
    y = 680
    for j, (a, b) in enumerate(rows):
        s.text(M, y, f"{j + 1:02d}", f(BOLD, 22), ORANGE)
        s.text(M + 56, y, a, f(BOLD, 36), NAVY)
        s.text(M + 56, y + 40, b, f(REG, 24), GREY)
        y += 108


def closing_footer(s):
    smallcaps(s, M, BASE + 72, "Read the full post · Soma zaidi", 17, SOFT)
    s.text(M, BASE + 132, POST_URL, f(BOLD, fit(s, POST_URL, BOLD, 40, W - 2 * M)), WHITE_T)
    hairline(s, M, W - M, BASE + 162, (38, 60, 100))
    s.text(M, BASE + 224, "Link in bio", f(SEMI, 24), SOFT)
    s.text(W - M, BASE + 224, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")


def chat(s, x, y, w, text, who, mine=True, size=24, lh=34, tag=None, tag_ok=True):
    """Chat bubble (mine = navy on the right look, else white). Returns bottom y."""
    fnt = f(MED if mine else REG, size)
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if s.width(trial, fnt) > w - 56 and line:
            lines.append(line)
            line = word
        else:
            line = trial
    lines.append(line)
    h = 64 + lh * len(lines)
    bg, fg = (NAVY, WHITE_T) if mine else ((255, 255, 255), NAVY)
    s.rect(x + 6, y + 8, x + w + 6, y + h + 8, (205, 211, 224), r=22)
    s.d.rounded_rectangle([k(x), k(y), k(x + w), k(y + h)], radius=k(22), fill=bg, outline=NAVY, width=k(2.5))
    smallcaps(s, x + 28, y + 34, who, 13, ORANGE if mine else GREY)
    yy = y + 34 + lh
    for ln in lines:
        s.text(x + 28, yy, ln, fnt, fg)
        yy += lh
    if tag:
        sticker(s, x + w - 60, y - 6, tag, angle=6 if tag_ok else -6, size=17, bg=GREEN_OK if tag_ok else RED_NO)
    return y + h


# ── posters (feed 1080x1350 and status 1080x1920) ─────────────────────────────────────────────────
def poster_start(height, top, label):
    global H, _TERRAIN
    H, _TERRAIN = height, None
    s = Slide()
    paper(s)
    smallcaps(s, M, top, label, 17, ORANGE)
    s.text(W - M, top, "depriver.tech", f(SEMI, 21), NAVY, anchor="rs")
    hairline(s, M, W - M, top + 22, RULE)
    return s


def poster_end(s, blk, kicker, name):
    s.rect(0, blk, W, H, NAVY)
    s.rect(0, blk - 5, W, blk, ORANGE)
    smallcaps(s, M, blk + 86, kicker, 17, SOFT)
    s.text(M, blk + 150, POST_URL, f(BOLD, fit(s, POST_URL, BOLD, 44, W - 2 * M)), WHITE_T)
    hairline(s, M, W - M, blk + 182, (38, 60, 100))
    s.text(M, blk + 236, "Link in bio", f(SEMI, 24), SOFT)
    s.text(W - M, blk + 236, "@_depriver", f(SEMI, 22), WHITE_T, anchor="rs")
    finish(s)
    s.im.save(f"{OUT}{name}.jpg", quality=95)
