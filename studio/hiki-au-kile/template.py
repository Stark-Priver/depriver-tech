"""Hiki au Kile (this or that): shared 7-slide template. Each episode lives in studio/hiki-au-kile-NN/make.py, sets EP
and execs this file. The device is two versus cards with a VS badge; my pick gets a "Chaguo langu" sticker (or none
when the honest answer is "it depends"). Slides: cover with the five match-ups, five rounds, your turn.
EP keys: num, theme, theme_sw, rounds [dict(a, a_pts[2], b, b_pts[2], pick 0|1|None, reason, note, sw)]."""
TOTAL = 7
POST_URL = f"depriver.tech/blog/hiki-au-kile-{EP['num']:02d}"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing


def ep_tag(s, x, y, size=22):
    t = f"Hiki au Kile #{EP['num']:02d}"
    w_ = s.width(t, f(BOLD, size)) + 40
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + size * 2.1)], radius=k(size), fill=ORANGE)
    s.text(x + w_ / 2, y + size * 1.08, t, f(BOLD, size), WHITE_T, anchor="mm")


def vs_badge(s, cx, cy, r=44):
    s.d.ellipse([k(cx - r + 4), k(cy - r + 6), k(cx + r + 4), k(cy + r + 6)], fill=(205, 211, 224))
    s.d.ellipse([k(cx - r), k(cy - r), k(cx + r), k(cy + r)], fill=ORANGE, outline=NAVY, width=k(4))
    s.text(cx, cy, "VS", f(BOLD, r * 0.72), WHITE_T, anchor="mm")


if "SKIP_SLIDES" not in globals():
    # ── 1 · cover ────────────────────────────────────────────────────────────────────────────────
    s = page(1, "This or that · " + EP["theme"])
    ep_tag(s, M, 165)
    s.text(M - 6, 345, "Hiki", f(BOLD, 150), NAVY)
    s.text(M - 6, 480, "au Kile?", f(BOLD, 150), ORANGE)
    s.text(M, 570, EP["theme_sw"], f(SIG, fit(s, EP["theme_sw"], SIG, 56, W - 2 * M)), NAVY)
    swash(s, M + 8, M + 520, 596, ORANGE, 6)
    for j, (lab, dx, dy, col) in enumerate([("Hiki", 640, 640, NAVY), ("Kile", 760, 760, ORANGE)]):
        card(s, (dx, dy, dx + 250, dy + 230), r=18)
        s.d.rounded_rectangle([k(dx), k(dy), k(dx + 250), k(dy + 70)], radius=k(18), fill=col)
        s.rect(dx, dy + 50, dx + 250, dy + 70, col)
        s.text(dx + 125, dy + 36, lab, f(BOLD, 30), WHITE_T, anchor="mm")
        for q in range(3):
            s.d.rounded_rectangle([k(dx + 30), k(dy + 100 + q * 38), k(dx + 210 - q * 30), k(dy + 114 + q * 38)], radius=k(7), fill=(201, 212, 234))
    vs_badge(s, 760, 760, 52)
    y = 680
    for i, r in enumerate(EP["rounds"]):
        s.text(M, y, f"{i + 1:02d}", f(BOLD, 24), ORANGE)
        s.text(M + 60, y, r["a"], f(BOLD, 30), NAVY)
        x = M + 60 + s.width(r["a"], f(BOLD, 30)) + 16
        s.text(x, y, "vs", f(SIG, 34), ORANGE)
        s.text(x + 50, y, r["b"], f(BOLD, 30), NAVY)
        y += 66
    horizon(s, 1)
    cover_footer(s, "Swipe, then vote in the comments")
    finish(s)
    s.save(1)

    # ── 2–6 · rounds ─────────────────────────────────────────────────────────────────────────────
    for i, r in enumerate(EP["rounds"]):
        n = i + 2
        s = page(n, f"Raundi {i + 1:02d} · Round {i + 1}", f"Hiki au Kile #{EP['num']:02d}")
        ts = fit(s, r["a"] + " vs " + r["b"], BOLD, 76, W - 2 * M)
        s.text(M - 4, 250, r["a"], f(BOLD, ts), NAVY)
        x = M - 4 + s.width(r["a"], f(BOLD, ts)) + 18
        s.text(x, 250, "vs", f(SIG, ts * 1.05), ORANGE)
        s.text(x + s.width("vs", f(SIG, ts * 1.05)) + 18, 250, r["b"], f(BOLD, ts), NAVY)
        cw = (W - 2 * M - 40) / 2
        top, bot = 330, 700
        for j, (name, pts) in enumerate([(r["a"], r["a_pts"]), (r["b"], r["b_pts"])]):
            x0 = M + j * (cw + 40)
            picked = r["pick"] == j
            card(s, (x0, top, x0 + cw - 8, bot), r=20, fill=(255, 255, 255))
            s.d.rounded_rectangle([k(x0), k(top), k(x0 + cw - 8), k(top + 96)], radius=k(20), fill=NAVY if not picked else ORANGE)
            s.rect(x0, top + 70, x0 + cw - 8, top + 96, NAVY if not picked else ORANGE)
            s.text(x0 + (cw - 8) / 2, top + 50, name, f(BOLD, fit(s, name, BOLD, 34, cw - 50)), WHITE_T, anchor="mm")
            yy = top + 175
            for p in r[f"{'ab'[j]}_pts"]:
                mark(s, x0 + 42, yy - 11, True, r=16)
                yy = s.para(x0 + 74, yy, p, f(SEMI, 29), cw - 110, 40, NAVY) + 40
            if picked:
                sticker(s, x0 + cw - 70, bot - 10, "Chaguo langu", angle=-8, size=20)
        vs_badge(s, W / 2, (top + bot) / 2)
        smallcaps(s, M, 790, "Chaguo langu · My pick" if r["pick"] is not None else "Jibu la kweli · Honest answer", 15, ORANGE)
        s.para(M, 850, r["reason"], f(SEMI, 34), W - 2 * M, 48, NAVY)
        horizon(s, n)
        navy_note(s, "But", r["note"], r["sw"], seed=n)
        finish(s)
        s.save(n)

    # ── 7 · your turn ────────────────────────────────────────────────────────────────────────────
    s = page(TOTAL, "The end · Mwisho", f"Hiki au Kile #{EP['num']:02d}")
    closing(s, "Which one do you", "disagree with?", [("Vote", "comment 1A, 2B, 3A... for your picks"), ("Share", "with the friend who will argue"),
                                                   ("Suggest", "the next match-up")])
    horizon(s, TOTAL)
    closing_footer(s)
    finish(s)
    s.save(TOTAL)
    print("ok")
