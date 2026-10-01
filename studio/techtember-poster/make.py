"""Status poster (1080x1920, 9:16, exported at 2x): "Techtember" as one simple poster built around the photo.
Same visual system as the techtember carousel: paper, outlined numeral, swash, stickers, taped polaroid, navy block.
Key content stays inside the status safe zone (clear of the top ~180 px and bottom ~200 px app overlays)."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools
H = 1920                                             # 9:16 status format

M = 72
RULE = (200, 206, 218)
WHITE_T = (255, 255, 255)
SOFT = (190, 202, 226)
SNAP = os.path.join(STUDIO, "assets", "techtember.jpg")
POST_URL = "depriver.tech/blog/techtember"


def polaroid(s, cx, cy, width, angle, caption, cap_size=40, ratio=1.0):
    """The photo as a printed polaroid, taped on at a slight angle, with a handwritten caption."""
    pw = k(width - 44)
    ph = int(pw * ratio)
    src = Image.open(SNAP).convert("RGB")
    src = ImageOps.fit(src, (pw, ph), Image.LANCZOS, centering=(0.5, 0.3))
    src = ImageEnhance.Color(src).enhance(0.86)
    src = ImageEnhance.Contrast(src).enhance(1.06)
    src = grain(src, 0.06)
    pad, foot = k(24), k(cap_size * 2.4)
    card = Image.new("RGBA", (pw + 2 * pad, ph + pad + foot), (252, 251, 247, 255))
    card.paste(src, (pad, pad))
    cd = ImageDraw.Draw(card)
    cd.text((card.width // 2, ph + pad + foot // 2 + k(6)), caption, font=f(SIG, cap_size), fill=NAVY + (255,), anchor="mm")
    for tx in (0.18, 0.82):
        tape = Image.new("RGBA", (k(150), k(44)), (233, 214, 160, 190))
        tape = tape.rotate(-14 if tx < 0.5 else 12, resample=Image.BICUBIC, expand=True)
        card.alpha_composite(tape, (int(card.width * tx) - tape.width // 2, -k(6)))
    big = Image.new("RGBA", (card.width + k(60), card.height + k(60)), (0, 0, 0, 0))
    big.paste(card, (k(30), k(30)))
    big = big.rotate(angle, resample=Image.BICUBIC, expand=True)
    sh = big.getchannel("A").filter(ImageFilter.GaussianBlur(k(14))).point(lambda v: v * 85 // 255)
    px, py = k(cx) - big.width // 2, k(cy) - big.height // 2
    s.im.paste(Image.new("RGB", big.size, INK), (px + k(12), py + k(18)), sh)
    s.im.paste(big, (px, py), big)


s = Slide()
paper(s)
smallcaps(s, M, 200, "Monthly recap · Sep to Oct 2026", 18, ORANGE)
s.text(W - M, 200, "depriver.tech", f(SEMI, 22), NAVY, anchor="rs")
hairline(s, M, W - M, 224, RULE)

outline_text(s, W + 20, 560, "09", f(BOLD, 420), stroke=3, color=RULE, anchor="rs")
size = fit(s, "Techtember", BOLD, 180, W - 2 * M)
s.text(M - 8, 400, "Techtember", f(BOLD, size), NAVY)
s.text(M - 4, 500, "was a whole movie.", f(BOLD, 80), ORANGE)
s.text(M, 590, "Septemba imenifundisha mengi", f(SIG, 62), ORANGE)
swash(s, M + 10, M + 560, 620, ORANGE, 6)

# navy block first, so the polaroid breaks into it
blk = 1500
s.rect(0, blk, W, H, NAVY)
s.rect(0, blk - 5, W, blk, ORANGE)

polaroid(s, W / 2 + 10, 1110, 800, -3, "me vs. bugs, sept '26", cap_size=46)
sticker(s, 190, 720, "6 lessons", angle=-8, size=26)
sticker(s, 900, 1380, "Oktoba loading...", angle=6, size=24)

# bottom: October loading bar + where to find the lessons
y = blk + 150
smallcaps(s, M, y, "Next episode · October is loading", 17, SOFT)
bx0, by, bx1 = M, y + 30, W - M
s.rect(bx0, by, bx1, by + 30, (38, 60, 100), r=15)
s.rect(bx0, by, bx0 + (bx1 - bx0) / 31 + 20, by + 30, ORANGE, r=15)
s.text(M, by + 120, POST_URL, f(BOLD, fit(s, POST_URL, BOLD, 44, W - 2 * M)), WHITE_T)
s.text(M, by + 176, "All 6 lessons on my blog", f(REG, 26), SOFT)
s.text(W - M, by + 176, "@_depriver", f(SEMI, 24), WHITE_T, anchor="rs")

finish(s)
s.im.save(f"{OUT}techtember-poster.jpg", quality=95)
print("ok")
