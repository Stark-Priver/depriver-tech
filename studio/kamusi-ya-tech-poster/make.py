"""Feed poster (1080x1350) and status (1080x1920) for kamusi-ya-tech, exported at 2x. One dictionary entry (API)
as the hero plus the episode's word list. Status keeps clear of the top/bottom app overlays."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
SRC = open(os.path.join(STUDIO, "kamusi-ya-tech", "make.py")).read()
exec(SRC[:SRC.index("# ── 1 · cover")].replace('OUT = os.path', '_OUT = os.path'))


def render(name, height, top, ty, ey, cy, blk):
    s = poster_start(height, top, "Toleo 01 · Episode 01")
    s.text(M - 6, ty, "Kamusi", f(BOLD, 140), NAVY)
    s.text(M - 6, ty + 124, "ya Tech.", f(BOLD, 140), ORANGE)
    s.text(M, ty + 214, "Maneno ya tech kwa Kiswahili rahisi", f(SIG, 52), NAVY)
    swash(s, M + 8, M + 640, ty + 240, ORANGE, 6)
    card(s, (M, ey, W - M - 8, ey + 300))
    s.text(M + 34, ey + 100, "API", f(BOLD, 84), NAVY)
    s.text(M + 220, ey + 64, "/ei-pi-ai/", f(REG, 24), GREY)
    s.text(M + 220, ey + 100, "(nomino)", f(SEMI, 24), ORANGE)
    s.para(M + 34, ey + 170, "Njia ambayo programu moja huongea na programu nyingine. Kama mhudumu wa mgahawa.",
           f(MED, 27), W - 2 * M - 80, 38, NAVY)
    x, y = M, cy
    for w_ in [w[0] for w in WORDS]:
        ww = s.width(w_, f(SEMI, 22)) + 36
        if x + ww > W - M:
            x, y = M, y + 58
        s.d.rounded_rectangle([k(x), k(y), k(x + ww), k(y + 46)], radius=k(23), fill=(255, 255, 255), outline=NAVY, width=k(2.5))
        s.text(x + ww / 2, y + 24, w_, f(SEMI, 22), NAVY, anchor="mm")
        x += ww + 10
    poster_end(s, blk, "8 words · maana · mfano", name)


render("kamusi-ya-tech-poster", 1350, top=96, ty=250, ey=560, cy=920, blk=1080)
render("kamusi-ya-tech-status", 1920, top=210, ty=420, ey=760, cy=1150, blk=1500)
print("ok")
