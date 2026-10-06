"""Carousel: don't get hacked, scams every Tanzanian student gets (9 slides, 1080x1350, exported at 2x).
Same editorial / print direction as kamusi-ya-tech. Every scam is the real-looking message (SMS / WhatsApp bubble
from a masked number) stamped UTAPELI, then the truth and what to do. Reporting: forward to TCRA's free 15040."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 9
POST_URL = "depriver.tech/blog/dont-get-hacked"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, chat, closing


def stamp(s, cx, cy, text="UTAPELI", angle=-12, size=46, color=RED_NO):
    """Rubber stamp: outlined box with worn ink."""
    fnt = f(BOLD, size)
    tw = s.width(text, fnt)
    w, h = tw + 50, size * 1.7
    lay = Image.new("RGBA", (k(w + 30), k(h + 30)), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    ink = color + (225,)
    ld.rounded_rectangle([k(15), k(15), k(15 + w), k(15 + h)], radius=k(10), outline=ink, width=k(6))
    ld.text((k(15 + w / 2), k(15 + h / 2 + 2)), text, font=fnt, fill=ink, anchor="mm")
    worn = Image.effect_noise(lay.size, 90).point(lambda v: 255 if v > 64 else 110)
    lay.putalpha(ImageChops.multiply(lay.getchannel("A"), worn))
    lay = lay.rotate(angle, resample=Image.BICUBIC, expand=True)
    s.im.paste(lay, (k(cx) - lay.width // 2, k(cy) - lay.height // 2), lay)
    s.d = ImageDraw.Draw(s.im)


def truth(s, y, ukweli, fanya):
    x0, x1 = M, W - M - 8
    lines = wrap_lines(s, ukweli, f(MED, 31), x1 - x0 - 60) + wrap_lines(s, fanya, f(REG, 28), x1 - x0 - 60)
    h = 160 + lines * 44
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + h)], radius=k(18), fill=NAVY)
    smallcaps(s, x0 + 30, y + 46, "Ukweli · The truth", 15, ORANGE)
    yy = s.para(x0 + 30, y + 96, ukweli, f(MED, 31), x1 - x0 - 60, 44, WHITE_T)
    smallcaps(s, x0 + 30, yy + 22, "Fanya hivi · Do this", 15, (120, 220, 160))
    s.para(x0 + 30, yy + 66, fanya, f(REG, 28), x1 - x0 - 60, 42, SOFT)
    return y + h


def scam_slide(n, label, t1, t2, who, msg, ukweli, fanya, sw, rule):
    s = page(n, label)
    title2(s, t1, t2, y=220, size=80)
    y = chat(s, M, 380, W - 2 * M - 90, msg, who, mine=False, size=30, lh=42)
    stamp(s, W - M - 170, y - 10, angle=-10)
    truth(s, y + 50, ukweli, fanya)
    horizon(s, n)
    navy_note(s, "Kumbuka", rule, sw, seed=n)
    finish(s)
    s.save(n)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Cyber safety for students")
s.text(M - 6, 250, "Umeshinda", f(BOLD, 104), NAVY)
s.text(M - 6, 360, "milioni 5?", f(BOLD, 104), NAVY)
s.text(M - 8, 490, "Hapana.", f(BOLD, 140), ORANGE)
s.text(M, 580, "Usitapeliwe mtandaoni", f(SIG, 62), NAVY)
swash(s, M + 8, M + 480, 606, ORANGE, 6)
s.para(M, 690, "Five scams every student in Tanzania gets, how to spot them, and how to report them.", f(REG, 27), 420, 40, GREY)
y = chat(s, 520, 650, 470, "Hongera! Umeshinda TZS 5,000,000. Tuma 20,000 ya usajili kupokea zawadi yako.", "+255 7XX XXX XXX", mine=False, size=23, lh=32)
y = chat(s, 560, y + 30, 430, "Nimekosea kutuma pesa kwako, naomba unirudishie.", "+255 6XX XXX XXX", mine=False, size=23, lh=32)
stamp(s, 790, 760, angle=-12, size=40)
horizon(s, 1)
cover_footer(s, "Swipe before you send anything")
finish(s)
s.save(1)

# ── 2–6 · scams ──────────────────────────────────────────────────────────────────────────────────
scam_slide(2, "Scam 01 · Nimekosea kutuma", "“I sent you", "money by mistake.”", "SMS · +255 7XX XXX XXX",
           "Ndugu, nimekosea kutuma TZS 50,000 kwenye namba yako. Naomba unirudishie kwa namba hii, Mungu akubariki.",
           "The “you received money” SMS is fake. It's typed to look like a real confirmation, but no money came.",
           "Check your balance in your official mobile money menu or app, never in the SMS. No money, no refund.",
           "Angalia salio lako kwanza", "The SMS is not your balance. Your menu is.")
scam_slide(3, "Scam 02 · WhatsApp code", "“Send me", "that 6-digit code.”", "WhatsApp · Rafiki?",
           "Samahani, nimekutumia code ya tarakimu 6 kwa makosa. Tafadhali nitumie, ni ya akaunti yangu mpya.",
           "That code is YOUR WhatsApp login. Send it and they take your account, then ask your contacts for money in your name.",
           "Never share login codes with anyone. Turn on WhatsApp two-step verification: Settings, Account, Two-step verification.",
           "Code yako ni siri yako", "No real friend needs your login code.")
scam_slide(4, "Scam 03 · Fake job or scholarship", "“You got the job.", "Pay 30k to register.”", "SMS · HR Recruitment",
           "Hongera! Umechaguliwa kazi ya data entry, mshahara 800,000 kwa mwezi. Lipa 30,000 ya usajili leo kuthibitisha nafasi yako.",
           "Real employers and scholarships never ask you to pay to get the job. Pay to get a job = scam.",
           "Search the company yourself, call their official number, and never pay a “registration fee”.",
           "Kazi halisi haikulipishi", "Real work pays you. Scams ask you to pay.")
scam_slide(5, "Scam 04 · Bonyeza link", "“Free bundle.", "Just click the link.”", "WhatsApp · Group forward",
           "OFA! Pata GB 50 bure kwa siku 30. Bonyeza link hii na weka namba yako na password kuthibitisha: bit.ly/...",
           "Fake links copy real login pages to steal your passwords, or install apps that spy on your phone.",
           "Don't open links from forwards. Type the real website yourself. Never enter passwords after clicking a link.",
           "Usibonyeze kila link", "Free + urgent + link = think twice.")
scam_slide(6, "Scam 05 · SIM swap", "“Customer care", "needs your PIN.”", "Call · “Huduma kwa wateja”",
           "Habari, tunahakiki laini yako ili isifungwe. Tafadhali tuambie PIN yako ya pesa na majina kamili.",
           "Your network will never ask for your PIN. Scammers use your details to move your number to their SIM.",
           "Hang up. If your line suddenly shows “No service”, call your provider from another phone immediately.",
           "PIN yako ni yako peke yako", "Nobody from your network ever asks for your PIN.")

# ── 7 · protection kit ───────────────────────────────────────────────────────────────────────────
s = page(7, "Your protection kit · Kinga")
title2(s, "Lock your", "digital life.", y=220, size=84)
kit_ = [("Two-step verification everywhere", "Email, WhatsApp, Instagram, banking apps."),
        ("Different password per account", "Use a password manager, not your birthday."),
        ("Screen lock on your phone", "PIN or fingerprint. Phones get lost."),
        ("Log out on public computers", "Cyber cafés and lab PCs remember you."),
        ("Update your phone and apps", "Updates close holes that hackers use."),
        ("Check app permissions", "A torch app doesn't need your contacts.")]
y = 420
for a, b in kit_:
    mark(s, M + 18, y - 10, True)
    s.text(M + 56, y, a, f(BOLD, fit(s, a, BOLD, 30, W - 2 * M - 60)), NAVY)
    s.text(M + 56, y + 38, b, f(REG, 23), GREY)
    y += 100
horizon(s, 7)
navy_note(s, "Start with", "Turn on two-step verification on WhatsApp today.", "Funga mlango", seed=7)
finish(s)
s.save(7)

# ── 8 · report ───────────────────────────────────────────────────────────────────────────────────
s = page(8, "Report it · Ripoti utapeli")
title2(s, "Report scams", "to 15040.", y=220, size=88)
s.text(M, 410, "Free · TCRA, with the police and your network", f(SEMI, 26), GREY)
for j, (hdr, steps) in enumerate([("Scam SMS", ["Forward the scam message to 15040", "Then enter the number that sent it"]),
                                 ("Scam call", ["Send the word UTAPELI to 15040", "Then enter the number that called you"])]):
    y0 = 460 + j * 230
    card(s, (M, y0, W - M - 8, y0 + 200))
    s.text(M + 30, y0 + 58, hdr, f(BOLD, 34), ORANGE)
    for i, st in enumerate(steps):
        s.text(M + 30, y0 + 112 + i * 48, f"{i + 1}.", f(BOLD, 26), NAVY)
        s.text(M + 70, y0 + 112 + i * 48, st, f(MED, 26), NAVY)
s.text(M, 960, "Hacked already? Recover the account, then warn your contacts.", f(SEMI, fit(s, "Hacked already? Recover the account, then warn your contacts.", SEMI, 26, W - 2 * M)), NAVY)
horizon(s, 8)
navy_note(s, "Then", "Tell your friends. Scammers reuse the same tricks.", "Ripoti, linda wenzako", seed=8)
finish(s)
s.save(8)

# ── 9 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which scam message", "have you received?", [("Save", "before your next “umeshinda” SMS"), ("Share", "with family, especially parents"),
                                                       ("Comment", "the scam you've seen")])
stamp(s, 820, 760, angle=-12, size=50)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
