"""Carousel: Let me introduce myself (5 slides, 1080x1350)."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers

# ── 1 · hook ─────────────────────────────────────────────
s = Slide()
s.rect(0, 830, 560, 872, BLUE)
s.rect(0, 872, 560, H, NAVY)
s.photo(470, 780, fade="left")
s.text(96, 330, "I don’t think I’ve done this, so", f(MED, 32), NAVY)
s.text(90, 470, "Let me", f(BOLD, 112), NAVY)
s.text(90, 610, "Introduce", f(BOLD, 112), ORANGE)
s.text(90, 750, "Myself", f(BOLD, 112), NAVY)
s.rect(210, 1128, 380, 1170, ORANGE)
s.text(96, 1060, "Privatus", f(SIG, 112), (255, 255, 255))
s.text(170, 1170, "Cosmas", f(SIG, 112), (255, 255, 255))
s.swipe(640, 1150)
s.counter(1)
s.save(1)

# ── 2 · who I am ─────────────────────────────────────────
s = Slide()
s.rect(620, 1030, W, 1072, BLUE)
s.rect(620, 1072, W, H, NAVY)
s.photo(-250, 900, fade="right", fade_w=200)
x = 560
s.text(x, 380, "My name is", f(MED, 36), NAVY)
s.text(x, 450, "Privatus Cosmas", f(BOLD, 50), NAVY)
y = s.para(x, 500, "(From Kagera, now based in Mbeya, Tanzania. Online I go by @_depriver.)", f(REG, 23), 440, 34, GREY)
y = s.para(x, y + 40, "I’m a Software Engineer & Digital Innovator who loves building things that matter.", f(MED, 33), 450, 46, NAVY)
s.para(x, y + 6, "(Yep, I wear many hats... I’ll reveal them as we go on.)", f(REG, 23), 440, 34, GREY)
s.swipe(560, 930)
s.counter(2)
s.save(2)

# ── 3 · software ─────────────────────────────────────────
s = Slide()
s.text(90, 250, "I Build", f(BOLD, 112), NAVY)
s.text(90, 375, "Software", f(BOLD, 112), ORANGE)
y = s.para(94, 440, "From idea to launch, I design and build digital products that help businesses work smarter.",
           f(REG, 26), 620, 38, GREY)
s.bullets(96, y + 44, ["Web & mobile applications", "SaaS platforms & business systems",
                       "Custom systems integration", "Cloud, DevOps & AI"], lh=50)
s.swipe(770, 640)
tiles = [("Python", "Backend", NAVY), ("React", "Frontend", CHAR), ("Flutter", "Mobile", ORANGE),
         ("Django", "Web apps", (20, 52, 102)), ("AWS", "Cloud", INK), ("AI", "Automation", (58, 88, 140))]
gx0, gy0, gw, gh = 70, 790, (W - 140) / 3, 305
mask = Image.new("L", s.im.size, 0)
ImageDraw.Draw(mask).rounded_rectangle([k(gx0), k(gy0), k(W - 70), k(H + 60)], radius=k(34), fill=255)
grid = Image.new("RGB", s.im.size, WHITE)
gd = ImageDraw.Draw(grid)
for i, (name, cap, col) in enumerate(tiles):
    cx, cy = gx0 + (i % 3) * gw, gy0 + (i // 3) * gh
    gd.rectangle([k(cx), k(cy), k(cx + gw), k(cy + gh)], fill=col)
    gd.text((k(cx + gw / 2), k(cy + gh / 2 - 6)), name, font=f(BOLD, 50), fill=(255, 255, 255), anchor="ms")
    gd.text((k(cx + gw / 2), k(cy + gh / 2 + 36)), cap.upper(), font=f(MED, 17), fill=(255, 255, 255, 180),
            anchor="ms")
s.im.paste(grid, (0, 0), mask)
s.counter(3)
s.save(3)

# ── 4 · data for business ───────────────────────────────
s = Slide()
s.text(90, 250, "Data Analysis", f(BOLD, 100), NAVY)
s.text(90, 365, "for Business", f(BOLD, 100), ORANGE)
y = s.para(94, 432, "I turn raw business numbers into clear insights that drive better decisions.",
           f(REG, 26), 640, 38, GREY)
s.bullets(96, y + 44, ["Dashboards & reporting", "Sales & performance analysis", "Forecasting & trends"])
s.swipe(770, 600)
# chart card
cx0, cy0, cx1, cy1 = 70, 740, W - 70, 1270
s.rect(cx0, cy0, cx1, cy1, NAVY, r=34)
s.text(cx0 + 50, cy0 + 70, "From data to decisions", f(SEMI, 28), (255, 255, 255))
s.text(cx1 - 50, cy0 + 70, "SAMPLE DASHBOARD", f(MED, 16), BLUE, anchor="rs")
vals = [0.34, 0.46, 0.41, 0.58, 0.63, 0.72, 0.69, 0.86]
base_y, top_h = cy1 - 70, 300
bw_, gap = 62, 44
bx = cx0 + 60
pts = []
for i, v in enumerate(vals):
    x0 = bx + i * (bw_ + gap)
    h = v * top_h
    col = ORANGE if i == len(vals) - 1 else (BLUE if i % 2 else (120, 150, 205))
    s.rect(x0, base_y - h, x0 + bw_, base_y, col, r=10)
    pts.append((k(x0 + bw_ / 2), k(base_y - h - 26)))
s.d.line(pts, fill=(255, 255, 255), width=k(3), joint="curve")
for p in pts:
    s.d.ellipse([p[0] - k(7), p[1] - k(7), p[0] + k(7), p[1] + k(7)], fill=(255, 255, 255))
s.rect(cx0 + 50, base_y, cx1 - 50, base_y + 2, (60, 82, 122))
s.counter(4)
s.save(4)

# ── 5 · also + contact ──────────────────────────────────
s = Slide()
s.photo(520, 760, fade="left")
s.text(90, 230, "What I", f(BOLD, 112), NAVY)
s.text(90, 355, "Also Do", f(BOLD, 112), ORANGE)
s.bullets(96, 470, [("Multimedia & Content", "Video, photography and visuals that tell a clear story."),
                    ("Solving Social Problems", "Using technology to tackle real challenges in our communities."),
                    ("Digital Innovation", "Rethinking everyday work with smart, simple technology.")],
          maxw=440)
cx0, cy0, cx1, cy1 = 70, 870, 700, 1270
s.rect(cx0, cy0, cx1, cy1, NAVY, r=30)
s.text(cx0 + 50, cy0 + 80, "Let’s work together", f(BOLD, 40), (255, 255, 255))
s.rect(cx0 + 50, cy0 + 108, cx0 + 130, cy0 + 114, ORANGE)
rows = [("Phone", "+255 752 747 681"), ("Website", "depriver.tech"), ("Instagram", "@_depriver")]
for i, (lab, val) in enumerate(rows):
    yy = cy0 + 180 + i * 72
    s.text(cx0 + 50, yy, lab.upper(), f(MED, 16), BLUE)
    s.text(cx0 + 50, yy + 34, val, f(SEMI, 30), (255, 255, 255))
s.counter(5)
s.save(5)
print("ok")
