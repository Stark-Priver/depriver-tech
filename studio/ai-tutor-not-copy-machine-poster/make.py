"""Feed poster (1080x1350) and status (1080x1920) for ai-tutor-not-copy-machine, exported at 2x.
Reuses the carousel's chat bubbles. Status keeps clear of the top/bottom app overlays."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
SRC = open(os.path.join(STUDIO, "ai-tutor-not-copy-machine", "make.py")).read()
exec(SRC[:SRC.index("def round_slide")].replace('OUT = os.path', '_OUT = os.path'))


def render(name, height, top, ty, chaty, blk, cs=28):
    s = poster_start(height, top, "For students learning tech")
    s.text(M - 6, ty, "Use AI like", f(BOLD, 100), NAVY)
    s.text(M - 6, ty + 110, "a tutor,", f(BOLD, 100), ORANGE)
    s.text(M - 6, ty + 210, "not a copy machine.", f(BOLD, 76), NAVY)
    s.text(M, ty + 300, "Akili ni yako", f(SIG, 62), ORANGE)
    swash(s, M + 8, M + 320, ty + 326, ORANGE, 6)
    y = chat(s, M, chaty, W - 2 * M - 110, "Write my assignment on linked lists.", "Copy machine", mine=False, size=cs, lh=cs * 1.42, tag="Copy", tag_ok=False)
    chat(s, M + 100, y + 50, W - 2 * M - 108, "Explain linked lists like I'm new, then give me one exercise. Don't show the answer.",
         "Tutor mode", mine=True, size=cs, lh=cs * 1.42, tag="Tutor", tag_ok=True)
    if height > 1400:
        sticker(s, W - M - 170, blk - 90, "Steal this prompt", angle=-5, size=22, bg=NAVY)
    poster_end(s, blk, "5 prompts to steal + 5 rules", name)


render("ai-tutor-not-copy-machine-poster", 1350, top=96, ty=230, chaty=640, blk=1080)
render("ai-tutor-not-copy-machine-status", 1920, top=210, ty=400, chaty=960, blk=1500, cs=34)

print("ok")
