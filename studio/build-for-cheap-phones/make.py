"""Carousel: build for a cheap Android phone, Jenga kwa Tanzania #3 (8 slides, 1080x1350, exported at 2x). The device
is two phones side by side: the developer's fast phone vs the user's entry-level phone stuck on "Inapakia...". No
invented market statistics."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/build-for-cheap-phones"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def series_tag(s, x, y, text="Jenga kwa Tanzania #03", size=20):
    w_ = s.width(text, f(BOLD, size)) + 40
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + size * 2.1)], radius=k(size), fill=NAVY)
    s.text(x + w_ / 2, y + size * 1.08, text, f(BOLD, size), WHITE_T, anchor="mm")


def app_screen(s, box, loading=False):
    x0, y0, x1, y1 = box
    if loading:
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2 - 20
        s.d.arc([k(cx - 36), k(cy - 36), k(cx + 36), k(cy + 36)], 0, 270, fill=ORANGE, width=k(8))
        s.text(cx, cy + 80, "Inapakia...", f(SEMI, 20), GREY, anchor="mm")
        return
    s.rect(x0, y0, x1, y0 + 70, ORANGE)
    s.text(x0 + 18, y0 + 46, "Duka App", f(BOLD, 20), WHITE_T)
    for i in range(4):
        yy = y0 + 96 + i * 92
        s.d.rounded_rectangle([k(x0 + 14), k(yy), k(x1 - 14), k(yy + 76)], radius=k(10), fill=(244, 245, 248), outline=(214, 219, 230), width=k(2))
        s.d.rounded_rectangle([k(x0 + 26), k(yy + 12), k(x0 + 78), k(yy + 64)], radius=k(8), fill=(201, 212, 234))
        s.d.rounded_rectangle([k(x0 + 92), k(yy + 20), k(x1 - 40), k(yy + 32)], radius=k(6), fill=(190, 198, 214))
        s.d.rounded_rectangle([k(x0 + 92), k(yy + 46), k(x1 - 90), k(yy + 56)], radius=k(5), fill=(214, 220, 232))


def phone_pair(s, y, w=270, h=520, gap=60, label=True):
    x0 = W / 2 - w - gap / 2
    app_screen(s, smartphone(s, x0, y, w, h))
    app_screen(s, smartphone(s, x0 + w + gap, y, w, h), loading=True)
    if label:
        s.text(x0 + w / 2, y + h + 50, "Your phone", f(BOLD, 24), NAVY, anchor="ms")
        s.text(x0 + w * 1.5 + gap, y + h + 50, "Her TZS 150k phone", f(BOLD, 24), RED_NO, anchor="ms")


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Build for Tanzania · Jenga kwa Tanzania")
series_tag(s, M, 165)
s.text(M - 6, 310, "Works on your phone.", f(BOLD, 72), NAVY)
s.text(M - 6, 392, "Does it work on hers?", f(BOLD, 72), ORANGE)
s.text(M, 470, "Jenga kwa simu za watu halisi", f(SIG, 52), NAVY)
swash(s, M + 8, M + 560, 494, ORANGE, 6)
phone_pair(s, 540, w=240, h=400)
horizon(s, 1)
cover_footer(s, "Swipe, build for everyone")
finish(s)
s.save(1)

# ── 2 · the reality ──────────────────────────────────────────────────────────────────────────────
s = page(2, "The reality · Hali halisi", "Jenga kwa Tanzania")
title2(s, "Your users are", "not on flagships.", y=220, size=82)
tick_fill(s, [("Entry-level Android phones", "Little RAM, slow processors, older Android versions."),
              ("Storage is always full", "Photos and WhatsApp media. Big apps get deleted first."),
              ("Data is expensive", "Every MB your app wastes costs your user money."),
              ("Networks drop", "3G or weak 4G, especially upcountry and on the road.")], 420, 990, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Rule", "Design for the phone your customer has, not the one you have.", "Simu ya mteja kwanza", seed=2)
finish(s)
s.save(2)

# ── 3 · keep it small ────────────────────────────────────────────────────────────────────────────
s = page(3, "Keep it small · Iwe nyepesi", "Jenga kwa Tanzania")
title2(s, "Small apps get", "installed.", y=220, size=88)
tick_fill(s, [("Fewer libraries", "Every package adds weight. Do you really need it?"),
              ("Android App Bundles", "The Play Store sends each phone only what it needs."),
              ("Web: less JavaScript", "Ship plain HTML first. Add JS where it truly helps."),
              ("Check the size every release", "Write it in the changelog. Notice when it grows.")], 420, 990, size=31, sub=26)
horizon(s, 3)
navy_note(s, "Ask", "“Would I download this on a full phone with 300 MB of data?”", "Uliza swali hili", seed=3)
finish(s)
s.save(3)

# ── 4 · images ───────────────────────────────────────────────────────────────────────────────────
s = page(4, "Images · Picha", "Jenga kwa Tanzania")
title2(s, "Images are the", "biggest leak.", y=220, size=86)
bars(s, [("Photo straight from the camera", 0.95, RED_NO), ("Resized to the size it's shown", 0.3, ORANGE), ("Resized + WebP + compressed", 0.08, GREEN_OK)],
     440, gap=120)
s.text(M, 790, "Illustration: same photo, very different download size.", f(REG, 22), GREY)
tick_list(s, [("Serve the size you display", None), ("Use WebP (or AVIF), compress", None), ("Lazy-load images below the screen", None)], 870, size=28)
horizon(s, 4)
navy_note(s, "Quick win", "Fixing images alone often makes a site several times lighter.", "Punguza picha", seed=4)
finish(s)
s.save(4)

# ── 5 · slow networks ────────────────────────────────────────────────────────────────────────────
s = page(5, "Slow networks · Mtandao hafifu", "Jenga kwa Tanzania")
title2(s, "Design for", "weak signal.", y=220, size=90)
tick_fill(s, [("Test with throttling", "Chrome DevTools “Slow 3G”, or the Android emulator's network settings."),
              ("Show something fast", "Skeleton screens and cached content, not a blank page."),
              ("Retry, don't crash", "Clear message: “Hakuna mtandao. Jaribu tena.”"),
              ("Small API responses", "Send only the fields the screen needs. Paginate lists.")], 420, 990, size=31, sub=26)
horizon(s, 5)
navy_note(s, "Remember", "Users blame your app, not the network.", "Wanalaumu app", seed=5)
finish(s)
s.save(5)

# ── 6 · storage & data ───────────────────────────────────────────────────────────────────────────
s = page(6, "Data & storage · Data na nafasi", "Jenga kwa Tanzania")
title2(s, "Respect their", "MBs.", y=220, size=92)
tick_fill(s, [("Cache what doesn't change", "Logos, product lists, yesterday's data."),
              ("Let users choose quality", "“Download on Wi-Fi only”, “low quality images”."),
              ("Clean up after yourself", "Delete temp files. Show a “clear cache” button."),
              ("Work offline where you can", "Save drafts and orders locally, sync later.")], 420, 990, size=31, sub=26)
horizon(s, 6)
navy_note(s, "Bonus", "Light apps also save battery. Users notice.", "Betri inadumu", seed=6)
finish(s)
s.save(6)

# ── 7 · test on a real phone ─────────────────────────────────────────────────────────────────────
s = page(7, "Test it · Jaribu", "Jenga kwa Tanzania")
title2(s, "Borrow a cheap", "phone. Test.", y=220, size=86)
table(s, M, 410, ["Check", "Pass if"], [["App size", "Small enough to keep"], ["First screen", "Shows in a few seconds"], ["Slow 3G", "Still usable, no crash"],
                                        ["No network", "Clear message, data kept"], ["Low storage", "Installs and runs"], ["Old Android", "Works, nothing cut off"]],
      [380, W - 2 * M - 8 - 380], size=26, rh=74)
horizon(s, 7)
navy_note(s, "Easy", "Ask a relative to use your app while you watch quietly.", "Mtazame mtumiaji", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which app is too", "heavy on your phone?", [("Comment", "the app (no shame)"), ("Save", "before your next release"),
                                                      ("Share", "with a mobile developer")])
app_screen(s, smartphone(s, 760, 640, 210, 380))
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
