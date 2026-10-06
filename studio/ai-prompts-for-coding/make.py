"""Carousel: AI prompts for coding and learning (8 slides, 1080x1350, exported at 2x). The device is a chat: a weak prompt
gets a red tag, a strong one (context, goal, constraints, format) gets a green one. Pairs with ai-tutor-not-copy-machine."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/ai-prompts-for-coding"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def prompt_card(s, y, label, text, col, size=27, lh=38):
    h = 90 + wrap_lines(s, text, f(MONO, size), W - 2 * M - 80) * lh
    card(s, (M, y, W - M - 8, y + h), r=18)
    s.rect(M + 2, y + 2, M + 12, y + h - 2, col)
    smallcaps(s, M + 40, y + 46, label, 14, col)
    s.para(M + 40, y + 94, text, f(MONO, size), W - 2 * M - 80, lh, NAVY)
    return y + h


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "AI for students · AI kwa wanafunzi")
s.text(M - 6, 250, "Better prompts,", f(BOLD, 96), NAVY)
s.text(M - 6, 350, "better code.", f(BOLD, 96), ORANGE)
s.text(M, 440, "Uliza kwa ufasaha", f(SIG, 58), NAVY)
swash(s, M + 8, M + 400, 466, ORANGE, 6)
chat(s, M, 540, 460, "nisaidie code", "Weak", mine=False, size=26, lh=36, tag="Haieleweki", tag_ok=False)
chat(s, M + 160, 720, 780, "I'm a 2nd-year student using Laravel 11. My form saves twice when I click fast. Explain why, then show the smallest fix.",
     "Strong", mine=True, size=24, lh=34, tag="Safi", tag_ok=True)
horizon(s, 1)
cover_footer(s, "Swipe for the formula")
finish(s)
s.save(1)

# ── 2 · weak prompt ──────────────────────────────────────────────────────────────────────────────
s = page(2, "The problem · Tatizo", "AI kwa wanafunzi")
title2(s, "Vague in,", "vague out.", y=220, size=92)
chat(s, M, 420, 520, "Make me a login system", "You", mine=True, size=26, lh=36)
chat(s, M + 140, 580, 800, "Here's a basic login system in Node.js with Express, MongoDB, JWT and React…", "AI", mine=False, size=25, lh=35,
     tag="Si unachohitaji", tag_ok=False)
s.para(M, 800, "You use PHP and MySQL. It guessed everything: the language, the database, your level. Now you have 200 lines you can't use.",
       f(MED, 29), W - 2 * M, 42, NAVY)
horizon(s, 2)
navy_note(s, "Truth", "AI fills every gap you leave with a guess.", "Usiiache ibahatishe", seed=2)
finish(s)
s.save(2)

# ── 3 · the formula ──────────────────────────────────────────────────────────────────────────────
s = page(3, "The formula · Kanuni", "AI kwa wanafunzi")
title2(s, "Four parts of a", "good prompt.", y=220, size=86)
flow(s, [("Context", "Who you are, your stack, what you tried"), ("Goal", "What you want, in one sentence"),
         ("Constraints", "Your version, no new libraries, beginner level"), ("Format", "Steps, a short example, a hint, a table…")],
     420, h=104, gap=36, size=31)
horizon(s, 3)
navy_note(s, "Remember", "Context, Goal, Constraints, Format.", "C · G · C · F", seed=3)
finish(s)
s.save(3)

# ── 4 · strong example ───────────────────────────────────────────────────────────────────────────
s = page(4, "Example · Mfano", "AI kwa wanafunzi")
title2(s, "The same request,", "done right.", y=220, size=84)
y = prompt_card(s, 400, "Weak prompt · Ombi dhaifu", "Make me a login system", RED_NO, size=26, lh=38)
prompt_card(s, y + 40, "Strong prompt · Ombi zuri",
            "I'm a 2nd-year student. PHP 8 + MySQL, no framework. I need a login page for my FYP. "
            "Explain the steps first, then show only the login code. Use password_verify(). Keep it under 40 lines.",
            GREEN_OK, size=26, lh=38)
horizon(s, 4)
navy_note(s, "Result", "Code that fits YOUR project, and you understand every line.", "Inafaa mradi wako", seed=4)
finish(s)
s.save(4)

# ── 5 · prompts to learn ─────────────────────────────────────────────────────────────────────────
s = page(5, "To learn · Kujifunza", "AI kwa wanafunzi")
title2(s, "Prompts that", "teach you.", y=220, size=90)
y = 410
for t_ in ["Explain this code line by line, like I'm in first year.", "Give me 3 small exercises on loops, without answers.",
           "Here's my code. Don't fix it: give me one hint.", "Quiz me with 5 questions on SQL JOINs."]:
    y = prompt_card(s, y, "Copy this · Nakili", t_, ORANGE, size=24, lh=34) + 24
horizon(s, 5)
navy_note(s, "Exams", "Use AI to practise, so you can do it alone in the exam room.", "Jifunze, usinakili", seed=5)
finish(s)
s.save(5)

# ── 6 · prompts to debug ─────────────────────────────────────────────────────────────────────────
s = page(6, "To debug · Kutatua makosa", "AI kwa wanafunzi")
title2(s, "Debug with AI,", "properly.", y=220, size=88)
tick_fill(s, [("Paste the FULL error", "Not “it doesn't work”."), ("Paste the smallest code that fails", "Not your whole project."),
              ("Say what you expected and what happened", "And what you already tried."), ("Ask for the cause first", "“Why does this happen?” before “fix it”.")],
          420, 990, size=31, sub=26)
horizon(s, 6)
navy_note(s, "Bonus", "Writing this out often solves the bug before you send it.", "Kuandika ni kufikiri", seed=6)
finish(s)
s.save(6)

# ── 7 · rules ────────────────────────────────────────────────────────────────────────────────────
s = page(7, "Rules · Kanuni", "AI kwa wanafunzi")
title2(s, "Use it, but", "stay in charge.", y=220, size=88)
tick_fill(s, [("Never paste secrets", "Passwords, API keys, client data, personal IDs."), ("Run and test everything", "AI code can look right and still be wrong."),
              ("Understand before you submit", "If you can't explain it, don't hand it in."), ("Follow your course's AI rules", "Ask your lecturer what's allowed.")],
          420, 990, size=31, sub=26)
horizon(s, 7)
navy_note(s, "Remember", "AI is your assistant. You are the developer.", "Wewe ndiye msanidi", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What's your best", "prompt?", [("Comment", "a prompt that works for you"), ("Save", "the 4 learning prompts"),
                                          ("Share", "with a classmate who copies blindly")])
stamp(s, 840, 860, "C·G·C·F", GREEN_OK, angle=-10, size=50)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
