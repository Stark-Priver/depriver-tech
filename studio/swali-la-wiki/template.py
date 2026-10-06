"""Swali la Wiki (question of the week): shared 6-slide template. Each episode lives in studio/swali-la-wiki-NN/make.py,
sets EP (dict below) and execs this file. Slides: cover question, jibu fupi (short answer), how (steps), tahadhari
(watch-outs), the next step, and "uliza swali lako". Also used by swali-la-wiki-poster for the feed poster and the
"ask me" status. EP keys: num, question, question_en, source, short, short_en, steps [(title, body)], careful [..],
next_step, sw (Swahili sign-off line)."""
TOTAL = 6
POST_URL = f"depriver.tech/blog/swali-la-wiki-{EP['num']:02d}"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing


def bubble(s, box, text, size, lh, tail=True):
    """Big question bubble: white, navy outline, offset ink, tail bottom-left."""
    x0, y0, x1, y1 = box
    s.rect(x0 + 10, y0 + 12, x1 + 10, y1 + 12, (205, 211, 224), r=34)
    if tail:
        s.d.polygon([(k(x0 + 70), k(y1 - 4)), (k(x0 + 150), k(y1 - 4)), (k(x0 + 56), k(y1 + 70))], fill=NAVY)
        s.d.polygon([(k(x0 + 78), k(y1 - 8)), (k(x0 + 138), k(y1 - 8)), (k(x0 + 66), k(y1 + 54))], fill=(255, 255, 255))
    s.d.rounded_rectangle([k(x0), k(y0), k(x1), k(y1)], radius=k(34), fill=(255, 255, 255), outline=NAVY, width=k(4))
    if tail:
        s.d.polygon([(k(x0 + 78), k(y1 - 10)), (k(x0 + 138), k(y1 - 10)), (k(x0 + 100), k(y1 + 6))], fill=(255, 255, 255))
    s.para(x0 + 44, y0 + 44 + size, text, f(BOLD, size), x1 - x0 - 88, lh, NAVY)


def episode_tag(s, x, y, size=22):
    t = f"Swali la Wiki #{EP['num']:02d}"
    w_ = s.width(t, f(BOLD, size)) + 40
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + size * 2.1)], radius=k(size), fill=ORANGE)
    s.text(x + w_ / 2, y + size * 1.08, t, f(BOLD, size), WHITE_T, anchor="mm")


if "SKIP_SLIDES" not in globals():
    # ── 1 · cover: the question ──────────────────────────────────────────────────────────────────
    s = page(1, "Swali la Wiki · Question of the week")
    outline_text(s, W - M + 10, 1010, "?", f(BOLD, 420), stroke=4, color=ORANGE, anchor="rs", opacity=0.6)
    episode_tag(s, M, 180)
    lines = wrap_lines(s, EP["question"], f(BOLD, 76), W - 2 * M - 88)
    bubble(s, (M, 290, W - M - 10, 290 + 100 + lines * 90), EP["question"], 76, 90)
    yq = 290 + 100 + lines * 90 + 120
    s.text(M, yq, EP["question_en"], f(MED, fit(s, EP["question_en"], MED, 34, W - 2 * M)), GREY)
    smallcaps(s, M, yq + 60, EP["source"], 15, ORANGE)
    s.text(M, yq + 170, "Jibu fupi liko ndani", f(SIG, 62), NAVY)
    swash(s, M + 8, M + 470, yq + 196, ORANGE, 6)
    horizon(s, 1)
    cover_footer(s, "Swipe for the answer")
    finish(s)
    s.save(1)

    # ── 2 · short answer ─────────────────────────────────────────────────────────────────────────
    s = page(2, "Jibu fupi · Short answer")
    episode_tag(s, M, 170, 18)
    s.text(M - 6, 380, EP["short"], f(BOLD, fit(s, EP["short"], BOLD, 140, W - 2 * M)), ORANGE)
    y = s.para(M, 480, EP["short_en"], f(MED, 36), W - 2 * M, 52, NAVY)
    hairline(s, M, W - M, y + 30, RULE)
    smallcaps(s, M, y + 100, "In this answer", 15, ORANGE)
    for j, (a, b) in enumerate([("How", EP["how_title"][0] + " " + EP["how_title"][1]), ("Limits", "what to watch out for"),
                                ("Your 7-day task", "one small step this week")]):
        yy = y + 160 + j * 92
        s.d.ellipse([k(M), k(yy - 34), k(M + 46), k(yy + 12)], fill=ORANGE if j % 2 == 0 else NAVY)
        s.text(M + 23, yy - 11, str(j + 3), f(BOLD, 24), WHITE_T, anchor="mm")
        s.text(M + 70, yy, a, f(BOLD, 32), NAVY)
        s.text(M + 70 + s.width(a, f(BOLD, 32)) + 18, yy, b, f(REG, 26), GREY)
    horizon(s, 2)
    navy_note(s, "In one line", EP["one_line"], EP["sw"], seed=2)
    finish(s)
    s.save(2)

    # ── 3 · how ──────────────────────────────────────────────────────────────────────────────────
    s = page(3, "Jinsi ya kufanya · How")
    title2(s, EP["how_title"][0], EP["how_title"][1], y=220, size=80)
    numbered(s, EP["steps"], 450, gap=140, ts=34, bs=26)
    horizon(s, 3)
    navy_note(s, "Tip", EP["how_tip"], seed=3)
    finish(s)
    s.save(3)

    # ── 4 · watch out ────────────────────────────────────────────────────────────────────────────
    s = page(4, "Tahadhari · Watch out")
    title2(s, "Know the", "limits.", y=220, size=88)
    y = 440
    for a, b in EP["careful"]:
        mark(s, M + 18, y - 10, False)
        s.text(M + 56, y, a, f(BOLD, fit(s, a, BOLD, 36, W - 2 * M - 60)), NAVY)
        s.text(M + 56, y + 46, b, f(REG, fit(s, b, REG, 27, W - 2 * M - 60)), GREY)
        y += 160
    horizon(s, 4)
    navy_note(s, "But", "Limits are not a reason to wait. Start with what you have.", "Anza ulipo", seed=4)
    finish(s)
    s.save(4)

    # ── 5 · next step ────────────────────────────────────────────────────────────────────────────
    s = page(5, "Hatua inayofuata · Next step")
    title2(s, "Do this", "this week.", y=230, size=96)
    card(s, (M, 420, W - M - 8, 760))
    smallcaps(s, M + 34, 476, "Your 7-day task", 15, ORANGE)
    s.para(M + 34, 540, EP["next_step"], f(SEMI, 34), W - 2 * M - 80, 48, NAVY)
    s.text(M, 860, "Done? Comment “Nimefanya” and show me.", f(SEMI, 30), ORANGE)
    horizon(s, 5)
    navy_note(s, "Remember", "Small steps every week beat big plans that never start.", "Hatua kwa hatua", seed=5)
    finish(s)
    s.save(5)

    # ── 6 · ask yours ────────────────────────────────────────────────────────────────────────────
    s = page(TOTAL, "Uliza swali lako · Ask yours")
    s.text(M - 6, 270, "Got a", f(BOLD, 112), NAVY)
    s.text(M - 6, 390, "question?", f(BOLD, 112), ORANGE)
    s.text(M, 480, "Nitajibu kwenye Swali la Wiki", f(SIG, 56), NAVY)
    swash(s, M + 8, M + 560, 506, ORANGE, 5, seed=6)
    ways = [("Comment", "your question below this post"), ("DM", "@_depriver on Instagram"), ("Tag", "#SwaliLaWiki on your story")]
    y = 620
    for j, (a, b) in enumerate(ways):
        s.text(M, y, f"{j + 1:02d}", f(BOLD, 22), ORANGE)
        s.text(M + 56, y, a, f(BOLD, 36), NAVY)
        s.text(M + 56, y + 40, b, f(REG, 24), GREY)
        y += 108
    bubble(s, (620, 640, W - M - 10, 900), "Uliza chochote kuhusu tech.", 34, 44)
    horizon(s, TOTAL)
    closing_footer(s)
    finish(s)
    s.save(TOTAL)
    print("ok")
