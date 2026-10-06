"""Feed poster (1080x1350) and status (1080x1920) for the talk recap, exported at 2x.
Uses the carousel's PHOTOS[0] as the polaroid (a marked placeholder until the talk photos are in).
Status keeps clear of the top/bottom app overlays."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
SRC = open(os.path.join(STUDIO, "life-in-uni-vs-real-world-in-tech", "make.py")).read()
exec(SRC[:SRC.index("# ── 1 · cover")].replace('OUT = os.path', '_OUT = os.path'))
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # poster_start / poster_end


def render(name, height, top, ty, size, photo_c, photo_w, blk):
    s = poster_start(height, top, "Talk recap · MUST · 7 Oct 2026")
    s.text(M - 4, ty, "I went back to MUST.", f(BOLD, size * 0.56), NAVY)
    s.text(M - 4, ty + size * 1.12, "Life in Uni", f(BOLD, size), NAVY)
    vs_badge(s, M + 40, ty + size * 1.12 + size * 0.86, r=40, size=32)
    s.text(M + 100, ty + size * 2.22, "Real World", f(BOLD, size), ORANGE)
    s.text(M + 100, ty + size * 3.28, "in Tech.", f(BOLD, size), ORANGE)
    f0, c0 = photo(0)
    polaroid(s, photo_c[0], photo_c[1], photo_w, 4, f0, c0)
    sticker(s, 210, photo_c[1] + 60, "First FPT here, 2024", angle=-6, size=20, bg=NAVY)
    poster_end(s, blk, "The six rounds, the money talk and your questions", name)


render("life-in-uni-vs-real-world-in-tech-poster", 1350, top=96, ty=210, size=96, photo_c=(760, 830), photo_w=440, blk=1080)
render("life-in-uni-vs-real-world-in-tech-status", 1920, top=210, ty=380, size=110, photo_c=(560, 1180), photo_w=620, blk=1500)
print("ok")
