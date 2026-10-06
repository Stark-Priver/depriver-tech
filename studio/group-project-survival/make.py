"""Carousel: group project survival guide (9 slides, 1080x1350, exported at 2x). Same editorial / print direction as
portfolio-in-a-weekend. The device is a class WhatsApp group chat ("Guys tumefika wapi?"), then the fixes: roles,
a task board, Git branches, check-ins, and what to do when someone disappears."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 9
POST_URL = "depriver.tech/blog/group-project-survival"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing


def group_header(s, y, title="Group 7 · Final Project", sub="5 members · 1 doing everything"):
    s.d.rounded_rectangle([k(M), k(y), k(W - M - 8), k(y + 90)], radius=k(18), fill=NAVY)
    s.d.ellipse([k(M + 20), k(y + 15), k(M + 80), k(y + 75)], fill=ORANGE)
    s.text(M + 50, y + 46, "G7", f(BOLD, 22), WHITE_T, anchor="mm")
    s.text(M + 100, y + 42, title, f(BOLD, 28), WHITE_T)
    s.text(M + 100, y + 74, sub, f(REG, 20), SOFT)


def msg(s, y, who, text, mine=False, w=640):
    x = W - M - 8 - w if mine else M
    return chat(s, x, y, w, text, who, mine=mine, size=24, lh=33) + 20


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For every student in a group")
s.text(M - 6, 250, "One person", f(BOLD, 104), NAVY)
s.text(M - 6, 360, "does everything?", f(BOLD, 88), NAVY)
s.text(M - 8, 480, "Not anymore.", f(BOLD, 104), ORANGE)
s.text(M, 570, "Kazi ya kikundi, si ya mtu mmoja", f(SIG, 54), NAVY)
swash(s, M + 8, M + 600, 596, ORANGE, 6)
group_header(s, 640)
y = msg(s, 750, "Baraka", "Guys tumefika wapi? Presentation ni kesho", w=640)
y = msg(s, y - 6, "You", "Nimetuma final_FINAL2.zip", mine=True, w=470)
horizon(s, 1)
cover_footer(s, "Swipe for the survival guide")
finish(s)
s.save(1)

# ── 2 · the problem ──────────────────────────────────────────────────────────────────────────────
s = page(2, "Sound familiar? · Unafahamu hii?")
title2(s, "The group", "project curse.", y=220, size=84)
group_header(s, 390)
y = 510
for who, t_, mine in [("Juma", "Mimi nitafanya presentation tu", False), ("Rehema", "Sorry guys network ilikuwa mbaya wiki nzima", False),
                      ("You", "Nimefanya backend, frontend, database na report...", True),
                      ("Lecturer", "Kila mtu aeleze sehemu yake kesho.", False)]:
    y = msg(s, y, who, t_, mine=mine, w=700)
horizon(s, 2)
navy_note(s, "At work", "Everyone ships, and Git shows who did what.", "Kazini hakuna kujificha", seed=2)
finish(s)
s.save(2)

# ── 3 · day 1 ────────────────────────────────────────────────────────────────────────────────────
s = page(3, "Day 1 · Siku ya kwanza")
title2(s, "Split the work", "on day one.", y=220, size=84)
roles = [("Lead", "Keeps the plan, runs check-ins"), ("Frontend", "Screens and user flow"), ("Backend", "API, logic, security"),
         ("Database", "Tables, sample data"), ("Docs & tests", "Report, README, testing")]
y = 440
for i, (a, b) in enumerate(roles):
    s.d.rounded_rectangle([k(M), k(y - 40), k(M + 230), k(y + 14)], radius=k(27), fill=ORANGE if i % 2 == 0 else NAVY)
    s.text(M + 115, y - 13, a, f(BOLD, 24), WHITE_T, anchor="mm")
    s.text(M + 260, y - 2, b, f(SEMI, 28), NAVY)
    hairline(s, M + 260, W - M, y + 28, RULE)
    y += 104
horizon(s, 3)
navy_note(s, "Write it down", "Put names next to tasks in the group chat. No confusion later.", "Kila mtu na kazi yake", seed=3)
finish(s)
s.save(3)

# ── 4 · task board ───────────────────────────────────────────────────────────────────────────────
s = page(4, "Task board · Ubao wa kazi")
title2(s, "Make the work", "visible.", y=220, size=88)
cols = [("To do", ["Login screen · Neema", "Report ch. 3 · Juma"]), ("Doing", ["Sales API · Baraka", "ER diagram · Rehema"]),
        ("Done", ["Repo setup · You", "Wireframes · Neema"])]
cw = (W - 2 * M - 30) / 3
for i, (h_, items) in enumerate(cols):
    x = M + i * (cw + 15)
    s.d.rounded_rectangle([k(x), k(400), k(x + cw), k(460)], radius=k(14), fill=[NAVY, ORANGE, GREEN_OK][i])
    s.text(x + cw / 2, 431, h_, f(BOLD, 26), WHITE_T, anchor="mm")
    for j, it in enumerate(items):
        y0 = 480 + j * 150
        card(s, (x, y0, x + cw - 8, y0 + 128), r=12)
        task, who = it.split(" · ")
        s.para(x + 18, y0 + 44, task, f(SEMI, 22), cw - 40, 30, NAVY)
        s.text(x + 18, y0 + 110, who, f(MED, 20), ORANGE)
s.text(M, 860, "Free tools: GitHub Projects, Trello, or a shared Google Sheet.", f(SEMI, fit(s, "Free tools: GitHub Projects, Trello, or a shared Google Sheet.", SEMI, 27, W - 2 * M)), NAVY)
horizon(s, 4)
navy_note(s, "Why", "Nobody can hide when the board shows every task.", "Uwazi ni nguvu", seed=4)
finish(s)
s.save(4)

# ── 5 · git branches ─────────────────────────────────────────────────────────────────────────────
s = page(5, "Git for teams · Git kwa timu")
title2(s, "No more", "final_FINAL2.zip.", y=220, size=84)
y0 = 470
s.d.line([k(M + 20), k(y0), k(W - M - 20), k(y0)], fill=NAVY, width=k(8))
s.text(M + 20, y0 - 30, "main", f(BOLD, 24), NAVY)
for i, (nm, col, x0, x1) in enumerate([("neema/login", ORANGE, 160, 520), ("baraka/sales-api", GREEN_OK, 360, 760), ("rehema/database", (37, 99, 235), 560, 900)]):
    yy = y0 + 90 + i * 90
    s.d.line([k(x0), k(y0), k(x0 + 40), k(yy), k(x1 - 40), k(yy), k(x1), k(y0)], fill=col, width=k(6), joint="curve")
    s.text(x0 + 50, yy - 16, nm, f(SEMI, 22), col)
    for cx in (x0, x1):
        s.d.ellipse([k(cx - 12), k(y0 - 12), k(cx + 12), k(y0 + 12)], fill=WHITE_T, outline=col, width=k(5))
y = 820
for a in ["Everyone works on their own branch", "Merge to main through a pull request", "Commit messages show who did what"]:
    mark(s, M + 18, y - 10, True)
    s.text(M + 56, y, a, f(SEMI, 28), NAVY)
    y += 60
horizon(s, 5)
navy_note(s, "Bonus", "Your Git history becomes proof of your contribution.", "Historia haidanganyi", seed=5)
finish(s)
s.save(5)

# ── 6 · check-ins ────────────────────────────────────────────────────────────────────────────────
s = page(6, "Weekly check-in · Kikao cha wiki")
title2(s, "15 minutes,", "every week.", y=220, size=88)
s.text(M, 420, "Each person answers three questions:", f(MED, 28), GREY)
qs = [("What did I finish?", "Show it, don't just say it."), ("What will I do next?", "One task, with a day."),
      ("What's blocking me?", "Ask for help early, not the night before.")]
numbered(s, qs, 510, gap=130, ts=36, bs=26)
horizon(s, 6)
navy_note(s, "Keep notes", "Write the decisions in the group chat after every meeting.", "Andika maamuzi", seed=6)
finish(s)
s.save(6)

# ── 7 · someone disappears ───────────────────────────────────────────────────────────────────────
s = page(7, "Someone disappeared? · Amepotea?")
title2(s, "When someone", "doesn't contribute.", y=220, size=80)
steps = [("Talk early, in private", "Maybe they're stuck or struggling. Ask kindly."), ("Give a clear task and a date", "Small, specific, written in the chat."),
         ("Keep records", "Task board, Git history, chat decisions."), ("Then tell the lecturer", "Calmly, with the records, not gossip."),
         ("Never cover silently", "Doing their part hides the problem, and you burn out.")]
numbered(s, steps, 430, gap=112)
horizon(s, 7)
navy_note(s, "Remember", "Being fair is not being harsh. Records protect everyone.", "Haki kwa wote", seed=7)
finish(s)
s.save(7)

# ── 8 · presentation day ─────────────────────────────────────────────────────────────────────────
s = page(8, "Presentation day · Siku ya kuwasilisha")
title2(s, "Everyone", "speaks.", y=230, size=96)
pres = [("Each person presents their part", "You built it, you explain it."), ("Rehearse together once", "Time it. Fix the hand-overs."),
        ("Demo on real data", "And have screenshots ready if the network fails."), ("Know the whole project", "Questions can go to anyone.")]
y = 450
for a, b in pres:
    mark(s, M + 18, y - 10, True)
    s.text(M + 56, y, a, f(BOLD, 31), NAVY)
    s.text(M + 56, y + 40, b, f(REG, 24), GREY)
    y += 128
horizon(s, 8)
navy_note(s, "Plan B", "Network down? Run it locally. Laptop dead? Screenshots.", "Daima kuwa na mpango B", seed=8)
finish(s)
s.save(8)

# ── 9 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Who's the one", "doing everything?", [("Tag", "your group members (kindly)"), ("Share", "in your project WhatsApp group"),
                                                ("Comment", "your worst group project story")])
chat(s, 620, 720, 380, "Tumefanya wote. Asanteni timu!", "Group 7", mine=False, size=24, lh=33)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
