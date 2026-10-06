"""Njia za Tech (tech career paths): shared 8-slide template. Each episode lives in studio/njia-za-tech-<role>/make.py,
sets EP and execs this file. The device is a staff ID card for the role. Slides: cover (ID card), what they do (with an
everyday analogy), a day in the job, the tools, is it for you, start today, where they work in Tanzania, your turn.
No salary numbers: we never invent them.
EP keys: num, slug, role, role_sw, initials, sw, cover_line, one_line, what, analogy, duties [3], day [(time, task)], tools [(group, [items])],
like [..], not_for [..], steps [(title, body)], first_project, where [..], where_note, question."""
TOTAL = 8
POST_URL = f"depriver.tech/blog/{EP['slug']}"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing


def series_tag(s, x, y, size=22):
    t = f"Njia za Tech #{EP['num']:02d}"
    w_ = s.width(t, f(BOLD, size)) + 40
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + size * 2.1)], radius=k(size), fill=ORANGE)
    s.text(x + w_ / 2, y + size * 1.08, t, f(BOLD, size), WHITE_T, anchor="mm")
    return x + w_


def id_card(s, x, y, w=420):
    """Staff ID on a lanyard: navy header, initials badge, name/role rows, barcode. Everything scales with w."""
    q = w / 420
    h = w * 1.42
    cx = x + w / 2
    s.d.line([k(cx - 70 * q), k(y - 150 * q), k(cx - 18 * q), k(y + 6)], fill=ORANGE, width=k(16 * q))
    s.d.line([k(cx + 70 * q), k(y - 150 * q), k(cx + 18 * q), k(y + 6)], fill=ORANGE, width=k(16 * q))
    s.d.rounded_rectangle([k(cx - 34 * q), k(y - 18 * q), k(cx + 34 * q), k(y + 22 * q)], radius=k(8 * q), fill=(150, 158, 175), outline=NAVY, width=k(3))
    card(s, (x, y, x + w, y + h), r=26 * q)
    s.d.rounded_rectangle([k(x), k(y), k(x + w), k(y + 120 * q)], radius=k(26 * q), fill=NAVY)
    s.rect(x, y + 90 * q, x + w, y + 120 * q, NAVY)
    s.d.rounded_rectangle([k(cx - 40 * q), k(y + 26 * q), k(cx + 40 * q), k(y + 42 * q)], radius=k(8 * q), fill=(255, 255, 255))
    lab = "Tech Tanzania · Staff"
    lw = smallcaps(s, -2000, 0, lab, 14 * q, SOFT)
    smallcaps(s, cx - lw / 2, y + 90 * q, lab, 14 * q, SOFT)
    r = w * 0.2
    top = y + 150 * q
    s.d.ellipse([k(cx - r), k(top), k(cx + r), k(top + 2 * r)], fill=ORANGE, outline=NAVY, width=k(4 * q))
    s.text(cx, top + r, EP["initials"], f(BOLD, r * 0.8), WHITE_T, anchor="mm")
    yy = top + 2 * r + 56 * q
    s.text(cx, yy, "Jina: Wewe", f(SEMI, 22 * q), GREY, anchor="ms")
    s.text(cx, yy + 50 * q, EP["role"], f(BOLD, fit(s, EP["role"], BOLD, 34 * q, w - 50 * q)), NAVY, anchor="ms")
    s.text(cx, yy + 88 * q, EP["role_sw"], f(MED, fit(s, EP["role_sw"], MED, 22 * q, w - 50 * q, smallest=8)), ORANGE, anchor="ms")
    bx, by = x + 46 * q, y + h - 74 * q
    import random
    rnd = random.Random(EP["num"])
    while bx < x + w - 50 * q:
        bw = rnd.choice([3, 3, 5, 8]) * q
        s.rect(bx, by, bx + bw, by + 44 * q, NAVY)
        bx += bw + rnd.choice([4, 5, 7]) * q
    return y + h


if "SKIP_SLIDES" not in globals():
    # ── 1 · cover ────────────────────────────────────────────────────────────────────────────────
    s = page(1, "Tech careers, explained · Njia za Tech")
    series_tag(s, M, 170)
    words = EP["role"].split()
    head = [" ".join(words[:-1]), words[-1]] if len(words) > 1 else [EP["role"], ""]
    s.text(M - 6, 345, head[0], f(BOLD, fit(s, head[0], BOLD, 96, 520)), NAVY)
    s.text(M - 6, 448, head[1], f(BOLD, fit(s, head[1], BOLD, 96, 520)), ORANGE)
    s.text(M, 530, EP["sw"], f(SIG, fit(s, EP["sw"], SIG, 50, 500)), NAVY)
    swash(s, M + 8, M + min(440, s.width(EP["sw"], f(SIG, fit(s, EP["sw"], SIG, 50, 500))) * 0.9), 554, ORANGE, 5)
    s.para(M, 640, EP["cover_line"], f(REG, 27), 470, 40, GREY)
    smallcaps(s, M, 790, "Inside", 15, ORANGE)
    x, y = M, 812
    for lab in ["What they do", "A day", "Tools", "Start free", "Where in TZ"]:
        ww = s.width(lab, f(SEMI, 21)) + 32
        if x + ww > 560:
            x, y = M, y + 56
        s.d.rounded_rectangle([k(x), k(y), k(x + ww), k(y + 42)], radius=k(21), fill=(255, 255, 255), outline=NAVY, width=k(2.5))
        s.text(x + ww / 2, y + 22, lab, f(SEMI, 21), NAVY, anchor="mm")
        x += ww + 10
    s.text(M, y + 110, "No made-up salaries. Just the honest picture.", f(SEMI, 23), GREY)
    id_card(s, 600, 290, 400)
    horizon(s, 1)
    cover_footer(s, "Swipe, is this you?")
    finish(s)
    s.save(1)

    # ── 2 · what they do ─────────────────────────────────────────────────────────────────────────
    s = page(2, "Kazi yao · What they do", EP["role"])
    title2(s, "What they", "actually do.", y=220, size=88)
    y = s.para(M, 420, EP["what"], f(MED, 30), W - 2 * M, 44, NAVY) + 30
    for a in EP["duties"]:
        mark(s, M + 18, y - 10, True)
        s.text(M + 56, y, a, f(SEMI, fit(s, a, SEMI, 28, W - 2 * M - 60)), NAVY)
        y += 52
    box_h = 96 + wrap_lines(s, EP["analogy"], f(REG, 27), W - 2 * M - 80) * 40
    y += 10
    card(s, (M, y, W - M - 8, y + box_h), r=18)
    s.rect(M + 2, y + 2, M + 12, y + box_h - 2, ORANGE)
    smallcaps(s, M + 40, y + 50, "Kwa mfano wa maisha · Like this", 14, ORANGE)
    s.para(M + 40, y + 98, EP["analogy"], f(REG, 27), W - 2 * M - 80, 40, NAVY)
    horizon(s, 2)
    navy_note(s, "In one line", EP["one_line"], EP["sw"], seed=2)
    finish(s)
    s.save(2)

    # ── 3 · a day ────────────────────────────────────────────────────────────────────────────────
    s = page(3, "Siku moja · A day in the job", EP["role"])
    title2(s, "A normal", "working day.", y=220, size=88)
    y, n = 430, len(EP["day"])
    gap = min(132, 560 / max(1, n - 1)) if n > 1 else 0
    s.d.line([k(M + 112), k(y - 20), k(M + 112), k(y + gap * (n - 1) + 10)], fill=RULE, width=k(4))
    for i, (t_, task) in enumerate(EP["day"]):
        yy = y + i * gap
        s.text(M, yy, t_, f(BOLD, 26), ORANGE)
        s.d.ellipse([k(M + 100), k(yy - 22), k(M + 124), k(yy + 2)], fill=NAVY if i % 2 else ORANGE, outline=NAVY, width=k(3))
        s.para(M + 150, yy, task, f(SEMI, 28), W - 2 * M - 150, 38, NAVY)
    horizon(s, 3)
    navy_note(s, "Truth", "Every day is different, but this is the rhythm.", "Kila siku ni tofauti", seed=3)
    finish(s)
    s.save(3)

    # ── 4 · tools ────────────────────────────────────────────────────────────────────────────────
    s = page(4, "Zana · The tools", EP["role"])
    title2(s, "The tools", "on their desk.", y=220, size=88)
    y = 430
    for grp, items in EP["tools"]:
        smallcaps(s, M, y, grp, 15, ORANGE)
        x, y = M, y + 24
        for it in items:
            ww = s.width(it, f(SEMI, 25)) + 40
            if x + ww > W - M:
                x, y = M, y + 66
            s.d.rounded_rectangle([k(x + 4), k(y + 6), k(x + ww + 4), k(y + 56)], radius=k(25), fill=(205, 211, 224))
            s.d.rounded_rectangle([k(x), k(y), k(x + ww), k(y + 50)], radius=k(25), fill=(255, 255, 255), outline=NAVY, width=k(2.5))
            s.text(x + ww / 2, y + 26, it, f(SEMI, 25), NAVY, anchor="mm")
            x += ww + 12
        y += 120
    horizon(s, 4)
    navy_note(s, "Don't panic", "Nobody learns all of these at once. Start with the first one.", "Moja baada ya nyingine", seed=4)
    finish(s)
    s.save(4)

    # ── 5 · is it for you ────────────────────────────────────────────────────────────────────────
    s = page(5, "Ni yako? · Is it for you?", EP["role"])
    title2(s, "Is this path", "for you?", y=220, size=88)
    smallcaps(s, M, 420, "You'll enjoy it if", 15, GREEN_OK)
    y = 480
    for a in EP["like"]:
        mark(s, M + 18, y - 10, True)
        y = s.para(M + 56, y, a, f(SEMI, 29), W - 2 * M - 60, 40, NAVY) + 26
    smallcaps(s, M, y + 20, "Maybe not if", 15, RED_NO)
    y += 80
    for a in EP["not_for"]:
        mark(s, M + 18, y - 10, False)
        y = s.para(M + 56, y, a, f(SEMI, 29), W - 2 * M - 60, 40, NAVY) + 26
    horizon(s, 5)
    navy_note(s, "Remember", "You can try a path for a month before you decide.", "Jaribu kwanza", seed=5)
    finish(s)
    s.save(5)

    # ── 6 · start today ──────────────────────────────────────────────────────────────────────────
    s = page(6, "Anza leo · Start today", EP["role"])
    title2(s, "How to start,", "for free.", y=220, size=88)
    numbered(s, EP["steps"], 430, gap=112, ts=31, bs=23)
    horizon(s, 6)
    navy_note(s, "First project", EP["first_project"], seed=6)
    finish(s)
    s.save(6)

    # ── 7 · where in Tanzania ────────────────────────────────────────────────────────────────────
    s = page(7, "Wapi Tanzania · Where they work", EP["role"])
    title2(s, "Who hires them", "in Tanzania.", y=220, size=86)
    y = 430
    cw = (W - 2 * M - 24) / 2
    for i, wh in enumerate(EP["where"]):
        x0 = M + (i % 2) * (cw + 24)
        yy = y + (i // 2) * 128
        card(s, (x0, yy, x0 + cw - 8, yy + 104), r=16)
        s.d.ellipse([k(x0 + 26), k(yy + 38), k(x0 + 54), k(yy + 66)], fill=ORANGE if i % 2 == 0 else NAVY)
        s.para(x0 + 74, yy + 62 - (17 if wrap_lines(s, wh, f(SEMI, 26), cw - 110) > 1 else 0), wh, f(SEMI, 26), cw - 110, 34, NAVY)
    horizon(s, 7)
    navy_note(s, "Pay?", EP["where_note"], "Uliza watu halisi", seed=7)
    finish(s)
    s.save(7)

    # ── 8 · closing ──────────────────────────────────────────────────────────────────────────────
    s = page(TOTAL, "The end · Mwisho", EP["role"])
    closing(s, EP["question"][0], EP["question"][1], [("Save", "for when you choose your path"), ("Share", "with a friend who'd love this job"),
                                                    ("Comment", "which path I should explain next")])
    id_card(s, 720, 600, 290)
    horizon(s, TOTAL)
    closing_footer(s)
    finish(s)
    s.save(TOTAL)
    print("ok")
