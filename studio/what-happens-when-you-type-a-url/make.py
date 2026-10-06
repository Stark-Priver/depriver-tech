"""Carousel: what happens when you type a URL and press Enter, Inavyofanya kazi #2 (8 slides, 1080x1350, exported at 2x).
The device is a browser address bar plus a five-stop journey track: DNS, connect, request, response, render."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/what-happens-when-you-type-a-url"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs

STOPS = 5


def address_bar(s, y, text="depriver.tech", x0=M, x1=None, size=34):
    x1 = x1 or W - M - 8
    h = size * 2.4
    s.rect(x0 + 8, y + 10, x1 + 8, y + h + 10, INK_SHADOW, r=h / 2)
    s.d.rounded_rectangle([k(x0), k(y), k(x1), k(y + h)], radius=k(h / 2), fill=(255, 255, 255), outline=NAVY, width=k(3))
    lx, ly = x0 + h * 0.55, y + h / 2
    s.d.rounded_rectangle([k(lx - 11), k(ly - 4), k(lx + 11), k(ly + 14)], radius=k(3), fill=GREEN_OK)
    s.d.arc([k(lx - 8), k(ly - 18), k(lx + 8), k(ly + 4)], 180, 360, fill=GREEN_OK, width=k(4))
    s.text(lx + 30, ly + size * 0.36, text, f(SEMI, size), NAVY)
    cx = lx + 30 + s.width(text, f(SEMI, size)) + 6
    s.rect(cx, ly - size * 0.55, cx + 3, ly + size * 0.55, ORANGE)
    s.d.rounded_rectangle([k(x1 - 150), k(y + 12), k(x1 - 14), k(y + h - 12)], radius=k((h - 24) / 2), fill=ORANGE)
    s.text(x1 - 82, ly, "Enter", f(BOLD, size * 0.62), WHITE_T, anchor="mm")
    return y + h


def stop_page(n, stop, label, t1, t2):
    s = page(n, f"Stop {stop} of {STOPS} · {label}", "Inavyofanya kazi")
    track(s, stop, STOPS, y=168)
    title2(s, t1, t2, y=300, size=80)
    return s


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "How it works · Inavyofanya kazi #02")
s.text(M - 6, 250, "You press", f(BOLD, 100), NAVY)
s.text(M - 6, 356, "Enter.", f(BOLD, 100), ORANGE)
s.text(M, 448, "Sekunde moja, safari ndefu", f(SIG, 58), NAVY)
swash(s, M + 8, M + 520, 474, ORANGE, 6)
address_bar(s, 560)
s.para(M, 760, "In under a second your browser finds a server, makes a safe connection, asks for the page and draws it. Five stops.",
       f(REG, 28), W - 2 * M, 42, GREY)
chip_row(s, ["DNS", "Connect", "Request", "Response", "Render"], M, 910, size=22)
horizon(s, 1)
cover_footer(s, "Swipe, follow the request")
finish(s)
s.save(1)

# ── 2 · DNS ──────────────────────────────────────────────────────────────────────────────────────
s = stop_page(2, 1, "DNS", "Find the", "address.")
s.para(M, 510, "Computers use numbers (IP addresses), not names. DNS is the internet's phonebook.", f(MED, 31), W - 2 * M, 44, NAVY)
flow(s, [("Browser asks: depriver.tech?", "First checks its own memory (cache)"), ("DNS resolver looks it up", "Usually from your network provider"),
         ("Answer: an IP address", "e.g. 104.21.x.x, the server's number")], 650, h=92, gap=28, size=28)
horizon(s, 2)
navy_note(s, "Like", "Your phonebook: you tap “Juma”, the phone dials the number.", "Jina kwenda namba", seed=2)
finish(s)
s.save(2)

# ── 3 · connect ──────────────────────────────────────────────────────────────────────────────────
s = stop_page(3, 2, "Connect", "Shake hands,", "lock the line.")
tick_fill(s, [("Open a connection to the server", "Your device and the server agree to talk (TCP)."),
              ("Secure it with HTTPS (TLS)", "They agree on secret keys. Nobody in between can read it."),
              ("Check the certificate", "Proof the server really is depriver.tech, not an impostor.")], 520, 960, size=31, sub=27)
horizon(s, 3)
navy_note(s, "The padlock", "That small lock icon means this step worked.", "Kufuli ni usalama", seed=3)
finish(s)
s.save(3)

# ── 4 · request ──────────────────────────────────────────────────────────────────────────────────
s = stop_page(4, 3, "Request", "Ask for", "the page.")
terminal(s, 500, ["# what your browser sends (simplified)", "GET /blog HTTP/1.1", "Host: depriver.tech", "Accept: text/html",
                  "User-Agent: Chrome on Android"], title="HTTP request", size=26, lh=46)
s.para(M, 880, "GET means “give me”. Forms use POST: “here's data”.", f(MED, 29), W - 2 * M, 42, NAVY)
horizon(s, 4)
navy_note(s, "Every click", "Every page, image and button press is a request like this.", "Kila bonyezo ni ombi", seed=4)
finish(s)
s.save(4)

# ── 5 · response ─────────────────────────────────────────────────────────────────────────────────
s = stop_page(5, 4, "Response", "The server", "answers.")
table(s, M, 500, ["Code", "Means"], [["200 OK", "Here's the page"], ["301", "It moved, go here instead"], ["404", "Not found"],
                                     ["500", "The server crashed"]], [260, W - 2 * M - 8 - 260], size=28, rh=80)
s.text(M, 960, "Then it sends the HTML: the page's content and structure.", f(MED, 27), NAVY)
horizon(s, 5)
navy_note(s, "Debug tip", "Status codes tell you whose problem it is: yours or the server's.", "Soma namba ya jibu", seed=5)
finish(s)
s.save(5)

# ── 6 · render ───────────────────────────────────────────────────────────────────────────────────
s = stop_page(6, 5, "Render", "The browser", "draws it.")
flow(s, [("Read the HTML", "Builds the page structure"), ("Fetch CSS, JS and images", "More requests, often dozens"),
         ("Apply CSS", "Colours, layout, fonts"), ("Run JavaScript", "Buttons, menus, live data")], 500, h=92, gap=28, size=28)
horizon(s, 6)
navy_note(s, "Why slow?", "Huge images and too much JavaScript, usually. Not your bundle.", "Picha kubwa ni tatizo", seed=6)
finish(s)
s.save(6)

# ── 7 · for developers ───────────────────────────────────────────────────────────────────────────
s = page(7, "For developers · Kwa wasanidi", "Inavyofanya kazi")
title2(s, "See it yourself", "in DevTools.", y=230, size=82)
tick_fill(s, [("Open DevTools: F12 or Ctrl+Shift+I", "Then the Network tab, and reload the page."),
              ("Every row is one request", "Status, size and time for each file."),
              ("Find the slowest file", "Sort by time or size. That's what to fix first."),
              ("Try “Slow 3G”", "Feel what your users on bad networks feel.")], 440, 990, size=31, sub=26)
horizon(s, 7)
navy_note(s, "Interview", "“What happens when you type a URL?” is a classic question.", "Sasa unajua jibu", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which stop", "surprised you?", [("Comment", "1 to 5"), ("Save", "for your next interview"), ("Share", "with a classmate")])
address_bar(s, 870, "Imefunguka!", x0=560, size=26)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
