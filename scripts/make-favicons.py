#!/usr/bin/env python3
"""Favicons + app icons from the portrait (public/img/me-cut.webp): navy disc, orange ring, B&W face."""
from PIL import Image, ImageDraw, ImageEnhance
from pathlib import Path

root = Path(__file__).resolve().parent.parent
cut = Image.open(root / "public/img/me-cut.webp").convert("RGBA")
W, H = cut.size
NAVY, ORANGE = (11, 30, 63, 255), (232, 96, 58, 255)
wide = cut.crop((int(W * 0.16), int(H * 0.10), int(W * 0.84), int(H * 0.10) + int(W * 0.68)))   # head & shoulders
tight = cut.crop((int(W * 0.24), int(H * 0.13), int(W * 0.76), int(H * 0.13) + int(W * 0.52)))  # face, for tiny sizes

def icon(size):
    head = tight if size <= 48 else wide
    S = size * 4
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(im).ellipse([0, 0, S - 1, S - 1], fill=NAVY)
    inset = int(S * 0.07)
    face = head.resize((S - 2 * inset, S - 2 * inset), Image.LANCZOS)
    rgb = ImageEnhance.Contrast(face.convert("RGB")).enhance(1.2 if size <= 48 else 1.12)
    face = Image.merge("RGBA", (*rgb.split(), face.getchannel("A")))
    layer = Image.new("RGBA", (S, S), (0, 0, 0, 0)); layer.paste(face, (inset, inset), face)
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).ellipse([inset, inset, S - 1 - inset, S - 1 - inset], fill=255)
    im = Image.composite(Image.alpha_composite(im, layer), im, mask)
    w = max(4, int(S * (0.075 if size <= 48 else 0.055)))
    ImageDraw.Draw(im).ellipse([w // 2, w // 2, S - 1 - w // 2, S - 1 - w // 2], outline=ORANGE, width=w)
    return im.resize((size, size), Image.LANCZOS)

def square(size, pad):
    S = size * 2
    im = Image.new("RGBA", (S, S), NAVY)
    inner = int(S * (1 - pad * 2))
    im.alpha_composite(icon(inner // 2).resize((inner, inner), Image.LANCZOS), ((S - inner) // 2, (S - inner) // 2))
    return im.resize((size, size), Image.LANCZOS).convert("RGB")

pub = root / "public"
icon(16).save(pub / "favicon-16.png")
icon(32).save(pub / "favicon-32.png")
icon(48).save(pub / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)], append_images=[icon(16), icon(32)])
square(180, 0.06).save(pub / "apple-touch-icon.png")
icon(192).save(pub / "icon-192.png")
icon(512).save(pub / "icon-512.png", optimize=True)
square(512, 0.12).save(pub / "icon-maskable-512.png", optimize=True)
print("icons written")
