"""Carousel: SMS still wins, Jenga kwa Tanzania #5 (8 slides, 1080x1350, exported at 2x). The device is a phone inbox of
real-life SMS (clinic reminder, school fees, crop prices) plus a send-SMS code window. Providers only as examples."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/sms-still-wins"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def series_tag(s, x, y, text="Jenga kwa Tanzania #05", size=20):
    w_ = s.width(text, f(BOLD, size)) + 40
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + size * 2.1)], radius=k(size), fill=NAVY)
    s.text(x + w_ / 2, y + size * 1.08, text, f(BOLD, size), WHITE_T, anchor="mm")


INBOX = [("KLINIKI", "Kumbusho: miadi yako ni kesho saa 3 asubuhi. Jibu 1 kuthibitisha."),
         ("SHULE", "Ada ya muhula wa 2 ni TZS 450,000. Salio: TZS 150,000."),
         ("SOKO", "Bei leo Mbeya: Mahindi TZS 900/kg, Maharage TZS 2,800/kg.")]

# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Build for Tanzania · Jenga kwa Tanzania")
series_tag(s, M, 165)
s.text(M - 6, 320, "SMS still", f(BOLD, 110), NAVY)
s.text(M - 6, 430, "wins.", f(BOLD, 110), ORANGE)
s.text(M, 520, "Ujumbe mfupi, kazi kubwa", f(SIG, 56), NAVY)
swash(s, M + 8, M + 500, 546, ORANGE, 6)
s.para(M, 630, "Every phone gets it. No data, no app, no smartphone. That's why clinics, schools and banks still use it.", f(REG, 27), 440, 40, GREY)
x0, y0, x1, y1 = smartphone(s, 600, 330, 400, 690, fill=(244, 245, 248))
y = y0 + 24
for who, msg in INBOX:
    y = sms(s, x0 + 16, y, x1 - x0 - 32, msg, sender=who, size=19, lh=27) + 18
horizon(s, 1)
cover_footer(s, "Swipe, send your first SMS")
finish(s)
s.save(1)

# ── 2 · why ──────────────────────────────────────────────────────────────────────────────────────
s = page(2, "Why SMS · Kwa nini", "Jenga kwa Tanzania")
title2(s, "Reaches people", "apps can't.", y=220, size=88)
tick_fill(s, [("Works on every phone", "Kitochi, smartphone, old or new."), ("No data, no install", "Arrives even when the bundle is finished."),
              ("Read quickly", "People open SMS from known senders fast."), ("Trusted", "Official messages from a registered sender name.")],
          420, 990, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Best together", "Use the app for rich features, SMS for must-see messages.", "App + SMS", seed=2)
finish(s)
s.save(2)

# ── 3 · use cases ────────────────────────────────────────────────────────────────────────────────
s = page(3, "Use cases · Matumizi", "Jenga kwa Tanzania")
title2(s, "What people", "build with SMS.", y=220, size=86)
uses = [("Reminders", "Clinic visits, loan dates, meetings"), ("Fees & bills", "Balance and due dates"), ("Codes (OTP)", "Login and payment checks"),
        ("Order updates", "“Mzigo wako umefika”"), ("Alerts", "Prices, weather, outbreaks"), ("Surveys", "Reply 1, 2 or 3")]
cw = (W - 2 * M - 24) / 2
for i, (a, b) in enumerate(uses):
    xx, yy = M + (i % 2) * (cw + 24), 410 + (i // 2) * 190
    card(s, (xx, yy, xx + cw - 8, yy + 160), r=16)
    s.text(xx + 28, yy + 62, f"{i + 1:02d}", f(BOLD, 24), ORANGE)
    s.text(xx + 80, yy + 62, a, f(BOLD, 29), NAVY)
    s.para(xx + 28, yy + 112, b, f(REG, 23), cw - 60, 31, GREY)
horizon(s, 3)
navy_note(s, "Final year?", "An SMS reminder system is a simple, useful FYP.", "Tatua tatizo halisi", seed=3)
finish(s)
s.save(3)

# ── 4 · how ──────────────────────────────────────────────────────────────────────────────────────
s = page(4, "How it works · Inavyofanya kazi", "Jenga kwa Tanzania")
title2(s, "From your code", "to their phone.", y=220, size=86)
flow(s, [("Your app decides to send", "e.g. the night before an appointment"), ("Calls an SMS gateway API", "e.g. Africa's Talking, Beem, NextSMS"),
         ("Gateway passes it to the networks", "Vodacom, Airtel, Yas, Halotel…"), ("The phone receives it", "From your sender name, e.g. KLINIKI"),
         ("Delivery report comes back", "Delivered, failed or pending")], 410, h=88, gap=28, size=28)
horizon(s, 4)
navy_note(s, "Simple", "For you it's one HTTP request per message.", "Ombi moja tu", seed=4)
finish(s)
s.save(4)

# ── 5 · code ─────────────────────────────────────────────────────────────────────────────────────
s = page(5, "The code · Code", "Jenga kwa Tanzania")
title2(s, "Send one SMS", "in a few lines.", y=220, size=86)
y = code_window(s, 380, ["import requests", "", "def send_sms(phone, text):", "    return requests.post(GATEWAY_URL,",
                         "        headers={\"apiKey\": API_KEY},", "        data={\"to\": phone,", "              \"message\": text,",
                         "              \"from\": \"KLINIKI\"})"], file="sms.py", lang="Python", size=24, lh=40)
s.para(M, y + 56, "Generic example. Each gateway has its own URL, field names and SDK: copy them from its docs.", f(REG, 24), W - 2 * M, 34, GREY)
horizon(s, 5)
navy_note(s, "Secret", "Keep API_KEY in an environment variable, never in GitHub.", "Funguo ni siri", seed=5)
finish(s)
s.save(5)

# ── 6 · rules ────────────────────────────────────────────────────────────────────────────────────
s = page(6, "Rules · Kanuni", "Jenga kwa Tanzania")
title2(s, "Send SMS", "responsibly.", y=220, size=88)
tick_fill(s, [("Register your sender name", "Sender IDs need approval. It takes time, start early."),
              ("Only send to people who agreed", "Opt-in, and an easy way to stop."), ("Mind the length", "160 characters per part. Emojis and some symbols cut it to 70."),
              ("Right time of day", "No marketing SMS at 11 p.m.")], 420, 990, size=31, sub=26)
horizon(s, 6)
navy_note(s, "Cost", "You pay per SMS part. Short messages save money.", "Fupi ni nafuu", seed=6)
finish(s)
s.save(6)

# ── 7 · two-way ──────────────────────────────────────────────────────────────────────────────────
s = page(7, "Two-way SMS · Jibu", "Jenga kwa Tanzania")
title2(s, "Let people", "reply.", y=220, size=92)
sms(s, M, 420, 620, "Kumbusho: miadi yako ni kesho saa 3. Jibu 1 kuthibitisha, 2 kubadilisha.", sender="KLINIKI", size=26, lh=36)
sms(s, W - M - 8 - 140, 620, 140, "1", sender="You", size=30, lh=36, mine=True)
sms(s, M, 760, 620, "Asante! Miadi imethibitishwa. Karibu kesho.", sender="KLINIKI", size=26, lh=36)
s.para(M, 940, "Replies arrive at your server through the gateway, like a webhook.", f(MED, 27), W - 2 * M, 40, NAVY)
horizon(s, 7)
navy_note(s, "Value", "Fewer missed appointments is something a clinic will pay for.", "Thamani halisi", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What SMS service", "would you build?", [("Comment", "your SMS idea"), ("Save", "for your project"),
                                                   ("Share", "with your FYP group")])
stamp(s, 840, 860, "IMEFIKA", GREEN_OK, angle=-10, size=50)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
