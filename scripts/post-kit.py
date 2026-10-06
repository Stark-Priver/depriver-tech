#!/usr/bin/env python3
"""Build the posting kit: one folder per scheduled post, in timetable order, ready to post from the phone.

    python3 scripts/post-kit.py            # all posts dated from today on (scheduled), plus drafts with a date

~/Pictures/Priver/Ratiba/NN · Tue 13 Oct · <slug>/
    slides/            carousel JPGs (from studio/<slug>/export)
    <slug>-linkedin.pdf
    <slug>-poster.jpg, <slug>-status.jpg   (from studio/<slug>-poster/export, or studio/swali-la-wiki-poster)
    caption.txt        Instagram / LinkedIn caption: hook, description, link, question, hashtags

Swali la Wiki Sundays without an episode yet get a "to make" folder. The site itself publishes each post at
19:00 EAT on its date (see src/lib/posts.ts and the scheduled deploy)."""
import datetime as dt
import glob
import os
import re
import shutil
import yaml
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.expanduser("~/Pictures/Priver/Ratiba")
BLOG = os.path.join(ROOT, "src", "content", "blog")
TODAY = dt.date.today()
BASE_TAGS = ["#depriver", "#TechTanzania", "#WanafunziWaTech", "#Kiswahili"]
SWALI_SUNDAYS = ["2026-10-18", "2026-10-25", "2026-11-01", "2026-11-08"]


def read(path):
    text = open(path).read()
    _, fm, body = text.split("---", 2)
    return yaml.safe_load(fm), body


def plain(s):
    return re.sub(r"[*_`]|\[([^\]]+)\]\([^)]+\)", lambda m: m.group(1) or "", s).strip()


def caption(slug, data, body):
    hook = data.get("slides", [data["title"]])[0]
    question = ""
    for line in reversed(body.strip().splitlines()):
        if "?" in line:
            question = plain(line)
            break
    tags = BASE_TAGS + ["#" + re.sub(r"[^A-Za-z0-9]", "", t.title()) for t in data.get("tags", []) if t != "kiswahili"]
    return "\n\n".join(x for x in [hook, data["description"], f"👉 Full post: depriver.tech/blog/{slug} (link in bio)",
                                    question, " ".join(dict.fromkeys(tags))] if x) + "\n"


def posters(slug):
    for d in (f"{slug}-poster", "swali-la-wiki-poster" if slug.startswith("swali-la-wiki") else None):
        if d:
            yield from glob.glob(os.path.join(ROOT, "studio", d, "export", f"{slug}-*.jpg"))


def main():
    posts = []
    for path in glob.glob(os.path.join(BLOG, "*.md")):
        data, body = read(path)
        when = data["date"] if isinstance(data["date"], dt.datetime) else dt.datetime.combine(data["date"], dt.time())
        if when.date() >= TODAY:
            posts.append((when, os.path.basename(path)[:-3], data, body))
    items = [(p[0].date(), p) for p in posts] + [(dt.date.fromisoformat(d), None) for d in SWALI_SUNDAYS]
    items.sort(key=lambda x: x[0])
    os.makedirs(KIT, exist_ok=True)
    for n, (day, post) in enumerate(items, 1):
        label = day.strftime("%a %d %b")
        if post is None:
            folder = os.path.join(KIT, f"{n:02d} · {label} · swali-la-wiki (to make)")
            os.makedirs(folder, exist_ok=True)
            open(os.path.join(folder, "TODO.txt"), "w").write(
                "Swali la Wiki: pick a real question from comments, DMs or the MUST talk.\n"
                "Copy studio/swali-la-wiki-01 to the next number, change EP, then npm run carousel -- swali-la-wiki-NN.\n")
            print(f"{n:02d}  {label}  Swali la Wiki (to make)")
            continue
        when, slug, data, body = post
        draft = data.get("status") == "draft"
        folder = os.path.join(KIT, f"{n:02d} · {label} · {slug}" + (" (draft, needs photos)" if draft else ""))
        for old in glob.glob(os.path.join(KIT, f"* · {slug}*")):
            if old != folder:
                shutil.move(old, folder)
        os.makedirs(os.path.join(folder, "slides"), exist_ok=True)
        slides = sorted(glob.glob(os.path.join(ROOT, "studio", slug, "export", "slide-*.jpg")),
                        key=lambda p: int(re.findall(r"(\d+)\.jpg$", p)[0]))
        for s in slides:
            shutil.copy2(s, os.path.join(folder, "slides", os.path.basename(s)))
        if slides:
            ims = [Image.open(s).convert("RGB") for s in slides]
            ims[0].save(os.path.join(folder, f"{slug}-linkedin.pdf"), save_all=True, append_images=ims[1:], resolution=200)
        for p in posters(slug):
            shutil.copy2(p, folder)
        open(os.path.join(folder, "caption.txt"), "w").write(caption(slug, data, body))
        print(f"{n:02d}  {label}  {slug}{'  (draft)' if draft else ''}")


if __name__ == "__main__":
    main()
