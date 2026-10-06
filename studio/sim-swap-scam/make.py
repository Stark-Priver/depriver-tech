"""Carousel: SIM swap scams, how they work and how to stop them, Inavyofanya kazi #3 (8 slides, 1080x1350, exported at 2x).
Timed for the holiday season. The device is a phone stuck on "No service" while alerts arrive. Defensive only."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/sim-swap-scam"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def no_service_phone(s, x, y, w=320, h=560):
    x0, y0, x1, y1 = smartphone(s, x, y, w, h, fill=(244, 245, 248))
    s.text(x0 + 20, y0 - 8, "No service", f(SEMI, 18), RED_NO)
    for i in range(4):
        bx = x1 - 70 + i * 12
        s.rect(bx, y0 - 10 - (i + 1) * 6, bx + 7, y0 - 10, (200, 205, 215))
    s.d.line([k(x1 - 74), k(y0 - 42), k(x1 - 18), k(y0 - 8)], fill=RED_NO, width=k(3))
    cx = (x0 + x1) / 2
    s.text(cx, y0 + 120, "SOS only", f(BOLD, 34), NAVY, anchor="mm")
    s.text(cx, y0 + 160, "Hakuna mtandao", f(MED, 22), GREY, anchor="mm")
    sms(s, x0 + 14, y0 + 220, x1 - x0 - 28, "Email: password yako imebadilishwa.", sender="Gmail · 02:14", size=19, lh=26)
    sms(s, x0 + 14, y0 + 330, x1 - x0 - 28, "Umetuma TZS 850,000…", sender="Mobile money · 02:16", size=19, lh=26)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Stay safe · Usalama · Inavyofanya kazi #03")
s.text(M - 6, 250, "“No service.”", f(BOLD, 92), NAVY)
s.text(M - 6, 350, "Your money is", f(BOLD, 80), ORANGE)
s.text(M - 6, 436, "leaving.", f(BOLD, 80), ORANGE)
s.text(M, 520, "Usipuuze “No service”", f(SIG, 54), NAVY)
swash(s, M + 8, M + 460, 546, ORANGE, 6)
s.para(M, 630, "SIM swap fraud: how criminals take over your number, the warning signs, and what to do in the first 10 minutes.",
       f(REG, 27), 470, 40, GREY)
no_service_phone(s, 640, 400)
horizon(s, 1)
cover_footer(s, "Swipe, protect your number")
finish(s)
s.save(1)

# ── 2 · what it is ───────────────────────────────────────────────────────────────────────────────
s = page(2, "What it is · Ni nini", "SIM swap")
title2(s, "They don't steal", "your phone.", y=220, size=86)
s.para(M, 410, "They steal your NUMBER. A criminal gets your phone number moved to a SIM card they hold. Your SIM goes dead.",
       f(MED, 31), W - 2 * M, 46, NAVY)
label_box(s, (M, 600, W - M - 8, 860), "Why it's dangerous · Kwa nini ni hatari",
          "Your number receives the OTP codes for mobile money, banks, email and WhatsApp. Whoever holds the number can reset them.", col=RED_NO, size=29, lh=42)
horizon(s, 2)
navy_note(s, "In short", "Your number is a key to your accounts.", "Namba yako ni ufunguo", seed=2)
finish(s)
s.save(2)

# ── 3 · how it happens ───────────────────────────────────────────────────────────────────────────
s = page(3, "How it happens · Inavyotokea", "SIM swap")
title2(s, "How the attack", "usually goes.", y=220, size=84)
flow(s, [("They collect your details", "Leaked IDs, fake calls, your social media"), ("They request a new SIM", "Pretending to be you, or with an insider"),
         ("Your SIM goes dead", "“No service”, often late at night"), ("They reset your accounts", "OTPs now arrive on their phone"),
         ("Money moves fast", "Mobile money, bank, then gone")], 410, h=90, gap=28, size=28, colors=[NAVY, RED_NO])
horizon(s, 3)
navy_note(s, "Notice", "It starts long before the swap, with your personal details.", "Linda taarifa zako", seed=3)
finish(s)
s.save(3)

# ── 4 · warning signs ────────────────────────────────────────────────────────────────────────────
s = page(4, "Warning signs · Dalili", "SIM swap")
title2(s, "Signs you must", "not ignore.", y=220, size=86)
tick_fill(s, [("“No service” for a long time", "In a place where your network is usually fine."),
              ("An SMS about a SIM change", "“Your SIM has been replaced” that you didn't request."),
              ("Calls and SMS stop arriving", "Friends say your number rings somewhere else."),
              ("Login or password alerts", "Email or apps saying a new device signed in.")], 420, 990, size=31, sub=26, ok=False)
horizon(s, 4)
navy_note(s, "Rule", "Strange “No service”? Act now, not tomorrow morning.", "Chukua hatua sasa", seed=4)
finish(s)
s.save(4)

# ── 5 · first 10 minutes ─────────────────────────────────────────────────────────────────────────
s = page(5, "First 10 minutes · Dakika 10 za kwanza", "SIM swap")
title2(s, "Act in the first", "10 minutes.", y=220, size=86)
numbered(s, [("Borrow a phone, call your network", "Ask them to block the number and the new SIM."), ("Call your bank", "Freeze cards and online banking."),
             ("Change your email password", "From a computer. Email resets everything else."), ("Warn family on WhatsApp", "Scammers will message them as you."),
             ("Report it", "Police cybercrime desk, with dates and references.")], 430, gap=112)
horizon(s, 5)
navy_note(s, "Save now", "Write your network's and bank's helpline numbers on paper.", "Andika namba za msaada", seed=5)
finish(s)
s.save(5)

# ── 6 · prevent ──────────────────────────────────────────────────────────────────────────────────
s = page(6, "Prevent it · Zuia", "SIM swap")
title2(s, "Make yourself", "a hard target.", y=220, size=86)
tick_fill(s, [("Never post your ID or full details", "No NIDA photos, no birth date + phone number together."),
              ("A PIN that isn't your birthday", "For mobile money and your SIM, if your network offers one."),
              ("Authenticator app, not SMS", "For email and social media 2FA, where possible."),
              ("Never share OTPs", "No real staff will ever ask for a code sent to you.")], 420, 990, size=31, sub=26)
horizon(s, 6)
navy_note(s, "Remember", "Most swaps start with information you gave away.", "Usitoe taarifa zako", seed=6)
finish(s)
s.save(6)

# ── 7 · for developers ───────────────────────────────────────────────────────────────────────────
s = page(7, "For developers · Kwa wasanidi", "SIM swap")
title2(s, "Build apps that", "survive a swap.", y=220, size=84)
tick_fill(s, [("Don't trust SMS OTP alone for big actions", "Add a second factor: PIN, app approval, or a delay."),
              ("Check for a recent SIM change", "Some networks and gateways offer a SIM-swap check. Ask yours."),
              ("Step up on new devices", "New phone + big withdrawal = extra checks."),
              ("Alert on every change", "Email the user when phone number or password changes.")], 420, 990, size=30, sub=26)
horizon(s, 7)
navy_note(s, "Design rule", "Security that only uses SMS is only as strong as the SIM.", "SMS peke yake haitoshi", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Share this with", "your parents.", [("Share", "in the family WhatsApp group"), ("Save", "the 10-minute checklist"),
                                               ("Comment", "“nimeshare” when you've sent it")])
stamp(s, 840, 860, "IMEZUIWA", GREEN_OK, angle=-10, size=48)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
