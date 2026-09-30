"""Carousel: Tech advice I learnt the hard way (11 slides, 1080x1350, exported at 2x).
Site palette on terrain paper, neumorphic cards, frosted-glass panels over colour glows,
and cartoon vector illustrations (SVG rasterised with rsvg-convert). No portrait on this one."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers

exec(open(os.path.join(STUDIO, "kit.py")).read())  # glass, neumorphism, illustrations (ART)
TOTAL = 11

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
