"""Feed poster (1080x1350) and status (1080x1920) for final-year-project-ideas, exported at 2x. The ten idea names
with their difficulty badges. Status keeps clear of the top/bottom app overlays."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
SRC = open(os.path.join(STUDIO, "final-year-project-ideas", "make.py")).read()
exec(SRC[:SRC.index("# ── 1 · cover")].replace('OUT = os.path', '_OUT = os.path'))


def render(name, height, top, ty, ly, row, blk):
    s = poster_start(height, top, "For final year students · Tanzania")
    s.text(M - 6, ty, "10 project ideas", f(BOLD, 86), NAVY)
    s.text(M - 6, ty + 96, "that solve real", f(BOLD, 86), NAVY)
    s.text(M - 6, ty + 192, "Tanzanian problems.", f(BOLD, 78), ORANGE)
    s.text(M, ty + 276, "Tatua matatizo ya Tanzania", f(SIG, 54), NAVY)
    swash(s, M + 8, M + 520, ty + 300, ORANGE, 6)
    colw = (W - 2 * M) / 2
    for i, idea in enumerate(IDEAS):
        x = M + (i // 5) * colw
        y = ly + (i % 5) * row
        s.text(x, y, f"{i + 1:02d}", f(BOLD, 24), ORANGE)
        s.text(x + 46, y, idea[0], f(SEMI, 27), NAVY)
        lv = idea[6]
        s.d.ellipse([k(x + colw - 50), k(y - 20), k(x + colw - 34), k(y - 4)], fill=LEVEL[lv])
        if i % 5 < 4:
            hairline(s, x, x + colw - 30, y + row / 2 - 4, RULE)
    poster_end(s, blk, "Tatizo · suluhisho · stack · difficulty", name)


render("final-year-project-ideas-poster", 1350, top=96, ty=230, ly=640, row=82, blk=1080)
render("final-year-project-ideas-status", 1920, top=210, ty=400, ly=880, row=110, blk=1500)
print("ok")
