"""Carousel: offline-first apps, Jenga kwa Tanzania #4 (8 slides, 1080x1350, exported at 2x). The device is a phone with
an offline banner and a sync queue of pending orders that go out when the network returns."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/offline-first-apps"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def series_tag(s, x, y, text="Jenga kwa Tanzania #04", size=20):
    w_ = s.width(text, f(BOLD, size)) + 40
    s.d.rounded_rectangle([k(x), k(y), k(x + w_), k(y + size * 2.1)], radius=k(size), fill=NAVY)
    s.text(x + w_ / 2, y + size * 1.08, text, f(BOLD, size), WHITE_T, anchor="mm")


def offline_phone(s, x, y, w=330, h=580, online=False):
    x0, y0, x1, y1 = smartphone(s, x, y, w, h, fill=(244, 245, 248))
    col = GREEN_OK if online else (176, 62, 30)
    s.rect(x0, y0, x1, y0 + 56, col)
    s.text(x0 + 18, y0 + 37, "Online · imesawazishwa" if online else "Offline · 3 zinasubiri", f(BOLD, 19), WHITE_T)
    rows = [("Oda #104", "12,000"), ("Oda #105", "4,500"), ("Oda #106", "30,000"), ("Oda #103", "8,000")]
    for i, (item, amt) in enumerate(rows[:max(1, int((y1 - y0 - 80) // 96))]):
        yy = y0 + 80 + i * 96
        pending = i < 3 and not online
        s.d.rounded_rectangle([k(x0 + 14), k(yy), k(x1 - 14), k(yy + 80)], radius=k(10), fill=(255, 255, 255), outline=(214, 219, 230), width=k(2))
        s.text(x0 + 32, yy + 36, item, f(BOLD, 20), NAVY)
        s.text(x0 + 32, yy + 64, "TZS " + amt, f(REG, 18), GREY)
        tag = "Inasubiri" if pending else "Imetumwa"
        tw = s.width(tag, f(SEMI, 15)) + 20
        s.d.rounded_rectangle([k(x1 - 30 - tw), k(yy + 24), k(x1 - 30), k(yy + 54)], radius=k(15), fill=(240, 180, 60) if pending else GREEN_OK)
        s.text(x1 - 30 - tw / 2, yy + 39, tag, f(SEMI, 15), WHITE_T, anchor="mm")


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Build for Tanzania · Jenga kwa Tanzania")
series_tag(s, M, 165)
s.text(M - 6, 320, "No network?", f(BOLD, 92), NAVY)
s.text(M - 6, 420, "Keep working.", f(BOLD, 92), ORANGE)
s.text(M, 510, "Mtandao ukikata, kazi iendelee", f(SIG, 50), NAVY)
swash(s, M + 8, M + 540, 534, ORANGE, 6)
s.para(M, 620, "Offline-first apps save work on the phone and sync when the network comes back. Perfect for shops, field agents and upcountry users.",
       f(REG, 26), 470, 38, GREY)
offline_phone(s, 690, 545, 290, 480)
horizon(s, 1)
cover_footer(s, "Swipe, build it to last")
finish(s)
s.save(1)

# ── 2 · why ──────────────────────────────────────────────────────────────────────────────────────
s = page(2, "Why offline · Kwa nini", "Jenga kwa Tanzania")
title2(s, "The network", "will drop.", y=220, size=90)
tick_fill(s, [("Field agents and drivers", "Collecting data in villages, on roads, in markets."),
              ("Shops and pharmacies", "A sale can't wait for 4G to come back."),
              ("Bundles run out", "Users shouldn't lose their work when data ends."),
              ("Power and network cuts", "Normal days, not rare accidents.")], 420, 990, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Rule", "Treat no-network as a normal state, not an error.", "Ni hali ya kawaida", seed=2)
finish(s)
s.save(2)

# ── 3 · the idea ─────────────────────────────────────────────────────────────────────────────────
s = page(3, "The idea · Wazo kuu", "Jenga kwa Tanzania")
title2(s, "Save locally.", "Sync later.", y=220, size=90)
flow(s, [("User saves an order", "Written to the phone's own database first"), ("It shows as “Inasubiri”", "The user can keep working"),
         ("Network comes back", "The app notices automatically"), ("Queue is sent to the server", "Oldest first, one by one"),
         ("Marked “Imetumwa”", "Server confirms each item")], 410, h=88, gap=28, size=28)
horizon(s, 3)
navy_note(s, "Key idea", "The phone is the first home of the data. The server is the second.", "Simu kwanza", seed=3)
finish(s)
s.save(3)

# ── 4 · the queue ────────────────────────────────────────────────────────────────────────────────
s = page(4, "The sync queue · Foleni", "Jenga kwa Tanzania")
title2(s, "Every change waits", "in a queue.", y=220, size=82)
table(s, M, 410, ["ID", "Action", "Status"], [["a7f3…", "create order #104", "Inasubiri"], ["b21c…", "create order #105", "Inasubiri"],
                                              ["c90e…", "update stock", "Inasubiri"], ["9d1a…", "create order #103", "Imetumwa"]],
      [200, 450, W - 2 * M - 8 - 650], size=26, rh=78, hl_rows=(0, 1, 2))
s.para(M, 860, "IDs are created on the phone (UUIDs), so nothing clashes when items reach the server.", f(MED, 27), W - 2 * M, 40, NAVY)
horizon(s, 4)
navy_note(s, "Safe retries", "The server must accept the same item twice without duplicating it.", "Bila kurudia", seed=4)
finish(s)
s.save(4)

# ── 5 · conflicts ────────────────────────────────────────────────────────────────────────────────
s = page(5, "Conflicts · Migongano", "Jenga kwa Tanzania")
title2(s, "Two phones edit", "the same thing?", y=220, size=82)
tick_fill(s, [("Last write wins", "Simple. Fine for notes and settings."), ("Merge the changes", "Stock: add both sales, don't overwrite the count."),
              ("Ask the user", "Show both versions when it really matters."), ("Record events, not totals", "“Sold 2” is easier to merge than “stock = 18”.")],
          420, 990, size=31, sub=26)
horizon(s, 5)
navy_note(s, "Design first", "Decide the rule for each type of data before you code.", "Panga kanuni mapema", seed=5)
finish(s)
s.save(5)

# ── 6 · tools ────────────────────────────────────────────────────────────────────────────────────
s = page(6, "Tools · Zana", "Jenga kwa Tanzania")
title2(s, "Tools that", "do the heavy lifting.", y=220, size=82)
table(s, M, 410, ["Platform", "Local storage + sync"], [["Web (PWA)", "Service Worker + IndexedDB"], ["Android", "Room + WorkManager"],
                                                       ["Flutter", "Drift, sqflite or Hive"], ["Any app", "Firestore offline persistence"]],
      [300, W - 2 * M - 8 - 300], size=27, rh=86)
horizon(s, 6)
navy_note(s, "Start small", "Make one screen work offline first, then grow.", "Skrini moja kwanza", seed=6)
finish(s)
s.save(6)

# ── 7 · UX ───────────────────────────────────────────────────────────────────────────────────────
s = page(7, "User experience · Mtumiaji", "Jenga kwa Tanzania")
title2(s, "Tell the user", "what's happening.", y=220, size=82)
tick_fill(s, [("Clear offline banner", "“Offline · 3 zinasubiri”, not a silent failure."), ("Never lose data", "Saved means saved, even if the app closes."),
              ("Sync on its own", "No “press here to upload” buttons to forget."), ("Show when it's done", "A green “Imetumwa” builds trust.")],
          420, 990, size=31, sub=26)
horizon(s, 7)
navy_note(s, "Trust", "Users trust apps that never lose their work.", "Uaminifu", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which app should", "work offline?", [("Comment", "an app that fails you offline"), ("Save", "for your next project"),
                                                ("Share", "with your mobile dev friend")])
stamp(s, 840, 860, "IMETUMWA", GREEN_OK, angle=-10, size=48)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
