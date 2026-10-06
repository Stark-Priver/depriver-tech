"""Single-image posters for the make-your-fpt-count post: a feed poster (1080x1350) and a WhatsApp/Instagram
status (1080x1920), both exported at 2x. Reuses the carousel's logbook art, ruled page and supervisor stamp.
Status keeps key content clear of the top ~180 px and bottom ~200 px app overlays."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
SRC = open(os.path.join(STUDIO, "make-your-fpt-count", "make.py")).read()
exec(SRC[:SRC.index("# ── 1 · cover")].replace('OUT = os.path', '_OUT = os.path'))  # palette, kit, art, stamp()

MOVES = ["Show up like staff", "Write the logbook daily", "Ask for real work", "Learn their tools",
         "Meet the people", "Collect proof", "Get the letter early", "Protect your name"]


def render(name, height, top, ty, art, card, row, blk):
    global H, _TERRAIN
    H, _TERRAIN = height, None
    s = Slide()
    paper(s)
    smallcaps(s, M, top, "For students on field practical training", 17, ORANGE)
    s.text(W - M, top, "depriver.tech", f(SEMI, 21), NAVY, anchor="rs")
    hairline(s, M, W - M, top + 22, RULE)

    s.text(M - 4, ty, "FPT is not a holiday.", f(BOLD, 64), NAVY)
    s.text(M - 6, ty + 140, "Make it", f(BOLD, 120), ORANGE)
    s.text(M - 10, ty + 290, "count.", f(BOLD, 160), ORANGE)
    s.text(M, ty + 390, "Mafunzo si likizo", f(SIG, 64), NAVY)
    swash(s, M + 8, M + 400, ty + 416, ORANGE, 6)
    ax, ay, aw = art
    paste_print(s, print_art("logbook", k(aw)), ax, ay)

    # the eight weeks on one logbook page
    c0, c1 = card
    ruled_card(s, (M, c0, W - M - 8, c1), margin=None, gap=row)
    smallcaps(s, M + 24, c0 + 44, "8 weeks · 8 moves", 15, MARGIN_RED)
    colw = (W - 2 * M - 8) / 2
    for j, mv in enumerate(MOVES):
        x = M + 24 + (j // 4) * colw
        y = c0 + 58 + row * (j % 4 + 1) - 14
        s.text(x, y, f"{j + 1:02d}", f(BOLD, 22), ORANGE)
        s.text(x + 48, y, mv, f(SEMI, fit(s, mv, SEMI, 27, colw - 80)), NAVY)
    stamp(s, W - M - 70, c0 + 4, 8, angle=12)

    # navy block with the link
    s.rect(0, blk, W, H, NAVY)
    s.rect(0, blk - 5, W, blk, ORANGE)
    url = "depriver.tech/blog/make-your-fpt-count"
    smallcaps(s, M, blk + 86, "The full week-by-week guide", 17, SOFT)
    s.text(M, blk + 150, url, f(BOLD, fit(s, url, BOLD, 44, W - 2 * M)), WHITE_T)
    hairline(s, M, W - M, blk + 182, (38, 60, 100))
    s.text(M, blk + 236, "Link in bio", f(SEMI, 24), SOFT)
    s.text(W - M, blk + 236, "@_depriver", f(SEMI, 22), WHITE_T, anchor="rs")
    finish(s)
    s.im.save(f"{OUT}{name}.jpg", quality=95)


render("make-your-fpt-count-poster", 1350, top=96, ty=210, art=(560, 250, 460), card=(680, 1010), row=64, blk=1080)
render("make-your-fpt-count-status", 1920, top=210, ty=360, art=(600, 500, 420), card=(960, 1400), row=88, blk=1500)
print("ok")
