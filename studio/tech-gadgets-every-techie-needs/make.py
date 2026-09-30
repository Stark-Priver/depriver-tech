"""'Tech gadgets every tech person needs' carousel for Privatus Cosmas (11 slides, 1080x1350, JPG only).
Reuses the design system (fonts, colours, Slide helpers) from the intro carousel so the series matches."""

import random

import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers

TOTAL = 11
WHITE_T = (255, 255, 255)
SOFT = (196, 208, 232)
PALE = (236, 239, 246)


def terrain_field():
    """One wide low-res height field spanning all slides, so contours flow from slide to slide."""
    random.seed(7)
    fw, fh = W * TOTAL // 4, H // 4
    field = None
    for cells, weight in ((5, 1.0), (11, 0.45), (23, 0.18)):
        cw_, ch_ = int(cells * 0.8 * TOTAL) + 1, cells
        small = Image.new("L", (cw_, ch_))
        small.putdata([random.randint(0, 255) for _ in range(cw_ * ch_)])
        layer = small.resize((fw, fh), Image.BICUBIC)
        field = layer if field is None else Image.blend(field, layer, weight / (1 + weight))
    return ImageOps.autocontrast(field.filter(ImageFilter.GaussianBlur(3)))


FIELD = terrain_field()


def terrain(n):
    """Off-white paper with topographic contour lines and fine grain for slide n."""
    fw = W // 4
    part = FIELD.crop(((n - 1) * fw, 0, n * fw, FIELD.height)).resize((W * K, H * K), Image.BICUBIC)
    part = part.filter(ImageFilter.GaussianBlur(14))
    step = 11
    bands = part.point(lambda v: (v // step) * step)
    edges = bands.filter(ImageFilter.FIND_EDGES).point(lambda v: 255 if v else 0).filter(ImageFilter.MaxFilter(3))
    # soften the stair-steps from 8-bit levels into smooth anti-aliased lines
    edges = edges.filter(ImageFilter.GaussianBlur(2.2)).point(lambda v: min(255, v * 3))
    major = bands.point(lambda v: 255 if (v // step) % 5 == 0 else 0)
    edges_major = ImageChops.multiply(edges, major.filter(ImageFilter.MaxFilter(5)))
    bg = Image.new("RGB", part.size, WHITE)
    shade = Image.new("RGB", part.size, (238, 240, 244))
    bg = Image.composite(shade, bg, part.point(lambda v: int(v * 0.35)))  # soft tonal hills
    bg.paste(Image.new("RGB", part.size, (214, 220, 231)), (0, 0), edges.point(lambda v: v * 115 // 255))
    bg.paste(Image.new("RGB", part.size, (196, 205, 222)), (0, 0), edges_major.point(lambda v: v * 140 // 255))
    grain = Image.effect_noise(part.size, 40).convert("RGB")
    return Image.blend(bg, ImageChops.multiply(bg, ImageOps.autocontrast(grain, cutoff=2).point(
        lambda v: 215 + v * 40 // 255)), 0.55)


class GSlide(Slide):
    def __init__(self, n):
        super().__init__()
        self.im = terrain(n)
        self.d = ImageDraw.Draw(self.im)

    def counter(self, n):
        self.text(W - 60, 70, f"{n:02d} / {TOTAL:02d}", f(MED, 18), GREY, anchor="rs")

    def save(self, n):
        self.im.save(f"{OUT}slide-{n}.jpg", quality=95)

    def fit(self, lines, font_name, max_size, maxw):
        size = max_size
        while size > 40 and any(self.width(t, f(font_name, size)) > maxw for t in lines):
            size -= 2
        return size

    def check(self, x, y, r=15, fill=ORANGE):
        self.d.ellipse([k(x - r), k(y - r), k(x + r), k(y + r)], fill=fill)
        self.d.line([k(x - 7), k(y), k(x - 2), k(y + 6), k(x + 8), k(y - 6)], fill=WHITE_T, width=k(3.4),
                    joint="curve")

    def header(self, label, l1, l2, max_size=96, maxw=900):
        self.text(90, 190, label, f(SEMI, 20), ORANGE)
        self.rect(90, 208, 150, 213, ORANGE)
        size = self.fit([l1, l2], BOLD, max_size, maxw)
        self.text(88, 210 + size * 1.12, l1, f(BOLD, size), NAVY)
        self.text(88, 210 + size * 2.3, l2, f(BOLD, size), ORANGE)
        return 210 + size * 2.3

    # ── line icons, drawn inside a navy tile centred on (cx, cy) ──
    def ln(self, pts, w=7, fill=WHITE_T):
        self.d.line([(k(x), k(y)) for x, y in pts], fill=fill, width=k(w), joint="curve")

    def box(self, x0, y0, x1, y1, r=10, w=7, fill=None, outline=WHITE_T):
        self.d.rounded_rectangle([k(x0), k(y0), k(x1), k(y1)], radius=k(r), fill=fill, outline=outline,
                                 width=k(w) if outline else 0)

    def dot(self, x, y, r, fill=ORANGE):
        self.d.ellipse([k(x - r), k(y - r), k(x + r), k(y + r)], fill=fill)

    def icon(self, kind, cx, cy):
        self.rect(cx - 115, cy - 115, cx + 115, cy + 115, NAVY, r=40)
        if kind == "laptop":
            self.box(cx - 62, cy - 52, cx + 62, cy + 26, r=8)
            self.box(cx - 44, cy - 34, cx + 44, cy + 8, r=3, w=0, fill=ORANGE, outline=None)
            self.ln([(cx - 84, cy + 44), (cx + 84, cy + 44)], w=9)
        elif kind == "monitor":
            self.box(cx - 72, cy - 58, cx + 72, cy + 30, r=8)
            self.ln([(cx, cy + 32), (cx, cy + 54)], w=8)
            self.ln([(cx - 36, cy + 58), (cx + 36, cy + 58)], w=8)
            self.ln([(cx - 40, cy - 22), (cx + 10, cy - 22)], w=6, fill=ORANGE)
            self.ln([(cx - 40, cy - 2), (cx + 36, cy - 2)], w=6, fill=BLUE)
        elif kind == "keyboard":
            self.box(cx - 80, cy - 30, cx + 36, cy + 36, r=10)
            for r_ in range(2):
                for c_ in range(4):
                    x = cx - 62 + c_ * 25
                    self.dot(x + 5, cy - 8 + r_ * 22, 5, fill=WHITE_T)
            self.box(cx + 50, cy - 30, cx + 86, cy + 36, r=18, w=0, fill=ORANGE, outline=None)
            self.ln([(cx + 68, cy - 26), (cx + 68, cy - 6)], w=4, fill=NAVY)
        elif kind == "earbuds":
            for sx in (-1, 1):
                bx = cx + sx * 38
                self.dot(bx, cy - 26, 30, fill=WHITE_T)
                self.dot(bx, cy - 26, 12, fill=ORANGE)
                self.box(bx - 10 + sx * 8, cy - 8, bx + 10 + sx * 8, cy + 62, r=10, w=0, fill=WHITE_T, outline=None)
        elif kind == "power":
            self.box(cx - 70, cy - 36, cx + 58, cy + 36, r=12)
            self.box(cx + 62, cy - 14, cx + 76, cy + 14, r=4, w=0, fill=WHITE_T, outline=None)
            self.d.polygon([(k(cx + 6), k(cy - 30)), (k(cx - 26), k(cy + 6)), (k(cx - 2), k(cy + 6)),
                            (k(cx - 12), k(cy + 32)), (k(cx + 22), k(cy - 6)), (k(cx - 2), k(cy - 6))], fill=ORANGE)
        elif kind == "wifi":
            for i, r_ in enumerate((78, 52, 26)):
                self.d.arc([k(cx - r_), k(cy + 34 - r_), k(cx + r_), k(cy + 34 + r_)], 225, 315,
                           fill=WHITE_T if i < 2 else BLUE, width=k(10))
            self.dot(cx, cy + 34, 11)
        elif kind == "storage":
            self.box(cx - 48, cy - 64, cx + 48, cy + 64, r=16)
            self.ln([(cx - 22, cy + 28), (cx + 22, cy + 28)], w=6, fill=BLUE)
            self.dot(cx + 22, cy - 38, 8)
            self.d.arc([k(cx - 24), k(cy - 38), k(cx + 24), k(cy + 10)], 0, 360, fill=WHITE_T, width=k(5))
        elif kind == "phone":
            self.box(cx - 42, cy - 72, cx + 42, cy + 72, r=16)
            self.ln([(cx - 12, cy - 56), (cx + 12, cy - 56)], w=6)
            self.box(cx - 26, cy - 40, cx + 26, cy + 38, r=4, w=0, fill=ORANGE, outline=None)
            self.dot(cx, cy + 56, 6, fill=WHITE_T)
        elif kind == "extras":
            self.box(cx - 30, cy - 36, cx + 30, cy + 24, r=12, w=0, fill=WHITE_T, outline=None)
            self.ln([(cx - 14, cy - 36), (cx - 14, cy - 68)], w=9)
            self.ln([(cx + 14, cy - 36), (cx + 14, cy - 68)], w=9)
            self.ln([(cx, cy + 24), (cx, cy + 44), (cx + 30, cy + 64), (cx + 70, cy + 64)], w=8, fill=ORANGE)
        elif kind == "check":
            self.dot(cx, cy, 64, fill=ORANGE)
            self.ln([(cx - 28, cy + 2), (cx - 8, cy + 24), (cx + 30, cy - 22)], w=12)


def look_for(s, y0, items, label="WHAT TO LOOK FOR"):
    cx0, cx1 = 70, W - 70
    y1 = y0 + 116 + len(items) * 60
    s.rect(cx0, y0, cx1, y1, NAVY, r=34)
    s.text(cx0 + 56, y0 + 62, label, f(SEMI, 18), BLUE)
    s.rect(cx0 + 56, y0 + 80, cx0 + 116, y0 + 85, ORANGE)
    for j, t in enumerate(items):
        yy = y0 + 144 + j * 60
        s.check(cx0 + 72, yy - 10)
        s.text(cx0 + 106, yy, t, f(MED, 28), WHITE_T)
    return y1


def tip(s, y0, text):
    cx0, cx1 = 70, W - 70
    s.rect(cx0, y0, cx1, y0 + 132, ORANGE, r=30)
    s.rect(cx0 + 12, y0, cx1, y0 + 132, PALE, r=28)
    s.text(cx0 + 50, y0 + 50, "PRO TIP", f(SEMI, 18), ORANGE)
    s.para(cx0 + 50, y0 + 90, text, f(MED, 24), cx1 - cx0 - 100, 34, NAVY)
    return y0 + 132


def price_tag(s, x, y, r=13, fill=ORANGE):
    """Small tag glyph with its hole."""
    s.d.polygon([(k(x), k(y)), (k(x + 26), k(y)), (k(x + 40), k(y + 14)), (k(x + 26), k(y + 28)), (k(x), k(y + 28))],
                fill=fill)
    s.dot(x + 27, y + 14, 4, fill=WHITE_T)


def prices(s, y0, items):
    cx0, cx1 = 70, W - 70
    y1 = y0 + 140
    s.rect(cx0, y0, cx1, y1, WHITE_T, r=28)
    s.d.rounded_rectangle([k(cx0), k(y0), k(cx1), k(y1)], radius=k(28), outline=ORANGE, width=k(3))
    price_tag(s, cx0 + 44, y0 + 26)
    s.text(cx0 + 98, y0 + 48, "PRICE GUIDE (TZS)", f(SEMI, 18), ORANGE)
    s.text(cx1 - 40, y0 + 48, "approx. 2026", f(REG, 17), GREY, anchor="rs")
    colw = (cx1 - cx0 - 88) / len(items)
    for j, (lab, amt) in enumerate(items):
        x = cx0 + 44 + j * colw
        if j:
            s.rect(x - 22, y0 + 72, x - 20, y0 + 122, (226, 228, 233))
        s.text(x, y0 + 86, lab, f(REG, 19), GREY)
        s.text(x, y0 + 120, amt, f(BOLD, 27), NAVY)
    return y1


# ── 1 · hook ─────────────────────────────────────────────
s = GSlide(1)
s.rect(0, 830, 560, 872, BLUE)
s.rect(0, 872, 560, H, NAVY)
s.photo(470, 780, fade="left")
s.text(96, 330, "Building your tech setup?", f(MED, 30), NAVY)
lines = ["Tech Gadgets", "Every Techie", "Needs"]
size = s.fit(lines, BOLD, 112, 570)
for i, (t, c) in enumerate(zip(lines, (NAVY, ORANGE, NAVY))):
    s.text(90, 470 + i * size * 1.24, t, f(BOLD, size), c)
s.rect(210, 1128, 380, 1170, ORANGE)
s.text(96, 1060, "Privatus", f(SIG, 112), WHITE_T)
s.text(170, 1170, "Cosmas", f(SIG, 112), WHITE_T)
s.swipe(640, 1150)
s.counter(1)
s.save(1)

# ── 2–9 · gadgets ────────────────────────────────────────
gadgets = [
    ("laptop", "A Reliable", "Laptop",
     "Your main tool. Everything else on this list is optional, this one is not.",
     ["16GB RAM (8GB at the very least)", "SSD storage, 512GB if you can", "Good keyboard & 6+ hour battery"],
     "A good used business laptop beats a new cheap one. Check the battery health before you pay.",
     [("Used business", "600K – 1.2M"), ("New mid-range", "1.5M – 3M"), ("New high-end", "3.5M+")]),
    ("monitor", "An External", "Monitor",
     "Code on one screen, docs or preview on the other. Less switching, more focus.",
     ["24 inch, Full HD or better", "IPS panel for clear colours", "HDMI or USB-C that fits your laptop"],
     "No monitor yet? A TV with an HDMI port works as a second screen.",
     [("Used 24 inch", "150K – 250K"), ("New 24 inch FHD", "250K – 450K"), ("27 inch / 2K", "500K – 900K")]),
    ("keyboard", "Keyboard", "& Mouse",
     "You type all day. Comfort today saves your wrists, neck and back later.",
     ["Full-size or compact (tenkeyless) keyboard", "A mouse that fits your hand well", "Wireless with long battery life"],
     "Raise your laptop to eye level and type on an external keyboard. Instant posture fix.",
     [("Basic combo", "25K – 60K"), ("Wireless combo", "60K – 150K"), ("Mechanical", "120K – 350K")]),
    ("earbuds", "Wireless", "Earbuds",
     "Block the noise to focus deeply, and sound clear in every meeting and call.",
     ["Noise cancelling (ANC)", "A clear mic for calls", "Long battery + charging case"],
     None, None),
    ("power", "Power", "Backup",
     "Power cuts can wipe out hours of unsaved work and even damage your devices.",
     ["A UPS for your router & monitor", "A power bank that can charge a laptop", "A surge protector on every socket"],
     "Save often (Ctrl + S) and push your code to GitHub every day.",
     [("UPS", "150K – 400K"), ("Laptop power bank", "80K – 250K"), ("Surge protector", "20K – 60K")]),
    ("wifi", "Internet", "Backup",
     "No internet, no work. One connection is never enough when deadlines are close.",
     ["Home Wi-Fi or fibre as your main line", "A MiFi or 4G/5G router as backup", "Phone hotspot as the last option"],
     "Use two different networks so one outage never cuts you off completely.",
     [("MiFi", "60K – 150K"), ("4G/5G router", "100K – 300K"), ("Data / month", "30K – 100K")]),
    ("storage", "Storage &", "Backup",
     "Laptops get stolen and drives die. Your work must live in more than one place.",
     ["External SSD: fast and tough", "Flash drive for quick transfers", "Cloud: Google Drive, GitHub"],
     "Follow the 3-2-1 rule: 3 copies, on 2 devices, 1 kept off-site.",
     [("Flash drive 64GB", "15K – 35K"), ("External SSD 1TB", "180K – 400K"), ("Cloud / month", "Free – 25K")]),
    ("phone", "A Phone for", "Testing",
     "Your apps will run on phones. Test on a real device, not only an emulator.",
     ["An Android phone, even a budget one", "Enough RAM to run apps smoothly", "An authenticator app for 2FA"],
     "Test on a low-end phone too. Most of your users won't have a flagship.",
     [("Budget Android", "200K – 450K"), ("Mid-range", "500K – 1M"), ("Authenticator", "Free")]),
]
for i, (ic, l1, l2, why, look, tp, pr) in enumerate(gadgets):
    n = i + 2
    s = GSlide(n)
    bottom = s.header(f"GADGET {i + 1:02d} / 09", l1, l2, 100, maxw=640)
    s.icon(ic, W - 70 - 115, 330)
    s.swipe(W - 70 - 214, 110)
    y = s.para(92, bottom + 80, why, f(REG, 29), 900, 43, GREY)
    yb = look_for(s, y + 22, look)
    if tp:
        yt = tip(s, yb + 22, tp)
        prices(s, yt + 22, pr)
    else:  # earbuds: brand picks with prices
        yy = yb + 30
        s.text(90, yy + 40, "MY PICKS", f(SEMI, 18), ORANGE)
        s.rect(90, yy + 58, 150, yy + 63, ORANGE)
        picks = [("Oraimo", "Affordable, easy to find, strong battery life", "40K – 120K"),
                 ("Soundcore", "Great sound and noise cancelling for the price", "80K – 300K")]
        pw = (W - 140 - 18) / 2
        for j, (b, d, amt) in enumerate(picks):
            x0 = 70 + j * (pw + 18)
            s.rect(x0, yy + 80, x0 + pw, yy + 300, NAVY if j == 0 else PALE, r=26)
            s.text(x0 + 34, yy + 140, b, f(BOLD, 38), WHITE_T if j == 0 else ORANGE)
            s.para(x0 + 34, yy + 182, d, f(REG, 21), pw - 64, 30, SOFT if j == 0 else GREY)
            price_tag(s, x0 + 34, yy + 248)
            s.text(x0 + 86, yy + 272, f"TZS {amt}", f(BOLD, 26), WHITE_T if j == 0 else NAVY)
    s.counter(n)
    s.save(n)

# ── 10 · small things ────────────────────────────────────
s = GSlide(10)
bottom = s.header("GADGET 09 / 09", "The Small", "Things", 100, maxw=640)
s.icon("extras", W - 70 - 115, 330)
s.swipe(W - 70 - 214, 110)
s.para(92, bottom + 80, "Cheap extras that make long days easier and your setup look pro.", f(REG, 29), 900, 43, GREY)
extras = [("Laptop stand", "Screen at eye level, cooler laptop.", "25K – 70K"),
          ("USB-C hub", "More ports: HDMI, USB, card reader.", "40K – 120K"),
          ("A good chair", "You sit for hours. Your back matters.", "150K – 600K"),
          ("Desk lamp", "Less eye strain on late nights.", "20K – 60K"),
          ("Cable organiser", "Clean desk, clear mind.", "5K – 20K"),
          ("Webcam", "Sharp video for calls and content.", "50K – 200K")]
gx0, gy0, gap = 70, 640, 18
cw_, ch_ = (W - 140 - gap) / 2, 196
for i, (name, what, amt) in enumerate(extras):
    cx, cy = gx0 + (i % 2) * (cw_ + gap), gy0 + (i // 2) * (ch_ + gap)
    dark = (i // 2 + i % 2) % 2 == 0
    s.rect(cx, cy, cx + cw_, cy + ch_, NAVY if dark else PALE, r=26)
    s.text(cx + 34, cy + 62, name, f(BOLD, 31), WHITE_T if dark else NAVY)
    s.rect(cx + 34, cy + 80, cx + 80, cy + 85, ORANGE)
    s.para(cx + 34, cy + 122, what, f(REG, 21), cw_ - 64, 30, SOFT if dark else GREY)
    price_tag(s, cx + 34, cy + 146)
    s.text(cx + 84, cy + 170, f"TZS {amt}", f(BOLD, 23), WHITE_T if dark else NAVY)
s.text(90, gy0 + 3 * (ch_ + gap) + 24, "Prices are rough estimates for Tanzania (2026). Always compare shops.",
       f(REG, 19), GREY)
s.counter(10)
s.save(10)

# ── 11 · checklist + connect ────────────────────────────
s = GSlide(11)
s.photo(520, 760, fade="left")
s.text(90, 230, "Build It", f(BOLD, 112), NAVY)
s.text(90, 355, "Step by Step", f(BOLD, 88), ORANGE)
y = s.para(94, 430, "You don't need everything at once. Start with the laptop and add one piece at a time.",
           f(REG, 27), 470, 40, GREY)
s.bullets(96, y + 44, ["Laptop first", "Power & internet backup", "Earbuds & monitor", "Storage & the extras"],
          lh=48, title_font=f(SEMI, 27))
cx0, cy0, cx1, cy1 = 70, 950, 700, 1270
s.rect(cx0, cy0, cx1, cy1, NAVY, r=30)
s.text(cx0 + 50, cy0 + 72, "Let’s connect", f(BOLD, 38), WHITE_T)
s.rect(cx0 + 50, cy0 + 96, cx0 + 130, cy0 + 102, ORANGE)
rows = [("Phone", "+255 752 747 681"), ("Website", "depriver.tech"), ("Instagram", "@_depriver")]
for i, (lab, val) in enumerate(rows):
    yy = cy0 + 150 + i * 56
    s.text(cx0 + 50, yy, lab.upper(), f(MED, 15), BLUE)
    s.text(cx0 + 230, yy + 1, val, f(SEMI, 27), WHITE_T)
s.counter(11)
s.save(11)
print("ok")
