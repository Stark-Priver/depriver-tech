"""Carousel: betting and forex are not side hustles, myth vs reality (9 slides, 1080x1350, exported at 2x).
Same editorial / print direction as ai-tutor-not-copy-machine. Tone: a big brother, never a preacher. Every myth is a
torn betting slip ("Hadithi"), every reality a navy card ("Ukweli"). No shaming, and a clear way out at the end."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 9
POST_URL = "depriver.tech/blog/betting-and-forex-trap"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, chat, closing

ART.update({
    # a betting slip stamped LOST next to a red candlestick chart falling
    "slip": svg(GROUND + f'''
      <g transform="rotate(-6 180 230)">
        <path d="M80 60 h200 v300 l-12 10 l-12-10 l-12 10 l-12-10 l-12 10 l-12-10 l-12 10 l-12-10 l-12 10 l-12-10 l-12 10 l-12-10 l-12 10 l-12-10 l-12 10 l-12-10 l-12 10 l-12-10 l-8 6z" fill="#fff" {ST}/>
        <text x="180" y="100" text-anchor="middle" font-family="Liberation Mono" font-weight="700" font-size="20" fill="#0b1e3f">MULTIBET</text>
        <path d="M104 130 h150 M104 166 h120 M104 202 h140 M104 238 h100" stroke="#c9d4ea" stroke-width="10" stroke-linecap="round"/>
        <text x="104" y="290" font-family="Liberation Mono" font-weight="700" font-size="18" fill="#0b1e3f">ODDS 58.40</text>
        <g transform="rotate(-18 180 200)"><rect x="100" y="170" width="160" height="64" rx="10" fill="none" stroke="#c43434" stroke-width="7"/>
          <text x="180" y="216" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="38" fill="#c43434">LOST</text></g></g>
      <g transform="translate(330 70)">
        <path d="M0 0 V300 H240" fill="none" {ST} stroke-width="5"/>
        {"".join(f'<path d="M{30 + i * 40} {y0 - 14} v{h + 28}" stroke="#0b1e3f" stroke-width="4"/><rect x="{20 + i * 40}" y="{y0}" width="20" height="{h}" rx="3" fill="{c}" {ST} stroke-width="4"/>' for i, (y0, h, c) in enumerate([(40, 40, "#3ddc84"), (60, 50, "#c43434"), (100, 60, "#c43434"), (150, 30, "#3ddc84"), (170, 70, "#c43434"), (230, 50, "#c43434")]))}
        <path d="M20 40 C80 60 120 120 160 170 S220 260 240 280" fill="none" stroke="#c43434" stroke-width="7" stroke-linecap="round"/>
        <path d="M222 272 l20 10 l-4 -22" fill="none" stroke="#c43434" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>'''),
})


def myth(s, y, said, n):
    """Myth as a torn slip: white card with a zigzag bottom edge."""
    x0, x1, h = M, W - M - 8, 150
    pts = [(x0, y), (x1, y), (x1, y + h)]
    x = x1
    while x > x0:
        pts += [(x - 12, y + h + 12), (max(x0, x - 24), y + h)]
        x -= 24
    pts.append((x0, y + h))
    s.d.polygon([(k(a + 8), k(b + 10)) for a, b in pts], fill=(205, 211, 224))
    s.d.polygon([(k(a), k(b)) for a, b in pts], fill=(255, 255, 255), outline=NAVY)
    s.d.line([(k(a), k(b)) for a, b in pts + [pts[0]]], fill=NAVY, width=k(3))
    smallcaps(s, x0 + 30, y + 44, f"Hadithi · Myth {n:02d}", 15, RED_NO)
    s.text(x0 + 30, y + 112, said, f(BOLD, fit(s, said, BOLD, 44, x1 - x0 - 60)), NAVY)
    return y + h + 12


def reality(s, y, lines, y1=None):
    x0, x1 = M, W - M - 8
    h = 70 + 44 * len(lines) + 10
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + h)], radius=k(18), fill=NAVY)
    smallcaps(s, x0 + 30, y + 46, "Ukweli · Reality", 15, ORANGE)
    yy = y + 98
    for ln in lines:
        s.text(x0 + 30, yy, ln, f(MED, fit(s, ln, MED, 27, x1 - x0 - 60)), WHITE_T)
        yy += 44
    return y + h


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "The talk nobody gives you")
s.text(M - 6, 250, "Betting is not", f(BOLD, 96), NAVY)
s.text(M - 6, 354, "a side hustle.", f(BOLD, 96), ORANGE)
s.text(M - 4, 450, "Neither is that forex “mentor”.", f(BOLD, 50), NAVY)
s.text(M, 545, "Pesa ya haraka ni mtego", f(SIG, 62), ORANGE)
swash(s, M + 8, M + 520, 571, ORANGE, 6)
s.para(M, 660, "Four myths students believe, what's really going on, and how to get out if you're in.", f(REG, 27), 430, 40, GREY)
paste_print(s, print_art("slip", k(520)), 500, 600)
horizon(s, 1)
cover_footer(s, "Swipe, no judgement")
finish(s)
s.save(1)

# ── 2 · no judgement ─────────────────────────────────────────────────────────────────────────────
s = page(2, "Before we start · Kabla hatujaanza")
title2(s, "No judgement.", "Just honesty.", y=240, size=88)
s.para(M, 440, "Betting adverts are everywhere: on the radio, on jerseys, in every WhatsApp group. "
       "Forex “mentors” post cars and cash on Instagram.", f(MED, 28), W - 2 * M, 42, NAVY)
s.para(M, 600, "Meanwhile, students quietly lose fee money, rent money, even laptops. "
       "Nobody talks about that part, so let's talk about it.", f(REG, 26), W - 2 * M, 38, GREY)
smallcaps(s, M, 790, "What students lose quietly", 15, GREY)
x, y = M, 820
for a in ["Fee money", "Rent money", "Laptops", "Friendships"]:
    w_ = s.width(a, f(SEMI, 24)) + 44
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + 50)], radius=k(25), fill=(255, 255, 255), outline=RED_NO, width=k(2.5))
    s.text(x + w_ / 2, y + 26, a, f(SEMI, 24), RED_NO, anchor="mm")
    s.d.line([k(x + 14), k(y + 26), k(x + w_ - 14), k(y + 26)], fill=RED_NO, width=k(3))
    x += w_ + 14
horizon(s, 2)
navy_note(s, "This post", "Is for you, or for a friend who needs it.", "Tuongee ukweli", seed=2)
finish(s)
s.save(2)

# ── 3 · win it back ──────────────────────────────────────────────────────────────────────────────
s = page(3, "Myth 01 · Nitarudisha")
title2(s, "“I'll win", "it back.”", y=230, size=92)
y = myth(s, 392, "“Nikibet mara moja tu, nitarudisha.”", 1)
smallcaps(s, M, y + 50, "How chasing works", 15, GREY)
steps = [("Lose", "5,000"), ("Double", "10,000"), ("Double", "20,000"), ("Double", "40,000")]
x = M
for j, (a, b) in enumerate(steps):
    bw = 196
    card(s, (x, y + 70, x + bw - 16, y + 190), r=14)
    s.text(x + 18, y + 110, a, f(SEMI, 20), GREY)
    s.text(x + 18, y + 162, b, f(BOLD, 34), RED_NO)
    x += bw + 14
s.text(M, y + 250, "= TZS 75,000 gone, chasing a 5,000 loss.", f(BOLD, 32), NAVY)
reality(s, y + 290, ["Chasing losses is how small losses become big ones."])
horizon(s, 3)
navy_note(s, "Rule", "Lost money is gone. Don't send more after it.", "Kilichoenda kimeenda", seed=3)
finish(s)
s.save(3)

# ── 4 · my friend won ────────────────────────────────────────────────────────────────────────────
s = page(4, "Myth 02 · Rafiki yangu alishinda")
title2(s, "“My friend", "won 2 million.”", y=230, size=88)
y = myth(s, 392, "“Jamaa alishinda milioni mbili!”", 2)
# 100 dots: one winner everyone hears about
x0, y0, gap = M + 6, y + 56, 40
for i in range(100):
    cx, cy = x0 + (i % 20) * 46 + 16, y0 + (i // 20) * gap + 16
    win = i == 27
    s.d.ellipse([k(cx - 15), k(cy - 15), k(cx + 15), k(cy + 15)], fill=ORANGE if win else (200, 206, 218))
    if win: wx, wy = cx, cy
sticker(s, wx + 190, wy + 2, "the one you hear about", angle=-4, size=16, bg=NAVY)
s.text(M, y0 + 5 * gap + 34, "Illustration: the winners talk, the losers stay quiet.", f(REG, 21), GREY)
reality(s, y0 + 5 * gap + 60, ["Odds are built so the house wins over time.", "That's how betting companies pay for the ads."])
horizon(s, 4)
navy_note(s, "Remember", "The house always has the edge. Always.", "Nyumba haishindwi", seed=4)
finish(s)
s.save(4)

# ── 5 · forex mentor ─────────────────────────────────────────────────────────────────────────────
s = page(5, "Myth 03 · Forex mentor")
title2(s, "“Double your", "money in a week.”", y=220, size=80)
y = chat(s, M, 390, W - 2 * M - 120, "Join my VIP signals group, only 50k. Send your capital to my account manager and earn 30% weekly, guaranteed!",
         "Forex mentor · DM", mine=False, size=27, lh=38, tag="Red flag", tag_ok=False)
reality(s, y + 40, ["Most retail forex traders lose money. Regulated", "brokers in the UK and EU must warn: often 70%+.",
                    "“Guaranteed” returns = scam. Every time.", "Never send money to an “account manager”."])
horizon(s, 5)
navy_note(s, "Check", "Anyone handling your money must be licensed (CMSA).", "Usitapeliwe", seed=5)
finish(s)
s.save(5)

# ── 6 · just small money ─────────────────────────────────────────────────────────────────────────
s = page(6, "Myth 04 · Ni pesa ndogo tu")
title2(s, "“It's just", "small money.”", y=230, size=88)
rows = [("Per day", "TZS 2,000", NAVY), ("Per month", "TZS 60,000", NAVY), ("Per year", "TZS 730,000", RED_NO)]
y = 420
for a, b, col in rows:
    s.text(M, y, a, f(SEMI, 28), GREY)
    s.text(W - M, y, b, f(BOLD, 56 if col == RED_NO else 46), col, anchor="rs")
    hairline(s, M, W - M, y + 26, RULE)
    y += 96
smallcaps(s, M, y + 20, "What 730,000 could buy instead", 15, ORANGE)
buys = ["A year of internet bundles", "Domain + hosting for years", "A certificate exam", "Half a used laptop"]
y += 60
for j, b in enumerate(buys):
    x = M + (j % 2) * ((W - 2 * M) / 2)
    yy = y + (j // 2) * 64
    mark(s, x + 16, yy - 9, True, r=14)
    s.text(x + 42, yy, b, f(SEMI, 25), NAVY)
horizon(s, 6)
navy_note(s, "Try this", "Write down every shilling you bet for one month.", "Hesabu haidanganyi", seed=6)
finish(s)
s.save(6)

# ── 7 · signs ────────────────────────────────────────────────────────────────────────────────────
s = page(7, "Check yourself · Jipime")
title2(s, "Is it becoming", "a problem?", y=220, size=84)
signs = ["You borrow money to bet", "You hide it from family or friends", "Fee or rent money goes to bets",
         "You chase losses to “win it back”", "You think about bets during class", "You feel restless when you stop"]
y = 420
for t_ in signs:
    s.d.rounded_rectangle([k(M), k(y - 30), k(M + 34), k(y + 4)], radius=k(7), outline=NAVY, width=k(3))
    s.text(M + 56, y, t_, f(SEMI, 30), NAVY)
    hairline(s, M + 56, W - M, y + 24, RULE)
    y += 82
sticker(s, W - M - 190, 940, "2 or more? Talk to someone", angle=-5, size=19)
horizon(s, 7)
navy_note(s, "It's not weakness", "These apps are designed to keep you playing.", "Si udhaifu, ni mtego", seed=7)
finish(s)
s.save(7)

# ── 8 · way out ──────────────────────────────────────────────────────────────────────────────────
s = page(8, "The way out · Njia ya kutoka")
title2(s, "Want out?", "Start today.", y=220, size=88)
steps = [("Delete the apps", "And log out of betting sites on every device."),
         ("Tell one person you trust", "A friend, a sibling, a parent. Secrets feed it."),
         ("Make money hard to reach", "Move savings where you can't spend them fast."),
         ("Talk to a counsellor", "Most universities have one. It's confidential."),
         ("Replace it with a skill", "Put that time into a gig that actually pays.")]
numbered(s, steps, 430, gap=110)
horizon(s, 8)
navy_note(s, "Remember", "One bad season doesn't define you. What you do now does.", "Bado hujachelewa", seed=8)
finish(s)
s.save(8)

# ── 9 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What would you do", "with 730k a year?", [("Save", "for the day someone says “nitarudisha”"),
                                                     ("Share", "with a friend who needs it, quietly"),
                                                     ("Comment", "what you'd build with 730k")])
s.text(W - M, 980, "Real money is slow.", f(BOLD, 30), NAVY, anchor="rs")
s.text(W - M, 1020, "Skills are faster.", f(BOLD, 30), ORANGE, anchor="rs")
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
