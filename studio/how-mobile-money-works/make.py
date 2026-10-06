"""Carousel: how a mobile money transfer works, Inavyofanya kazi #1 (8 slides, 1080x1350, exported at 2x). The device is
a five-stop journey track at the top of each slide, following TZS 10,000 from your phone to Juma's. General, not tied to
one operator."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/how-mobile-money-works"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs

STOPS = 5


def stop_page(n, stop, label, t1, t2):
    s = page(n, f"Stop {stop} of {STOPS} · {label}", "Inavyofanya kazi")
    track(s, stop, STOPS, y=168)
    title2(s, t1, t2, y=300, size=80)
    return s


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "How it works · Inavyofanya kazi #01")
s.text(M - 6, 250, "Where does", f(BOLD, 92), NAVY)
s.text(M - 6, 348, "your money go?", f(BOLD, 92), ORANGE)
s.text(M, 440, "Safari ya shilingi elfu kumi", f(SIG, 56), NAVY)
swash(s, M + 8, M + 560, 466, ORANGE, 6)
s.para(M, 550, "You send TZS 10,000 to Juma. Seconds later he has it. Here is everything that happens in between.", f(REG, 28), 470, 42, GREY)
scr = smartphone(s, 640, 520, 330, 520)
sms(s, scr[0] + 16, scr[1] + 30, scr[2] - scr[0] - 32, "Umetuma TZS 10,000 kwa JUMA. Salio jipya TZS 24,500. Kumb: 8KX2…", sender="Mobile money", size=20, lh=28)
sms(s, scr[0] + 16, scr[1] + 210, scr[2] - scr[0] - 32, "Asante kaka, nimepokea!", sender="Juma", size=20, lh=28)
horizon(s, 1)
cover_footer(s, "Swipe, follow the money")
finish(s)
s.save(1)

# ── 2 · stop 1: you ──────────────────────────────────────────────────────────────────────────────
s = stop_page(2, 1, "You", "You start the", "transfer.")
tick_fill(s, [("You dial the USSD code or open the app", "Choose send money, enter Juma's number and the amount."),
              ("You enter your PIN", "This proves it's really you. Staff will never ask for it."),
              ("Your phone sends the request", "A short message with: from, to, amount, PIN check.")], 520, 980, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Safety", "Your PIN is the key to the wallet. Never share it, not even with an agent.", "PIN ni siri yako", seed=2)
finish(s)
s.save(2)

# ── 3 · stop 2: the network ──────────────────────────────────────────────────────────────────────
s = stop_page(3, 2, "The network", "Through the", "mobile network.")
flow(s, [("Your phone", "USSD session or app data"), ("Nearest tower", "Radio signal to the operator"),
         ("Operator's core network", "Routes it to the money platform"), ("Mobile money platform", "The system that holds the wallets")],
     520, h=96, gap=30, size=29)
horizon(s, 3)
navy_note(s, "Why USSD", "It works without internet, so it reaches almost every phone.", "Hata bila data", seed=3)
finish(s)
s.save(3)

# ── 4 · stop 3: the checks ───────────────────────────────────────────────────────────────────────
s = stop_page(4, 3, "The checks", "Checked in", "milliseconds.")
tick_fill(s, [("Is the PIN correct?", "Wrong too many times and the wallet locks."), ("Is there enough balance?", "Amount plus the fee."),
              ("Within the limits?", "Daily and per-transaction limits set by rules."), ("Does it look like fraud?", "Unusual patterns can be held for review.")],
          520, 990, size=31, sub=26)
horizon(s, 4)
navy_note(s, "If one fails", "Nothing moves, and you get a failure SMS.", "Hakuna kinachopotea", seed=4)
finish(s)
s.save(4)

# ── 5 · stop 4: the ledger ───────────────────────────────────────────────────────────────────────
s = stop_page(5, 4, "The ledger", "The money moves", "in a ledger.")
y = table(s, M, 510, ["Wallet", "Before", "After"], [["You", "35,000", "24,500"], ["Juma", "2,000", "12,000"], ["Fee", "", "+500"]],
          [340, 270, W - 2 * M - 8 - 610], size=27, rh=70)
s.para(M, y + 70, "No cash travels. One database transaction subtracts from you and adds to Juma at the same moment.", f(MED, 29), W - 2 * M, 42, NAVY)
s.text(M, y + 190, "Example numbers only. Fees vary by operator and amount.", f(REG, 22), GREY)
horizon(s, 5)
navy_note(s, "Backed by cash", "The real money behind e-money sits in trust accounts at banks.", "Pesa halisi iko benki", seed=5)
finish(s)
s.save(5)

# ── 6 · stop 5: the SMS ──────────────────────────────────────────────────────────────────────────
s = stop_page(6, 5, "The confirmation", "Two SMS,", "one reference.")
sms(s, M, 520, 600, "Umetuma TZS 10,000 kwa JUMA. Kumb: 8KX2… Ada TZS 500.", sender="To you", size=26, lh=36)
sms(s, W - M - 600, 700, 600, "Umepokea TZS 10,000 kutoka kwa WEWE. Kumb: 8KX2…", sender="To Juma", size=26, lh=36, mine=True)
s.para(M, 900, "Different networks? The operators record it, then settle with each other later.", f(MED, 28), W - 2 * M, 40, NAVY)
horizon(s, 6)
navy_note(s, "Keep it", "The reference number is your proof if anything goes wrong.", "Hifadhi kumbukumbu", seed=6)
finish(s)
s.save(6)

# ── 7 · lessons for developers ───────────────────────────────────────────────────────────────────
s = page(7, "For developers · Kwa wasanidi", "Inavyofanya kazi")
title2(s, "What money systems", "teach developers.", y=230, size=78)
tick_fill(s, [("All or nothing (atomic)", "Debit and credit happen together, or neither happens."),
              ("Never twice (idempotent)", "A repeated request must not send the money again."),
              ("Log everything", "Every step has an ID you can trace later."),
              ("Plan for failure", "Timeouts, reversals and “pending” are normal states.")], 430, 990, size=31, sub=26)
horizon(s, 7)
navy_note(s, "Learn it", "Database transactions are the place to start.", "Anza na transactions", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What should I", "explain next?", [("Save", "to understand your next transfer"), ("Share", "with a friend who loves fintech"),
                                             ("Comment", "the tech you want explained")])
stamp(s, 840, 860, "IMEFIKA", GREEN_OK, angle=-10, size=48)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
