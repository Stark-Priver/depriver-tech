"""Carousel: USSD apps, Jenga kwa Tanzania #1 (9 slides, 1080x1350, exported at 2x). The device is a feature phone
showing a USSD menu, from dialling to the server's reply. Providers are named only as examples."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 9
POST_URL = "depriver.tech/blog/ussd-apps"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def series_tag(s, x, y, text="Jenga kwa Tanzania #01", size=20):
    w_ = s.width(text, f(BOLD, size)) + 40
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + size * 2.1)], radius=k(size), fill=NAVY)
    s.text(x + w_ / 2, y + size * 1.08, text, f(BOLD, size), WHITE_T, anchor="mm")


MENU = ["1. Angalia bei", "2. Weka oda", "3. Salio la deni", "4. Msaada"]

# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Build for Tanzania · Jenga kwa Tanzania")
series_tag(s, M, 165)
s.text(M - 6, 330, "*150*00#", f(BOLD, 100), ORANGE)
s.text(M - 6, 430, "is an app too.", f(BOLD, 76), NAVY)
s.text(M, 520, "Programu bila internet", f(SIG, 58), NAVY)
swash(s, M + 8, M + 470, 546, ORANGE, 6)
s.para(M, 630, "Millions use USSD every day on phones without internet. Most students never learn to build it.", f(REG, 28), 470, 42, GREY)
s.text(M, 860, "How it works, how to build", f(SEMI, 27), NAVY)
s.text(M, 900, "one for free, and app ideas.", f(SEMI, 27), NAVY)
feature_phone(s, 640, 190, 330, MENU, title="Duka la Mama Asha", size=22, lh=34)
horizon(s, 1)
cover_footer(s, "Swipe, let's build one")
finish(s)
s.save(1)

# ── 2 · why ──────────────────────────────────────────────────────────────────────────────────────
s = page(2, "Why USSD · Kwa nini USSD")
title2(s, "Works on every", "phone in Tanzania.", y=220, size=80)
tick_fill(s, [("No internet, no smartphone needed", "A TZS 25,000 kitochi works perfectly."),
              ("Nothing to install", "Dial a code, the menu appears."),
              ("People already trust it", "Mobile money, banks and bundles all use USSD."),
              ("Fast and cheap for the user", "Short text menus, answers in seconds.")], 420, 1000, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Think", "Your users may not have data. They almost always have airtime.", "Mfikie kila mtu", seed=2)
finish(s)
s.save(2)

# ── 3 · how it works ─────────────────────────────────────────────────────────────────────────────
s = page(3, "How it works · Inavyofanya kazi")
title2(s, "From *123# to", "your server.", y=220, size=84)
flow(s, [("User dials the code", "e.g. *123*45#"), ("Mobile network receives it", "Vodacom, Airtel, Yas, Halotel…"),
         ("USSD gateway / aggregator", "Turns it into a web request"), ("Your server decides", "Reads the choice, builds the next menu"),
         ("Text goes back to the phone", "The next menu, or the final answer")], 410, h=88, gap=28, size=28)
horizon(s, 3)
navy_note(s, "Key idea", "For you, a USSD app is just a web endpoint that returns text.", "Ni API inayorudisha maandishi", seed=3)
finish(s)
s.save(3)

# ── 4 · code ─────────────────────────────────────────────────────────────────────────────────────
s = page(4, "The code · Code yenyewe")
title2(s, "CON continues.", "END finishes.", y=220, size=84)
y = code_window(s, 370, ['@app.post("/ussd")', "def ussd():", '    text = request.form["text"]', '    if text == "":',
                         '        return "CON Karibu\\n1. Bei\\n2. Oda"', '    if text == "1":', '        return "END Sukari: TZS 3,000"',
                         '    return "END Asante!"'], file="ussd.py", lang="Python · Flask", size=24, lh=40)
s.para(M, y + 60, "This is the Africa's Talking style: text holds the user's choices so far, like \"1*2\". Other gateways are similar.",
       f(REG, 25), W - 2 * M, 36, GREY)
horizon(s, 4)
navy_note(s, "That's it", "About 10 lines give you a working menu.", "Mistari kumi tu", seed=4)
finish(s)
s.save(4)

# ── 5 · design rules ─────────────────────────────────────────────────────────────────────────────
s = page(5, "Design rules · Kanuni za muundo")
title2(s, "Short menus", "win.", y=220, size=92)
tick_fill(s, [("Keep each screen short", "USSD screens hold about 182 characters. Count them."),
              ("Numbered choices, max 5 or 6", "Add 0 for “back” and 00 for “main menu”."),
              ("Speak the user's language", "Kiswahili first. “Salio”, not “Account balance”."),
              ("Sessions time out fast", "Few steps. Never make people type long text.")], 410, 1000, size=31, sub=26)
horizon(s, 5)
navy_note(s, "Always", "Confirm before money moves: “Lipa TZS 3,000? 1. Ndiyo 2. Hapana”.", "Thibitisha kwanza", seed=5)
finish(s)
s.save(5)

# ── 6 · build it free ────────────────────────────────────────────────────────────────────────────
s = page(6, "Build it free · Jenga bure")
title2(s, "Test it today,", "for free.", y=220, size=88)
numbered(s, [("Write the endpoint", "Flask, Express, Laravel: any web framework works."), ("Expose it to the internet", "Deploy free, or use a tunnel like ngrok while testing."),
             ("Open a gateway sandbox", "e.g. Africa's Talking has a free USSD simulator."), ("Dial it in the simulator", "Click through every path, including mistakes."),
             ("Record a demo video", "Perfect for your portfolio and CV.")], 420, gap=112)
horizon(s, 6)
navy_note(s, "Check", "Read the gateway's current docs. Details change.", "Soma docs", seed=6)
finish(s)
s.save(6)

# ── 7 · going live ───────────────────────────────────────────────────────────────────────────────
s = page(7, "Going live · Kwenda hewani")
title2(s, "Going live is a", "business step.", y=220, size=82)
tick_fill(s, [("You need a USSD code", "Shared or dedicated, through an aggregator and the networks."),
              ("Usually a registered business", "Live codes go to companies, schools, SACCOs and NGOs."),
              ("There are monthly costs", "Ask aggregators for current prices before you promise a client."),
              ("Rules apply", "Telecom regulations and data protection. Ask the provider what's needed.")], 410, 1000, size=31, sub=26)
horizon(s, 7)
navy_note(s, "Student tip", "Build the demo now. Sell it to a client who already has a code.", "Anza na demo", seed=7)
finish(s)
s.save(7)

# ── 8 · ideas ────────────────────────────────────────────────────────────────────────────────────
s = page(8, "Ideas · Mawazo ya kujenga")
title2(s, "USSD apps worth", "building.", y=220, size=84)
ideas = [("School fees balance", "Parents check fees and results"), ("Clinic appointments", "Book and get an SMS reminder"),
         ("Crop prices for farmers", "Today's price at nearby markets"), ("SACCO / VICOBA balance", "Members check savings and loans"),
         ("Shop orders", "Retailers order stock from a wholesaler"), ("Water bill check", "Balance and payment options")]
cw = (W - 2 * M - 24) / 2
for i, (a, b) in enumerate(ideas):
    x0, y0 = M + (i % 2) * (cw + 24), 410 + (i // 2) * 190
    card(s, (x0, y0, x0 + cw - 8, y0 + 160), r=16)
    s.text(x0 + 28, y0 + 58, f"{i + 1:02d}", f(BOLD, 24), ORANGE)
    s.para(x0 + 80, y0 + 58, a, f(BOLD, 27), cw - 120, 34, NAVY)
    s.para(x0 + 28, y0 + 124 if wrap_lines(s, a, f(BOLD, 27), cw - 120) == 1 else y0 + 132, b, f(REG, 22), cw - 60, 30, GREY)
horizon(s, 8)
navy_note(s, "Final year?", "Any of these is a strong, very Tanzanian final year project.", "Tatua tatizo la kwetu", seed=8)
finish(s)
s.save(8)

# ── 9 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What would you", "build with USSD?", [("Save", "for your next project"), ("Share", "with your FYP group"),
                                                 ("Comment", "your USSD idea")])
feature_phone(s, 720, 620, 250, ["Asante!", "Oda yako", "imepokelewa."], size=19, lh=28, keypad=False)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
