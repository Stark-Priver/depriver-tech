"""Single post (1080x1350, exported at 2x): all nine lessons from "Tech advice I learnt the hard way" on one poster."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # glass, neumorphism, illustrations (ART)

LESSONS = [
    ("start", "Start with what you have", "Anza na ulichonacho"),
    ("skills", "Skills can't be stolen", "Ujuzi hauibiwi"),
    ("habit", "Consistency beats talent", "Haba na haba hujaza kibaba"),
    ("public", "Build in public", "Onyesha kazi yako"),
    ("hustle", "Solve real problems", "Tatua matatizo halisi"),
    ("people", "Your people matter", "Mtu ni watu"),
    ("health", "Protect your health", "Afya ni mtaji"),
    ("path", "Your path is valid", "Njia yako ni yako"),
    ("backup", "Back up everything", "Usiweke mayai yote kikapu kimoja"),
]


def wrap(s, text, font, maxw):
    words, lines, line = text.split(), [], ""
    for w in words:
        trial = (line + " " + w).strip()
        if s.width(trial, font) > maxw and line:
            lines.append(line)
            line = w
        else:
            line = trial
    return lines + [line]


s = Slide()
paper(s)
glows(s, [(960, 300, 260, ORANGE, 0.85), (110, 760, 250, (111, 155, 255), 0.8), (700, 1180, 200, YELLOW, 0.6), (980, 1100, 180, ORANGE, 0.5)])

# header
brand(s)
pill(s, W - 70, 62, "9 lessons · masomo 9", f(SEMI, 20), anchor_right=True)
s.text(66, 250, "Tech advice I learnt", f(BOLD, 72), NAVY)
s.text(66, 332, "the hard way", f(BOLD, 72), ORANGE)
s.text(70, 400, "Mambo niliyojifunza kwa njia ngumu", f(SIG, 50), ORANGE)

# 3x3 grid of neumorphic lesson cards
gx0, gy0, gap = 70, 450, 22
cw, ch = (W - 140 - 2 * gap) / 3, 214
for i, (art, title, sw) in enumerate(LESSONS):
    x0 = gx0 + (i % 3) * (cw + gap)
    y0 = gy0 + (i // 3) * (ch + gap)
    neu(s, (x0, y0, x0 + cw, y0 + ch), 30, 0.7)
    # illustration in a small frosted well
    well = (x0 + 14, y0 + 14, x0 + cw - 14, y0 + 104)
    glass(s, well, 22, alpha=0.5, blur=14, border=True)
    place_art(s, art, well, pad=2)
    # number badge
    nb = (x0 + 22, y0 + 22, x0 + 62, y0 + 62)
    neu(s, nb, 14, 0.35)
    s.text((nb[0] + nb[2]) / 2, (nb[1] + nb[3]) / 2 + 1, f"{i + 1:02d}", f(BOLD, 17), ORANGE, anchor="mm")
    # text
    tf = f(BOLD, 23)
    lines = wrap(s, title, tf, cw - 36)
    ty = y0 + 136
    for line in lines[:2]:
        s.text(x0 + 18, ty, line, tf, NAVY)
        ty += 29
    sws = fit(s, sw, SIG, 30, cw - 84)  # script glyphs overhang their advance width
    s.text(x0 + 18, y0 + ch - 16, sw, f(SIG, sws), ORANGE)

# call to action: the full post (with practical tips for every lesson) lives on the site
URL = "depriver.tech/blog/tech-advice-i-learnt-the-hard-way"
cta = (70, 1150, W - 70, 1300)
glass(s, cta, 38, tint=(11, 30, 63), alpha=0.88, blur=20, border=False)
s.d.rounded_rectangle([k(v) for v in cta], radius=k(38), outline=(60, 82, 122), width=k(2))
s.text(cta[0] + 40, cta[1] + 52, "READ THE FULL POST · SOMA ZAIDI", f(SEMI, 18), BLUE)
s.text(cta[0] + 40, cta[1] + 82, "Practical tips for every lesson", f(REG, 20), (196, 208, 232))
go = (cta[2] - 40 - 220, cta[1] + 26, cta[2] - 40, cta[1] + 84)
shadow(s.im, go, 18, (120, 60, 45), (0, 12), 14, 160)
s.rect(*go, ORANGE, r=18)
s.text((go[0] + go[2]) / 2 - 14, (go[1] + go[3]) / 2 + 1, "Link in bio", f(SEMI, 22), (255, 255, 255), anchor="mm")
ax, ay = go[2] - 28, (go[1] + go[3]) / 2
s.d.line([k(ax - 14), k(ay), k(ax + 10), k(ay)], fill=(255, 255, 255), width=k(3.4))
s.d.line([k(ax), k(ay - 10), k(ax + 10), k(ay), k(ax), k(ay + 10)], fill=(255, 255, 255), width=k(3.4), joint="curve")
s.rect(cta[0] + 40, cta[1] + 100, cta[2] - 40, cta[1] + 102, (48, 70, 110))
s.text(cta[0] + 40, cta[1] + 132, URL, f(BOLD, fit(s, URL, BOLD, 34, cta[2] - cta[0] - 80)), (255, 255, 255))

s.im.save(f"{OUT}tech-advice-poster.jpg", quality=95)
print("ok")
