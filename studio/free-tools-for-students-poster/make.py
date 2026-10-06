"""Single-image posters for the free-tools-for-students post: a feed poster (1080x1350) and a WhatsApp/Instagram
status (1080x1920), both exported at 2x. Reuses the carousel's art and coupon ticket so they read as one campaign.
Status keeps key content clear of the top ~180 px and bottom ~200 px app overlays."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
SRC = open(os.path.join(STUDIO, "free-tools-for-students", "make.py")).read()
exec(SRC[:SRC.index("# ── 1 · cover")].replace('OUT = os.path', '_OUT = os.path'))  # palette, kit, art, ticket()


def render(name, height, top, title, art, tick, blk):
    global H, _TERRAIN
    H, _TERRAIN = height, None
    s = Slide()
    paper(s)
    smallcaps(s, M, top, "For every tech student", 17, ORANGE)
    s.text(W - M, top, "depriver.tech", f(SEMI, 21), NAVY, anchor="rs")
    hairline(s, M, W - M, top + 22, RULE)

    y, ts = title
    s.text(M - 6, y, "Your student ID", f(BOLD, ts), NAVY)
    s.text(M - 6, y + ts * 1.08, "is worth", f(BOLD, ts), NAVY)
    s.text(M - 10, y + ts * 2.75, "millions.", f(BOLD, ts * 1.7), ORANGE)
    sy = y + ts * 3.85
    s.text(M, sy, "Usiache bure", f(SIG, 68), NAVY)
    swash(s, M + 8, M + 320, sy + 26, ORANGE, 6)

    ax, ay, aw = art
    paste_print(s, print_art("idcard", k(aw)), ax, ay)

    # one coupon that sums up the post
    t0, th = tick
    box = (M, t0, W - M - 8, t0 + th)
    px = ticket(s, box, stub=160)
    stub_text(s, px, box, "FREE", "student deal")
    tx, tw = px + 34, W - M - 8 - px - 60
    s.text(tx, t0 + 62, "Pro tools, cloud & courses", f(BOLD, fit(s, "Pro tools, cloud & courses", BOLD, 34, tw)), NAVY)
    line = "GitHub Pack · JetBrains · Figma · Azure · Cisco"
    s.text(tx, t0 + 108, line, f(MED, fit(s, line, MED, 23, tw)), NAVY)
    hairline(s, tx, W - M - 38, t0 + 134, RULE)
    s.text(tx, t0 + 178, "You pay", f(SEMI, 24), GREY)
    s.text(tx + s.width("You pay", f(SEMI, 24)) + 16, t0 + 180, "TZS 0", f(BOLD, 40), ORANGE)

    # navy block with the link
    s.rect(0, blk, W, H, NAVY)
    s.rect(0, blk - 5, W, blk, ORANGE)
    sticker(s, W - M - 200, blk - 6, "Expires on graduation day", angle=-5, size=20, bg=NAVY)
    url = "depriver.tech/blog/free-tools-for-students"
    smallcaps(s, M, blk + 86, "11 free deals + how to claim them", 17, SOFT)
    s.text(M, blk + 150, url, f(BOLD, fit(s, url, BOLD, 42, W - 2 * M)), WHITE_T)
    hairline(s, M, W - M, blk + 182, (38, 60, 100))
    s.text(M, blk + 236, "Link in bio", f(SEMI, 24), SOFT)
    s.text(W - M, blk + 236, "@_depriver", f(SEMI, 22), WHITE_T, anchor="rs")
    finish(s)
    s.im.save(f"{OUT}{name}.jpg", quality=95)


render("free-tools-for-students-poster", 1350, top=96, title=(240, 86), art=(520, 470, 480), tick=(840, 196), blk=1080)
render("free-tools-for-students-status", 1920, top=210, title=(400, 96), art=(440, 760, 600), tick=(1190, 210), blk=1500)
print("ok")
