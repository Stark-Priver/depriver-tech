"""Shared design system for all carousels: palette, fonts, Slide helpers.
Executed by each studio/<slug>/make.py, which defines STUDIO (this folder) and OUT (its export folder)."""
import os
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageEnhance

FONTS = os.path.join(STUDIO, "fonts") + "/"
PHOTO = os.path.join(STUDIO, "assets", "photo.jpg")
W, H = 1080, 1350
K = 2  # export at 2160x2700

WHITE = (250, 250, 249)
NAVY = (11, 30, 63)
ORANGE = (232, 96, 58)
BLUE = (169, 196, 245)
INK = (24, 28, 36)
GREY = (92, 98, 110)
CHAR = (28, 30, 34)


def f(name, size):
    return ImageFont.truetype(FONTS + name, int(size * K))


BOLD, SEMI, MED, REG = "Poppins-Bold.ttf", "Poppins-SemiBold.ttf", "Poppins-Medium.ttf", "Poppins-Regular.ttf"
SIG = "MrDafoe-Regular.ttf"


def k(v):
    return int(round(v * K))


class Slide:
    def __init__(self):
        self.im = Image.new("RGB", (W * K, H * K), WHITE)
        self.d = ImageDraw.Draw(self.im)

    def rect(self, x0, y0, x1, y1, fill, r=0):
        box = [k(x0), k(y0), k(x1), k(y1)]
        if r:
            self.d.rounded_rectangle(box, radius=k(r), fill=fill)
        else:
            self.d.rectangle(box, fill=fill)

    def text(self, x, y, t, font, fill=INK, anchor="ls"):
        self.d.text((k(x), k(y)), t, font=font, fill=fill, anchor=anchor)

    def width(self, t, font):
        return self.d.textlength(t, font=font) / K

    def para(self, x, y, t, font, maxw, lh, fill=INK):
        """Word-wrapped paragraph; returns y after last line."""
        words, line = t.split(), ""
        for w in words:
            trial = (line + " " + w).strip()
            if self.width(trial, font) > maxw and line:
                self.text(x, y, line, font, fill)
                y += lh
                line = w
            else:
                line = trial
        if line:
            self.text(x, y, line, font, fill)
            y += lh
        return y

    def watermark(self, t, x, y, size):
        layer = Image.new("L", self.im.size, 0)
        ImageDraw.Draw(layer).text((k(x), k(y)), t, font=f(SIG, size), fill=255, anchor="mm")
        tint = Image.new("RGB", self.im.size, (236, 237, 240))
        self.im.paste(tint, (0, 0), layer)

    def photo(self, x0, width, fade="left", fade_w=160, bottom=H):
        """B&W high-contrast portrait on white, multiplied onto the slide so the white
        background disappears (cut-out look). Anchored to the bottom edge; one side feathered."""
        src = Image.open(PHOTO).convert("L")
        src = ImageOps.autocontrast(src, cutoff=0.5)
        src = ImageEnhance.Contrast(src).enhance(1.18)
        src = src.point(lambda v: 255 if v > 232 else v)  # clean studio white -> pure white
        pw = k(width)
        ph = int(pw * src.height / src.width)
        pic = src.resize((pw, ph), Image.LANCZOS)
        white = Image.new("L", (pw, ph), 255)
        mask = Image.new("L", (pw, ph), 255)
        md = ImageDraw.Draw(mask)
        fw = k(fade_w)
        for i in range(fw):
            a = int(255 * (i / fw) ** 1.4)
            if fade in ("left", "both"):
                md.line([(i, 0), (i, ph)], fill=a)
            if fade in ("right", "both"):
                md.line([(pw - 1 - i, 0), (pw - 1 - i, ph)], fill=a)
        pic = Image.composite(pic, white, mask).convert("RGB")
        X, Y = k(x0), k(bottom) - ph
        # crop to canvas, then multiply onto what is already there
        cx0, cy0 = max(X, 0), max(Y, 0)
        cx1, cy1 = min(X + pw, self.im.width), min(Y + ph, self.im.height)
        region = self.im.crop((cx0, cy0, cx1, cy1))
        part = pic.crop((cx0 - X, cy0 - Y, cx1 - X, cy1 - Y))
        self.im.paste(ImageChops.multiply(region, part), (cx0, cy0))

    def swipe(self, x, y):
        w, h = 214, 72
        sh = Image.new("L", self.im.size, 0)
        ImageDraw.Draw(sh).rounded_rectangle([k(x + 4), k(y + 8), k(x + w + 4), k(y + h + 8)], radius=k(16), fill=90)
        sh = sh.filter(ImageFilter.GaussianBlur(k(8)))
        self.im.paste(Image.new("RGB", self.im.size, (40, 40, 40)), (0, 0), sh)
        self.rect(x, y, x + w, y + h, ORANGE, r=16)
        self.text(x + 30, y + h / 2 + 2, "Swipe", f(SEMI, 34), (255, 255, 255), anchor="lm")
        ax, ay = x + 172, y + h / 2
        self.d.line([k(ax - 18), k(ay), k(ax + 12), k(ay)], fill=(255, 255, 255), width=k(4))
        self.d.line([k(ax), k(ay - 12), k(ax + 12), k(ay), k(ax), k(ay + 12)], fill=(255, 255, 255), width=k(4),
                    joint="curve")

    def counter(self, n):
        self.text(W - 60, 70, f"{n:02d} / 05", f(MED, 18), GREY, anchor="rs")

    def bullets(self, x, y, items, lh=52, title_font=None, body_font=None, maxw=520):
        tf = title_font or f(SEMI, 30)
        for item in items:
            if isinstance(item, tuple):
                title, body = item
                self.d.ellipse([k(x), k(y - 16), k(x + 12), k(y - 4)], fill=ORANGE)
                self.text(x + 28, y, title, tf, INK)
                y = self.para(x + 28, y + 40, body, body_font or f(REG, 24), maxw, 36, GREY) + 26
            else:
                self.d.ellipse([k(x), k(y - 16), k(x + 12), k(y - 4)], fill=ORANGE)
                self.text(x + 28, y, item, tf, INK)
                y += lh
        return y

    def save(self, n):
        self.im.save(f"{OUT}slide-{n}.jpg", quality=95)


