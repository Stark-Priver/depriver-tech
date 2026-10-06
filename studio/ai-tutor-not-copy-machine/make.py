"""Carousel: use AI like a tutor, not a copy machine (9 slides, 1080x1350, exported at 2x).
Same editorial / print direction as github-that-gets-you-hired. Every round is a chat: the copy-machine prompt
(red tag) against the tutor prompt (green tag), so students can steal the good prompts word for word."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 9
POST_URL = "depriver.tech/blog/ai-tutor-not-copy-machine"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, chat, closing

ART.update({
    # a photocopier spitting out identical pages vs a chalkboard: copy machine vs tutor
    "copier": svg(GROUND + f'''
      <rect x="110" y="150" width="260" height="210" rx="18" fill="#c9d4ea" {ST}/>
      <rect x="130" y="110" width="220" height="50" rx="10" fill="#fff" {ST}/>
      <rect x="150" y="200" width="120" height="60" rx="8" fill="#0b1e3f"/>
      <text x="210" y="240" text-anchor="middle" font-family="Liberation Mono" font-weight="700" font-size="22" fill="#e8603a">COPY</text>
      <circle cx="320" cy="230" r="16" fill="#e8603a" {ST} stroke-width="4"/>
      {"".join(f'<g transform="translate({380 + i * 34} {250 - i * 30}) rotate({8 + i * 6})"><rect width="120" height="150" rx="6" fill="#fff" {ST} stroke-width="5"/><path d="M20 40 h80 M20 70 h60 M20 100 h70" stroke="#c9d4ea" stroke-width="8" stroke-linecap="round"/><text x="60" y="135" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="18" fill="#c43434">0/20</text></g>' for i in range(3))}'''),
})


def round_slide(n, label, t1, t2, bad, good, note, got=("An answer you can't explain", "Understanding you keep")):
    s = page(n, label)
    title2(s, t1, t2, y=220, size=78)
    y = chat(s, M, 420, W - 2 * M - 100, bad, "Copy machine", mine=False, size=30, lh=42, tag="Copy", tag_ok=False)
    mark(s, M + 18, y + 44, False, r=15)
    s.text(M + 46, y + 54, "You get: " + got[0], f(SEMI, 24), RED_NO)
    y = chat(s, M + 60, y + 150, W - 2 * M - 68, good, "Tutor mode", mine=True, size=29, lh=41, tag="Tutor", tag_ok=True)
    mark(s, M + 78, y + 44, True, r=15)
    s.text(M + 106, y + 54, "You get: " + got[1], f(SEMI, 24), GREEN_OK)
    sticker(s, W - M - 150, min(y + 130, 990), "Steal this prompt", angle=-5, size=19, bg=NAVY)
    horizon(s, n)
    navy_note(s, *note, seed=n)
    finish(s)
    s.save(n)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For students learning tech")
s.text(M - 6, 250, "Use AI like", f(BOLD, 100), NAVY)
s.text(M - 6, 360, "a tutor,", f(BOLD, 100), ORANGE)
s.text(M - 6, 466, "not a copy machine.", f(BOLD, 76), NAVY)
s.text(M, 560, "Akili ni yako", f(SIG, 66), ORANGE)
swash(s, M + 8, M + 320, 586, ORANGE, 6)
s.para(M, 670, "Five ways to learn faster with AI, and the habit that turns it into a crutch.", f(REG, 27), 400, 40, GREY)
paste_print(s, print_art("copier", k(520)), 500, 600)
horizon(s, 1)
cover_footer(s, "Swipe for prompts to steal")
finish(s)
s.save(1)

# ── 2 · the trap ─────────────────────────────────────────────────────────────────────────────────
s = page(2, "The trap · Mtego")
title2(s, "Copy-paste works", "until it doesn't.", y=230, size=80)
moments = [("The exam", "No AI in the room. Just you and the paper."),
           ("The interview", "“Walk me through your code.” Silence."),
           ("The 2 a.m. bug", "Production is down and the answer isn't on any chat."),
           ("The job", "You get paid to think, not to paste.")]
y = 440
for a, b in moments:
    mark(s, M + 18, y - 10, False)
    s.text(M + 56, y, a, f(BOLD, 32), NAVY)
    s.text(M + 56, y + 40, b, f(REG, 24), GREY)
    y += 120
sticker(s, W - M - 210, 950, "If you can't explain it, you didn't learn it", angle=-4, size=18, bg=NAVY)
horizon(s, 2)
navy_note(s, "The rule", "AI should make you think more, not less.", "Usiache akili ilale", seed=2)
finish(s)
s.save(2)

# ── 3–7 · rounds ─────────────────────────────────────────────────────────────────────────────────
round_slide(3, "Round 01 · Ask for explanations", "Ask why,", "not just what.",
            "Write my assignment on linked lists.",
            "Explain linked lists like I'm new to them, with a real-life example. Then give me one small exercise, but don't show the answer.",
            ("Why it works", "You do the thinking. AI only lights the road.", "Elewa, usikariri"),
            got=("Homework done, nothing learnt", "You understand it, and practise"))
round_slide(4, "Round 02 · Debug with it", "Understand", "the error.",
            "Fix my code. [pastes 200 lines]",
            "Here's my error and the function it points to. What does this error mean, and where should I look first? Give me hints, not the fix.",
            ("Why it works", "Reading errors is the skill every job needs.", "Kosa ni mwalimu", ),
            got=("The same bug next week", "You can fix it yourself next time"))
round_slide(5, "Round 03 · Make it quiz you", "Let it test", "you first.",
            "Summarise chapter 5 for my exam.",
            "Quiz me with 5 questions on SQL joins, one at a time. Wait for my answer, then tell me what I got wrong and why.",
            ("Why it works", "Testing yourself beats re-reading notes.", "Jipime kabla ya mtihani"),
            got=("A summary you forget", "You find your weak spots"))
round_slide(6, "Round 04 · Get a code review", "Write it first.", "Then compare.",
            "Write a login page in PHP for me.",
            "I wrote this login function myself. What would a senior developer improve, especially security, and why?",
            ("Why it works", "You learn what seniors notice, on your own code.", "Andika kwanza wewe"),
            got=("Code you can't defend", "Senior-level feedback on your code"))
round_slide(7, "Round 05 · Check everything", "AI can be", "confidently wrong.",
            "AI said it, so it must be right.",
            "Show me where this is in the official docs, and give me a small test so I can check it works on my machine.",
            ("Why it works", "Run it, test it, and check the docs. Always.", "Hakiki kila jibu"),
            got=("Wrong answers, said confidently", "Answers you've proven"))

# ── 8 · rules ────────────────────────────────────────────────────────────────────────────────────
s = page(8, "House rules · Kanuni")
title2(s, "Five rules", "for using AI.", y=220, size=80)
rules = [("Know your school's rules", "Ask lecturers what's allowed in assignments."),
         ("Never paste secrets", "No passwords, client data or office code."),
         ("Try first, ask second", "Twenty minutes stuck, then ask for a hint."),
         ("Explain it back", "If you can't teach it to a friend, go again."),
         ("Credit it honestly", "Say when AI helped. Integrity is a skill.")]
numbered(s, rules, 430, gap=112)
horizon(s, 8)
navy_note(s, "Remember", "AI is a tool in your hand, not a brain in your place.", "Akili ni yako", seed=8)
finish(s)
s.save(8)

# ── 9 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which AI tool do", "you learn with?", [("Save", "and steal the tutor prompts"), ("Share", "with a classmate who copies"),
                                                 ("Comment", "your best learning prompt")])
chat(s, 620, 700, 380, "Quiz me. Don't give answers.", "Tutor mode", mine=True, size=22, lh=30)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
