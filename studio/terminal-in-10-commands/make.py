"""Carousel: the terminal in 10 commands (8 slides, 1080x1350, exported at 2x). Ujuzi wa kazini. The device is a dark
terminal window with real commands and output. Windows users: Git Bash or WSL."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/terminal-in-10-commands"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs


def cmd_rows(s, rows, y, start=1):
    """Command chip + meaning rows."""
    for i, (c, m) in enumerate(rows):
        ww = s.width(c, f(MONO_B, 28)) + 40
        s.d.rounded_rectangle([k(M), k(y - 38), k(M + ww), k(y + 14)], radius=k(12), fill=TERM_BG)
        s.text(M + 20, y - 3, c, f(MONO_B, 28), WHITE_T)
        s.text(M + ww + 24, y - 3, m, f(SEMI, fit(s, m, SEMI, 27, W - 2 * M - ww - 30)), NAVY)
        s.text(W - M, y - 3, f"#{start + i}", f(BOLD, 22), ORANGE, anchor="rs")
        y += 76
    return y


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Skills uni skips · Ujuzi wa kazini")
s.text(M - 6, 250, "The terminal", f(BOLD, 100), NAVY)
s.text(M - 6, 356, "in 10 commands.", f(BOLD, 92), ORANGE)
s.text(M, 445, "Usiogope skrini nyeusi", f(SIG, 58), NAVY)
swash(s, M + 8, M + 480, 471, ORANGE, 6)
terminal(s, 540, ["$ pwd", "/home/asha", "$ mkdir duka-app && cd duka-app", "$ touch index.html", "$ ls", "index.html"],
         title="asha@laptop: ~", size=25, lh=42)
s.text(M, 960, "Windows? Use Git Bash or WSL. Same commands.", f(SEMI, 25), GREY)
horizon(s, 1)
cover_footer(s, "Swipe, open a terminal")
finish(s)
s.save(1)

# ── 2 · why ──────────────────────────────────────────────────────────────────────────────────────
s = page(2, "Why bother · Kwa nini", "Ujuzi wa kazini")
title2(s, "Every developer", "uses it daily.", y=220, size=86)
tick_fill(s, [("Servers have no mouse", "Deploying and fixing servers happens in the terminal."),
              ("Git, npm, pip, Docker", "The tools you need all start with a command."),
              ("Faster than clicking", "Create, move and search files in seconds."),
              ("Interviewers notice", "Being comfortable here says “I've built real things”.")], 420, 990, size=31, sub=26)
horizon(s, 2)
navy_note(s, "Truth", "You only need about 10 commands to feel at home.", "Amri kumi zinatosha", seed=2)
finish(s)
s.save(2)

# ── 3 · where am I ───────────────────────────────────────────────────────────────────────────────
s = page(3, "Move around · Kuzunguka", "Ujuzi wa kazini")
title2(s, "Where am I?", "Move around.", y=220, size=88)
y = cmd_rows(s, [("pwd", "show the folder you're in"), ("ls", "list what's in this folder"), ("cd", "change folder (cd .. goes up)")], 440)
terminal(s, y + 10, ["$ cd Documents/projects", "$ ls", "duka-app  notes.txt  portfolio", "$ cd .."], title="terminal", size=24, lh=40)
horizon(s, 3)
navy_note(s, "Tip", "Press Tab to auto-complete folder names.", "Tab ni rafiki", seed=3)
finish(s)
s.save(3)

# ── 4 · make things ──────────────────────────────────────────────────────────────────────────────
s = page(4, "Create & move · Tengeneza", "Ujuzi wa kazini")
title2(s, "Create, copy,", "move.", y=220, size=88)
y = cmd_rows(s, [("mkdir", "make a new folder"), ("touch", "make an empty file"), ("cp", "copy a file (cp -r for folders)"),
                 ("mv", "move or rename")], 440, start=4)
terminal(s, y + 10, ["$ mkdir images", "$ cp logo.png images/", "$ mv index.html home.html"], title="terminal", size=24, lh=40)
horizon(s, 4)
navy_note(s, "Rename", "There's no rename command. mv old new does it.", "mv inabadilisha jina", seed=4)
finish(s)
s.save(4)

# ── 5 · read, find, delete ───────────────────────────────────────────────────────────────────────
s = page(5, "Read & find · Soma na tafuta", "Ujuzi wa kazini")
title2(s, "Read, search,", "delete (carefully).", y=220, size=82)
y = cmd_rows(s, [("cat", "print a file's contents"), ("grep", "search for text in files"), ("rm", "delete a file, FOREVER")], 440, start=8)
terminal(s, y + 10, ["$ grep -r \"TODO\" .", "./app.py:12: # TODO: add login", "$ rm old-notes.txt"], title="terminal", size=24, lh=40)
horizon(s, 5)
navy_note(s, "Warning", "rm has no recycle bin. Never run rm -rf on something you didn't read.", "Hakuna kurudisha", seed=5)
finish(s)
s.save(5)

# ── 6 · shortcuts ────────────────────────────────────────────────────────────────────────────────
s = page(6, "Shortcuts · Njia za mkato", "Ujuzi wa kazini")
title2(s, "Keys that", "save hours.", y=220, size=92)
table(s, M, 410, ["Key", "Does"], [["Tab", "Auto-complete names"], ["Up arrow", "Repeat previous commands"], ["Ctrl + C", "Stop what's running"],
                                    ["Ctrl + L / clear", "Clear the screen"], ["Ctrl + R", "Search your command history"]],
      [340, W - 2 * M - 8 - 340], size=27, rh=82)
horizon(s, 6)
navy_note(s, "Bonus", "command --help explains any command.", "Uliza --help", seed=6)
finish(s)
s.save(6)

# ── 7 · practise ─────────────────────────────────────────────────────────────────────────────────
s = page(7, "Practise · Zoezi", "Ujuzi wa kazini")
title2(s, "10-minute", "challenge.", y=220, size=92)
numbered(s, [("Make a folder called portfolio", "mkdir portfolio, then cd into it"), ("Create index.html and style.css", "touch index.html style.css"),
             ("Make an images folder", "and copy one photo into it"), ("Rename style.css to main.css", "mv style.css main.css"),
             ("List everything, then go back up", "ls, then cd ..")], 430, gap=112)
horizon(s, 7)
navy_note(s, "Done?", "You just used 7 of the 10. Screenshot it.", "Umeweza!", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which command", "was new to you?", [("Comment", "your favourite command"), ("Save", "as your cheat sheet"),
                                               ("Share", "with someone scared of the terminal")])
terminal(s, 780, ["$ echo \"nimeweza\"", "nimeweza"], title="terminal", size=22, lh=38, x0=600)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
