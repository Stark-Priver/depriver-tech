"""Feed poster (1080x1350) and status (1080x1920) for dont-get-hacked, exported at 2x. A stamped scam SMS as the hero
and the 15040 reporting number. Status keeps clear of the top/bottom app overlays."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
SRC = open(os.path.join(STUDIO, "dont-get-hacked", "make.py")).read()
exec(SRC[:SRC.index("# ── 1 · cover")].replace('OUT = os.path', '_OUT = os.path'))


def render(name, height, top, ty, cy, ry, blk):
    s = poster_start(height, top, "Cyber safety for students")
    s.text(M - 6, ty, "Umeshinda", f(BOLD, 104), NAVY)
    s.text(M - 6, ty + 110, "milioni 5?", f(BOLD, 104), NAVY)
    s.text(M - 8, ty + 240, "Hapana.", f(BOLD, 140), ORANGE)
    s.text(M, ty + 330, "Usitapeliwe mtandaoni", f(SIG, 60), NAVY)
    swash(s, M + 8, M + 470, ty + 356, ORANGE, 6)
    y = chat(s, M + 140, cy, W - 2 * M - 150, "Hongera! Umeshinda TZS 5,000,000. Tuma 20,000 ya usajili kupokea zawadi yako.",
             "SMS · +255 7XX XXX XXX", mine=False, size=27, lh=38)
    stamp(s, W - M - 180, y - 6, angle=-10)
    s.text(M, ry, "Report scam SMS: forward to", f(SEMI, 28), NAVY)
    s.text(M + s.width("Report scam SMS: forward to", f(SEMI, 28)) + 16, ry + 4, "15040", f(BOLD, 44), ORANGE)
    s.text(M, ry + 44, "Free · TCRA", f(REG, 22), GREY)
    poster_end(s, blk, "5 scams · how to spot them · how to report", name)


render("dont-get-hacked-poster", 1350, top=96, ty=230, cy=640, ry=960, blk=1080)
render("dont-get-hacked-status", 1920, top=210, ty=400, cy=860, ry=1300, blk=1500)
print("ok")
