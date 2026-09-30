"""Shared kit for glass + neumorphism carousels: terrain paper, colour glows, frosted glass, raised/pressed
neumorphic shapes, pills, and cartoon vector illustrations (SVG rasterised with rsvg-convert).
Executed after base.py by studio/<slug>/make.py files (needs STUDIO, K, W, H, f(), k(), Slide from base.py)."""
import io
import re
import subprocess
import tempfile

ROOT = os.path.dirname(STUDIO)
PAPER = (244, 245, 248)
HI, LO = (255, 255, 255), (208, 214, 226)
YELLOW, GREEN = (255, 200, 87), (61, 220, 132)
TOTAL = 11  # overridden by each make.py

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


def fit(s, text, name, size, maxw, smallest=14):
    """Largest font size <= size at which text fits maxw."""
    while size > smallest and s.width(text, f(name, size)) > maxw:
        size -= 2
    return size


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


ART_STYLE = globals().get("ART_STYLE", "cute")   # "print" = editorial style: no faces, no sparkles


def face(x, y, sc=1):
    if ART_STYLE == "print":
        return ""
    return f'''<g transform="translate({x} {y}) scale({sc})">
    <circle cx="-16" cy="0" r="6" fill="#0b1e3f"/><circle cx="16" cy="0" r="6" fill="#0b1e3f"/>
    <circle cx="-14" cy="-2" r="2" fill="#fff"/><circle cx="18" cy="-2" r="2" fill="#fff"/>
    <ellipse cx="-30" cy="12" rx="8" ry="5" fill="#ff9f8a" opacity=".85"/><ellipse cx="30" cy="12" rx="8" ry="5" fill="#ff9f8a" opacity=".85"/>
    <path d="M-10 12 Q0 22 10 12" fill="none" stroke="#0b1e3f" stroke-width="5" stroke-linecap="round"/></g>'''


def spark(x, y, sc=1, c="#ffc857"):
    if ART_STYLE == "print":
        return ""
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
      {"" if ART_STYLE == "print" else '<g transform="translate(300 272) scale(0.7)"><circle cx="-16" cy="0" r="7" fill="#fff"/><circle cx="16" cy="0" r="7" fill="#fff"/><path d="M-10 14 Q0 24 10 14" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/></g>'}
      <path d="M186 264 h96" stroke="#a9c4f5" stroke-width="8" stroke-linecap="round" opacity=".7"/>
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
        {"" if ART_STYLE == "print" else '<g transform="translate(0 6)"><circle cx="-15" cy="0" r="5" fill="#fff"/><circle cx="15" cy="0" r="5" fill="#fff"/><path d="M-10 16 Q0 24 10 16" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/></g>'}</g>"""
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



# ── editorial / print finishing (the "designed, not generated" layer) ───────────────────────────
INK = (11, 30, 63)


def grain(im, amount=0.07, seed_size=None):
    """Film/paper grain over an RGB image (multiply-style), like a printed or Photoshop-finished piece."""
    noise = Image.effect_noise(im.size, 64).convert("L")
    noise = noise.point(lambda v: 255 - int((255 - v) * amount * 2.2) if v < 128 else 255)
    return ImageChops.multiply(im, Image.merge("RGB", (noise, noise, noise)))


def print_art(key, width):
    """Illustration with grain in its fills (so flat vector reads like ink on paper)."""
    art = svg_image(ART[key], width)
    rgb = grain(art.convert("RGB"), 0.11)
    out = Image.merge("RGBA", (*rgb.split(), art.getchannel("A")))
    return out


def paste_print(s, art, x, y, offset=(9, 11), opacity=0.16):
    """Paste art with an offset ink shadow (risograph misregistration look)."""
    a = art.getchannel("A").point(lambda v: int(v * opacity))
    s.im.paste(Image.new("RGB", art.size, INK), (k(x + offset[0]), k(y + offset[1])), a)
    s.im.paste(art, (k(x), k(y)), art)


def outline_text(s, x, y, text, font, stroke=3, color=INK, anchor="ls", opacity=1.0):
    """Hollow, outlined display type (huge background numerals)."""
    full = Image.new("L", s.im.size, 0)
    inner = Image.new("L", s.im.size, 0)
    ImageDraw.Draw(full).text((k(x), k(y)), text, font=font, fill=255, anchor=anchor, stroke_width=k(stroke), stroke_fill=255)
    ImageDraw.Draw(inner).text((k(x), k(y)), text, font=font, fill=255, anchor=anchor)
    ring = ImageChops.subtract(full, inner).point(lambda v: int(v * opacity))
    s.im.paste(Image.new("RGB", s.im.size, color), (0, 0), ring)


def smallcaps(s, x, y, text, size, color, tracking=0.16, weight=None, anchor="left"):
    """Letter-spaced uppercase label."""
    font = f(weight or SEMI, size)
    text = text.upper()
    widths = [s.width(ch, font) for ch in text]
    total = sum(widths) + tracking * size * (len(text) - 1)
    cx = x - total if anchor == "right" else x
    for ch, w in zip(text, widths):
        s.text(cx, y, ch, font, color)
        cx += w + tracking * size
    return total


def hairline(s, x0, x1, y, color=(200, 206, 218), w=2):
    s.rect(x0, y, x1, y + w, color)


def swash(s, x0, x1, y, color=ORANGE, thick=7, seed=3):
    """Hand-drawn brush underline: tapered ends and a slight wobble."""
    import math, random
    rnd = random.Random(seed)
    layer = Image.new("L", s.im.size, 0)
    d = ImageDraw.Draw(layer)
    n = 60
    pts = []
    for i in range(n + 1):
        t = i / n
        xx = x0 + (x1 - x0) * t
        yy = y + math.sin(t * math.pi * 1.2 + 0.4) * 4 - t * 6 + rnd.uniform(-0.6, 0.6)
        pts.append((xx, yy, thick * math.sin(math.pi * (0.08 + 0.84 * t)) ** 0.6))
    for (xa, ya, wa), (xb, yb, wb) in zip(pts, pts[1:]):
        w = max(1.0, (wa + wb) / 2)
        d.line([k(xa), k(ya), k(xb), k(yb)], fill=235, width=k(w))
        d.ellipse([k(xb - w / 2), k(yb - w / 2), k(xb + w / 2), k(yb + w / 2)], fill=235)
    s.im.paste(Image.new("RGB", s.im.size, color), (0, 0), layer.filter(ImageFilter.GaussianBlur(k(0.6))))


def sticker(s, cx, cy, text, angle=-6, bg=ORANGE, fg=(255, 255, 255), size=24, script=False):
    """Rotated label, like a sticker placed by hand."""
    font = f(SIG, size * 1.6) if script else f(BOLD, size)
    tw = s.width(text, font)
    w, h = tw + 56, size * (2.6 if script else 2.3)
    lay = Image.new("RGBA", (k(w + 40), k(h + 40)), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    ld.rounded_rectangle([k(20), k(20), k(20 + w), k(20 + h)], radius=k(12), fill=bg + (255,))
    ld.text((k(20 + w / 2), k(20 + h / 2 + (2 if not script else 6))), text, font=font, fill=fg, anchor="mm")
    lay = lay.rotate(angle, resample=Image.BICUBIC, expand=True)
    sh = lay.getchannel("A").filter(ImageFilter.GaussianBlur(k(6))).point(lambda v: v * 70 // 255)
    px, py = k(cx) - lay.width // 2, k(cy) - lay.height // 2
    s.im.paste(Image.new("RGB", lay.size, INK), (px + k(4), py + k(8)), sh)
    s.im.paste(lay, (px, py), lay)


def finish(s, amount=0.045):
    """Final pass: light paper grain over the whole page."""
    s.im = grain(s.im, amount)
    s.d = ImageDraw.Draw(s.im)


# ── panorama: elements that run continuously across carousel slides ─────────────────────────────
import math
import random as _random

_FIELDS = {}


def _field(total, seed=7):
    """One wide, low-res height field spanning every slide, so contour lines flow across seams."""
    if (total, seed) not in _FIELDS:
        rnd = _random.Random(seed)
        fw, fh = W * total // 4, H // 4
        field = None
        for cells, weight in ((5, 1.0), (11, 0.45), (23, 0.18)):
            cw_, ch_ = int(cells * 0.8 * total) + 1, cells
            small = Image.new("L", (cw_, ch_))
            small.putdata([rnd.randint(0, 255) for _ in range(cw_ * ch_)])
            layer = small.resize((fw, fh), Image.BICUBIC)
            field = layer if field is None else Image.blend(field, layer, weight / (1 + weight))
        _FIELDS[(total, seed)] = ImageOps.autocontrast(field.filter(ImageFilter.GaussianBlur(3)))
    return _FIELDS[(total, seed)]


def panorama_paper(s, n, total, seed=7):
    """Paper with contour lines that continue from slide n-1 into n and on into n+1."""
    field = _field(total, seed)
    fw, pad = W // 4, 12                                   # pad so blurring never creates a seam
    x0 = (n - 1) * fw
    crop = field.crop((x0 - pad, 0, x0 + fw + pad, field.height))  # PIL pads outside with black; edges only
    if n == 1 or n == total:                               # outer edges: mirror-free, just clamp
        crop = field.crop((max(0, x0 - pad), 0, min(field.width, x0 + fw + pad), field.height))
    scale = k(W) / fw
    big = crop.resize((round(crop.width * scale), k(H)), Image.BICUBIC).filter(ImageFilter.GaussianBlur(14))
    left = round((x0 - max(0, x0 - pad)) * scale)
    step = 11
    # detect contour edges on the padded strip, then crop: no artificial edge at the slide border
    bands = big.point(lambda v: (v // step) * step)
    edges = bands.filter(ImageFilter.FIND_EDGES).point(lambda v: 255 if v else 0).filter(ImageFilter.MaxFilter(3))
    edges = edges.filter(ImageFilter.GaussianBlur(2.2)).point(lambda v: min(255, v * 3))
    major = bands.point(lambda v: 255 if (v // step) % 5 == 0 else 0)
    edges_major = ImageChops.multiply(edges, major.filter(ImageFilter.MaxFilter(5)))
    box = (left, 0, left + k(W), k(H))
    part, edges, edges_major = big.crop(box), edges.crop(box), edges_major.crop(box)
    bg = Image.new("RGB", part.size, PAPER)
    bg = Image.composite(Image.new("RGB", part.size, (234, 237, 243)), bg, part.point(lambda v: int(v * 0.35)))
    bg.paste(Image.new("RGB", part.size, (212, 218, 230)), (0, 0), edges.point(lambda v: v * 120 // 255))
    bg.paste(Image.new("RGB", part.size, (193, 202, 220)), (0, 0), edges_major.point(lambda v: v * 150 // 255))
    s.im.paste(bg)
    s.d = ImageDraw.Draw(s.im)


def wave_y(X, base=1060, amp=22, length=1.55, phase=0.6):
    """Height of the continuous navy horizon at panorama x (1080 px per slide)."""
    return base + amp * math.sin(2 * math.pi * X / (length * W) + phase) + amp * 0.35 * math.sin(2 * math.pi * X / (0.43 * W))


def navy_wave(s, n, base=1060, crest=ORANGE):
    """Navy block whose top edge is one wave running through every slide, with an orange crest line."""
    off = (n - 1) * W
    pts = [(x, wave_y(off + x, base)) for x in range(-6, W + 7, 4)]
    s.d.polygon([(k(x), k(y)) for x, y in pts] + [(k(W + 6), k(H + 6)), (k(-6), k(H + 6))], fill=NAVY)
    s.d.line([(k(x), k(y - 1)) for x, y in pts], fill=crest, width=k(5), joint="curve")


def seam_nodes(s, n, total, base=1060, r=30):
    """Arrow badges centred exactly on the seams: half shows on each slide and joins up when you swipe."""
    for sx in ([0] if n > 1 else []) + ([W] if n < total else []):
        cy = wave_y((n - 1) * W + sx, base)
        s.d.ellipse([k(sx - r - 6), k(cy - r - 6), k(sx + r + 6), k(cy + r + 6)], fill=PAPER)
        s.d.ellipse([k(sx - r), k(cy - r), k(sx + r), k(cy + r)], fill=ORANGE)
        s.d.line([k(sx - 11), k(cy), k(sx + 10), k(cy)], fill=(255, 255, 255), width=k(3.4))
        s.d.line([k(sx + 1), k(cy - 9), k(sx + 10), k(cy), k(sx + 1), k(cy + 9)], fill=(255, 255, 255), width=k(3.4), joint="curve")
