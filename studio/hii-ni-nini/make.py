"""Carousel: Hii ni nini? Guess the file from what's inside (8 slides, 1080x1350, exported at 2x). A light holiday quiz.
Five mystery files (name hidden as ????), each with three options; all answers and what each file does on slide 7."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/hii-ni-nini"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs

FILES = [
    ("package.json", ['{', '  "name": "duka-app",', '  "version": "1.0.0",', '  "scripts": {', '    "dev": "vite"', '  },',
                      '  "dependencies": {', '    "react": "^19.0.0"', '  }', '}'],
     ["A. config.php", "B. package.json", "C. index.html"], "Lists a JavaScript project's name, scripts and the packages it needs."),
    (".gitignore", ["node_modules/", ".env", "*.log", "__pycache__/", "dist/", ".DS_Store"],
     ["A. .gitignore", "B. README.md", "C. Makefile"], "Tells Git which files never to commit: secrets, build output, junk."),
    (".env", ["DB_HOST=localhost", "DB_USER=duka", "DB_PASSWORD=********", "SMS_API_KEY=********", "APP_DEBUG=false"],
     [".env", "", ""], "Secret settings and keys. Never commit it, never share it."),
    ("Dockerfile", ["FROM python:3.12-slim", "WORKDIR /app", "COPY requirements.txt .", "RUN pip install -r requirements.txt",
                    "COPY . .", 'CMD ["python", "app.py"]'],
     ["A. Dockerfile", "B. setup.py", "C. requirements.txt"], "Instructions to build a container: the same app runs the same everywhere."),
    ("README.md", ["# Duka App", "", "Simple stock and sales app for small shops.", "", "## Run it", "    npm install", "    npm run dev"],
     ["A. LICENSE", "B. notes.txt", "C. README.md"], "The front page of your project. Recruiters read it first."),
]
FILES[2] = (FILES[2][0], FILES[2][1], ["A. .env", "B. secrets.json", "C. config.yml"], FILES[2][3])

# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Quiz · Chemsha bongo")
s.text(M - 6, 280, "Hii ni", f(BOLD, 150), NAVY)
s.text(M - 6, 420, "nini?", f(BOLD, 150), ORANGE)
s.text(M, 510, "Taja jina la faili", f(SIG, 60), NAVY)
swash(s, M + 8, M + 420, 536, ORANGE, 6)
s.para(M, 620, "Five files every developer meets. You see what's inside, you guess the name. Answers on slide 7.", f(REG, 28), 450, 42, GREY)
outline_text(s, W - M + 10, 600, "?", f(BOLD, 420), stroke=4, color=ORANGE, anchor="rs", opacity=0.6)
code_window(s, 700, FILES[1][1][:5], file="????", lang="?", size=24, lh=40, x0=560)
horizon(s, 1)
cover_footer(s, "Swipe, count your score")
finish(s)
s.save(1)

# ── 2–6 · mystery files ──────────────────────────────────────────────────────────────────────────
for i, (name, lines, opts, _) in enumerate(FILES):
    n = i + 2
    s = page(n, f"Faili {i + 1:02d} / 05", "Hii ni nini?")
    s.text(M - 4, 250, "What's this", f(BOLD, 84), NAVY)
    s.text(M - 4, 340, "file called?", f(BOLD, 84), ORANGE)
    y = code_window(s, 400, lines, file="????", lang="?", size=25, lh=40)
    ow = (W - 2 * M - 40) / 3
    for j, o in enumerate(opts):
        x0 = M + j * (ow + 20)
        card(s, (x0, y + 50, x0 + ow - 8, y + 130), r=40)
        s.text(x0 + (ow - 8) / 2, y + 90, o, f(BOLD, fit(s, o, BOLD, 26, ow - 40)), NAVY, anchor="mm")
    horizon(s, n)
    navy_note(s, "Your answer", "Write A, B or C in the comments before slide 7.", "Usichungulie!", seed=n)
    finish(s)
    s.save(n)

# ── 7 · answers ──────────────────────────────────────────────────────────────────────────────────
s = page(7, "Majibu · Answers", "Hii ni nini?")
title2(s, "The answers.", "How many?", y=220, size=88)
letters = ["B", "A", "A", "A", "C"]
y = 410
for i, (name, _, _, what) in enumerate(FILES):
    s.d.ellipse([k(M), k(y - 34), k(M + 50), k(y + 16)], fill=ORANGE)
    s.text(M + 25, y - 9, letters[i], f(BOLD, 24), WHITE_T, anchor="mm")
    s.text(M + 74, y, name, f(MONO_B, 30), NAVY)
    s.para(M + 74, y + 40, what, f(REG, 24), W - 2 * M - 80, 33, GREY)
    y += 128
horizon(s, 7)
navy_note(s, "Score", "5/5 senior · 3/5 getting there · 1/5 just starting (that's fine)", "Hongera!", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "What did", "you score?", [("Comment", "your score out of 5"), ("Share", "and challenge a classmate"),
                                     ("Suggest", "a file for the next quiz")])
stamp(s, 840, 860, "5/5", GREEN_OK, angle=-10, size=70)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
