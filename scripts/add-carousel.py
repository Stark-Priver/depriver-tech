#!/usr/bin/env python3
"""Import a carousel (folder of slide-N.jpg/png) into the site.

    python3 scripts/add-carousel.py ~/Pictures/Priver/carousel-gadgets tech-gadgets

Writes public/carousels/<slug>/01.webp, 02.webp, ... (1080 px wide) and cover.jpg (used for link previews).
Then create src/content/blog/<slug>.md with `carousel: <slug>` and `status: live` to publish it.
"""
import re, sys
from pathlib import Path
from PIL import Image

src, slug = Path(sys.argv[1]).expanduser(), sys.argv[2]
out = Path(__file__).resolve().parent.parent / "public" / "carousels" / slug
out.mkdir(parents=True, exist_ok=True)
for old in out.glob("*"):
    old.unlink()

num = lambda p: int(re.findall(r"\d+", p.stem)[-1]) if re.findall(r"\d+", p.stem) else 0
slides = {}
for p in sorted(src.iterdir()):
    if p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp") and re.search(r"\d", p.stem):
        # prefer jpg over png when both exist for the same slide
        if num(p) not in slides or p.suffix.lower() in (".jpg", ".jpeg"):
            slides[num(p)] = p
if not slides:
    sys.exit(f"no numbered slides found in {src}")

for i, n in enumerate(sorted(slides), 1):
    im = Image.open(slides[n]).convert("RGB")
    im = im.resize((1080, round(im.height * 1080 / im.width)), Image.LANCZOS)
    im.save(out / f"{i:02d}.webp", quality=84, method=6)
    if i == 1:
        im.resize((720, round(im.height * 720 / 1080)), Image.LANCZOS).save(out / "cover.jpg", quality=84, optimize=True)
total = sum(f.stat().st_size for f in out.iterdir())
print(f"{slug}: {len(slides)} slides, {total / 1024:.0f} KB -> {out}")
