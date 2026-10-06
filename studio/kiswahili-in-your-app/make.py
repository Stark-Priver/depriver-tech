"""Carousel: put Kiswahili in your app (localisation), Jenga kwa Tanzania #6 (8 slides, 1080x1350, exported at 2x). The
device is a before/after pair of app screens (English vs natural Kiswahili) and translation files."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/kiswahili-in-your-app"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def series_tag(s, x, y, text="Jenga kwa Tanzania #06", size=20):
    w_ = s.width(text, f(BOLD, size)) + 40
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + size * 2.1)], radius=k(size), fill=NAVY)
    s.text(x + w_ / 2, y + size * 1.08, text, f(BOLD, size), WHITE_T, anchor="mm")


def app(s, x, y, w, h, title, rows, button):
    x0, y0, x1, y1 = smartphone(s, x, y, w, h, fill=(244, 245, 248))
    s.rect(x0, y0, x1, y0 + 64, ORANGE)
    s.text(x0 + 20, y0 + 42, title, f(BOLD, 22), WHITE_T)
    yy = y0 + 100
    for a, b in rows:
        s.text(x0 + 22, yy, a, f(MED, 18), GREY)
        s.text(x0 + 22, yy + 32, b, f(BOLD, 24), NAVY)
        yy += 86
    s.d.rounded_rectangle([k(x0 + 20), k(y1 - 90), k(x1 - 20), k(y1 - 34)], radius=k(28), fill=NAVY)
    s.text((x0 + x1) / 2, y1 - 62, button, f(BOLD, 22), WHITE_T, anchor="mm")


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Build for Tanzania · Jenga kwa Tanzania")
series_tag(s, M, 165)
s.text(M - 6, 320, "Your app should", f(BOLD, 84), NAVY)
s.text(M - 6, 410, "speak Kiswahili.", f(BOLD, 84), ORANGE)
s.text(M, 495, "Ongea lugha ya mtumiaji", f(SIG, 56), NAVY)
swash(s, M + 8, M + 470, 521, ORANGE, 6)
app(s, 110, 580, 380, 440, "My Wallet", [("Available balance", "TZS 24,500"), ("Last transaction", "Sent to JUMA")], "Make payment")
app(s, 590, 580, 380, 440, "Pochi Yangu", [("Salio", "TZS 24,500"), ("Muamala wa mwisho", "Umetuma kwa JUMA")], "Lipa")
horizon(s, 1)
cover_footer(s, "Swipe, localise it right")
finish(s)
s.save(1)

# ── 2 · why ──────────────────────────────────────────────────────────────────────────────────────
s = page(2, "Why · Kwa nini", "Jenga kwa Tanzania")
title2(s, "Language is", "trust.", y=220, size=92)
tick_fill(s, [("People understand faster", "No guessing what “Proceed” or “Submit” means."), ("Fewer mistakes with money", "Clear words prevent wrong payments."),
              ("Fewer support calls", "“Hii inamaanisha nini?” costs the business time."), ("Reach more people", "Parents, traders, farmers, not only graduates.")],
          420, 990, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Best", "Offer both languages, and remember the user's choice.", "Kiswahili + English", seed=2)
finish(s)
s.save(2)

# ── 3 · natural words ────────────────────────────────────────────────────────────────────────────
s = page(3, "Natural words · Maneno ya kawaida", "Jenga kwa Tanzania")
title2(s, "Translate meaning,", "not words.", y=220, size=82)
table(s, M, 410, ["English", "Natural Kiswahili"], [["Log in", "Ingia"], ["Balance", "Salio"], ["Make payment", "Lipa"], ["Settings", "Mipangilio"],
                                                    ["An error occurred", "Kuna tatizo. Jaribu tena."], ["Are you sure?", "Una uhakika?"]],
      [380, W - 2 * M - 8 - 380], size=27, rh=78)
horizon(s, 3)
navy_note(s, "Test", "Use the words people already see in mobile money menus.", "Maneno wanayoyajua", seed=3)
finish(s)
s.save(3)

# ── 4 · i18n basics ──────────────────────────────────────────────────────────────────────────────
s = page(4, "How · Jinsi", "Jenga kwa Tanzania")
title2(s, "Never hard-code", "your text.", y=220, size=86)
half = (W - 2 * M - 30) / 2
code_window(s, 410, ["{", '  "pay": "Make payment",', '  "balance": "Balance"', "}"], file="en.json", lang="JSON", size=22, lh=38, x0=M, x1=M + half)
code_window(s, 410, ["{", '  "pay": "Lipa",', '  "balance": "Salio"', "}"], file="sw.json", lang="JSON", size=22, lh=38, x0=M + half + 30, x1=W - M - 8)
code_window(s, 720, ['button.text = t("pay")'], file="app.js", lang="JavaScript", size=26, lh=44)
s.para(M, 940, "The code asks for a key. The language file gives the words.", f(MED, 27), W - 2 * M, 40, NAVY)
horizon(s, 4)
navy_note(s, "Name", "This is called internationalisation (i18n).", "Funguo, si maneno", seed=4)
finish(s)
s.save(4)

# ── 5 · watch out ────────────────────────────────────────────────────────────────────────────────
s = page(5, "Watch out · Tahadhari", "Jenga kwa Tanzania")
title2(s, "What breaks", "when you translate.", y=220, size=84)
tick_fill(s, [("Longer text", "Kiswahili phrases are often longer. Buttons must stretch."), ("Money format", "TZS 15,000, not $15.00 or 15000 TZS."),
              ("Dates and days", "Jumatatu, 12 Januari 2027. Use the locale, not your own code."), ("Plurals", "“1 oda”, “oda 3”: plan for both forms.")],
          420, 990, size=31, sub=26, ok=False)
horizon(s, 5)
navy_note(s, "Tip", "Test every screen in Kiswahili before release.", "Jaribu kila skrini", seed=5)
finish(s)
s.save(5)

# ── 6 · test with people ─────────────────────────────────────────────────────────────────────────
s = page(6, "Test it · Jaribu", "Jenga kwa Tanzania")
title2(s, "Ask real users,", "not Google.", y=220, size=86)
tick_fill(s, [("Test with people from different regions", "Words feel different in Dar, Mwanza, Mbeya."), ("Formal but friendly", "Avoid slang in money and health apps."),
              ("Keep a glossary", "Same word for the same thing on every screen."), ("Read it out loud", "If it sounds like a robot, rewrite it.")],
          420, 990, size=31, sub=26)
horizon(s, 6)
navy_note(s, "Machine translation", "Fine for a first draft. A person must check it.", "Mtu akague", seed=6)
finish(s)
s.save(6)

# ── 7 · tools ────────────────────────────────────────────────────────────────────────────────────
s = page(7, "Tools · Zana", "Jenga kwa Tanzania")
title2(s, "Built-in tools", "for every stack.", y=220, size=86)
table(s, M, 410, ["Stack", "Use"], [["Android", "res/values-sw/strings.xml"], ["Flutter", "intl + .arb files"], ["React / web", "i18next"],
                                    ["Laravel", "lang/sw/*.php"], ["Locale code", "sw or sw-TZ"]],
      [300, W - 2 * M - 8 - 300], size=27, rh=86)
horizon(s, 7)
navy_note(s, "Start now", "Even in English-only apps, use translation keys from day one.", "Anza mapema", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which app needs", "Kiswahili most?", [("Comment", "the app, and one word it gets wrong"), ("Save", "the word table on slide 3"),
                                                 ("Share", "with an app developer")])
stamp(s, 840, 860, "KISWAHILI", GREEN_OK, angle=-10, size=44)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
