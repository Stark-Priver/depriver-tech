"""Feed poster (1080x1350) and status (1080x1920) for betting-and-forex-trap, exported at 2x.
Reuses the carousel's betting-slip art and the 2,000-a-day maths. Status keeps clear of the top/bottom app overlays."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
SRC = open(os.path.join(STUDIO, "betting-and-forex-trap", "make.py")).read()
exec(SRC[:SRC.index("def myth")].replace('OUT = os.path', '_OUT = os.path'))


def render(name, height, top, ty, art, maths, blk):
    s = poster_start(height, top, "The talk nobody gives you")
    s.text(M - 6, ty, "Betting is not", f(BOLD, 96), NAVY)
    s.text(M - 6, ty + 104, "a side hustle.", f(BOLD, 96), ORANGE)
    s.text(M - 4, ty + 200, "Neither is that forex “mentor”.", f(BOLD, 50), NAVY)
    s.text(M, ty + 290, "Pesa ya haraka ni mtego", f(SIG, 60), ORANGE)
    swash(s, M + 8, M + 500, ty + 316, ORANGE, 6)
    ax, ay, aw = art
    paste_print(s, print_art("slip", k(aw)), ax, ay)
    y = maths
    for a, b, col in [("TZS 2,000 a day", "", NAVY), ("= TZS 730,000 a year", "", RED_NO)]:
        s.text(M, y, a, f(BOLD, 40 if col == NAVY else 46), col)
        y += 60
    s.text(M, y + 4, "What would you build with that?", f(SEMI, 26), GREY)
    poster_end(s, blk, "4 myths · the reality · the way out", name)


render("betting-and-forex-trap-poster", 1350, top=96, ty=230, art=(560, 600, 440), maths=700, blk=1080)
render("betting-and-forex-trap-status", 1920, top=210, ty=400, art=(400, 760, 600), maths=1260, blk=1500)
print("ok")
