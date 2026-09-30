"""Single post (1080x1350, exported at 2x): "Tech advice I learnt the hard way" as one editorial poster.
Magazine-index layout of the nine lessons with print-style illustrations, hairlines, outlined numeral,
navy call-to-action block with the full post link. Same visual system as the carousel."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

M = 72
RULE = (200, 206, 218)
WHITE_T = (255, 255, 255)
SOFT = (190, 202, 226)
POST_URL = "depriver.tech/blog/tech-advice-i-learnt-the-hard-way"
LESSONS = [
    ("start", "Start with what you have", "Anza na ulichonacho"),
    ("skills", "Skills can't be stolen", "Ujuzi hauibiwi"),
    ("habit", "Consistency beats talent", "Haba na haba hujaza kibaba"),
    ("public", "Build in public", "Onyesha kazi yako"),
    ("hustle", "Solve real problems", "Tatua matatizo halisi"),
    ("people", "Your people matter", "Mtu ni watu"),
    ("health", "Protect your health", "Afya ni mtaji"),
    ("path", "Your path is valid", "Njia yako ni yako"),
    ("backup", "Back up everything", "Usiweke mayai kikapu kimoja"),
]

s = Slide()
paper(s)
smallcaps(s, M, 96, "A field guide · 9 lessons", 17, ORANGE)
smallcaps(s, W - M, 96, "depriver.tech", 17, NAVY, anchor="right")
hairline(s, M, W - M, 118, RULE)

outline_text(s, W + 30, 520, "9", f(BOLD, 560), stroke=3, color=RULE, anchor="rs")
s.text(M - 5, 238, "Tech advice", f(BOLD, 92), NAVY)
s.text(M - 5, 332, "I learnt the hard way.", f(BOLD, fit(s, "I learnt the hard way.", BOLD, 92, W - 2 * M)), ORANGE)
s.text(M, 410, "Mambo niliyojifunza kwa njia ngumu", f(SIG, 50), ORANGE)
swash(s, M + 8, M + 470, 434, ORANGE, 5, seed=5)
sticker(s, 900, 420, "Hifadhi · Save", angle=-7, size=20)

# the index: two columns of lessons, each row = print illustration + number + title + Swahili line
top, row_h, col_gap = 486, 118, 36
col_w = (W - 2 * M - col_gap) / 2
for i, (art_key, title, sw) in enumerate(LESSONS):
    col, row = (0, i) if i < 5 else (1, i - 5)
    x = M + col * (col_w + col_gap)
    y = top + row * row_h
    art = print_art(art_key, k(118))
    paste_print(s, art, x - 6, y + 10, offset=(4, 5), opacity=0.14)
    s.text(x + 124, y + 42, f"{i + 1:02d}", f(BOLD, 20), ORANGE)
    tf = f(BOLD, fit(s, title, BOLD, 25, col_w - 170))
    s.text(x + 160, y + 42, title, tf, NAVY)
    s.text(x + 124, y + 86, sw, f(SIG, fit(s, sw, SIG, 30, col_w - 170)), ORANGE)
    hairline(s, x, x + col_w, y + row_h - 8, RULE, 1.5)

# fill the short second column with a pull quote
qx, qy = M + col_w + col_gap, top + 4 * row_h + 26
s.text(qx, qy + 36, "“", f(BOLD, 90), ORANGE)
s.para(qx + 46, qy + 20, "Skills are what they can't steal.", f(SEMI, 26), col_w - 60, 34, NAVY)

# call to action: the full post lives on the site
blk = 1112
s.rect(0, blk, W, H, NAVY)
smallcaps(s, M, blk + 58, "Read the full post · Soma zaidi", 17, SOFT)
s.text(M, blk + 96, "Practical tips for every lesson", f(REG, 22), SOFT)
s.text(M, blk + 162, POST_URL, f(BOLD, fit(s, POST_URL, BOLD, 40, W - 2 * M)), WHITE_T)
hairline(s, M, W - M, blk + 184, (38, 60, 100))
s.text(M, blk + 212, "Link in bio", f(SEMI, 22), ORANGE)
aw = M + s.width("Link in bio", f(SEMI, 22)) + 26
s.d.line([k(aw - 16), k(blk + 204), k(aw + 8), k(blk + 204)], fill=ORANGE, width=k(3))
s.d.line([k(aw - 2), k(blk + 196), k(aw + 8), k(blk + 204), k(aw - 2), k(blk + 212)], fill=ORANGE, width=k(3), joint="curve")
smallcaps(s, W - M, blk + 212, "@_depriver", 17, WHITE_T, anchor="right")

finish(s)
s.im.save(f"{OUT}tech-advice-poster.jpg", quality=95)
print("ok")
