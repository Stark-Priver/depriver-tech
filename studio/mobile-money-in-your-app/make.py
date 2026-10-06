"""Carousel: accept mobile money in your app, Jenga kwa Tanzania #2 (8 slides, 1080x1350, exported at 2x). The device is
a phone showing the PIN prompt (USSD push) and a payment flow from "Lipa" to "Paid". Providers named only as examples."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/mobile-money-in-your-app"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def series_tag(s, x, y, text="Jenga kwa Tanzania #02", size=20):
    w_ = s.width(text, f(BOLD, size)) + 40
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + size * 2.1)], radius=k(size), fill=NAVY)
    s.text(x + w_ / 2, y + size * 1.08, text, f(BOLD, size), WHITE_T, anchor="mm")


def pin_prompt(s, x, y, w=330, h=560):
    scr = smartphone(s, x, y, w, h, fill=(236, 239, 245))
    x0, y0, x1, y1 = scr
    bx0, bx1 = x0 + 18, x1 - 18
    by0 = y0 + 90
    s.d.rounded_rectangle([k(bx0), k(by0), k(bx1), k(by0 + 290)], radius=k(14), fill=(255, 255, 255), outline=NAVY, width=k(2))
    s.para(bx0 + 20, by0 + 46, "Lipa TZS 15,000 kwa DUKA LA ASHA. Weka PIN kuthibitisha.", f(MED, 21), bx1 - bx0 - 40, 30, NAVY)
    s.d.rounded_rectangle([k(bx0 + 20), k(by0 + 160), k(bx1 - 20), k(by0 + 210)], radius=k(8), fill=(244, 245, 248), outline=(180, 188, 205), width=k(2))
    s.text(bx0 + 40, by0 + 194, "• • • •", f(BOLD, 24), NAVY)
    s.text(bx0 + 30, by0 + 262, "CANCEL", f(SEMI, 18), GREY)
    s.text(bx1 - 30, by0 + 262, "SEND", f(BOLD, 18), ORANGE, anchor="rs")


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Build for Tanzania · Jenga kwa Tanzania")
series_tag(s, M, 165)
s.text(M - 6, 320, "“Lipa kwa", f(BOLD, 92), NAVY)
s.text(M - 6, 418, "simu”", f(BOLD, 92), ORANGE)
s.text(M - 6, 500, "inside your app.", f(BOLD, 60), NAVY)
s.text(M, 585, "Malipo ndani ya mfumo wako", f(SIG, 52), NAVY)
swash(s, M + 8, M + 520, 609, ORANGE, 6)
s.para(M, 690, "The flow every Tanzanian business app needs, how it works, and the rules that keep money safe.", f(REG, 27), 440, 40, GREY)
pin_prompt(s, 640, 330)
horizon(s, 1)
cover_footer(s, "Swipe, let's wire it up")
finish(s)
s.save(1)

# ── 2 · two roads ────────────────────────────────────────────────────────────────────────────────
s = page(2, "Two roads · Njia mbili", "Jenga kwa Tanzania")
title2(s, "Direct or through", "an aggregator.", y=230, size=80)
half = (W - 2 * M - 30) / 2
for j, (head, sub, pts, col) in enumerate([("Direct", "One operator's API", ["e.g. an operator's open API portal", "One network per integration", "Deeper control"], NAVY),
                                            ("Aggregator", "One API, many networks", ["e.g. Selcom, AzamPay, ClickPesa", "Most networks, cards, banks", "Fastest way to start"], ORANGE)]):
    x0 = M + j * (half + 30)
    card(s, (x0, 420, x0 + half - 8, 900), r=18)
    s.d.rounded_rectangle([k(x0), k(420), k(x0 + half - 8), k(540)], radius=k(18), fill=col)
    s.rect(x0, 510, x0 + half - 8, 540, col)
    s.text(x0 + 30, 474, head, f(BOLD, 36), WHITE_T)
    s.text(x0 + 30, 514, sub, f(MED, 22), WHITE_T)
    y = 600
    for p in pts:
        mark(s, x0 + 42, y - 10, True, r=14)
        y = s.para(x0 + 70, y, p, f(SEMI, 25), half - 110, 34, NAVY) + 38
horizon(s, 2)
navy_note(s, "Student tip", "Start with one aggregator sandbox. Learn the flow once.", "Anza na sandbox", seed=2)
finish(s)
s.save(2)

# ── 3 · the flow ─────────────────────────────────────────────────────────────────────────────────
s = page(3, "The flow · Mtiririko", "Jenga kwa Tanzania")
title2(s, "From “Lipa”", "to “Paid”.", y=220, size=88)
flow(s, [("Customer taps Lipa", "Enters phone number in your app"), ("Your server calls the provider", "Amount, phone, your order ID"),
         ("Phone shows a PIN prompt", "The USSD push on the customer's phone"), ("Customer enters PIN", "Money moves on the provider side"),
         ("Provider calls your callback", "Success or failure, with a reference"), ("You mark the order paid", "Then show the receipt")],
     400, h=80, gap=24, size=27)
horizon(s, 3)
navy_note(s, "Key idea", "Payment finishes on the provider's side. Your app waits for the callback.", "Subiri callback", seed=3)
finish(s)
s.save(3)

# ── 4 · callback code ────────────────────────────────────────────────────────────────────────────
s = page(4, "The callback · Code", "Jenga kwa Tanzania")
title2(s, "Trust the callback,", "not the button.", y=220, size=80)
y = code_window(s, 380, ['@app.post("/payments/callback")', "def callback():", "    data = verify(request)  # signature",
                         '    order = find(data["order_id"])', "    if order.paid:", "        return ok()  # already done",
                         '    if data["status"] == "SUCCESS":', '        order.mark_paid(data["ref"])', "    return ok()"],
                file="payments.py", lang="Python", size=23, lh=38)
s.para(M, y + 56, "Field names differ per provider. Read their docs for the exact payload and how to verify it.", f(REG, 24), W - 2 * M, 34, GREY)
horizon(s, 4)
navy_note(s, "Line 3", "Verify every callback. Anyone can send a fake “SUCCESS”.", "Thibitisha kila callback", seed=4)
finish(s)
s.save(4)

# ── 5 · golden rules ─────────────────────────────────────────────────────────────────────────────
s = page(5, "Golden rules · Kanuni", "Jenga kwa Tanzania")
title2(s, "Rules that keep", "money safe.", y=220, size=86)
tick_fill(s, [("Never trust the frontend", "The app can be faked. Only the provider's confirmation counts."),
              ("Verify callbacks", "Check the signature, or query the provider for the status."),
              ("Handle it once (idempotent)", "Callbacks can arrive twice. Don't deliver twice."),
              ("Save every reference", "Order ID, provider reference, time, amount."),
              ("Pending is normal", "Some payments take minutes. Show “inasubiri”, then update.")], 420, 1000, size=30, sub=25)
horizon(s, 5)
navy_note(s, "Remember", "A payment bug is a money bug. Test it twice.", "Pesa ni nyeti", seed=5)
finish(s)
s.save(5)

# ── 6 · sandbox ──────────────────────────────────────────────────────────────────────────────────
s = page(6, "Sandbox · Majaribio", "Jenga kwa Tanzania")
title2(s, "Test every", "outcome.", y=220, size=92)
table(s, M, 420, ["Test case", "Expected"], [["PIN correct", "Order paid, receipt"], ["Wrong PIN / cancel", "Order stays unpaid"],
                                              ["No response (timeout)", "Shows pending, retries"], ["Callback sent twice", "Delivered once"],
                                              ["Not enough balance", "Clear failure message"]],
      [470, W - 2 * M - 8 - 470], size=26, rh=76)
horizon(s, 6)
navy_note(s, "Portfolio", "A working sandbox demo is a strong project to show employers.", "Onyesha demo", seed=6)
finish(s)
s.save(6)

# ── 7 · going live ───────────────────────────────────────────────────────────────────────────────
s = page(7, "Going live · Kwenda hewani", "Jenga kwa Tanzania")
title2(s, "Live keys need", "a business.", y=220, size=88)
tick_fill(s, [("A registered business", "Providers onboard companies, with KYC documents."), ("An agreement and fees", "Usually a percentage per transaction. Ask for current rates."),
              ("Security review", "HTTPS, secret keys on the server only, never in the app."), ("A support plan", "Who answers when a customer says “nimelipa”?")],
          420, 990, size=31, sub=26)
horizon(s, 7)
navy_note(s, "For freelancers", "Use the client's business account. Never collect money in your own.", "Akaunti ya mteja", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What app would you", "add payments to?", [("Save", "for your next project"), ("Share", "with your team's backend dev"),
                                                     ("Comment", "your idea, I'll suggest the flow")])
stamp(s, 840, 860, "PAID", GREEN_OK, angle=-10, size=60)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
