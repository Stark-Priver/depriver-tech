#!/usr/bin/env python3
"""Render a carousel and import it into the site.

    npm run carousel -- coding-basics-for-beginners

1. runs studio/<slug>/make.py  -> full-size Instagram JPGs in studio/<slug>/export/ (not committed)
2. imports them into public/carousels/<slug>/ as web slides + cover.jpg (committed)
"""
import subprocess, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
if len(sys.argv) < 2:
    sys.exit("usage: npm run carousel -- <slug>   (folders: " + ", ".join(p.parent.name for p in sorted(root.glob("studio/*/make.py"))) + ")")
slug = sys.argv[1]
make = root / "studio" / slug / "make.py"
if not make.exists():
    sys.exit(f"missing {make}")
subprocess.run([sys.executable, str(make)], check=True)
subprocess.run([sys.executable, str(root / "scripts" / "add-carousel.py"), str(make.parent / "export"), slug], check=True)
post = root / "src" / "content" / "blog" / f"{slug}.md"
print(f"post: {post.relative_to(root)}" + ("" if post.exists() else "  (not created yet: add it with `status: draft` or `status: live`)"))
