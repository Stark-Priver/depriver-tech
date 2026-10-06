"""Carousel: your first tech interview (9 slides, 1080x1350, exported at 2x). Same editorial / print direction as
first-tech-cv. Every question is a flashcard pair: the white front with the question, the navy back with how to answer,
a formula and a short example, laid slightly askew like cards on a desk."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 9
POST_URL = "depriver.tech/blog/first-tech-interview"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing


def flashcard(s, cx, cy, w, h, angle, front, title, body, size=40):
    """A rotated index card. front=True: white with a big Q; else navy 'how to answer'."""
    lay = Image.new("RGBA", (k(w + 40), k(h + 40)), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    bg, fg = ((255, 255, 255), NAVY) if front else (NAVY, WHITE_T)
    ld.rounded_rectangle([k(20), k(20), k(20 + w), k(20 + h)], radius=k(16), fill=bg + (255,), outline=NAVY + (255,), width=k(3))
    if front:
        for i in range(1, int(h / 48)):
            ld.line([k(24), k(20 + 70 + i * 48), k(16 + w), k(20 + 70 + i * 48)], fill=(205, 220, 245, 255), width=k(1.5))
        ld.line([k(24), k(20 + 74), k(16 + w), k(20 + 74)], fill=(232, 96, 58, 200), width=k(2))
    tag = "Swali · Question" if front else "Jinsi ya kujibu · How to answer"
    ld.text((k(50), k(66)), tag.upper(), font=f(SEMI, 15), fill=ORANGE + (255,), anchor="ls")
    tmp = Slide.__new__(Slide)
    tmp.im, tmp.d = lay, ld
    y = 140
    fnt = f(BOLD, size)
    words, line = title.split(), ""
    for wd in words:
        trial = (line + " " + wd).strip()
        if tmp.width(trial, fnt) > w - 70 and line:
            ld.text((k(50), k(y)), line, font=fnt, fill=fg + (255,), anchor="ls")
            y += size * 1.2
            line = wd
        else:
            line = trial
    ld.text((k(50), k(y)), line, font=fnt, fill=fg + (255,), anchor="ls")
    y += size * 0.6
    for para in body:
        fb = f(REG if front else MED, 29)
        y += 44
        words, line = para.split(), ""
        for wd in words:
            trial = (line + " " + wd).strip()
            if tmp.width(trial, fb) > w - 70 and line:
                ld.text((k(50), k(y)), line, font=fb, fill=(GREY if front else SOFT) + (255,), anchor="ls")
                y += 40
                line = wd
            else:
                line = trial
        ld.text((k(50), k(y)), line, font=fb, fill=(GREY if front else SOFT) + (255,), anchor="ls")
    lay = lay.rotate(angle, resample=Image.BICUBIC, expand=True)
    sh = lay.getchannel("A").filter(ImageFilter.GaussianBlur(k(10))).point(lambda v: v * 80 // 255)
    px, py = k(cx) - lay.width // 2, k(cy) - lay.height // 2
    s.im.paste(Image.new("RGB", lay.size, INK), (px + k(8), py + k(14)), sh)
    s.im.paste(lay, (px, py), lay)
    s.d = ImageDraw.Draw(s.im)


def q_slide(n, label, question, formula, example, note):
    s = page(n, label)
    flashcard(s, 470, 330, 820, 300, -3, True, question, [], size=46)
    flashcard(s, 545, 770, 900, 430, 2, False, formula, [example], size=38)
    horizon(s, n)
    navy_note(s, *note, seed=n)
    finish(s)
    s.save(n)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For students & fresh graduates")
s.text(M - 6, 250, "Your first", f(BOLD, 104), NAVY)
s.text(M - 6, 360, "tech interview.", f(BOLD, 96), NAVY)
s.text(M - 8, 480, "Be ready.", f(BOLD, 110), ORANGE)
s.text(M, 570, "Usiende bila maandalizi", f(SIG, 58), NAVY)
swash(s, M + 8, M + 520, 596, ORANGE, 6)
s.para(M, 680, "The questions they always ask, how to answer, and the one word you must learn to say well.", f(REG, 27), 400, 40, GREY)
flashcard(s, 760, 760, 440, 300, -6, True, "Tell me about yourself.", [], size=34)
flashcard(s, 800, 900, 420, 200, 5, False, "Present · past · future.", [], size=30)
horizon(s, 1)
cover_footer(s, "Swipe through the cards")
finish(s)
s.save(1)

# ── 2 · prepare ──────────────────────────────────────────────────────────────────────────────────
s = page(2, "Before the day · Maandalizi")
title2(s, "Win it", "before you arrive.", y=220, size=84)
prep = [("Research the company", "What they build, who they serve, recent news."), ("Test your demo", "Open your project and run it the night before."),
        ("Re-read your CV", "They'll ask about every line on it."), ("Plan the trip", "Arrive 15 minutes early. Online? Charge, data, quiet room."),
        ("Dress one step up", "Neat and simple. Smart casual is safe.")]
numbered(s, prep, 430, gap=112)
horizon(s, 2)
navy_note(s, "Truth", "Confidence comes from preparation, not luck.", "Jiandae, jiamini", seed=2)
finish(s)
s.save(2)

# ── 3–7 · questions ──────────────────────────────────────────────────────────────────────────────
q_slide(3, "Question 01 · Kila mara", "Tell me about yourself.",
        "Present · past · future, in 60 seconds.",
        "“I'm a Computer Science graduate who builds web apps. During FPT I set up an office network and built an equipment tracker. Now I want to grow as a backend developer here.”",
        ("Tip", "Practise it out loud until it sounds natural, not memorised.", "Sekunde 60 tu"))
q_slide(4, "Question 02 · Mradi wako", "Walk me through a project you built.",
        "Problem · your part · tools · result · what you'd improve.",
        "Pick the project you know best. Show it running if you can. Be honest about what was hard.",
        ("Tip", "They're testing understanding. You must know your own code.", "Ijue code yako"))
q_slide(5, "Question 03 · Kwa nini wewe?", "Why should we hire you?",
        "Their need + your proof + your attitude.",
        "“You need someone who can support your systems. I did that daily during FPT, I learn fast, and I finish what I start.”",
        ("Tip", "Read the job advert. Answer with their words.", "Jibu hitaji lao"))
q_slide(6, "Question 04 · Sijui", "A question you can't answer.",
        "Say “sijui” well: honest + how you'd find out.",
        "“I haven't used Kubernetes yet. I'd start with the official docs, try it on a small project, and ask a senior. Here's how I learnt Docker last month…”",
        ("Remember", "Guessing loses trust. Honest + curious wins it.", "Sijui si kosa"))
q_slide(7, "Question 05 · Mwisho", "Do you have any questions for us?",
        "Always say yes. Ask about the work and growth.",
        "“What would my first 90 days look like?” · “How does the team review code?” · “Is there mentorship for juniors?”",
        ("Never say", "“No questions.” It sounds like you don't care.", "Uliza kitu"))

# ── 8 · after ────────────────────────────────────────────────────────────────────────────────────
s = page(8, "After · Baada ya interview")
title2(s, "Follow up", "within 24 hours.", y=230, size=88)
y = chat(s, M, 440, W - 2 * M - 60, "Good afternoon Mr. Mwakyusa, thank you for the interview today for the Junior Developer role. "
         "I enjoyed learning about your systems team, and I'm excited about the chance to contribute. Kind regards, Amina Juma.",
         "Email · thank you note", mine=False, size=26, lh=37)
s.text(M, y + 80, "Short, polite, specific. Then wait patiently.", f(SEMI, 30), NAVY)
s.text(M, y + 130, "No reply in a week or two? One short follow-up is fine.", f(REG, 25), GREY)
horizon(s, 8)
navy_note(s, "Didn't get it?", "Ask for feedback. Every interview is practice.", "Hujashindwa, umejifunza", seed=8)
finish(s)
s.save(8)

# ── 9 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which question", "scares you most?", [("Save", "the night before your interview"), ("Share", "with a friend who's job hunting"),
                                                ("Comment", "the question that scares you")])
flashcard(s, 820, 780, 380, 240, -5, True, "Any questions for us?", [], size=30)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
