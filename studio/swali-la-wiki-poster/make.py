"""Swali la Wiki posters, exported at 2x: the episode feed poster (1080x1350), the episode status (1080x1920), and an
evergreen "uliza swali lako" status that collects questions for next week. Change EP_DIR for a new episode."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
EP_DIR = "swali-la-wiki-01"
SRC = open(os.path.join(STUDIO, EP_DIR, "make.py")).read()
SKIP_SLIDES = True
exec(SRC.replace('OUT = os.path', '_OUT = os.path'))


def episode(name, height, top, by, sy, blk):
    s = poster_start(height, top, "Swali la Wiki · Question of the week")
    outline_text(s, W - M + 10, blk - 40, "?", f(BOLD, 380), stroke=4, color=ORANGE, anchor="rs", opacity=0.6)
    episode_tag(s, M, by - 110)
    lines = wrap_lines(s, EP["question"], f(BOLD, 76), W - 2 * M - 88)
    bubble(s, (M, by, W - M - 10, by + 100 + lines * 90), EP["question"], 76, 90)
    y = by + 100 + lines * 90 + 130
    s.text(M, y, EP["short"], f(BOLD, 72), ORANGE)
    s.text(M, y + 60, EP["question_en"], f(MED, 28), GREY)
    s.text(M, sy, "Jibu kamili liko kwenye blog", f(SIG, 54), NAVY)
    swash(s, M + 8, M + 520, sy + 26, ORANGE, 6)
    poster_end(s, blk, f"Swali la Wiki #{EP['num']:02d} · the full answer", name)


def ask(name):
    global POST_URL
    s = poster_start(1920, 210, "Swali la Wiki · Uliza swali lako")
    s.text(M - 6, 420, "Uliza swali", f(BOLD, 116), NAVY)
    s.text(M - 6, 540, "lolote.", f(BOLD, 116), ORANGE)
    s.text(M, 640, "Kuhusu tech, chuo, kazi au pesa", f(SIG, 56), NAVY)
    swash(s, M + 8, M + 600, 666, ORANGE, 6)
    bubble(s, (M, 760, W - M - 10, 1080), "Andika swali lako hapa...", 50, 60)
    s.text(M, 1260, "Reply to this status or DM @_depriver.", f(SEMI, 32), NAVY)
    s.text(M, 1310, "The best one becomes next week's Swali la Wiki.", f(REG, 28), GREY)
    outline_text(s, W - M + 10, 1460, "?", f(BOLD, 300), stroke=4, color=ORANGE, anchor="rs", opacity=0.6)
    POST_URL = "depriver.tech/blog"
    poster_end(s, 1500, "Every week · questions answered", name)


episode("swali-la-wiki-01-poster", 1350, top=96, by=280, sy=960, blk=1080)
episode("swali-la-wiki-01-status", 1920, top=210, by=480, sy=1340, blk=1500)
ask("swali-la-wiki-uliza-status")
print("ok")
