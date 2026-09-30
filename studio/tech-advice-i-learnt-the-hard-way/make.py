"""Carousel: Tech advice I learnt the hard way (11 slides, 1080x1350, exported at 2x).
Site palette on terrain paper, neumorphic cards, frosted-glass panels over colour glows,
and cartoon vector illustrations (SVG rasterised with rsvg-convert). No portrait on this one."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers

import io
import re
import subprocess
import tempfile

ROOT = os.path.dirname(STUDIO)
PAPER = (244, 245, 248)
HI, LO = (255, 255, 255), (208, 214, 226)
YELLOW, GREEN = (255, 200, 87), (61, 220, 132)
TOTAL = 11

# ── helpers: SVG → image, soft shadows, glass, neumorphism ───────────────────────────────────────
FONTCONF = os.path.join(tempfile.gettempdir(), "depriver-studio-fonts.conf")
with open(FONTCONF, "w") as fc:
    fc.write(f'<?xml version="1.0"?><fontconfig><dir>{STUDIO}/fonts</dir><include ignore_missing="yes">/etc/fonts/fonts.conf</include></fontconfig>')


def dedupe_attrs(svg):
    """Shapes may override the shared outline style (e.g. {ST} stroke-width="5"): keep the last value per tag."""
    def fix(tag):
        t = tag.group(0)
        for attr in set(re.findall(r'\s([a-z-]+)="', t)):
            hits = list(re.finditer(rf'\s{attr}="[^"]*"', t))
            for h in reversed(hits[:-1]):
                t = t[:h.start()] + t[h.end():]
        return t
    return re.sub(r"<[^!?/][^>]*>", fix, svg)


def svg_image(svg, width):
    """Rasterise an SVG string (Poppins available to it) to an RGBA image `width` px wide."""
    svg = dedupe_attrs(svg)
    r = subprocess.run(["rsvg-convert", "-w", str(width), "-f", "png"], input=svg.encode(), capture_output=True,
                       env={**os.environ, "FONTCONFIG_FILE": FONTCONF})
    if r.returncode:
        raise RuntimeError(f"rsvg-convert: {r.stderr.decode().strip()}")
    return Image.open(io.BytesIO(r.stdout)).convert("RGBA")


def rr_mask(size, box, r):
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle([k(v) for v in box], radius=k(r), fill=255)
    return m


def shadow(im, box, r, color, offset, blur, strength=255):
    x0, y0, x1, y1 = box
    m = rr_mask(im.size, (x0 + offset[0], y0 + offset[1], x1 + offset[0], y1 + offset[1]), r)
    m = m.filter(ImageFilter.GaussianBlur(k(blur))).point(lambda v: v * strength // 255)
    im.paste(Image.new("RGB", im.size, color), (0, 0), m)


def neu(s, box, r=36, depth=1.0, fill=PAPER):
    """Raised neumorphic surface: light from top-left, soft shade bottom-right."""
    shadow(s.im, box, r, HI, (-12 * depth, -12 * depth), 14 * depth)
    shadow(s.im, box, r, LO, (14 * depth, 16 * depth), 18 * depth)
    s.im.paste(Image.new("RGB", s.im.size, fill), (0, 0), rr_mask(s.im.size, box, r))


def neu_inset(s, box, r=20, fill=PAPER):
    """Pressed-in neumorphic well."""
    size = s.im.size
    base = rr_mask(size, box, r)
    s.im.paste(Image.new("RGB", size, fill), (0, 0), base)
    for color, off in ((LO, (6, 6)), (HI, (-6, -6))):
        hole = rr_mask(size, (box[0] + off[0], box[1] + off[1], box[2] + off[0], box[3] + off[1]), r)
        edge = ImageChops.subtract(base, hole).filter(ImageFilter.GaussianBlur(k(5)))
        s.im.paste(Image.new("RGB", size, color), (0, 0), ImageChops.multiply(edge, base))


def glass(s, box, r=44, tint=(255, 255, 255), alpha=0.42, blur=26, border=True):
    """Frosted glass: blur what's behind, tint it, add a bright rim and a soft drop shadow."""
    shadow(s.im, box, r, (150, 160, 185), (0, 26), 34, 140)
    x0, y0, x1, y1 = [k(v) for v in box]
    region = s.im.crop((x0, y0, x1, y1)).filter(ImageFilter.GaussianBlur(k(blur)))
    region = ImageEnhance.Color(region).enhance(1.35)
    region = Image.blend(region, Image.new("RGB", region.size, tint), alpha)
    m = rr_mask(s.im.size, box, r).crop((x0, y0, x1, y1))
    s.im.paste(region, (x0, y0), m)
    if border:
        s.d.rounded_rectangle([x0, y0, x1, y1], radius=k(r), outline=(255, 255, 255), width=k(2.5))
        s.d.line([x0 + k(r), y0 + k(3), x1 - k(r), y0 + k(3)], fill=(255, 255, 255), width=k(2))


def glows(s, spots):
    layer = Image.new("RGB", s.im.size, PAPER)
    mask = Image.new("L", s.im.size, 0)
    for (x, y, rad, color, a) in spots:
        spot = Image.new("L", s.im.size, 0)
        ImageDraw.Draw(spot).ellipse([k(x - rad), k(y - rad), k(x + rad), k(y + rad)], fill=int(255 * a))
        layer.paste(Image.new("RGB", s.im.size, color), (0, 0), spot)
        mask = ImageChops.lighter(mask, spot)
    blurred_mask = mask.filter(ImageFilter.GaussianBlur(k(70)))
    s.im.paste(layer.filter(ImageFilter.GaussianBlur(k(70))), (0, 0), blurred_mask)


_TERRAIN = None


def paper(s):
    """Site paper: soft grey-blue terrain lines (same artwork as depriver.tech)."""
    global _TERRAIN
    if _TERRAIN is None:
        svg = open(os.path.join(ROOT, "public", "terrain-light.svg")).read()
        t = svg_image(svg, k(W) * 2)                      # svg is 1.6:1, cover the 4:5 slide
        t = t.resize((round(t.width * k(H) / t.height), k(H)), Image.LANCZOS)
        left = (t.width - k(W)) // 2
        _TERRAIN = t.crop((left, 0, left + k(W), k(H)))
    s.im.paste(Image.new("RGB", s.im.size, PAPER))
    s.im.paste(Image.new("RGB", s.im.size, (213, 219, 231)), (0, 0), _TERRAIN.getchannel("A").point(lambda v: v * 200 // 255))


def place_art(s, key, box, pad=30):
    """Fit an illustration (600x420 art board) inside a panel, centred, without spilling out."""
    x0, y0, x1, y1 = box
    h = (y1 - y0) - 2 * pad
    w = min((x1 - x0) - 2 * pad, h * 600 / 420)
    art = svg_image(ART[key], k(w))
    s.im.paste(art, (k(x0 + ((x1 - x0) - w) / 2), k(y0 + ((y1 - y0) - art.height / K) / 2)), art)


def check(s, x, y, r=17):
    s.d.ellipse([k(x - r), k(y - r), k(x + r), k(y + r)], fill=ORANGE)
    s.d.line([k(x - 8), k(y + 1), k(x - 2), k(y + 7), k(x + 9), k(y - 6)], fill=(255, 255, 255), width=k(3.6), joint="curve")


def pill(s, x, y, text, font, raised=True, anchor_right=False, color=None):
    w = s.width(text, font) + 48
    if anchor_right:
        x -= w
    box = (x, y, x + w, y + 60)
    neu(s, box, 30, 0.55) if raised else glass(s, box, 30, alpha=0.5, blur=16)
    s.text(x + w / 2, y + 31, text, font, color or NAVY, anchor="mm")
    return box


def swipe_btn(s, x, y):
    w, h = 190, 64
    shadow(s.im, (x, y, x + w, y + h), 18, (232, 150, 125), (0, 14), 14)
    s.rect(x, y, x + w, y + h, ORANGE, r=18)
    s.text(x + 30, y + h / 2 + 1, "Swipe", f(SEMI, 25), (255, 255, 255), anchor="lm")
    ax, ay = x + 150, y + h / 2
    s.d.line([k(ax - 16), k(ay), k(ax + 12), k(ay)], fill=(255, 255, 255), width=k(3.6))
    s.d.line([k(ax), k(ay - 11), k(ax + 12), k(ay), k(ax), k(ay + 11)], fill=(255, 255, 255), width=k(3.6), joint="curve")


def brand(s):
    s.text(70, 104, "Privatus", f(SIG, 50), NAVY)
    s.text(262, 100, "depriver.tech", f(SEMI, 20), GREY)


# ── cartoon vector illustrations (flat colours, navy outlines, little faces) ─────────────────────
ST = 'stroke="#0b1e3f" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'


def face(x, y, sc=1):
    return f'''<g transform="translate({x} {y}) scale({sc})">
    <circle cx="-16" cy="0" r="6" fill="#0b1e3f"/><circle cx="16" cy="0" r="6" fill="#0b1e3f"/>
    <circle cx="-14" cy="-2" r="2" fill="#fff"/><circle cx="18" cy="-2" r="2" fill="#fff"/>
    <ellipse cx="-30" cy="12" rx="8" ry="5" fill="#ff9f8a" opacity=".85"/><ellipse cx="30" cy="12" rx="8" ry="5" fill="#ff9f8a" opacity=".85"/>
    <path d="M-10 12 Q0 22 10 12" fill="none" stroke="#0b1e3f" stroke-width="5" stroke-linecap="round"/></g>'''


def spark(x, y, sc=1, c="#ffc857"):
    return f'<path transform="translate({x} {y}) scale({sc})" d="M0-18 L5-5 L18 0 L5 5 L0 18 L-5 5 L-18 0 L-5-5Z" fill="{c}" {ST} stroke-width="4"/>'


def heart(x, y, sc=1, c="#e8603a"):
    return f'<path transform="translate({x} {y}) scale({sc})" d="M0 14 C-26-4-22-26-8-26 C-2-26 0-20 0-18 C0-20 2-26 8-26 C22-26 26-4 0 14Z" fill="{c}" {ST} stroke-width="4"/>'


def svg(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 420">{body}</svg>'


GROUND = '<ellipse cx="300" cy="392" rx="230" ry="18" fill="#0b1e3f" opacity=".12"/>'

ART = {
    "rocket": svg(GROUND + f'''
      <path d="M110 330 h380 l40 40 H70z" fill="#c9d4ea" {ST}/>
      <rect x="140" y="130" width="320" height="200" rx="18" fill="#fff" {ST}/>
      <rect x="162" y="152" width="276" height="156" rx="10" fill="#0b1e3f"/>
      <path d="M186 186 h70 M186 212 h120 M270 238 h60 M186 238 h54" stroke="#a9c4f5" stroke-width="8" stroke-linecap="round"/>
      <path d="M186 186 h30" stroke="#e8603a" stroke-width="8" stroke-linecap="round"/>
      <g transform="translate(300 272) scale(0.7)"><circle cx="-16" cy="0" r="7" fill="#fff"/><circle cx="16" cy="0" r="7" fill="#fff"/>
        <path d="M-10 14 Q0 24 10 14" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/></g>
      <g transform="translate(420 110) rotate(35)">
        <path d="M0-120 C40-80 44-10 30 40 H-30 C-44-10-40-80 0-120Z" fill="#fff" {ST}/>
        <circle cx="0" cy="-50" r="20" fill="#a9c4f5" {ST}/>
        <path d="M-30 10 L-62 50 L-30 40Z M30 10 L62 50 L30 40Z" fill="#e8603a" {ST}/>
        <path d="M-18 44 Q0 110 18 44Z" fill="#ffc857" {ST} stroke-width="5"/>
        <path d="M-8 44 Q0 80 8 44Z" fill="#e8603a"/></g>
      {spark(90, 110, 1.2)}{spark(535, 300, 0.9, "#a9c4f5")}{spark(530, 40, 0.7, "#e8603a")}'''),

    "start": svg(GROUND + f'''
      <path d="M70 330 h300 l30 36 H40z" fill="#c9d4ea" {ST}/>
      <rect x="90" y="150" width="260" height="180" rx="16" fill="#e7ecf6" {ST}/>
      <rect x="110" y="170" width="220" height="140" rx="8" fill="#fff" {ST} stroke-width="4"/>
      <path d="M296 150 l44 64" stroke="#ffc857" stroke-width="22" opacity=".9"/>
      {face(220, 235)}
      <rect x="420" y="170" width="110" height="200" rx="24" fill="#e8603a" {ST}/>
      <rect x="438" y="192" width="74" height="70" rx="8" fill="#a9c4f5" {ST} stroke-width="4"/>
      <g fill="#fff" {ST} stroke-width="3">{"".join(f'<circle cx="{452 + c * 23}" cy="{290 + r * 24}" r="7"/>' for r in range(3) for c in range(3))}</g>
      {face(475, 226, 0.55)}
      {heart(475, 120, 1.3)}
      {spark(560, 90, 0.8)}{spark(70, 100, 0.9, "#a9c4f5")}'''),

    "skills": svg(GROUND + f'''
      <path d="M240 300 h120 v40 a20 20 0 0 1-20 20 h-80 a20 20 0 0 1-20-20z" fill="#c9d4ea" {ST}/>
      <path d="M300 60 a120 120 0 0 1 70 218 v22 h-140 v-22 a120 120 0 0 1 70-218z" fill="#ffc857" {ST}/>
      <path d="M270 300 v-60 l30 24 30-24 v60" fill="none" {ST} stroke-width="5"/>
      {face(300, 170)}
      <g transform="translate(110 150)"><circle r="46" fill="#a9c4f5" {ST}/><path d="M-14-14 L-28 0 L-14 14 M14-14 L28 0 L14 14" fill="none" {ST}/></g>
      <g transform="translate(490 150)"><circle r="46" fill="#e8603a" {ST}/><circle r="16" fill="#fff" {ST} stroke-width="5"/>
        {"".join(f'<rect x="-7" y="-40" width="14" height="14" rx="3" fill="#fff" {ST} stroke-width="4" transform="rotate({a})"/>' for a in range(0, 360, 60))}</g>
      <g transform="translate(470 320) rotate(-10)"><rect x="-50" y="-34" width="100" height="68" rx="8" fill="#fff" {ST} stroke-width="5"/>
        <path d="M-30-12 h60 M-30 6 h40" stroke="#a9c4f5" stroke-width="6" stroke-linecap="round"/><circle cx="30" cy="16" r="10" fill="#e8603a"/>
        <path d="M-60-44 L60 44" stroke="#e8603a" stroke-width="10" stroke-linecap="round"/></g>
      {spark(170, 60, 0.9)}{spark(430, 50, 0.7, "#e8603a")}'''),

    "habit": svg(GROUND + f'''
      <rect x="330" y="70" width="220" height="230" rx="20" fill="#fff" {ST}/>
      <path d="M350 70 h180 a20 20 0 0 1 20 20 v36 h-220 v-36 a20 20 0 0 1 20-20z" fill="#e8603a" {ST}/>
      <path d="M375 56 v30 M505 56 v30" {ST} stroke-width="8"/>
      {"".join((f'<path d="M{362 + c * 48 - 10} {150 + r * 46} l8 8 14-16" fill="none" stroke="#2fbf6c" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>' if r * 4 + c < 9 else f'<circle cx="{362 + c * 48}" cy="{150 + r * 46}" r="9" fill="none" stroke="#c9d4ea" stroke-width="5"/>') for r in range(3) for c in range(4))}
      <path d="M110 300 h150 l-18 80 h-114z" fill="#e8603a" {ST}/>
      <path d="M100 300 h170" {ST} stroke-width="10"/>
      <path d="M185 300 C185 240 180 200 185 150" fill="none" stroke="#2f9e5e" stroke-width="10" stroke-linecap="round"/>
      <path d="M185 220 C130 220 110 180 120 160 C160 160 185 180 185 220Z" fill="#3ddc84" {ST} stroke-width="5"/>
      <path d="M185 190 C240 190 260 150 250 130 C210 130 185 150 185 190Z" fill="#3ddc84" {ST} stroke-width="5"/>
      <circle cx="185" cy="118" r="34" fill="#ffc857" {ST} stroke-width="5"/>
      {face(185, 116, 0.6)}
      {spark(270, 70, 0.8)}{spark(80, 110, 0.7, "#a9c4f5")}'''),

    "public": svg(GROUND + f'''
      <rect x="60" y="80" width="340" height="260" rx="22" fill="#fff" {ST}/>
      <path d="M60 130 h340" {ST}/><circle cx="92" cy="105" r="8" fill="#e8603a"/><circle cx="118" cy="105" r="8" fill="#ffc857"/><circle cx="144" cy="105" r="8" fill="#3ddc84"/>
      <rect x="90" y="160" width="130" height="90" rx="12" fill="#a9c4f5" {ST} stroke-width="4"/>
      <path d="M130 225 l20-22 20 16 26-30" fill="none" stroke="#0b1e3f" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M240 170 h130 M240 200 h100 M240 230 h120 M90 280 h270 M90 306 h180" stroke="#c9d4ea" stroke-width="10" stroke-linecap="round"/>
      <g transform="translate(455 250) rotate(-18)">
        <path d="M-70-30 L40-80 V80 L-70 30Z" fill="#e8603a" {ST}/>
        <rect x="-100" y="-30" width="34" height="60" rx="10" fill="#fff" {ST}/>
        <path d="M-60 30 L-40 90 H-10 L-26 38" fill="#fff" {ST} stroke-width="5"/>
        <ellipse cx="42" cy="0" rx="14" ry="80" fill="#ffc857" {ST}/>
        {face(-14, 0, 0.55)}</g>
      {heart(530, 110, 1.1)}{heart(565, 190, 0.8, "#ff9f8a")}
      <g transform="translate(505 50)"><circle r="22" fill="#a9c4f5" {ST} stroke-width="4"/>
        <path d="M-9 0 h6 v12 h-6z M-1 0 l6-12 a4 4 0 0 1 6 4 l-2 8 h8 v12 h-18z" fill="#fff" stroke="#0b1e3f" stroke-width="3"/></g>'''),

    "hustle": svg(GROUND + f'''
      <path d="M200 110 v-50 M400 110 v-50" {ST} stroke-width="10"/>
      <circle cx="200" cy="56" r="10" fill="#e8603a" {ST} stroke-width="4"/><circle cx="400" cy="56" r="10" fill="#e8603a" {ST} stroke-width="4"/>
      <rect x="140" y="110" width="320" height="170" rx="40" fill="#fff" {ST}/>
      {face(300, 180)}
      <circle cx="190" cy="250" r="8" fill="#3ddc84"/><circle cx="216" cy="250" r="8" fill="#3ddc84"/><circle cx="242" cy="250" r="8" fill="#ffc857"/>
      <path d="M110 150 a60 60 0 0 0 0 90 M80 120 a100 100 0 0 0 0 150" fill="none" stroke="#a9c4f5" stroke-width="10" stroke-linecap="round"/>
      <path d="M490 150 a60 60 0 0 1 0 90 M520 120 a100 100 0 0 1 0 150" fill="none" stroke="#a9c4f5" stroke-width="10" stroke-linecap="round"/>
      {"".join(f'<ellipse cx="470" cy="{360 - i * 18}" rx="46" ry="14" fill="#ffc857" {ST} stroke-width="5"/>' for i in range(4))}
      <text x="470" y="313" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="22" fill="#0b1e3f">TSh</text>
      <g transform="translate(120 330)"><rect x="-40" y="-26" width="80" height="52" rx="10" fill="#e8603a" {ST} stroke-width="5"/>
        <path d="M-16-26 v-10 h32 v10" fill="none" {ST} stroke-width="5"/><path d="M-40 -2 h80" {ST} stroke-width="4"/></g>
      {spark(545, 60, 0.8)}{spark(60, 70, 0.7, "#e8603a")}'''),

    "people": svg(GROUND + f'''
      <path d="M160 190 L300 110 L440 190 L300 290Z M160 190 L440 190 M300 110 L300 290" fill="none" stroke="#a9c4f5" stroke-width="8" stroke-dasharray="4 16" stroke-linecap="round"/>
      {"".join(f"""<g transform="translate({x} {y})"><path d="M-58 90 a58 50 0 0 1 116 0z" fill="{shirt}" {ST}/>
        <circle r="48" fill="{skin}" {ST}/><path d="M-46 -14 a48 48 0 0 1 92 0 a40 30 0 0 0-92 0z" fill="#0b1e3f"/>
        <g transform="translate(0 6)"><circle cx="-15" cy="0" r="5" fill="#fff"/><circle cx="15" cy="0" r="5" fill="#fff"/>
        <path d="M-10 16 Q0 24 10 16" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/></g></g>"""
        for x, y, skin, shirt in [(300, 110, "#8d5524", "#e8603a"), (160, 190, "#6b3e1d", "#a9c4f5"), (440, 190, "#a0673a", "#ffc857"), (300, 290, "#7a4a26", "#3ddc84")])}
      {heart(300, 205, 1.1)}
      {spark(80, 80, 0.8)}{spark(530, 330, 0.8, "#e8603a")}'''),

    "health": svg(GROUND + f'''
      <path d="M300 340 C170 260 120 190 150 130 C180 70 260 80 300 140 C340 80 420 70 450 130 C480 190 430 260 300 340Z" fill="#e8603a" {ST}/>
      {face(300, 200)}
      <g transform="translate(470 300) rotate(-30)"><rect x="-70" y="-8" width="140" height="16" rx="8" fill="#c9d4ea" {ST} stroke-width="5"/>
        <rect x="-86" y="-34" width="26" height="68" rx="8" fill="#0b1e3f"/><rect x="60" y="-34" width="26" height="68" rx="8" fill="#0b1e3f"/></g>
      <g transform="translate(110 290)"><rect x="-26" y="-60" width="52" height="110" rx="16" fill="#a9c4f5" {ST} stroke-width="5"/>
        <rect x="-16" y="-78" width="32" height="20" rx="6" fill="#fff" {ST} stroke-width="5"/><path d="M-26 -10 h52" stroke="#fff" stroke-width="6"/></g>
      <path d="M505 55 a42 42 0 1 0 40 58 a34 34 0 1 1-40-58z" fill="#ffc857" {ST} stroke-width="5"/>
      <text x="444" y="70" font-family="Poppins" font-weight="700" font-size="28" fill="#0b1e3f">z</text>
      <text x="418" y="100" font-family="Poppins" font-weight="700" font-size="20" fill="#0b1e3f">z</text>
      {spark(90, 90, 0.8, "#a9c4f5")}'''),

    "path": svg(GROUND + f'''
      <path d="M40 390 C160 330 120 250 260 230 C400 210 360 130 520 110" fill="none" stroke="#c9d4ea" stroke-width="54" stroke-linecap="round"/>
      <path d="M40 390 C160 330 120 250 260 230 C400 210 360 130 520 110" fill="none" stroke="#fff" stroke-width="6" stroke-dasharray="18 22" stroke-linecap="round"/>
      <path d="M520 110 V30" {ST} stroke-width="7"/><path d="M520 32 l56 18 -56 18z" fill="#e8603a" {ST} stroke-width="5"/>
      <path d="M200 380 V150" {ST} stroke-width="12"/>
      <path d="M210 150 h150 l26 26 -26 26 h-150z" fill="#e8603a" {ST} stroke-width="5"/>
      <text x="228" y="186" font-family="Poppins" font-weight="700" font-size="24" fill="#fff">Diploma</text>
      <path d="M190 220 h-130 l-26 24 26 24 h130z" fill="#e7ecf6" {ST} stroke-width="5"/>
      <text x="66" y="253" font-family="Poppins" font-weight="600" font-size="22" fill="#5c626e">A-Level</text>
      <circle cx="200" cy="318" r="40" fill="#ffc857" {ST} stroke-width="5"/>
      {face(200, 316, 0.6)}
      {spark(430, 300, 0.9)}{spark(565, 200, 0.7, "#a9c4f5")}'''),

    "backup": svg(GROUND + f'''
      <path d="M190 250 a70 70 0 0 1 10-140 a100 100 0 0 1 190-10 a80 80 0 0 1 20 150z" fill="#fff" {ST}/>
      {face(300, 170)}
      <g transform="translate(300 300)"><path d="M0-60 L70-36 V10 C70 50 30 76 0 88 C-30 76-70 50-70 10 V-36Z" fill="#e8603a" {ST}/>
        <rect x="-26" y="-6" width="52" height="42" rx="8" fill="#fff" {ST} stroke-width="5"/><path d="M-16-6 v-12 a16 16 0 0 1 32 0 v12" fill="none" {ST} stroke-width="5"/></g>
      {"".join(f"""<g transform="translate({x} {y})"><path d="M-44-30 h30 l10 10 h48 v54 h-88z" fill="{c}" {ST} stroke-width="5"/>
        <text x="0" y="18" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="30" fill="#0b1e3f">{n}</text></g>"""
        for x, y, c, n in [(100, 300, "#a9c4f5", "1"), (100, 190, "#ffc857", "2"), (505, 250, "#3ddc84", "3")])}
      <path d="M150 300 H228 M150 190 C190 190 200 215 222 228 M455 250 C420 250 410 280 380 290" fill="none" stroke="#0b1e3f" stroke-width="4" stroke-dasharray="6 10" stroke-linecap="round"/>
      {spark(525, 90, 0.8)}{spark(80, 90, 0.7, "#e8603a")}'''),
}

# ── content ──────────────────────────────────────────────────────────────────────────────────────
LESSONS = [
    ("start", "Start with", "what you have", "Anza na ulichonacho",
     "I once went back to university with only a small feature phone. Don't wait for the perfect laptop. Start today.",
     ["Learn on your phone with free apps", "Use campus and library computers", "Upgrade when the work starts paying"]),
    ("skills", "Skills can't", "be stolen", "Ujuzi hauibiwi",
     "I lost my laptop, phone and certificates in one night. What I knew came home with me.",
     ["Invest in learning, not only papers", "Build projects that prove your skills", "Keep learning after class ends"]),
    ("habit", "Consistency", "beats talent", "Haba na haba hujaza kibaba",
     "Thirty minutes every day beats five hours once a week. Small steps add up faster than you think.",
     ["Pick a fixed daily learning time", "Track your streak", "Missed a day? Never miss two"]),
    ("public", "Build in", "public", "Onyesha kazi yako",
     "Nobody can hire what they can't see. Share what you learn and what you build.",
     ["Push your projects to GitHub", "Post progress, not perfection", "Write about what you learnt"]),
    ("hustle", "Solve real", "problems", "Tatua matatizo halisi",
     "Reselling Wi-Fi and repairing computers taught me more business than any class did.",
     ["Find a problem near you", "Charge fairly, deliver well", "Learn from every customer"]),
    ("people", "Your people", "matter", "Mtu ni watu",
     "Friends, teachers and customers carried me through my hardest seasons. Nobody makes it alone.",
     ["Help others generously", "Ask for help with context", "Stay in touch, not only when in need"]),
    ("health", "Protect", "your health", "Afya ni mtaji",
     "Stomach ulcers taught me early: no deadline and no code is worth your health.",
     ["Sleep, drink water, move your body", "Take real breaks from the screen", "Talk to someone when it's heavy"]),
    ("path", "Your path", "is valid", "Njia yako ni yako",
     "People said a diploma was for those who failed. It became my way into tech.",
     ["Choose what fits your goals", "Listen to advice, ignore the noise", "Compare yourself to yesterday"]),
    ("backup", "Back up", "everything", "Usiweke mayai yote kwenye kikapu kimoja",
     "Laptops get stolen and drives fail. Protect your work before you need to.",
     ["3 copies · 2 devices · 1 in the cloud", "Push your code to GitHub daily", "Turn on 2FA everywhere"]),
]
assert len(LESSONS) + 2 == TOTAL

STAGE_GLOWS = [(930, 330, 250, ORANGE, 0.85), (140, 520, 230, (111, 155, 255), 0.8), (720, 560, 150, YELLOW, 0.7)]


def new_slide():
    s = Slide()
    paper(s)
    return s


def fit(s, text, name, size, maxw):
    while size > 30 and s.width(text, f(name, size)) > maxw:
        size -= 2
    return size


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = new_slide()
glows(s, [(900, 760, 280, ORANGE, 0.85), (160, 900, 250, (111, 155, 255), 0.8), (640, 1000, 170, YELLOW, 0.7)])
brand(s)
swipe_btn(s, W - 70 - 190, 60)
pill(s, 70, 180, "For everyone in tech · Kwa wote kwenye tech", f(SEMI, 23))
for i, (t, c) in enumerate([("Tech advice", NAVY), ("I learnt the", NAVY), ("hard way", ORANGE)]):
    s.text(66, 360 + i * 104, t, f(BOLD, 100), c)
s.text(72, 628, "Mambo niliyojifunza kwa njia ngumu", f(SIG, 54), ORANGE)
stage = (70, 690, W - 70, 1170)
glass(s, stage, 46)
place_art(s, "rocket", stage, pad=34)
pill(s, 100, 1120, "9 lessons · masomo 9", f(SEMI, 22), raised=False)
pill(s, W - 100, 710, "Save this for later", f(SEMI, 22), raised=False, anchor_right=True)
s.text(72, 1262, "From my journey · Kagera to Mbeya", f(MED, 24), GREY)
pill(s, W - 70, 1222, f"01 / {TOTAL}", f(SEMI, 20), anchor_right=True)
s.save(1)

# ── 2–10 · lessons ───────────────────────────────────────────────────────────────────────────────
for i, (art_key, t1, t2, sw, body, todo) in enumerate(LESSONS):
    n = i + 2
    s = new_slide()
    glows(s, STAGE_GLOWS)
    brand(s)
    pill(s, W - 70, 62, f"{n:02d} / {TOTAL}", f(SEMI, 20), anchor_right=True)

    stage = (70, 170, W - 70, 620)
    glass(s, stage, 44)
    place_art(s, art_key, stage, pad=26)
    neu(s, (104, 130, 208, 234), 30, 0.8)                       # lesson number badge
    s.text(156, 184, f"{i + 1:02d}", f(BOLD, 40), ORANGE, anchor="mm")
    tag = "Methali" if sw.startswith(("Haba", "Mtu ni", "Usiweke", "Afya")) else "Kiswahili"
    pill(s, W - 100, 540, tag, f(SEMI, 20), raised=False, anchor_right=True)

    size = fit(s, f"{t1} {t2}", BOLD, 70, W - 150)
    s.text(74, 718, t1 + " ", f(BOLD, size), NAVY)
    s.text(74 + s.width(t1 + " ", f(BOLD, size)), 718, t2, f(BOLD, size), ORANGE)
    s.text(78, 786, sw, f(SIG, fit(s, sw, SIG, 54, W - 150)), ORANGE)
    s.para(78, 842, body, f(REG, 27), W - 156, 40, GREY)

    card = (70, 960, W - 70, 1286)
    neu(s, card, 36)
    s.text(card[0] + 36, card[1] + 54, "FANYA HIVI · DO THIS", f(SEMI, 18), ORANGE)
    s.rect(card[0] + 300, card[1] + 47, card[2] - 36, card[1] + 49, LO)
    for j, t in enumerate(todo):
        y0 = card[1] + 82 + j * 76
        neu_inset(s, (card[0] + 30, y0, card[2] - 30, y0 + 62), 20)
        check(s, card[0] + 70, y0 + 31)
        s.text(card[0] + 102, y0 + 32, t, f(MED, 26), NAVY, anchor="lm")
    s.save(n)

# ── 11 · closing ─────────────────────────────────────────────────────────────────────────────────
s = new_slide()
glows(s, [(900, 1010, 260, ORANGE, 0.8), (160, 1080, 240, (111, 155, 255), 0.8), (560, 640, 160, YELLOW, 0.6)])
brand(s)
pill(s, W - 70, 62, f"{TOTAL} / {TOTAL}", f(SEMI, 20), anchor_right=True)
s.text(66, 280, "Keep learning,", f(BOLD, 88), NAVY)
s.text(66, 380, "keep building", f(BOLD, 88), ORANGE)
s.text(72, 452, "Hifadhi, shiriki, tuendelee kujifunza pamoja", f(SIG, 46), ORANGE)
s.para(74, 510, "Which lesson hit home for you? Tell me in the comments, and send this to someone starting their tech journey.",
       f(REG, 27), W - 150, 40, GREY)

ICONS = {
    "save": '<path d="M6 3h12v18l-6-4-6 4z"/>',
    "share": '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4M15.4 6.5l-6.8 4"/>',
    "comment": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1.1-4.3A8 8 0 1 1 21 12Z"/>',
}
cw = (W - 140 - 2 * 28) / 3
for j, (key, title, sub) in enumerate([("save", "Save", "Hifadhi kwa baadaye"), ("share", "Share", "Mtumie rafiki yako"), ("comment", "Comment", "Niambie somo lako")]):
    x0 = 70 + j * (cw + 28)
    box = (x0, 640, x0 + cw, 900)
    neu(s, box, 34)
    well = (x0 + cw / 2 - 50, 672, x0 + cw / 2 + 50, 772)
    neu_inset(s, well, 30)
    ic = svg_image(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#e8603a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{ICONS[key]}</svg>', k(48))
    s.im.paste(ic, (k(x0 + cw / 2 - 24), k(698)), ic)
    s.text(x0 + cw / 2, 826, title, f(BOLD, 30), NAVY, anchor="ms")
    s.text(x0 + cw / 2, 866, sub, f(REG, 21), GREY, anchor="ms")

card = (70, 950, W - 70, 1140)
glass(s, card, 38, tint=(11, 30, 63), alpha=0.86, blur=20, border=False)
s.d.rounded_rectangle([k(v) for v in card], radius=k(38), outline=(60, 82, 122), width=k(2))
s.text(card[0] + 44, card[1] + 64, "READ MORE ON MY BLOG", f(MED, 19), BLUE)
s.text(card[0] + 44, card[1] + 132, "depriver.tech", f(BOLD, 50), (255, 255, 255))
s.text(card[2] - 44, card[1] + 70, "Questions? Ask my AI assistant", f(REG, 21), (196, 208, 232), anchor="rs")
s.text(card[2] - 44, card[1] + 140, "viora", f(SIG, 64), ORANGE, anchor="rs")

line = "Instagram @_depriver  ·  WhatsApp +255 752 747 681"
pill(s, W / 2 - (s.width(line, f(SEMI, 22)) + 48) / 2, 1190, line, f(SEMI, 22), raised=False)
s.save(TOTAL)
print("ok")
