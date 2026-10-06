"""Carousel: recap of my FPT talk at MUST, "Life in Uni vs Real World in Tech" (7 Oct 2026)
(9 slides, 1080x1350, exported at 2x). Same editorial / print direction as make-your-fpt-count.

After the talk: drop photos in studio/assets/talk/ and list them in PHOTOS (first one is the cover), and fill
QUESTIONS with the best questions students asked plus my short answer. Empty slots render as marked placeholders,
so the post stays `status: draft` until both are filled."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools
TOTAL = 9
M = 72
RULE = (200, 206, 218)
WHITE_T = (255, 255, 255)
SOFT = (190, 202, 226)
POST_URL = "depriver.tech/blog/life-in-uni-vs-real-world-in-tech"
BASE = 1060

# ── fill these after the talk ────────────────────────────────────────────────────────────────────
TALK = os.path.join(STUDIO, "assets", "talk")
PHOTOS = [  # (file in assets/talk/, handwritten caption); first = cover
    # ("stage.jpg", "MUST, 7 Oct 2026"),
]
QUESTIONS = [  # (question a student asked, my short answer)
    # ("Do I need a degree to get hired?", "No. Show what you've built, and keep learning."),
]

ROUNDS = [("Code on paper", "code on screen", "Type your paper code on a computer the same day."),
          ("Memorise it", "find it", "Learn to read official documentation."),
          ("Group work", "teamwork", "Do your part, and keep it on GitHub."),
          ("Toy projects", "real users", "Build one thing a real person uses, every semester."),
          ("Diagrams", "production", "Put your projects online, even on a free tier."),
          ("Grades", "GitHub", "Keep three projects you can demo in two minutes.")]


def page(n, label_left, label_right="depriver.tech"):
    s = Slide()
    panorama_paper(s, n, TOTAL)
    smallcaps(s, M, 96, label_left, 17, ORANGE)
    s.text(W - M, 96, label_right, f(SEMI, 20), NAVY, anchor="rs")
    hairline(s, M, W - M, 118, RULE)
    return s


def horizon(s, n):
    navy_wave(s, n, BASE)
    seam_nodes(s, n, TOTAL, BASE)


def arrow(s, x, y, color=WHITE_T, w=3.4, size=12):
    s.d.line([k(x - size - 6), k(y), k(x + size - 2), k(y)], fill=color, width=k(w))
    s.d.line([k(x), k(y - size + 2), k(x + size - 2), k(y), k(x), k(y + size - 2)], fill=color, width=k(w), joint="curve")


def navy_note(s, label, line, sw=None, seed=0):
    smallcaps(s, M, BASE + 74, label, 16, ORANGE)
    s.text(M, BASE + 130, line, f(SEMI, fit(s, line, SEMI, 31, W - 2 * M)), WHITE_T)
    if sw:
        sws = fit(s, sw, SIG, 54, W - 2 * M - 40)
        s.text(M, BASE + 214, sw, f(SIG, sws), ORANGE)
        swash(s, M + 6, M + min(s.width(sw, f(SIG, sws)) * 0.9, 620), BASE + 238, ORANGE, 5, seed=seed)


def title2(s, a, b, y=230, size=84):
    s.text(M - 4, y, a, f(BOLD, size), NAVY)
    s.text(M - 4, y + size * 1.08, b, f(BOLD, size), ORANGE)


def vs_badge(s, cx, cy, r=22, size=18):
    s.d.ellipse([k(cx - r + 3), k(cy - r + 4), k(cx + r + 3), k(cy + r + 4)], fill=NAVY)
    s.d.ellipse([k(cx - r), k(cy - r), k(cx + r), k(cy + r)], fill=ORANGE)
    s.text(cx, cy + 1, "vs", f(BOLD, size), WHITE_T, anchor="mm")


def polaroid(s, cx, cy, width, angle, photo, caption, cap_size=34, ratio=0.8):
    """A talk photo as a taped polaroid. With no photo yet, a dashed slot marked for replacement."""
    pw = k(width - 44)
    ph = int(pw * ratio)
    pad, foot = k(22), k(cap_size * 2.2)
    card = Image.new("RGBA", (pw + 2 * pad, ph + pad + foot), (252, 251, 247, 255))
    cd = ImageDraw.Draw(card)
    if photo:
        src = ImageOps.exif_transpose(Image.open(os.path.join(TALK, photo))).convert("RGB")
        src = ImageOps.fit(src, (pw, ph), Image.LANCZOS, centering=(0.5, 0.35))
        src = grain(ImageEnhance.Color(src).enhance(0.9), 0.05)
        card.paste(src, (pad, pad))
    else:
        cd.rectangle([pad, pad, pad + pw, pad + ph], fill=(226, 230, 238))
        for x in range(pad, pad + pw, k(18)):
            cd.line([x, pad, min(x + k(9), pad + pw), pad], fill=GREY, width=k(2))
            cd.line([x, pad + ph, min(x + k(9), pad + pw), pad + ph], fill=GREY, width=k(2))
        for y in range(pad, pad + ph, k(18)):
            cd.line([pad, y, pad, min(y + k(9), pad + ph)], fill=GREY, width=k(2))
            cd.line([pad + pw, y, pad + pw, min(y + k(9), pad + ph)], fill=GREY, width=k(2))
        cd.text((pad + pw // 2, pad + ph // 2), "PHOTO FROM THE TALK", font=f(BOLD, max(14, width / 22)), fill=GREY, anchor="mm")
    cd.text((card.width // 2, ph + pad + foot // 2 + k(4)), caption, font=f(SIG, cap_size), fill=NAVY + (255,), anchor="mm")
    for tx in (0.2, 0.8):
        tape = Image.new("RGBA", (k(width * 0.22), k(36)), (233, 214, 160, 190))
        tape = tape.rotate(-14 if tx < 0.5 else 12, resample=Image.BICUBIC, expand=True)
        card.alpha_composite(tape, (int(card.width * tx) - tape.width // 2, -k(6)))
    big = Image.new("RGBA", (card.width + k(60), card.height + k(60)), (0, 0, 0, 0))
    big.paste(card, (k(30), k(30)))
    big = big.rotate(angle, resample=Image.BICUBIC, expand=True)
    sh = big.getchannel("A").filter(ImageFilter.GaussianBlur(k(12))).point(lambda v: v * 85 // 255)
    px, py = k(cx) - big.width // 2, k(cy) - big.height // 2
    s.im.paste(Image.new("RGB", big.size, INK), (px + k(10), py + k(16)), sh)
    s.im.paste(big, (px, py), big)
    s.d = ImageDraw.Draw(s.im)


def photo(i):
    return PHOTOS[i] if i < len(PHOTOS) else (None, "coming soon")


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Talk recap · MUST · 7 Oct 2026")
s.text(M - 4, 210, "I went back to MUST.", f(BOLD, 60), NAVY)
s.text(M - 4, 330, "Life in Uni", f(BOLD, 104), NAVY)
vs_badge(s, M + 42, 418, r=42, size=34)
s.text(M + 104, 450, "Real World", f(BOLD, 104), ORANGE)
s.text(M + 104, 562, "in Tech.", f(BOLD, 104), ORANGE)
f0, c0 = photo(0)
polaroid(s, 790, 850, 440, 4, f0, c0)
s.para(M, 690, "My first FPT was at MUST in 2024. This time I came back to talk to students finishing theirs.",
       f(REG, 26), 420, 38, GREY)
s.text(M, 900, "Tuko pamoja", f(SIG, 62), NAVY)
swash(s, M + 8, M + 300, 926, ORANGE, 6)
horizon(s, 1)
sticker(s, 230, wave_y(230) - 6, "FPT talk recap", angle=-5, size=20, bg=NAVY)
s.text(M, 1262, "Swipe for the whole talk", f(SEMI, 30), WHITE_T)
arrow(s, M + s.width("Swipe for the whole talk", f(SEMI, 30)) + 34, 1251)
s.text(W - M, 1262, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(1)

# ── 2 · full circle ──────────────────────────────────────────────────────────────────────────────
s = page(2, "Full circle · Nimekaa kiti chako")
outline_text(s, M - 10, 400, "2024", f(BOLD, 230), stroke=3, color=RULE)
outline_text(s, W - M + 10, 640, "2026", f(BOLD, 230), stroke=3, color=ORANGE, anchor="rs", opacity=0.8)
s.text(M, 470, "Trainee at MUST", f(BOLD, 40), NAVY)
s.text(W - M, 710, "Back on the stage", f(BOLD, 40), ORANGE, anchor="rs")
s.para(M, 800, "In 2024 I sat in the same seats, doing my first FPT. Today I'm a Software Engineer & Digital Innovator "
       "at Rohi Company Ltd and the founder of INCPRITECH.", f(MED, 27), W - 2 * M, 40, NAVY)
s.text(M, 960, "I sat in your seat. Nimekaa kiti chako.", f(SEMI, 27), ORANGE)
horizon(s, 2)
navy_note(s, "Why I came back", "To tell them what I wish someone told me.", "Ushauri wa kaka", seed=2)
finish(s)
s.save(2)

# ── 3 · six rounds ───────────────────────────────────────────────────────────────────────────────
s = page(3, "Part 01 · The six rounds")
title2(s, "What uni teaches", "vs what work expects.", y=210, size=66)
smallcaps(s, M + 90, 360, "Life in Uni", 15, NAVY)
smallcaps(s, M + 470, 360, "Real world in tech", 15, ORANGE)
y = 432
for j, (a, b, tip) in enumerate(ROUNDS):
    s.text(M, y, f"{j + 1:02d}", f(BOLD, 30), ORANGE)
    s.text(M + 90, y, a, f(BOLD, fit(s, a, BOLD, 32, 300)), NAVY)
    vs_badge(s, M + 420, y - 11, r=20, size=15)
    s.text(M + 470, y, b, f(BOLD, fit(s, b, BOLD, 32, W - M - 470 - M)), ORANGE)
    s.text(M + 90, y + 38, "Do this: " + tip, f(REG, fit(s, "Do this: " + tip, REG, 22, W - 2 * M - 90)), GREY)
    if j < 5:
        hairline(s, M + 90, W - M, y + 60, RULE)
    y += 102
horizon(s, 3)
navy_note(s, "In one line", "Learn it in class. Prove it in projects.", "Shule inakupa msingi", seed=3)
finish(s)
s.save(3)

# ── 4 · start now + finish strong ────────────────────────────────────────────────────────────────
s = page(4, "Part 02 · Start now, finish strong")
title2(s, "Habits to", "start now.", y=210, size=80)
habits = [("Type up your paper code", "same day"), ("Ship a real project", "every semester"),
          ("Live on GitHub", "commit, push, repeat"), ("Use AI as a tutor", "not a copy machine"),
          ("Treat projects like real work", "real users, deadlines"), ("Respect the fundamentals", "logic, data, maths")]
cw = (W - 2 * M - 24) / 2
for j, (a, b) in enumerate(habits):
    x = M + (j % 2) * (cw + 24)
    y = 370 + (j // 2) * 136
    s.rect(x + 6, y + 8, x + cw + 6, y + 120, (205, 211, 224), r=14)
    s.d.rounded_rectangle([k(x), k(y), k(x + cw), k(y + 112)], radius=k(14), fill=(255, 255, 255), outline=NAVY, width=k(2.5))
    s.text(x + 22, y + 50, f"{j + 1:02d}", f(BOLD, 24), ORANGE)
    s.text(x + 72, y + 50, a, f(BOLD, fit(s, a, BOLD, 25, cw - 92)), NAVY)
    s.text(x + 72, y + 86, b, f(REG, 22), GREY)
smallcaps(s, M, 840, "Before FPT ends", 15, ORANGE)
fin = ["Logbook that shows skill", "Ask for the letter", "Keep your contacts", "Collect proof"]
x, y = M, 878
for j, t in enumerate(fin):
    fnt = f(SEMI, 23)
    w_ = s.width(t, fnt) + 44
    if x + w_ > W - M:
        x, y = M, y + 70
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + 52)], radius=k(26), fill=NAVY if j % 2 == 0 else (255, 255, 255),
                          outline=NAVY, width=k(2.5))
    s.text(x + w_ / 2, y + 27, t, fnt, WHITE_T if j % 2 == 0 else NAVY, anchor="mm")
    x += w_ + 14
horizon(s, 4)
navy_note(s, "Full guide", "depriver.tech/blog/make-your-fpt-count", "Maliza kwa nguvu", seed=4)
finish(s)
s.save(4)

# ── 5 · money talk ───────────────────────────────────────────────────────────────────────────────
s = page(5, "Part 03 · Money talk")
title2(s, "Earn smart.", "Skip the traps.", y=210, size=84)
money = [("Use your student status", "Free pro tools, cloud credits and certificates. They expire when you graduate.", ORANGE, "Claim"),
         ("A gig pays you twice", "Money + experience. Start local: websites, IT support, design.", NAVY, "Earn"),
         ("Betting & forex", "Not a side hustle. If someone asks you to pay to get a job, it's a scam.", (180, 40, 40), "Avoid")]
y = 380
for a, b, col, tag in money:
    s.rect(M + 8, y + 10, W - M, y + 180, (205, 211, 224), r=18)
    s.d.rounded_rectangle([k(M), k(y), k(W - M - 8), k(y + 170)], radius=k(18), fill=(255, 255, 255), outline=NAVY, width=k(3))
    s.d.rounded_rectangle([k(M), k(y), k(M + 150), k(y + 170)], radius=k(18), fill=col)
    s.rect(M + 130, y, M + 150, y + 170, col)
    s.text(M + 75, y + 96, tag, f(BOLD, 30), WHITE_T, anchor="mm")
    s.text(M + 180, y + 66, a, f(BOLD, fit(s, a, BOLD, 32, W - 2 * M - 220)), NAVY)
    s.para(M + 180, y + 108, b, f(REG, 23), W - 2 * M - 220, 33, GREY)
    y += 200
horizon(s, 5)
navy_note(s, "Free tools list", "depriver.tech/blog/free-tools-for-students", "Pesa ya haraka ni mtego", seed=5)
finish(s)
s.save(5)

# ── 6 · moments ──────────────────────────────────────────────────────────────────────────────────
s = page(6, "Moments · Picha za siku")
title2(s, "Asanteni,", "MUST.", y=210, size=92)
f1, c1 = photo(1)
f2, c2 = photo(2)
f3, c3 = photo(3)
polaroid(s, 300, 560, 410, -4, f1, c1, cap_size=28, ratio=0.7)
polaroid(s, 790, 520, 400, 5, f2, c2, cap_size=28, ratio=0.7)
polaroid(s, 580, 870, 410, -2, f3, c3, cap_size=28, ratio=0.7)
horizon(s, 6)
navy_note(s, "Thank you", "To the FPT coordinators, staff and every student who came.", "Tuko pamoja", seed=6)
finish(s)
s.save(6)

# ── 7 · your questions ───────────────────────────────────────────────────────────────────────────
s = page(7, "Q&A · Maswali yenu")
title2(s, "You asked.", "Here's my answer.", y=210, size=80)
qs = QUESTIONS + [("Question from the talk, coming soon", "My short answer goes here.")] * (3 - len(QUESTIONS))
y = 380
for j, (q, a) in enumerate(qs[:3]):
    s.rect(M + 8, y + 10, W - M, y + 200, (205, 211, 224), r=18)
    s.d.rounded_rectangle([k(M), k(y), k(W - M - 8), k(y + 190)], radius=k(18), fill=(255, 255, 255), outline=NAVY, width=k(3))
    s.text(M + 30, y + 64, "Q", f(BOLD, 48), ORANGE)
    yy = s.para(M + 100, y + 52, q, f(BOLD, 28), W - 2 * M - 140, 38, NAVY)
    s.text(M + 30, yy + 34, "A", f(BOLD, 34), NAVY)
    s.para(M + 100, yy + 28, a, f(REG, 24), W - 2 * M - 140, 34, GREY)
    y += 214
horizon(s, 7)
navy_note(s, "Missed something?", "Ask in the comments. I'll answer every one.", "Uliza, nitajibu", seed=7)
finish(s)
s.save(7)

# ── 8 · the line ─────────────────────────────────────────────────────────────────────────────────
s = page(8, "One last time, together")
s.rect(0, 140, W, BASE + 40, NAVY)
s.rect(0, 140, W, 146, ORANGE)
smallcaps(s, M, 250, "What we said together", 16, ORANGE)
s.text(M - 4, 370, "Your starting", f(BOLD, 96), WHITE_T)
s.text(M - 4, 474, "point is not your", f(BOLD, 96), WHITE_T)
s.text(M - 4, 578, "destination.", f(BOLD, 96), WHITE_T)
s.text(M - 4, 720, "What you do now", f(BOLD, 96), ORANGE)
s.text(M - 4, 824, "shapes it.", f(BOLD, 96), ORANGE)
s.text(M, 960, "Asanteni sana!", f(SIG, 80), SOFT)
horizon(s, 8)
navy_note(s, "Save this", "For the days you doubt where you started.")
finish(s)
s.save(8)

# ── 9 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
s.text(M - 6, 290, "Were you", f(BOLD, 112), NAVY)
s.text(M - 6, 400, "there?", f(BOLD, 112), NAVY)
s.text(M, 490, "What stuck with you?", f(BOLD, 50), ORANGE)
s.text(M, 580, "Niambie kwenye comments", f(SIG, 52), ORANGE)
swash(s, M + 6, M + 440, 606, ORANGE, 5, seed=9)
rows = [("Tag", "a classmate who was in the room"), ("Share", "with someone starting FPT next year"),
        ("Comment", "your favourite round")]
y = 720
for j, (a, b) in enumerate(rows):
    s.text(M, y, f"{j + 1:02d}", f(BOLD, 22), ORANGE)
    s.text(M + 56, y, a, f(BOLD, 36), NAVY)
    s.text(M + 56, y + 40, b, f(REG, 24), GREY)
    y += 100
f4, c4 = photo(4)
polaroid(s, 840, 760, 340, 6, f4, c4, cap_size=26)
horizon(s, TOTAL)
smallcaps(s, M, BASE + 72, "Read the full recap · Soma zaidi", 17, SOFT)
s.text(M, BASE + 132, POST_URL, f(BOLD, fit(s, POST_URL, BOLD, 40, W - 2 * M)), WHITE_T)
hairline(s, M, W - M, BASE + 162, (38, 60, 100))
s.text(M, BASE + 224, "Link in bio", f(SEMI, 24), SOFT)
s.text(W - M, BASE + 224, "@_depriver", f(SEMI, 21), WHITE_T, anchor="rs")
finish(s)
s.save(TOTAL)
print("ok")
