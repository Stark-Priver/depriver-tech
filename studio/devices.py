"""Shared drawing devices for the post bank (Nov 2026 → Mar 2027): phones, USSD screens, SMS, terminal windows, paper
documents, journey tracks, bars and flow boxes. Executed after editorial.py."""
import random

PALE = (232, 235, 242)
INK_SHADOW = (205, 211, 224)
TERM_BG = (14, 24, 44)


def feature_phone(s, x, y, w=300, lines=(), title=None, size=24, lh=34, keypad=True):
    """Old-style feature phone: navy body, small green-grey screen with mono text, keypad grid. Returns bottom y."""
    h = w * (2.05 if keypad else 1.2)
    s.rect(x + 10, y + 12, x + w + 10, y + h + 12, INK_SHADOW, r=w * 0.16)
    s.d.rounded_rectangle([k(x), k(y), k(x + w), k(y + h)], radius=k(w * 0.16), fill=NAVY)
    s.d.rounded_rectangle([k(x + w * 0.38), k(y + 18), k(x + w * 0.62), k(y + 26)], radius=k(4), fill=(60, 80, 120))
    sx0, sy0, sx1 = x + w * 0.09, y + 44, x + w * 0.91
    sh = 40 + lh * max(len(lines), 5) + (lh if title else 0)
    s.d.rounded_rectangle([k(sx0), k(sy0), k(sx1), k(sy0 + sh)], radius=k(10), fill=(214, 226, 210), outline=(40, 60, 90), width=k(3))
    yy = sy0 + 20 + lh * 0.75
    if title:
        s.text(sx0 + 16, yy, title, f(MONO_B, size), NAVY)
        yy += lh
    for ln in lines:
        s.text(sx0 + 16, yy, ln, f(MONO, fit(s, ln, MONO, size, sx1 - sx0 - 30, smallest=10)), NAVY)
        yy += lh
    if keypad:
        ky = sy0 + sh + 34
        kw, kh = (sx1 - sx0 - 24) / 3, 44 * w / 300
        keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#"]
        for i, key in enumerate(keys):
            cx0 = sx0 + (i % 3) * (kw + 12)
            cy0 = ky + (i // 3) * (kh + 12)
            if cy0 + kh > y + h - 16:
                break
            s.d.rounded_rectangle([k(cx0), k(cy0), k(cx0 + kw), k(cy0 + kh)], radius=k(kh / 2), fill=(38, 58, 96))
            s.text(cx0 + kw / 2, cy0 + kh / 2, key, f(SEMI, 20 * w / 300), WHITE_T, anchor="mm")
    return y + h


def smartphone(s, x, y, w=330, h=600, fill=(255, 255, 255)):
    """Smartphone outline (navy frame, notch). Returns the screen box (x0, y0, x1, y1)."""
    s.rect(x + 10, y + 12, x + w + 10, y + h + 12, INK_SHADOW, r=44)
    s.d.rounded_rectangle([k(x), k(y), k(x + w), k(y + h)], radius=k(44), fill=NAVY)
    s.d.rounded_rectangle([k(x + 12), k(y + 12), k(x + w - 12), k(y + h - 12)], radius=k(34), fill=fill)
    s.d.rounded_rectangle([k(x + w / 2 - 50), k(y + 22), k(x + w / 2 + 50), k(y + 42)], radius=k(10), fill=NAVY)
    return (x + 12, y + 56, x + w - 12, y + h - 24)


def sms(s, x, y, w, text, sender=None, size=23, lh=32, mine=False):
    """SMS bubble (grey for incoming, navy for sent). Returns bottom y."""
    fnt = f(REG if not mine else MED, size)
    n = wrap_lines(s, text, fnt, w - 48)
    h = 36 + lh * n + (30 if sender else 0)
    bg, fg = ((NAVY, WHITE_T) if mine else ((255, 255, 255), NAVY))
    s.rect(x + 5, y + 7, x + w + 5, y + h + 7, INK_SHADOW, r=18)
    s.d.rounded_rectangle([k(x), k(y), k(x + w), k(y + h)], radius=k(18), fill=bg, outline=NAVY, width=k(2))
    yy = y + 14
    if sender:
        smallcaps(s, x + 24, yy + 18, sender, 12, ORANGE)
        yy += 30
    s.para(x + 24, yy + lh * 0.72, text, fnt, w - 48, lh, fg)
    return y + h


def terminal(s, y, lines, title="bash", size=25, lh=40, x0=M, x1=None, prompt="$ "):
    """Dark terminal window. Lines starting with '$' are commands (orange prompt), '#' comments, others output."""
    x1 = x1 or W - M - 8
    h = 64 + 26 + lh * len(lines) + 16
    s.rect(x0 + 10, y + 12, x1 + 10, y + h + 12, INK_SHADOW, r=20)
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + h)], radius=k(20), fill=TERM_BG, outline=NAVY, width=k(3))
    for i, c in enumerate([RED_NO, (240, 180, 60), GREEN_OK]):
        s.d.ellipse([k(x0 + 26 + i * 30), k(y + 22), k(x0 + 46 + i * 30), k(y + 42)], fill=c)
    s.text((x0 + x1) / 2, y + 40, title, f(MONO, 20), SOFT, anchor="ms")
    hairline(s, x0 + 3, x1 - 3, y + 62, (40, 56, 90))
    yy = y + 64 + 26 + lh * 0.6
    for ln in lines:
        if ln.startswith("$"):
            s.text(x0 + 28, yy, prompt.strip(), f(MONO_B, size), ORANGE)
            s.text(x0 + 28 + s.width(prompt, f(MONO_B, size)), yy, ln[1:].strip(), f(MONO_B, size), WHITE_T)
        elif ln.startswith("#"):
            s.text(x0 + 28, yy, ln, f(MONO, size), (120, 136, 170))
        elif ln.startswith("!"):
            s.text(x0 + 28, yy, ln[1:].strip(), f(MONO, size), (255, 120, 110))
        else:
            s.text(x0 + 28, yy, ln, f(MONO, size), (190, 215, 200))
        yy += lh
    return y + h


def paper_doc(s, box, title=None, rule=False, fold=True):
    """Sheet of paper: white, navy outline, folded top-right corner, optional ruled lines. Returns content top y."""
    x0, y0, x1, y1 = box
    s.rect(x0 + 10, y0 + 12, x1 + 10, y1 + 12, INK_SHADOW, r=6)
    c = 46 if fold else 0
    pts = [(x0, y0), (x1 - c, y0), (x1, y0 + c), (x1, y1), (x0, y1)]
    s.d.polygon([(k(a), k(b)) for a, b in pts], fill=(255, 255, 255))
    s.d.line([(k(a), k(b)) for a, b in pts + [pts[0]]], fill=NAVY, width=k(3))
    if fold:
        s.d.polygon([(k(x1 - c), k(y0)), (k(x1 - c), k(y0 + c)), (k(x1), k(y0 + c))], fill=PALE, outline=NAVY)
        s.d.line([(k(x1 - c), k(y0)), (k(x1 - c), k(y0 + c)), (k(x1), k(y0 + c))], fill=NAVY, width=k(3))
    if rule:
        for yy in range(int(y0 + 120), int(y1 - 20), 44):
            s.rect(x0 + 20, yy, x1 - 20, yy + 1.5, (214, 222, 238))
        s.rect(x0 + 80, y0 + 3, x0 + 81.5, y1 - 3, (240, 170, 160))
    ty = y0 + 70
    if title:
        s.text(x0 + 36, ty, title, f(BOLD, fit(s, title, BOLD, 32, x1 - x0 - 120)), NAVY)
    return ty + 30


def red_ring(s, x0, y0, x1, y1, w=4):
    for d in (0, 3):
        s.d.ellipse([k(x0 - d), k(y0 - d), k(x1 + d), k(y1 + d)], outline=RED_NO, width=k(w))


def strike(s, x0, x1, y, col=RED_NO, w=4):
    s.d.line([k(x0), k(y + 2), k(x1), k(y - 3)], fill=col, width=k(w))


def red_note(s, x, y, text, size=40):
    """Handwritten red-pen note."""
    s.text(x, y, text, f(SIG, size), RED_NO)


def track(s, n, total, y=150, labels=None):
    """Journey progress track under the header: numbered stops, the current one filled orange."""
    x0, x1 = M + 20, W - M - 20
    gap = (x1 - x0) / max(1, total - 1)
    s.rect(x0, y - 2, x1, y + 2, RULE)
    s.rect(x0, y - 2, x0 + gap * (n - 1), y + 2, ORANGE)
    for i in range(total):
        cx = x0 + i * gap
        done, cur = i < n - 1, i == n - 1
        r = 20 if cur else 14
        s.d.ellipse([k(cx - r), k(y - r), k(cx + r), k(y + r)], fill=ORANGE if cur else (NAVY if done else (255, 255, 255)),
                    outline=NAVY, width=k(3))
        s.text(cx, y, str(i + 1), f(BOLD, 18 if cur else 14), WHITE_T if (cur or done) else NAVY, anchor="mm")


def stamp(s, cx, cy, text, col=RED_NO, angle=-12, size=64, box=True):
    """Rubber stamp: bordered word, rotated, slightly faded, pasted centred on (cx, cy)."""
    fnt = f(BOLD, size)
    tw = s.d.textlength(text, font=fnt)
    pad = k(size * 0.35)
    lw, lh = int(tw + 2 * pad), int(k(size) * 1.5)
    layer = Image.new("RGBA", (lw, lh), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    rgba = col + (225,)
    if box:
        d.rounded_rectangle([k(4), k(4), lw - k(4), lh - k(4)], radius=k(12), outline=rgba, width=k(6))
    d.text((lw / 2, lh / 2), text, font=fnt, fill=rgba, anchor="mm")
    layer = layer.rotate(angle, expand=True, resample=Image.BICUBIC)
    s.im.paste(layer, (int(k(cx) - layer.width / 2), int(k(cy) - layer.height / 2)), layer)


def bars(s, items, y, x0=M, x1=None, gap=104, h=30, size=28):
    """Horizontal bars: (label, value 0..1, colour or None). Returns bottom y."""
    x1 = x1 or W - M
    for lab, v, col in items:
        s.text(x0, y, lab, f(SEMI, fit(s, lab, SEMI, size, x1 - x0)), NAVY)
        s.d.rounded_rectangle([k(x0), k(y + 18), k(x1), k(y + 18 + h)], radius=k(h / 2), fill=PALE)
        s.d.rounded_rectangle([k(x0), k(y + 18), k(x0 + max(h, (x1 - x0) * v)), k(y + 18 + h)], radius=k(h / 2), fill=col or ORANGE)
        y += gap
    return y


def flow(s, items, y, x0=M, x1=None, h=88, gap=40, size=28, colors=None):
    """Vertical flow: boxes joined by down arrows. items: (title, sub). Returns bottom y."""
    x1 = x1 or W - M - 8
    for i, (a, b) in enumerate(items):
        col = (colors or [NAVY, ORANGE])[i % len(colors or [NAVY, ORANGE])]
        s.rect(x0 + 6, y + 8, x1 + 6, y + h + 8, INK_SHADOW, r=16)
        s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + h)], radius=k(16), fill=(255, 255, 255), outline=NAVY, width=k(3))
        s.d.rounded_rectangle([k(x0), k(y), k(x0 + 70), k(y + h)], radius=k(16), fill=col)
        s.rect(x0 + 50, y, x0 + 70, y + h, col)
        s.text(x0 + 35, y + h / 2, str(i + 1), f(BOLD, 28), WHITE_T, anchor="mm")
        if b:
            s.text(x0 + 96, y + h / 2 - 6, a, f(BOLD, fit(s, a, BOLD, size, x1 - x0 - 120)), NAVY)
            s.text(x0 + 96, y + h / 2 + 28, b, f(REG, fit(s, b, REG, size - 6, x1 - x0 - 120)), GREY)
        else:
            s.text(x0 + 96, y + h / 2 + 10, a, f(BOLD, fit(s, a, BOLD, size, x1 - x0 - 120)), NAVY)
        if i < len(items) - 1:
            cx = (x0 + x1) / 2
            s.d.line([k(cx), k(y + h + 6), k(cx), k(y + h + gap - 6)], fill=ORANGE, width=k(4))
            s.d.polygon([(k(cx - 10), k(y + h + gap - 14)), (k(cx + 10), k(y + h + gap - 14)), (k(cx), k(y + h + gap - 2))], fill=ORANGE)
        y += h + gap
    return y - gap


def tick_list(s, items, y, x=M, size=31, sub=27, gap=40, ok=True, maxw=None):
    """Tick (or cross) rows: (bold line, grey line) or plain strings. Returns bottom y."""
    maxw = maxw or W - M - x
    for it in items:
        a, b = it if isinstance(it, tuple) else (it, None)
        mark(s, x + 18, y - 10, ok)
        s.text(x + 56, y, a, f(BOLD, fit(s, a, BOLD, size, maxw - 60)), NAVY)
        if b:
            y = s.para(x + 56, y + 44, b, f(REG, sub), maxw - 60, sub * 1.4, GREY) + gap
        else:
            y += 60
    return y


def chip_row(s, items, x, y, size=22, maxx=None, fill=(255, 255, 255), fg=None):
    maxx = maxx or W - M
    for it in items:
        ww = s.width(it, f(SEMI, size)) + 34
        if x + ww > maxx:
            x, y = M, y + size * 2.6
        s.d.rounded_rectangle([k(x), k(y), k(x + ww), k(y + size * 2)], radius=k(size), fill=fill, outline=NAVY, width=k(2.5))
        s.text(x + ww / 2, y + size, it, f(SEMI, size), fg or NAVY, anchor="mm")
        x += ww + 10
    return y + size * 2


def label_box(s, box, label, text, col=ORANGE, size=27, lh=None):
    """Card with an orange edge, small-caps label and wrapped text."""
    x0, y0, x1, y1 = box
    card(s, box, r=16)
    s.rect(x0 + 2, y0 + 2, x0 + 12, y1 - 2, col)
    smallcaps(s, x0 + 36, y0 + 48, label, 14, col)
    s.para(x0 + 36, y0 + 96, text, f(REG, size), x1 - x0 - 70, lh or size * 1.45, NAVY)


def para_h(s, text, size, maxw, lh, font=REG):
    return wrap_lines(s, text, f(font, size), maxw) * lh


CODE_KW = {"def", "return", "for", "in", "if", "else", "elif", "while", "print", "range", "len", "const", "let", "function",
           "UPDATE", "SET", "WHERE", "SELECT", "FROM", "AND", "OR", "INSERT", "INTO", "VALUES", "or", "and", "not", "echo",
           "await", "async", "true", "false", "True", "False", "null", "None", "new", "import", "from", "class", "try", "except",
           "GROUP", "BY", "ORDER", "JOIN", "ON", "COUNT", "SUM", "AS", "DESC", "LIMIT", "fetch", "then"}


def code_text(s, x, y, line, size):
    """One line of code with simple colouring: keywords, strings, numbers, comments."""
    import re as _re
    fnt, fb = f(MONO, size), f(MONO_B, size)
    for tok in _re.findall(r"#.*$|--.*$|//.*$|\"[^\"]*\"|'[^']*'|\$?\w+|\s+|.", line):
        if tok.startswith(("#", "//", "--")):
            col, ft = GREY, fnt
        elif tok[0] in "\"'":
            col, ft = (22, 128, 70), fnt
        elif tok.isdigit():
            col, ft = (37, 99, 235), fnt
        elif tok in CODE_KW:
            col, ft = ORANGE, fb
        else:
            col, ft = NAVY, fnt
        s.text(x, y, tok, ft, col)
        x += s.width(tok, ft)


def code_window(s, y, lines, file="app.py", lang="Python", size=25, lh=42, x0=M, x1=None, hl=(), hl_col=(219, 242, 227)):
    """Light code editor window. Returns bottom y."""
    x1 = x1 or W - M - 8
    h = 64 + 26 + lh * len(lines) + 16
    s.rect(x0 + 10, y + 12, x1 + 10, y + h + 12, INK_SHADOW, r=20)
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + h)], radius=k(20), fill=(255, 255, 255), outline=NAVY, width=k(3))
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + 64)], radius=k(20), fill=NAVY)
    s.rect(x0, y + 40, x1, y + 64, NAVY)
    for i, c in enumerate([RED_NO, (240, 180, 60), GREEN_OK]):
        s.d.ellipse([k(x0 + 26 + i * 30), k(y + 22), k(x0 + 46 + i * 30), k(y + 42)], fill=c)
    s.text(x0 + 130, y + 40, file, f(MONO, 21), SOFT)
    s.text(x1 - 24, y + 40, lang, f(SEMI, 19), ORANGE, anchor="rs")
    yy = y + 64 + 26
    for i, ln in enumerate(lines):
        if i in hl:
            s.rect(x0 + 3, yy - 4, x1 - 3, yy + lh - 6, hl_col)
        s.text(x0 + 44, yy + lh * 0.62, str(i + 1), f(MONO, size - 4), (150, 158, 175), anchor="rs")
        code_text(s, x0 + 64, yy + lh * 0.66, ln, size)
        yy += lh
    return y + h


def table(s, x0, y, cols, rows, widths, size=25, rh=58, head_fill=NAVY, hl_rows=()):
    """Simple ruled table with a navy header row. Returns bottom y."""
    x1 = x0 + sum(widths)
    s.rect(x0 + 8, y + 10, x1 + 8, y + rh * (len(rows) + 1) + 10, INK_SHADOW, r=12)
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + rh * (len(rows) + 1))], radius=k(12), fill=(255, 255, 255), outline=NAVY, width=k(3))
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + rh)], radius=k(12), fill=head_fill)
    s.rect(x0, y + rh - 14, x1, y + rh, head_fill)
    x = x0
    for c, wd in zip(cols, widths):
        s.text(x + 18, y + rh * 0.64, c, f(BOLD, size - 2), WHITE_T)
        x += wd
    for r_i, row in enumerate(rows):
        yy = y + rh * (r_i + 1)
        if r_i in hl_rows:
            s.rect(x0 + 3, yy, x1 - 3, yy + rh, (253, 236, 230))
        if r_i:
            s.rect(x0 + 3, yy, x1 - 3, yy + 1.5, RULE)
        x = x0
        for c_i, (cell, wd) in enumerate(zip(row, widths)):
            fnt = f(MONO if c_i else SEMI, size) if isinstance(cell, str) and cell[:1].isdigit() else f(SEMI if c_i == 0 else REG, size)
            s.text(x + 18, yy + rh * 0.64, str(cell), f(SEMI if c_i == 0 else MED, fit(s, str(cell), MED, size, wd - 30)), NAVY)
            x += wd
    return y + rh * (len(rows) + 1)


def tick_fill(s, items, y0, y1=990, size=31, sub=27, ok=True, x=M, maxw=None, max_gap=90):
    """tick_list spread evenly between y0 and y1 (extra space shared out, capped at max_gap per row)."""
    maxw = maxw or W - M - x
    hs = []
    for it in items:
        a, b = it if isinstance(it, tuple) else (it, None)
        hs.append(44 + (wrap_lines(s, b, f(REG, sub), maxw - 60) * sub * 1.4 if b else 0))
    gap = min(max_gap, max(24, (y1 - y0 - sum(hs)) / max(1, len(items) - 1)))
    y = y0
    for it, h in zip(items, hs):
        a, b = it if isinstance(it, tuple) else (it, None)
        mark(s, x + 18, y - 10, ok if not isinstance(ok, (list, tuple)) else ok[items.index(it)])
        s.text(x + 56, y, a, f(BOLD, fit(s, a, BOLD, size, maxw - 60)), NAVY)
        if b:
            s.para(x + 56, y + 44, b, f(REG, sub), maxw - 60, sub * 1.4, GREY)
        y += h + gap
    return y - gap
