"""Carousel: password managers and 2FA (8 slides, 1080x1350, exported at 2x). Usalama. The device is a key ring (one key
per account vs one key for everything) and a 6-digit authenticator code card."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/password-managers-and-2fa"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def key_ring(s, cx, cy, labels, r=70, col=ORANGE):
    """A ring with keys hanging off it, each labelled."""
    s.d.ellipse([k(cx - r), k(cy - r), k(cx + r), k(cy + r)], outline=NAVY, width=k(8))
    n = len(labels)
    import math
    for i, lab in enumerate(labels):
        a = math.pi * (0.15 + 0.7 * i / max(1, n - 1))
        x, y = cx + math.cos(a) * r, cy + math.sin(a) * r
        ex, ey = cx + math.cos(a) * (r + 150), cy + math.sin(a) * (r + 150)
        s.d.line([k(x), k(y), k(ex), k(ey)], fill=col, width=k(10))
        s.d.ellipse([k(x - 16), k(y - 16), k(x + 16), k(y + 16)], fill=col, outline=NAVY, width=k(3))
        w_ = s.width(lab, f(SEMI, 20)) + 26
        s.d.rounded_rectangle([k(ex - w_ / 2), k(ey + 6), k(ex + w_ / 2), k(ey + 44)], radius=k(19), fill=(255, 255, 255), outline=NAVY, width=k(2))
        s.text(ex, ey + 25, lab, f(SEMI, 20), NAVY, anchor="mm")


def code_card(s, x, y, w=380, code="482 913", label="Gmail · asha.juma"):
    card(s, (x, y, x + w, y + 170), r=20)
    smallcaps(s, x + 28, y + 46, "Authenticator", 13, ORANGE)
    s.text(x + 28, y + 80, label, f(MED, 20), GREY)
    s.text(x + 28, y + 146, code, f(MONO_B, 52), NAVY)
    cx, cy = x + w - 54, y + 110
    s.d.ellipse([k(cx - 26), k(cy - 26), k(cx + 26), k(cy + 26)], outline=PALE, width=k(7))
    s.d.arc([k(cx - 26), k(cy - 26), k(cx + 26), k(cy + 26)], -90, 150, fill=ORANGE, width=k(7))


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Stay safe · Usalama")
s.text(M - 6, 250, "One password", f(BOLD, 96), NAVY)
s.text(M - 6, 350, "for everything?", f(BOLD, 96), NAVY)
s.text(M - 6, 460, "One leak, all gone.", f(BOLD, 72), ORANGE)
s.text(M, 545, "Funguo moja, milango yote", f(SIG, 54), NAVY)
swash(s, M + 8, M + 520, 571, ORANGE, 6)
key_ring(s, 330, 680, ["Email", "M-Pesa", "Instagram", "Bank"], r=60, col=RED_NO)
code_card(s, 620, 820, 380)
horizon(s, 1)
cover_footer(s, "Swipe, lock it down")
finish(s)
s.save(1)

# ── 2 · the problem ──────────────────────────────────────────────────────────────────────────────
s = page(2, "The problem · Tatizo", "Usalama")
title2(s, "Sites get hacked.", "Not your fault.", y=220, size=84)
flow(s, [("A website you used gets leaked", "Your email + password end up on a list"), ("Criminals try that pair everywhere", "Gmail, Facebook, banking apps"),
         ("Same password = they get in", "To every account that shares it")], 430, h=130, gap=70, size=31, colors=[NAVY, RED_NO])
horizon(s, 2)
navy_note(s, "Fix", "A different password for every account. Impossible to remember, so don't.", "Neno siri tofauti kila mahali", seed=2)
finish(s)
s.save(2)

# ── 3 · password manager ─────────────────────────────────────────────────────────────────────────
s = page(3, "Password manager · Kidhibiti", "Usalama")
title2(s, "Let an app", "remember them.", y=220, size=88)
tick_fill(s, [("It stores every password, encrypted", "You remember ONE strong master password."),
              ("It creates strong ones for you", "Long and random, like tR8#vQ2!mZp9…"), ("It fills them in", "On your phone and laptop.")], 420, 760, size=31, sub=26)
smallcaps(s, M, 830, "Free options", 15, ORANGE)
chip_row(s, ["Bitwarden", "Google Password Manager", "Apple Passwords", "KeePassXC"], M, 856, size=22)
horizon(s, 3)
navy_note(s, "Start", "Your browser's built-in manager is better than one password everywhere.", "Anza leo", seed=3)
finish(s)
s.save(3)

# ── 4 · master password ──────────────────────────────────────────────────────────────────────────
s = page(4, "Master password · Neno kuu", "Usalama")
title2(s, "One passphrase", "you never forget.", y=220, size=84)
for j, (lab, ex, ok) in enumerate([("Weak", "Asha1999", False), ("Weak", "Password@123", False), ("Strong", "4–5 random words, e.g. 'nanasi-taa-mvua-kobe-saba'", True)]):
    y = 420 + j * 150
    card(s, (M, y, W - M - 8, y + 120), r=18)
    mark(s, M + 50, y + 60, ok, r=20)
    smallcaps(s, M + 90, y + 44, lab, 14, GREEN_OK if ok else RED_NO)
    s.text(M + 90, y + 92, ex, f(MONO_B if not ok else SEMI, fit(s, ex, SEMI, 30, W - 2 * M - 130)), NAVY)
s.para(M, 900, "Random words are long, easy to type and hard to guess. Don't use this exact example.", f(MED, 27), W - 2 * M, 40, NAVY)
horizon(s, 4)
navy_note(s, "Never", "Birthdays, names, phone numbers, or anything on your Instagram.", "Usitumie tarehe ya kuzaliwa", seed=4)
finish(s)
s.save(4)

# ── 5 · 2FA ──────────────────────────────────────────────────────────────────────────────────────
s = page(5, "Two-factor · Hatua mbili", "Usalama")
title2(s, "Password + phone", "= two locks.", y=220, size=84)
table(s, M, 410, ["Second factor", "Strength"], [["SMS code", "OK (SIM swap risk)"], ["Authenticator app", "Better"], ["Passkey / security key", "Best"]],
      [520, W - 2 * M - 8 - 520], size=28, rh=90)
code_card(s, M, 790, 440)
s.para(M + 480, 840, "Codes change every 30 seconds and never travel by SMS.", f(MED, 26), W - 2 * M - 490, 38, NAVY)
horizon(s, 5)
navy_note(s, "Apps", "Google Authenticator, Microsoft Authenticator, Aegis (Android).", "Programu ya kuthibitisha", seed=5)
finish(s)
s.save(5)

# ── 6 · set up today ─────────────────────────────────────────────────────────────────────────────
s = page(6, "Set up today · Fanya leo", "Usalama")
title2(s, "Do it in", "this order.", y=220, size=92)
numbered(s, [("Your main email first", "It resets everything else."), ("WhatsApp two-step PIN", "Settings > Account > Two-step verification."),
             ("Banking and mobile money apps", "Strong PIN, never your birthday."), ("Social media and GitHub", "Turn on 2FA with an authenticator app."),
             ("Save the backup codes", "On paper, somewhere safe at home.")], 430, gap=112)
horizon(s, 6)
navy_note(s, "Time", "About 30 minutes for everything. Worth it.", "Dakika 30 tu", seed=6)
finish(s)
s.save(6)

# ── 7 · for developers ───────────────────────────────────────────────────────────────────────────
s = page(7, "For developers · Kwa wasanidi", "Usalama")
title2(s, "Build login", "the safe way.", y=220, size=88)
tick_fill(s, [("Offer 2FA (TOTP) and passkeys", "Libraries exist for every framework."), ("Limit login attempts", "Slow down password guessing."),
              ("Block known-leaked passwords", "e.g. Have I Been Pwned's free password range API."), ("Alert on new devices", "Email the user when someone signs in.")],
          420, 990, size=31, sub=26)
horizon(s, 7)
navy_note(s, "Next", "How passwords are stored (hashing) gets its own post.", "Inakuja", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "How many accounts", "share a password?", [("Comment", "an honest number"), ("Save", "the setup order on slide 6"),
                                                     ("Share", "with someone who uses one password")])
code_card(s, 640, 860, 360, "731 205", "You · secured")
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
