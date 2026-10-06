"""Feed poster (1080x1350) and status (1080x1920) for github-that-gets-you-hired, exported at 2x.
Reuses the carousel's profile card and contribution graph. Status keeps clear of the top/bottom app overlays."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
SRC = open(os.path.join(STUDIO, "github-that-gets-you-hired", "make.py")).read()
exec(SRC[:SRC.index("# ── 1 · cover")].replace('OUT = os.path', '_OUT = os.path'))


def render(name, height, top, ty, cardy, chipy, blk):
    s = poster_start(height, top, "For students & junior devs")
    s.text(M - 6, ty, "Your GitHub", f(BOLD, 104), NAVY)
    s.text(M - 6, ty + 112, "is your CV.", f(BOLD, 104), NAVY)
    s.text(M - 8, ty + 232, "Make it hire you.", f(BOLD, 86), ORANGE)
    s.text(M, ty + 322, "Kazi yako ionekane", f(SIG, 62), NAVY)
    swash(s, M + 8, M + 420, ty + 348, ORANGE, 6)
    card(s, (M, cardy, W - M - 8, cardy + 300))
    avatar(s, M + 80, cardy + 80, 46)
    s.text(M + 150, cardy + 70, "Your Name", f(BOLD, 32), NAVY)
    s.text(M + 150, cardy + 106, "@username · Software developer", f(REG, 21), GREY)
    graph(s, M + 32, cardy + 160, 40, rows=5, cell=17, gap=5, seed=11)
    smallcaps(s, M, chipy, "6 steps inside", 15, ORANGE)
    x, y = M, chipy + 24
    for t in ["Profile", "README", "Pin 6", "READMEs", "Clean commits", "No secrets"]:
        w_ = s.width(t, f(SEMI, 20)) + 34
        if x + w_ > W - M:
            x, y = M, y + 62
        s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + 48)], radius=k(24), fill=(255, 255, 255), outline=NAVY, width=k(2.5))
        s.text(x + w_ / 2, y + 25, t, f(SEMI, 20), NAVY, anchor="mm")
        x += w_ + 10
    poster_end(s, blk, "6 steps to a GitHub that gets you hired", name)


render("github-that-gets-you-hired-poster", 1350, top=96, ty=230, cardy=610, chipy=955, blk=1080)
render("github-that-gets-you-hired-status", 1920, top=210, ty=400, cardy=860, chipy=1250, blk=1500)
print("ok")
