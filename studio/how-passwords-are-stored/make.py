"""Carousel: how passwords are stored (hashing and salt), Inavyofanya kazi #6 (8 slides, 1080x1350, exported at 2x). The
device is a hash machine: a password goes in, scrambled text comes out, and nothing comes back the other way."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/how-passwords-are-stored"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def machine(s, y, inp, out, label="HASH", x0=M, x1=None):
    """Input pill -> navy machine box -> output pill, with a crossed-out return arrow."""
    x1 = x1 or W - M - 8
    mw = 230
    mx = (x0 + x1) / 2 - mw / 2
    s.rect(mx + 8, y + 10, mx + mw + 8, y + 170, INK_SHADOW, r=24)
    s.d.rounded_rectangle([k(mx), k(y), k(mx + mw), k(y + 160)], radius=k(24), fill=NAVY)
    for i in range(3):
        s.d.ellipse([k(mx + 40 + i * 60), k(y + 100), k(mx + 80 + i * 60), k(y + 140)], outline=ORANGE, width=k(5))
    s.text(mx + mw / 2, y + 60, label, f(BOLD, 34), WHITE_T, anchor="mm")
    pw = (mx - x0) - 50
    for j, (txt, xx, col) in enumerate([(inp, x0, NAVY), (out, mx + mw + 50, GREY)]):
        s.d.rounded_rectangle([k(xx), k(y + 50), k(xx + pw), k(y + 110)], radius=k(30), fill=(255, 255, 255), outline=NAVY, width=k(3))
        s.text(xx + pw / 2, y + 80, txt, f(MONO_B, fit(s, txt, MONO_B, 26, pw - 30, smallest=10)), col, anchor="mm")
    for ax in (mx - 44, mx + mw + 6):
        s.d.line([k(ax), k(y + 80), k(ax + 36), k(y + 80)], fill=ORANGE, width=k(5))
        s.d.polygon([(k(ax + 30), k(y + 70)), (k(ax + 42), k(y + 80)), (k(ax + 30), k(y + 90))], fill=ORANGE)
    yy = y + 220
    s.d.line([k(mx + mw), k(yy), k(mx), k(yy)], fill=(150, 158, 175), width=k(4))
    s.d.polygon([(k(mx + 10), k(yy - 10)), (k(mx - 2), k(yy)), (k(mx + 10), k(yy + 10))], fill=(150, 158, 175))
    red_ring(s, mx + mw / 2 - 30, yy - 30, mx + mw / 2 + 30, yy + 30)
    s.d.line([k(mx + mw / 2 - 21), k(yy - 21), k(mx + mw / 2 + 21), k(yy + 21)], fill=RED_NO, width=k(5))
    s.text(mx + mw / 2, yy + 60, "No way back · Haiwezi kurudi", f(SEMI, 21), RED_NO, anchor="mm")
    return yy + 80


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "How it works · Inavyofanya kazi #06")
s.text(M - 6, 250, "Websites shouldn't", f(BOLD, 84), NAVY)
s.text(M - 6, 340, "know your password.", f(BOLD, 84), ORANGE)
s.text(M, 430, "Hata wao hawajui", f(SIG, 58), NAVY)
swash(s, M + 8, M + 380, 456, ORANGE, 6)
s.para(M, 540, "Good systems store a scrambled fingerprint, not the password. Here's how hashing works.", f(REG, 28), W - 2 * M, 42, GREY)
machine(s, 690, "embe123", "$2b$12$Kx9…")
horizon(s, 1)
cover_footer(s, "Swipe, look inside")
finish(s)
s.save(1)

# ── 2 · never plain text ─────────────────────────────────────────────────────────────────────────
s = page(2, "The wrong way · Njia mbaya", "Inavyofanya kazi")
title2(s, "Plain text is", "a disaster.", y=220, size=88)
table(s, M, 410, ["email", "password"], [["asha@…", "Asha1999"], ["juma@…", "embe123"], ["neema@…", "Password@123"]],
      [440, W - 2 * M - 8 - 440], size=27, rh=80, hl_rows=(0, 1, 2))
stamp(s, 850, 690, "HATARI", RED_NO, angle=-12, size=50)
s.para(M, 800, "One leak and every user's password is exposed, and they probably use it on other sites too.", f(MED, 30), W - 2 * M, 44, NAVY)
horizon(s, 2)
navy_note(s, "Red flag", "If “forgot password” emails you your old password, they store it wrongly.", "Ishara mbaya", seed=2)
finish(s)
s.save(2)

# ── 3 · hashing ──────────────────────────────────────────────────────────────────────────────────
s = page(3, "Hashing · Kusaga", "Inavyofanya kazi")
title2(s, "A one-way", "machine.", y=220, size=92)
y = machine(s, 420, "embe123", "a8f3…91c")
tick_list(s, [("Same input, same output, every time", None), ("Tiny change, totally different output", None), ("You can't turn the output back", None)], y + 60, size=29)
horizon(s, 3)
navy_note(s, "Like", "Blending a mango: easy to make juice, impossible to rebuild the mango.", "Kama juisi ya embe", seed=3)
finish(s)
s.save(3)

# ── 4 · login check ──────────────────────────────────────────────────────────────────────────────
s = page(4, "Logging in · Kuingia", "Inavyofanya kazi")
title2(s, "How login checks", "without knowing.", y=220, size=82)
flow(s, [("You type your password", "embe123"), ("The server hashes it again", "Same machine, same settings"), ("Compares with the stored hash", "Does a8f3…91c = a8f3…91c?"),
         ("Match? You're in", "No match? “Password si sahihi”")], 410, h=100, gap=36, size=29)
horizon(s, 4)
navy_note(s, "So", "The real password is never saved anywhere.", "Haihifadhiwi popote", seed=4)
finish(s)
s.save(4)

# ── 5 · salt ─────────────────────────────────────────────────────────────────────────────────────
s = page(5, "Salt · Chumvi", "Inavyofanya kazi")
title2(s, "Add salt, so twins", "look different.", y=220, size=82)
table(s, M, 410, ["User", "Password", "Salt", "Stored hash"], [["Asha", "embe123", "x7Q…", "91be…"], ["Juma", "embe123", "Lp2…", "c04f…"]],
      [190, 250, 190, W - 2 * M - 8 - 630], size=26, rh=86)
s.para(M, 720, "Salt is random text added to each password before hashing. Same password, different hashes.", f(MED, 30), W - 2 * M, 44, NAVY)
s.para(M, 860, "This stops attackers using giant pre-computed tables of common passwords.", f(REG, 27), W - 2 * M, 40, GREY)
horizon(s, 5)
navy_note(s, "Good news", "Modern tools add the salt for you automatically.", "Zana zinafanya kazi hii", seed=5)
finish(s)
s.save(5)

# ── 6 · slow hashes ──────────────────────────────────────────────────────────────────────────────
s = page(6, "Slow is good · Polepole ni bora", "Inavyofanya kazi")
title2(s, "Use a slow", "password hash.", y=220, size=88)
table(s, M, 410, ["Algorithm", "For passwords?"], [["bcrypt", "Yes"], ["Argon2", "Yes (modern choice)"], ["scrypt", "Yes"], ["MD5 / SHA-1", "No, far too fast"],
                                                   ["SHA-256 alone", "No, also too fast"]],
      [420, W - 2 * M - 8 - 420], size=27, rh=82, hl_rows=(3, 4))
horizon(s, 6)
navy_note(s, "Why slow?", "Slow for one login is fine. Slow for a billion guesses stops attackers.", "Mwizi achoke", seed=6)
finish(s)
s.save(6)

# ── 7 · code ─────────────────────────────────────────────────────────────────────────────────────
s = page(7, "The code · Code", "Inavyofanya kazi")
title2(s, "Two functions.", "That's it.", y=220, size=88)
y = code_window(s, 400, ["// register", "$hash = password_hash($password,", "                      PASSWORD_DEFAULT);", "",
                         "// login", "if (password_verify($password, $hash)) {", '    echo "Karibu!";', "}"], file="auth.php", lang="PHP", size=24, lh=40)
s.para(M, y + 56, "Laravel's Hash::make() and Django's auth do this for you. Python: the bcrypt or argon2 packages.", f(REG, 25), W - 2 * M, 36, GREY)
horizon(s, 7)
navy_note(s, "Rule", "Never write your own hashing. Use the framework's.", "Usibuni yako", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "How does your", "project store them?", [("Check", "your FYP or project code today"), ("Save", "the code on slide 7"),
                                                    ("Share", "with your backend teammate")])
stamp(s, 840, 860, "SALAMA", GREEN_OK, angle=-10, size=56)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
