"""Carousel: which tech path fits you? The Njia za Tech finale quiz (8 slides, 1080x1350, exported at 2x). The device is
a yes/no flowchart: each slide is one question card with two arrows to a role or to the next slide; slide 7 maps all
nine roles back to their Njia za Tech episodes."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/which-tech-path"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def question(s, y, q, h=None):
    h = h or 90 + wrap_lines(s, q, f(BOLD, 40), W - 2 * M - 80) * 52
    s.rect(M + 10, y + 12, W - M + 2, y + h + 12, INK_SHADOW, r=24)
    s.d.rounded_rectangle([k(M), k(y), k(W - M - 8), k(y + h)], radius=k(24), fill=NAVY)
    s.para(M + 40, y + 74, q, f(BOLD, 40), W - 2 * M - 80, 52, WHITE_T)
    return y + h


def branch(s, y, yes, no):
    """Two arrows down from the question to YES (left) and NO (right) result boxes. yes/no: (title, sub, is_role)."""
    cw = (W - 2 * M - 40) / 2
    for j, (lab, (title, sub, role, desc)) in enumerate([("Ndiyo · Yes", yes), ("Hapana · No", no)]):
        x0 = M + j * (cw + 40)
        cx = x0 + cw / 2
        s.d.line([k(cx), k(y + 6), k(cx), k(y + 90)], fill=ORANGE, width=k(5))
        s.d.polygon([(k(cx - 14), k(y + 80)), (k(cx + 14), k(y + 80)), (k(cx), k(y + 100))], fill=ORANGE)
        s.d.rounded_rectangle([k(cx - 100), k(y + 24), k(cx + 100), k(y + 66)], radius=k(21), fill=(255, 255, 255), outline=ORANGE, width=k(3))
        s.text(cx, y + 46, lab, f(BOLD, 21), ORANGE, anchor="mm")
        by = y + 120
        bh = 380
        if role:
            s.rect(x0 + 8, by + 10, x0 + cw + 8, by + bh + 10, INK_SHADOW, r=20)
            s.d.rounded_rectangle([k(x0), k(by), k(x0 + cw), k(by + bh)], radius=k(20), fill=ORANGE)
            smallcaps(s, x0 + 30, by + 50, "Your path", 14, WHITE_T)
            yy = s.para(x0 + 30, by + 104, title, f(BOLD, 34), cw - 60, 42, WHITE_T)
            s.para(x0 + 30, yy + 14, desc, f(MED, 23), cw - 60, 32, WHITE_T)
            s.text(x0 + 30, by + bh - 30, sub, f(SEMI, 21), WHITE_T)
        else:
            card(s, (x0, by, x0 + cw, by + bh), r=20)
            smallcaps(s, x0 + 30, by + 50, "Keep going", 14, ORANGE)
            yy = s.para(x0 + 30, by + 104, title, f(BOLD, 32), cw - 60, 40, NAVY)
            s.para(x0 + 30, yy + 14, desc, f(MED, 23), cw - 60, 32, GREY)
            s.text(x0 + 30, by + bh - 30, sub, f(SEMI, 21), ORANGE)


def q_slide(n, label, q, yes, no, note):
    s = page(n, label, "Which tech path?")
    y = question(s, 200, q)
    branch(s, y + 20, yes, no)
    horizon(s, n)
    navy_note(s, *note, seed=n)
    finish(s)
    s.save(n)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Njia za Tech · The finale")
s.text(M - 6, 260, "Which tech", f(BOLD, 110), NAVY)
s.text(M - 6, 370, "path fits you?", f(BOLD, 100), ORANGE)
s.text(M, 460, "Njia yako ni ipi?", f(SIG, 60), NAVY)
swash(s, M + 8, M + 400, 486, ORANGE, 6)
s.para(M, 570, "Five yes/no questions. Nine possible paths. Answer honestly, not what sounds cool.", f(REG, 28), W - 2 * M, 42, GREY)
nodes = [(W / 2, 700, "Start"), (W / 2 - 240, 820, "Yes"), (W / 2 + 240, 820, "No")]
s.d.line([k(W / 2), k(722), k(W / 2 - 240), k(798)], fill=NAVY, width=k(4))
s.d.line([k(W / 2), k(722), k(W / 2 + 240), k(798)], fill=NAVY, width=k(4))
for xx, (lab, col) in zip([W / 2 - 380, W / 2 - 120, W / 2 + 120, W / 2 + 380], [("UI/UX", ORANGE), ("Frontend", NAVY), ("Data", NAVY), ("Backend", ORANGE)]):
    px = W / 2 - 240 if xx < W / 2 else W / 2 + 240
    s.d.line([k(px), k(842), k(xx), k(910)], fill=NAVY, width=k(3))
    s.d.rounded_rectangle([k(xx - 100), k(910), k(xx + 100), k(966)], radius=k(28), fill=col)
    s.text(xx, 938, lab, f(BOLD, 22), WHITE_T, anchor="mm")
for xx, yy, lab in nodes:
    w_ = s.width(lab, f(BOLD, 24)) + 48
    s.d.rounded_rectangle([k(xx - w_ / 2), k(yy - 24), k(xx + w_ / 2), k(yy + 24)], radius=k(24), fill=(255, 255, 255), outline=NAVY, width=k(3))
    s.text(xx, yy, lab, f(BOLD, 24), NAVY, anchor="mm")
horizon(s, 1)
cover_footer(s, "Swipe, start the quiz")
finish(s)
s.save(1)

q_slide(2, "Question 1 · Swali la 1", "Do you care more about how things LOOK and FEEL than how they work inside?",
        ("Go to slide 3", "The creative side", False, "Screens, colours, how people feel using a product."), ("Go to slide 4", "The logic side", False, "Data, systems, rules and how things connect."),
        ("Honest", "Both answers are good. This just picks the direction.", "Hakuna jibu baya"))
q_slide(3, "Question 2 · Swali la 2", "Would you rather sketch and test ideas with users than write code all day?",
        ("UI/UX Designer", "Njia za Tech #05", True, "Research users, design flows in Figma, test ideas."), ("Frontend or Mobile", "#02 web · #06 phones", True, "Turn designs into real screens people tap."),
        ("Tip", "Frontend if you love the browser, mobile if you love apps.", "Muonekano + code"))
q_slide(4, "Question 3 · Swali la 3", "Do you enjoy finding stories and answers hidden in numbers?",
        ("Data Analyst", "Njia za Tech #03", True, "Excel, SQL and charts that answer real questions."), ("Go to slide 5", "More logic paths", False, "Security, systems and building the engine."),
        ("Tip", "Love Excel already? That's a strong sign.", "Namba zinazungumza"))
q_slide(5, "Question 4 · Swali la 4", "Do you like thinking like an attacker so you can protect systems?",
        ("Cybersecurity", "Njia za Tech #04", True, "Defend systems, find weak spots first."), ("Go to slide 6", "Builders and operators", False, "Build features, or keep systems running."),
        ("Remember", "Only ever practise on legal labs.", "Linda, usivamie"))
q_slide(6, "Question 5 · Swali la 5", "Do you prefer keeping systems running and automating them over building features?",
        ("DevOps Engineer", "Njia za Tech #07", True, "Servers, cloud, automation, uptime."), ("Backend Developer", "Njia za Tech #01", True, "APIs, databases and the logic behind apps."),
        ("Also", "Love helping people more than code? Look at IT Support (#08) or Product (#09).", "Watu kwanza?"))

# ── 7 · all paths ────────────────────────────────────────────────────────────────────────────────
s = page(7, "All 9 paths · Njia zote", "Which tech path?")
title2(s, "Every path,", "one place.", y=220, size=90)
roles = [("Backend", "#01"), ("Frontend", "#02"), ("Data Analyst", "#03"), ("Cybersecurity", "#04"), ("UI/UX", "#05"), ("Mobile", "#06"),
         ("DevOps", "#07"), ("IT Support", "#08"), ("Product", "#09")]
cw = (W - 2 * M - 40) / 3
for i, (r, ep) in enumerate(roles):
    x0, y0 = M + (i % 3) * (cw + 20), 410 + (i // 3) * 190
    card(s, (x0, y0, x0 + cw - 8, y0 + 160), r=16)
    s.text(x0 + 24, y0 + 54, ep, f(BOLD, 24), ORANGE)
    s.text(x0 + 24, y0 + 112, r, f(BOLD, fit(s, r, BOLD, 30, cw - 50)), NAVY)
horizon(s, 7)
navy_note(s, "Read more", "Every role has its own Njia za Tech post on depriver.tech.", "Soma kila njia", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What path did", "you get?", [("Comment", "your result and if it fits"), ("Tag", "a friend to take the quiz"),
                                        ("Suggest", "a role for Njia za Tech season 2")])
stamp(s, 840, 860, "NJIA YANGU", GREEN_OK, angle=-10, size=42)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
