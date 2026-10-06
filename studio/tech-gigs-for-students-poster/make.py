"""Single-image posters for the tech-gigs-for-students post: a feed poster (1080x1350) and a WhatsApp/Instagram
status (1080x1920), both exported at 2x. Reuses the carousel's price board and payment notifications.
Status keeps key content clear of the top ~180 px and bottom ~200 px app overlays."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
SRC = open(os.path.join(STUDIO, "tech-gigs-for-students", "make.py")).read()
exec(SRC[:SRC.index("# ── 1 · cover")].replace('OUT = os.path', '_OUT = os.path'))  # palette, kit, price_board(), paid()

ROWS = [("Fix + format laptops", "15k – 35k"), ("Wi-Fi / router setup", "30k – 80k"), ("One-page business site", "150k – 400k"),
        ("Poster / flyer design", "10k – 40k"), ("Excel / coding class", "10k – 40k / hr")]


def render(name, height, top, ty, notes, board, blk):
    global H, _TERRAIN
    H, _TERRAIN = height, None
    s = Slide()
    paper(s)
    smallcaps(s, M, top, "For tech students · Tanzania price guide", 17, ORANGE)
    s.text(W - M, top, "depriver.tech", f(SEMI, 21), NAVY, anchor="rs")
    hairline(s, M, W - M, top + 22, RULE)

    s.text(M - 6, ty, "Your skills", f(BOLD, 96), NAVY)
    s.text(M - 6, ty + 104, "can pay", f(BOLD, 96), NAVY)
    s.text(M - 10, ty + 240, "your rent.", f(BOLD, 134), ORANGE)
    s.text(M, ty + 336, "Ujuzi ni pesa", f(SIG, 64), NAVY)
    swash(s, M + 8, M + 340, ty + 362, ORANGE, 6)
    for (cx, cy, amt, who, ang) in notes:
        paid(s, cx, cy, amt, who, angle=ang, w=380)

    b0, b1 = board
    price_board(s, (M, b0, W - M - 8, b1), ROWS)

    s.rect(0, blk, W, H, NAVY)
    s.rect(0, blk - 5, W, blk, ORANGE)
    url = "depriver.tech/blog/tech-gigs-for-students"
    smallcaps(s, M, blk + 86, "5 gigs · prices · how to get clients", 17, SOFT)
    s.text(M, blk + 150, url, f(BOLD, fit(s, url, BOLD, 44, W - 2 * M)), WHITE_T)
    hairline(s, M, W - M, blk + 182, (38, 60, 100))
    s.text(M, blk + 236, "Link in bio", f(SEMI, 24), SOFT)
    s.text(W - M, blk + 236, "@_depriver", f(SEMI, 22), WHITE_T, anchor="rs")
    finish(s)
    s.im.save(f"{OUT}{name}.jpg", quality=95)


render("tech-gigs-for-students-poster", 1350, top=96, ty=220,
       notes=[(800, 590, "TZS 350,000", "Website, Mama Shop", -4)],
       board=(670, 1030), blk=1080)
render("tech-gigs-for-students-status", 1920, top=210, ty=390,
       notes=[(800, 760, "TZS 25,000", "Laptop format", -5), (520, 900, "TZS 350,000", "Website, Mama Shop", 3)],
       board=(1020, 1420), blk=1500)
print("ok")
