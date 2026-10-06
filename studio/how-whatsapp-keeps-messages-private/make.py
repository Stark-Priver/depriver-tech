"""Carousel: how WhatsApp keeps messages private (end-to-end encryption), Inavyofanya kazi #4 (8 slides, 1080x1350,
exported at 2x). The device is a chat bubble travelling inside a locked box, with padlock-and-key drawings. Honest about
the limits (backups, metadata, an unlocked phone)."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/how-whatsapp-keeps-messages-private"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def padlock(s, cx, cy, size=80, col=NAVY, open_=False):
    w, h = size, size * 0.8
    s.d.rounded_rectangle([k(cx - w / 2 + 5), k(cy + 7), k(cx + w / 2 + 5), k(cy + h + 7)], radius=k(size * 0.12), fill=INK_SHADOW)
    sh = size * 0.32
    lift = size * 0.25 if open_ else 0
    s.d.arc([k(cx - sh), k(cy - sh * 1.6 - lift), k(cx + sh), k(cy + sh * 0.6 - lift)], 180, 360, fill=col, width=k(size * 0.11))
    s.d.line([k(cx - sh + size * 0.05), k(cy - sh * 0.5 - lift), k(cx - sh + size * 0.05), k(cy)], fill=col, width=k(size * 0.11))
    if not open_:
        s.d.line([k(cx + sh - size * 0.05), k(cy - sh * 0.5), k(cx + sh - size * 0.05), k(cy)], fill=col, width=k(size * 0.11))
    s.d.rounded_rectangle([k(cx - w / 2), k(cy), k(cx + w / 2), k(cy + h)], radius=k(size * 0.12), fill=col)
    s.d.ellipse([k(cx - size * 0.08), k(cy + h * 0.32), k(cx + size * 0.08), k(cy + h * 0.52)], fill=(255, 255, 255))
    s.rect(cx - size * 0.03, cy + h * 0.45, cx + size * 0.03, cy + h * 0.7, (255, 255, 255))


def key(s, x, y, size=70, col=ORANGE):
    r = size * 0.28
    s.d.ellipse([k(x), k(y - r), k(x + 2 * r), k(y + r)], outline=col, width=k(size * 0.1))
    s.d.line([k(x + 2 * r), k(y), k(x + size * 1.2), k(y)], fill=col, width=k(size * 0.1))
    for d in (0.85, 1.05):
        s.d.line([k(x + size * d), k(y), k(x + size * d), k(y + size * 0.22)], fill=col, width=k(size * 0.09))


def scrambled(s, x, y, w, seed=1):
    import random
    rnd = random.Random(seed)
    txt = "".join(rnd.choice("x9#Qa7@kL2%mZ8&") for _ in range(26))
    s.text(x, y, txt, f(MONO, fit(s, txt, MONO, 24, w)), GREY)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "How it works · Inavyofanya kazi #04")
s.text(M - 6, 250, "Can WhatsApp", f(BOLD, 92), NAVY)
s.text(M - 6, 348, "read your chats?", f(BOLD, 92), ORANGE)
s.text(M, 440, "Siri kati yako na yeye", f(SIG, 58), NAVY)
swash(s, M + 8, M + 480, 466, ORANGE, 6)
s.para(M, 550, "Short answer: no, not the messages. Long answer: end-to-end encryption, and the things it doesn't protect.",
       f(REG, 28), W - 2 * M, 42, GREY)
chat(s, M, 720, 480, "Tukutane saa kumi, usimwambie mtu", "You", mine=True, size=24, lh=33)
padlock(s, 660, 760, 110)
chat(s, 760, 760, 250, "x9#Qa7@kL2%", "Server", mine=False, size=22, lh=30)
horizon(s, 1)
cover_footer(s, "Swipe, follow your message")
finish(s)
s.save(1)

# ── 2 · E2E ──────────────────────────────────────────────────────────────────────────────────────
s = page(2, "End-to-end · Mwanzo hadi mwisho", "Inavyofanya kazi")
title2(s, "Locked on your phone.", "Opened only on theirs.", y=220, size=74)
s.para(M, 410, "End-to-end encryption (E2E) means the message is scrambled on your phone and unscrambled only on the receiver's phone.",
       f(MED, 30), W - 2 * M, 44, NAVY)
y = 620
for i, (lab, locked) in enumerate([("Your phone", False), ("WhatsApp server", True), ("Juma's phone", False)]):
    x0 = M + i * 310
    card(s, (x0, y, x0 + 280, y + 260), r=18)
    s.text(x0 + 140, y + 44, lab, f(BOLD, 24), NAVY, anchor="mm")
    padlock(s, x0 + 140, y + 125, 64, col=RED_NO if locked else GREEN_OK, open_=not locked)
    if locked:
        scrambled(s, x0 + 24, y + 225, 232)
    else:
        s.text(x0 + 140, y + 225, "“Tukutane saa kumi”", f(MED, 20), NAVY, anchor="mm")
horizon(s, 2)
navy_note(s, "So", "The server only ever sees scrambled text.", "Seva haioni ujumbe", seed=2)
finish(s)
s.save(2)

# ── 3 · keys ─────────────────────────────────────────────────────────────────────────────────────
s = page(3, "The keys · Funguo", "Inavyofanya kazi")
title2(s, "Open padlocks and", "secret keys.", y=220, size=80)
padlock(s, M + 80, 440, 90, col=ORANGE, open_=True)
s.text(M + 170, 470, "Public key", f(BOLD, 32), NAVY)
s.para(M + 170, 512, "Like an open padlock. Juma's phone gives copies to anyone who wants to send him a message.", f(REG, 26), W - 2 * M - 180, 37, GREY)
key(s, M + 20, 720, 90)
s.text(M + 170, 730, "Private key", f(BOLD, 32), NAVY)
s.para(M + 170, 772, "The only key that opens those padlocks. It is created on Juma's phone and never leaves it.", f(REG, 26), W - 2 * M - 180, 37, GREY)
s.para(M, 930, "You lock the message with Juma's padlock. Only his phone can open it.", f(SEMI, 28), W - 2 * M, 40, NAVY)
horizon(s, 3)
navy_note(s, "Name", "This is public-key cryptography (WhatsApp uses the Signal protocol).", "Kufuli na ufunguo", seed=3)
finish(s)
s.save(3)

# ── 4 · journey ──────────────────────────────────────────────────────────────────────────────────
s = page(4, "The journey · Safari", "Inavyofanya kazi")
title2(s, "Your message's", "trip.", y=220, size=88)
flow(s, [("You type and press send", "“Tukutane saa kumi”"), ("Locked on your phone", "With Juma's public key"), ("Server holds the locked box", "Delivers it, can't open it"),
         ("Juma's phone opens it", "With his private key"), ("Two blue ticks", "Delivered and read")], 410, h=88, gap=28, size=28)
horizon(s, 4)
navy_note(s, "Groups and calls", "Group chats, voice notes and calls are protected the same way.", "Hata simu", seed=4)
finish(s)
s.save(4)

# ── 5 · limits ───────────────────────────────────────────────────────────────────────────────────
s = page(5, "The limits · Mipaka", "Inavyofanya kazi")
title2(s, "What encryption", "can't protect.", y=220, size=84)
tick_fill(s, [("An unlocked phone", "Anyone holding it can read everything."), ("Screenshots and forwards", "Once Juma shares it, it's out."),
              ("Unencrypted backups", "Backups are only E2E if you turn that setting on."), ("Metadata", "Who you talk to and when can still be seen by the service."),
              ("Scams", "Encryption can't stop you sending money to a fake “boss”.")], 410, 1000, size=30, sub=25, ok=False)
horizon(s, 5)
navy_note(s, "Truth", "The weakest point is usually the person, not the maths.", "Mtu ndiye mlango", seed=5)
finish(s)
s.save(5)

# ── 6 · protect ──────────────────────────────────────────────────────────────────────────────────
s = page(6, "Protect yourself · Jilinde", "Inavyofanya kazi")
title2(s, "Five settings", "to turn on today.", y=220, size=84)
numbered(s, [("Two-step verification", "Settings > Account. A PIN stops number hijacks."), ("End-to-end encrypted backup", "Settings > Chats > Chat backup."),
             ("Screen lock on your phone", "PIN or fingerprint, always."), ("Check linked devices", "Remove any computer you don't recognise."),
             ("Never share the 6-digit code", "Nobody legit will ask you for it.")], 430, gap=112)
horizon(s, 6)
navy_note(s, "Two minutes", "Do it now, then send this to your family.", "Fanya sasa", seed=6)
finish(s)
s.save(6)

# ── 7 · for developers ───────────────────────────────────────────────────────────────────────────
s = page(7, "For developers · Kwa wasanidi", "Inavyofanya kazi")
title2(s, "What builders", "should learn.", y=220, size=86)
tick_fill(s, [("HTTPS everywhere", "Encrypts data between your app and your server."), ("Never invent your own crypto", "Use proven libraries like libsodium."),
              ("Hash passwords, never store them", "bcrypt or Argon2. More in a later post."), ("Keep secrets on the server", "API keys never ship inside the app.")],
          420, 990, size=31, sub=26)
horizon(s, 7)
navy_note(s, "Rule", "Security comes from tested tools, not clever ideas.", "Tumia zana zilizothibitishwa", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Did you turn on", "two-step?", [("Comment", "“nimewasha” when it's on"), ("Share", "with the family group"),
                                           ("Ask", "what tech I should explain next")])
padlock(s, 860, 780, 140, col=GREEN_OK)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
