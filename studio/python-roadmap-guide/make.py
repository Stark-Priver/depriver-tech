"""Book (PDF): "Python Daily: from beginner to professional" by Privatus Cosmas. A4 pages (1240x1754, exported at 2x = 300 dpi), same
palette, fonts and devices as the python-roadmap carousel. Content is a list of blocks per chapter; a small layout engine
measures each block and flows it onto pages (running head, page numbers), with chapter openers, contents and covers.

    python3 studio/python-roadmap-guide/make.py   -> export/page-NN.jpg + export/python-beginner-to-professional.pdf"""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())
W, H = 1240, 1754                                         # A4 portrait
exec(open(os.path.join(STUDIO, "kit.py")).read())
TOTAL, POST_URL = 1, "depriver.tech/blog/python-roadmap"
exec(open(os.path.join(STUDIO, "editorial.py")).read())
exec(open(os.path.join(STUDIO, "devices.py")).read())
exec(open(os.path.join(STUDIO, "python-roadmap", "data.py")).read())

BOOK = "Python Daily"
SUB = "From beginner to professional"
AUTHOR = "Privatus Cosmas"
BM = 120                       # book margin
CW = W - 2 * BM
TOP, BOTTOM = 190, H - 150
BODY, LH = 24, 38
PAPER_BOOK = (250, 249, 246)

# ══ content ═══════════════════════════════════════════════════════════════════════════════════════
# blocks: ("h2", t) ("h3", t) ("p", t) ("bul", [..]) ("num", [(a, b)]) ("code", file, [lines]) ("term", [lines])
#         ("table", cols, rows, widths) ("tip", label, text) ("ex", [..]) ("pb",)
CH = []


def chapter(title, sw, intro, blocks, label=None):
    CH.append(dict(title=title, sw=sw, intro=intro, blocks=blocks, label=label or title))


chapter("Why Python?", "Lugha ya kila fani",
        "Before you write a single line, it helps to know what you're learning, why it's worth it, and how this book will get you there.", [
    ("h2", "What Python is"),
    ("p", "Python is a programming language: a way of writing instructions that a computer can follow. It was created by Guido van Rossum and "
          "first released in 1991. Its big idea is that code should be easy for humans to read. That is why Python looks almost like English, "
          "and why so many schools and universities teach it first."),
    ("code", "hello.py", ['jina = "Asha"', 'print(f"Habari, {jina}!")']),
    ("p", "Even if you have never programmed before, you can probably guess what those two lines do: store a name, then greet it."),
    ("h2", "Why it's worth learning"),
    ("bul", ["It reads almost like English, so you spend your energy on logic, not on symbols.",
             "One language opens many careers: web development, data, AI, automation, cybersecurity, DevOps, research and more.",
             "It has a huge, free community. Almost every error you will meet, someone has already met and explained online.",
             "It is used by companies large and small, from global platforms to the startup down the road."]),
    ("h2", "How to use this book"),
    ("p", "The book follows six levels. Each level has a goal, the topics to learn, real code, practice exercises and a project. Don't rush. "
          "Move to the next level when you can do the practice without looking everything up."),
    ("table", ["Level", "Name", "Rough time"], [[a, b, c] for a, b, c, _ in LEVELS], [220, 400, 380]),
    ("tip", "Rough times", "These assume one to two hours a day. Going slower is fine. Stopping is the only thing that doesn't work."),
    ("p", "Type every example yourself. Don't copy and paste. Then change it, break it and fix it. That is how the knowledge moves from the page into your hands."),
])

chapter("Set up your tools", "Anza na ulicho nacho",
        "Level 0 takes one evening. By the end you will have Python installed, a proper code editor and your first program running.", [
    ("h2", "1. Install Python"),
    ("p", "Go to python.org, open Downloads and install the latest Python 3 version for your system."),
    ("bul", ["Windows: run the installer and tick “Add python.exe to PATH” before you click Install. This one tick saves hours of confusion.",
             "macOS: install from python.org, or with Homebrew if you already use it.",
             "Linux: Python 3 is usually already installed. Check in the terminal."]),
    ("term", ["$ python --version", "Python 3.13.0"]),
    ("tip", "Note", "On some systems the command is python3 instead of python. If one doesn't work, try the other."),
    ("h2", "2. Install VS Code"),
    ("p", "Download Visual Studio Code (free) from code.visualstudio.com. Open it, go to Extensions and install the official “Python” extension by Microsoft. "
          "It gives you colours, suggestions, error hints and a Run button."),
    ("h2", "3. Run your first program"),
    ("p", "Make a folder called python-journey. Open it in VS Code, create a file called hello.py and type:"),
    ("code", "hello.py", ['print("Habari, dunia!")', 'print("I am learning Python.")']),
    ("p", "Save it, then run it from the terminal inside VS Code:"),
    ("term", ["$ python hello.py", "Habari, dunia!", "I am learning Python."]),
    ("h2", "No laptop yet?"),
    ("p", "You can start in the browser with Google Colab or Replit, even on a phone. It is not ideal for big projects, but it is perfect for "
          "Level 1. Don't let missing equipment delay you."),
    ("ex", ["Install Python and check the version.", "Install VS Code and the Python extension.", "Run a file that prints your name and your town."]),
])

chapter("The basics", "Msingi imara",
        "Level 1, weeks 1 to 6. These ideas exist in every programming language. Learn them well here and every language after Python becomes easier.", [
    ("h2", "Variables and data types"),
    ("p", "A variable is a name that points to a value. Python works out the type from the value you give it."),
    ("code", "types.py", ['name = "Asha"        # str: text', "age = 19             # int: whole number", "height = 1.62        # float: decimal",
                          "is_student = True    # bool: True or False", "", "print(type(age))     # <class 'int'>"]),
    ("h2", "Strings and input"),
    ("p", "Strings hold text. f-strings let you put variables inside text. input() reads what the user types, always as a string, so convert it when you need a number."),
    ("code", "greet.py", ['name = input("Jina lako? ")', 'year = int(input("Mwaka uliozaliwa? "))', "age = 2026 - year",
                          'print(f"{name.title()}, you are about {age}.")']),
    ("h2", "Conditions"),
    ("p", "if, elif and else let your program make decisions. Indentation (four spaces) shows which lines belong to which branch."),
    ("code", "grade.py", ["mark = 72", "", "if mark >= 75:", '    print("A")', "elif mark >= 65:", '    print("B")', "elif mark >= 45:",
                          '    print("C")', "else:", '    print("Fail")']),
    ("h2", "Loops"),
    ("p", "A for loop repeats over a sequence. A while loop repeats until a condition becomes false."),
    ("code", "loops.py", ["marks = [78, 45, 90, 62]", "for m in marks:", '    print(m, "Pass" if m >= 50 else "Fail")', "",
                          "count = 3", "while count > 0:", "    print(count)", "    count -= 1"]),
    ("h2", "Functions"),
    ("p", "A function is a named block of code you write once and use many times. It takes inputs (parameters) and can return a result."),
    ("code", "functions.py", ["def average(numbers):", "    return sum(numbers) / len(numbers)", "", "print(average([78, 45, 90]))  # 71.0"]),
    ("h2", "Data structures"),
    ("table", ["Type", "Example", "Use it for"], [["list", "[78, 90, 62]", "Ordered items you can change"], ["dict", '{"name": "Asha"}', "Values found by a key"],
                                                  ["tuple", "(-6.8, 39.2)", "Fixed values, like a location"], ["set", '{"Dar", "Mbeya"}', "Unique items"]],
     [160, 380, 460]),
    ("code", "student.py", ['student = {"name": "Asha", "marks": [78, 90, 62]}', 'student["marks"].append(85)', 'best = max(student["marks"])',
                            'print(f"{student[\'name\']} best mark: {best}")']),
    ("h2", "Errors and files"),
    ("p", "Errors are normal. Read them from the bottom line up: it names the error and the line. Use try/except to handle errors you expect."),
    ("code", "safe.py", ["try:", '    age = int(input("Age? "))', "except ValueError:", '    print("Please type a number.")', "",
                         'with open("notes.txt", "a") as file:', '    file.write("Today I learned loops.\\n")']),
    ("h2", "Practice"),
    ("ex", ["Ask for two numbers and print their sum, difference and product.", "Print the multiplication table of any number the user types.",
            "Write a function is_even(n) that returns True or False.", "Count how many times each word appears in a sentence (use a dict).",
            "Save a list of names to a file, then read them back."]),
    ("h2", "Project: grade calculator"),
    ("p", "Ask for a student's name and five marks, then print the average, the highest mark and the grade, and save the result to a file. "
          "Handle wrong input without crashing. When you can build this without a tutorial, you're ready for Level 2."),
])

chapter("Intermediate Python", "Sasa unajenga",
        "Level 2, months 2 to 3. You'll stop writing everything yourself and start using other people's code, organise your own code into classes, "
        "and talk to the internet.", [
    ("h2", "Modules and the standard library"),
    ("p", "Python comes with batteries included: hundreds of ready modules. Import what you need."),
    ("code", "dates.py", ["from datetime import date", "import random", "", "print(date.today())", 'print(random.choice(["Dar", "Mbeya", "Arusha"]))']),
    ("h2", "pip and virtual environments"),
    ("p", "pip installs packages written by others. A virtual environment keeps each project's packages separate, so projects don't break each other."),
    ("term", ["$ python -m venv .venv", "# Windows: .venv\\Scripts\\activate", "$ source .venv/bin/activate", "$ pip install requests",
              "$ pip freeze > requirements.txt"]),
    ("h2", "Classes and objects"),
    ("p", "A class is a blueprint; an object is a thing built from it. Classes group data and the functions that work on it."),
    ("code", "account.py", ["class Account:", "    def __init__(self, owner, balance=0):", "        self.owner = owner", "        self.balance = balance", "",
                            "    def deposit(self, amount):", "        self.balance += amount", "", 'acc = Account("Asha")', "acc.deposit(5000)",
                            "print(acc.owner, acc.balance)"]),
    ("h2", "Comprehensions"),
    ("code", "comprehension.py", ["marks = [78, 45, 90, 62]", "passed = [m for m in marks if m >= 50]", "squares = {n: n * n for n in range(5)}"]),
    ("h2", "JSON and CSV"),
    ("p", "Most real data arrives as JSON (from APIs) or CSV (from spreadsheets). Python reads both out of the box."),
    ("code", "sales.py", ["import csv", "", 'with open("sales.csv") as file:', "    rows = list(csv.DictReader(file))", "",
                          'total = sum(float(r["amount"]) for r in rows)', 'print(f"Total sales: {total:,.0f}")']),
    ("h2", "Talking to APIs"),
    ("p", "An API is a door into another service. The requests package fetches data in a few lines. This uses the free Open-Meteo weather API (no key needed):"),
    ("code", "weather.py", ["import requests", "", 'url = "https://api.open-meteo.com/v1/forecast"', 'params = {"latitude": -8.9, "longitude": 33.46,',
                            '          "current_weather": True}', "data = requests.get(url, params=params).json()", 'print(data["current_weather"]["temperature"])']),
    ("h2", "Git and GitHub"),
    ("p", "Git saves the history of your code; GitHub stores it online and becomes your public portfolio. Learn these from now on, every day."),
    ("term", ["$ git init", "$ git add .", '$ git commit -m "Add weather app"', "$ git push"]),
    ("h2", "Practice"),
    ("ex", ["Create a class Student with a method that returns the average mark.", "Read a CSV of expenses and print the total per category.",
            "Fetch data from a free public API and print three facts from it.", "Put every project from now on in its own GitHub repository."]),
    ("h2", "Project: weather app"),
    ("p", "Ask for a town, look up its coordinates in a small dict, fetch the current weather and print a friendly message. Save every search "
          "to a JSON file and add a command that shows search history."),
])

chapter("Advanced Python", "Ubora ni kazi",
        "Level 3, months 4 to 6. Now you'll learn to write code that other people can read, trust and build on. This is the difference between "
        "code that works on your laptop and code a company can use.", [
    ("h2", "Type hints"),
    ("p", "Type hints say what a function expects and returns. Python doesn't enforce them, but editors and tools use them to catch mistakes early."),
    ("code", "typed.py", ["def average(marks: list[float]) -> float:", "    return sum(marks) / len(marks)"]),
    ("h2", "Testing with pytest"),
    ("p", "A test is code that checks your code. Run pytest and it finds every function that starts with test_."),
    ("code", "test_marks.py", ["from typed import average", "", "def test_average():", "    assert average([50, 100]) == 75", "",
                               "def test_single_mark():", "    assert average([80]) == 80"]),
    ("term", ["$ pip install pytest", "$ pytest", "2 passed in 0.01s"]),
    ("h2", "Clean code"),
    ("bul", ["Follow PEP 8, Python's style guide. Let a tool like ruff check and format your code automatically.",
             "Name things clearly: total_sales, not ts.", "Keep functions small: one function, one job.",
             "Write a README for every project: what it does, how to run it."]),
    ("h2", "Decorators and generators"),
    ("p", "A decorator wraps a function to add behaviour. A generator produces values one at a time with yield, which saves memory on big data."),
    ("code", "advanced.py", ["import time", "", "def timer(func):", "    def wrapper(*args):", "        start = time.time()", "        result = func(*args)",
                             '        print(f"{func.__name__} took {time.time() - start:.2f}s")', "        return result", "    return wrapper", "",
                             "def read_lines(path):", "    with open(path) as file:", "        for line in file:", "            yield line.strip()"]),
    ("h2", "Databases with SQL"),
    ("p", "Real apps store data in databases. Python includes sqlite3, so you can learn SQL with nothing to install."),
    ("code", "db.py", ["import sqlite3", "", 'con = sqlite3.connect("shop.db")', 'con.execute("CREATE TABLE IF NOT EXISTS sales (item TEXT, amount REAL)")',
                       'con.execute("INSERT INTO sales VALUES (?, ?)", ("Sugar", 3500))', "con.commit()",
                       'print(con.execute("SELECT SUM(amount) FROM sales").fetchone())']),
    ("tip", "Security", "Always use ? placeholders for values, never f-strings inside SQL. It protects you from SQL injection."),
    ("h2", "A first look at async"),
    ("p", "async lets one program wait for many slow things at once, such as many web requests. You'll meet it in FastAPI and bots. Understand the idea "
          "now; master it later in your specialisation."),
    ("h2", "Practice"),
    ("ex", ["Add type hints to every function in your Level 2 projects.", "Write at least five pytest tests for your grade calculator.",
            "Run ruff on your code and fix what it reports.", "Store your weather history in SQLite instead of JSON."]),
    ("h2", "Project: expense tracker"),
    ("p", "A command-line app that adds, lists and deletes expenses stored in SQLite, shows totals per category and per month, and has tests for "
          "every calculation. Put it on GitHub with a proper README. This is a portfolio project."),
])

area_blocks = [("p", "Here is where Python is used today, with the libraries professionals use and a first project for each. Read them all, then pick the one "
                     "that excites you most. That choice is Level 4."),
               ("tip", "Big names", "Instagram, Spotify, Netflix, Dropbox and NASA have all used Python in their work.")]
for i, (name, use, libs, proj) in enumerate(AREAS):
    area_blocks.append(("area", i + 1, name, use, libs, proj))
chapter("Where Python is used", "Python iko kila mahali",
        "Python isn't one job. It's a key that opens twenty different doors. This chapter walks through every major area.", area_blocks)

path_blocks = [("p", "By now you know Python itself. The next step is to go deep in one area. One path for six months beats six paths for one month.")]
for name, order, proj in PATHS:
    path_blocks += [("h3", name), ("p", f"Learn in this order: {order}."), ("p", f"Serious project: {proj}.")]
path_blocks += [("tip", "Can't decide?", "Choose the area whose first project you would build even if nobody paid you. Curiosity carries you further than salary.")]
chapter("Specialise", "Njia moja kwanza", "Level 4, months 6 to 9. Pick one path from the last chapter and go deep.", path_blocks)

chapter("Work like a professional", "Kuaminika ni ujuzi",
        "Level 5, month 9 and beyond. Professional doesn't mean knowing everything. It means being reliable: your code works, others can read it, "
        "and you deliver what you promise.", [
    ("h2", "The professional toolkit"),
    ("bul", ["Git every day: branches, pull requests and clear commit messages.", "Tests and code reviews: give feedback and receive it without taking it personally.",
             "Docker: package your app so it runs the same on every machine.", "Deploys: your code runs on servers, not only on your laptop.",
             "Documentation: READMEs and comments that help the next person."]),
    ("code", "Dockerfile", ["FROM python:3.13-slim", "WORKDIR /app", "COPY requirements.txt .", "RUN pip install -r requirements.txt", "COPY . .",
                            'CMD ["python", "main.py"]']),
    ("h2", "Getting hired"),
    ("bul", ["Three strong portfolio projects, live and explained.", "A clean GitHub and LinkedIn.",
             "Practice problem solving: lists, dicts, strings, sorting, searching and recursion, on sites like LeetCode or HackerRank.",
             "Real experience: freelance jobs, open source contributions, hackathons or a team project."]),
    ("h2", "Keep growing"),
    ("p", "Read other people's code. Follow the release notes of the tools you use. Teach what you learn; explaining is the fastest way to understand. "
          "And keep building: the habit that got you here is the habit that will keep you here."),
])

chapter("Your 12-month plan", "Polepole ndio mwendo", "Everything in this book, on one calendar.", [
    ("table", ["Months", "Focus", "Finish with"], [["1", "Set up + basics", "Small programs"], ["2", "Basics + practice", "Grade calculator"],
                                                   ["3", "Intermediate", "Weather app"], ["4–5", "Advanced", "Expense tracker"],
                                                   ["6–9", "Specialise", "One serious project"], ["10–12", "Professional", "Portfolio + applications"]],
     [180, 400, 420]),
    ("h2", "A daily routine"),
    ("num", [("10 minutes", "Review yesterday's code."), ("40 minutes", "Learn one new thing and type the examples."),
             ("30 minutes", "Build: add one small feature to your project."), ("5 minutes", "Commit and push to GitHub.")]),
    ("h2", "Habits that get you there"),
    ("bul", ["Code a little every day. One hour daily beats a weekend marathon.", "Read the error message, bottom line first.",
             "Build before you feel ready. You never will; build anyway.", "Use AI as a tutor: ask it to explain, not to do your work.",
             "Learn in public: share progress on LinkedIn or your status."]),
    ("h2", "Mistakes to avoid"),
    ("bul", ["Jumping to Django or AI before the basics.", "Watching tutorials without building anything.", "Switching languages every few weeks.",
             "Comparing your chapter 1 to someone else's chapter 10."]),
])

chapter("Resources and glossary", "Pakua, soma, jenga", "Free places to keep learning, and the words you'll hear most.", [
    ("h2", "Free resources"),
    ("num", RESOURCES + [("freeCodeCamp", "Free Python and data courses with certificates"), ("Official docs", "docs.python.org: the final word on everything")]),
    ("h2", "Glossary"),
    ("num", [("Variable", "A name that points to a value."), ("Function", "A named, reusable block of code."), ("Module", "A file of Python code you can import."),
             ("Package", "A collection of modules, often installed with pip."), ("Library / framework", "Ready code for common jobs; a framework also sets the structure."),
             ("API", "A way for programs to talk to each other."), ("Virtual environment", "A separate space for one project's packages."),
             ("Bug", "A mistake in code. Debugging is finding and fixing it."), ("Repository", "A project folder tracked by Git."),
             ("Deploy", "Putting your app on a server so others can use it.")]),
])

# ══ layout engine ═════════════════════════════════════════════════════════════════════════════════
_probe = Slide()


def lines_h(text, size, maxw, lh, font=REG):
    return wrap_lines(_probe, text, f(font, size), maxw) * lh


def measure(b):
    t = b[0]
    if t == "h2":
        return 96
    if t == "h3":
        return 66
    if t == "p":
        return lines_h(b[1], BODY, CW, LH) + 20
    if t in ("bul", "ex"):
        return sum(lines_h(x, BODY, CW - 44, LH) + 10 for x in b[1]) + 20 + (56 if t == "ex" else 0)
    if t == "num":
        return sum(40 + lines_h(bb, 22, CW - 60, 32) + 18 for _, bb in b[1]) + 10
    if t == "code":
        return 64 + 26 + 34 * len(b[2]) + 16 + 40
    if t == "term":
        return 64 + 26 + 34 * len(b[1]) + 16 + 40
    if t == "table":
        return 58 * (len(b[2]) + 1) + 40
    if t == "tip":
        return 100 + lines_h(b[2], 23, CW - 80, 34) + 40
    if t == "area":
        return 70 + lines_h(b[3], 22, CW - 80, 32) + 32 + 32 + 46
    return 0


def draw(s, b, y):
    t = b[0]
    if t == "h2":
        s.rect(BM, y + 30, BM + 46, y + 36, ORANGE)
        s.text(BM, y + 80, b[1], f(BOLD, 38), NAVY)
    elif t == "h3":
        s.text(BM, y + 46, b[1], f(BOLD, 30), ORANGE)
    elif t == "p":
        s.para(BM, y + 26, b[1], f(REG, BODY), CW, LH, INK)
    elif t in ("bul", "ex"):
        yy = y + 26
        if t == "ex":
            smallcaps(s, BM, yy + 6, "Practice · Mazoezi", 16, ORANGE)
            yy += 56
        for x in b[1]:
            if t == "ex":
                s.d.rounded_rectangle([k(BM), k(yy - 24), k(BM + 24), k(yy)], radius=k(5), outline=NAVY, width=k(2.5))
            else:
                s.d.ellipse([k(BM + 6), k(yy - 16), k(BM + 16), k(yy - 6)], fill=ORANGE)
            yy = s.para(BM + 44, yy, x, f(REG, BODY), CW - 44, LH, INK) + 10
    elif t == "num":
        yy = y + 30
        for i, (a, bb) in enumerate(b[1]):
            s.text(BM, yy, f"{i + 1:02d}", f(BOLD, 22), ORANGE)
            s.text(BM + 60, yy, a, f(BOLD, 26), NAVY)
            yy = s.para(BM + 60, yy + 36, bb, f(REG, 22), CW - 60, 32, GREY) + 18
    elif t == "code":
        code_window(s, y + 14, b[2], file=b[1], lang="Dockerfile" if b[1] == "Dockerfile" else "Python", size=21, lh=34, x0=BM, x1=W - BM - 10)
    elif t == "term":
        terminal(s, y + 14, b[1], title="terminal", size=21, lh=34, x0=BM, x1=W - BM - 10)
    elif t == "table":
        table(s, BM, y + 14, b[1], b[2], b[3], size=22, rh=58)
    elif t == "tip":
        h = measure(b) - 40
        card(s, (BM, y + 14, W - BM - 10, y + 14 + h), r=14)
        s.rect(BM + 2, y + 16, BM + 12, y + 12 + h, ORANGE)
        smallcaps(s, BM + 40, y + 60, b[1], 15, ORANGE)
        s.para(BM + 40, y + 102, b[2], f(MED, 23), CW - 80, 34, NAVY)
    elif t == "area":
        _, n, name, use, libs, proj = b
        h = measure(b) - 24
        card(s, (BM, y + 10, W - BM - 10, y + 10 + h), r=14)
        s.text(BM + 30, y + 58, f"{n:02d}", f(BOLD, 24), ORANGE)
        s.text(BM + 84, y + 58, name, f(BOLD, 30), NAVY)
        yy = s.para(BM + 84, y + 98, use, f(REG, 22), CW - 120, 32, INK)
        s.text(BM + 84, yy + 6, libs, f(MONO, 20), GREY)
        s.text(BM + 84, yy + 44, "First project: " + proj, f(SEMI, 21), ORANGE)


def flow(blocks):
    """Split blocks into pages; a heading never ends a page alone."""
    pages, cur, y = [], [], TOP
    for i, b in enumerate(blocks):
        h = measure(b)
        need = h + (measure(blocks[i + 1]) if b[0] in ("h2", "h3") and i + 1 < len(blocks) else 0)
        if cur and y + need > BOTTOM:
            pages.append(cur)
            cur, y = [], TOP
        cur.append((b, y))
        y += h
    if cur:
        pages.append(cur)
    return pages


FRONT = 5                                   # cover, title, copyright, contents, preface
layout, pno = [], FRONT + 1
for c in CH:
    c["page"] = pno
    body = flow(c["blocks"])
    layout.append((c, body))
    pno += 1 + len(body)
LAST = pno                                  # about the author, then back cover

# ══ page renderers ════════════════════════════════════════════════════════════════════════════════
pages = []


def new_page():
    s = Slide()
    s.im.paste(Image.new("RGB", s.im.size, PAPER_BOOK))
    s.d = ImageDraw.Draw(s.im)
    return s


def frame(s, n, head):
    smallcaps(s, BM, 110, head, 15, ORANGE)
    s.text(W - BM, 110, BOOK, f(MED, 18), GREY, anchor="rs")
    hairline(s, BM, W - BM, 130, RULE)
    hairline(s, BM, W - BM, H - 110, RULE)
    s.text(W / 2, H - 66, str(n), f(SEMI, 20), NAVY, anchor="ms")
    s.text(W - BM, H - 66, "depriver.tech", f(MED, 17), GREY, anchor="rs")


def done(s):
    finish(s, 0.03)
    pages.append(s.im)


def navy_block(s, y1):
    s.rect(0, 0, W, y1, NAVY)


# cover
s = new_page()
navy_block(s, H)
smallcaps(s, BM, 150, "A free guide · Mwongozo wa bure", 18, ORANGE)
s.text(BM - 8, 400, "Python", f(BOLD, 190), WHITE_T)
s.text(BM - 8, 590, "Daily.", f(BOLD, 190), ORANGE)
s.text(BM, 710, SUB, f(SEMI, 40), WHITE_T)
s.text(BM, 810, "Kidogo kidogo, kila siku", f(SIG, 64), SOFT)
swash(s, BM + 8, BM + 600, 838, ORANGE, 7)
s.para(BM, 920, "Six levels, real code, practice and projects, and every area where Python is used.", f(REG, 32), 620, 48, SOFT)
paste_print(s, print_art("python_light", k(540)), 640, 1000, opacity=0.3)
hairline(s, BM, W - BM, H - 230, (38, 60, 100))
s.text(BM, H - 160, AUTHOR, f(BOLD, 40), WHITE_T)
s.text(BM, H - 112, "depriver.tech · @_depriver", f(MED, 24), SOFT)
done(s)

# title page
s = new_page()
s.text(W / 2, 680, "Python Daily", f(BOLD, 110), NAVY, anchor="ms")
s.text(W / 2, 760, SUB, f(SEMI, 40), ORANGE, anchor="ms")
s.text(W / 2, 840, "Kidogo kidogo, kila siku", f(SIG, 48), NAVY, anchor="ms")
s.rect(W / 2 - 40, 880, W / 2 + 40, 884, ORANGE)
s.text(W / 2, 960, AUTHOR, f(SEMI, 34), NAVY, anchor="ms")
s.text(W / 2, H - 200, "depriver.tech", f(MED, 24), GREY, anchor="ms")
done(s)

# copyright
s = new_page()
y = H - 560
for ln, fnt, col in [(f"{BOOK}: {SUB}", f(BOLD, 26), NAVY), (f"© 2026 {AUTHOR}. First edition, October 2026.", f(REG, 22), INK),
                     ("Free to read, print and share with anyone learning. Please don't sell it.", f(REG, 22), INK),
                     ("Python is a trademark of the Python Software Foundation. Other names belong to their owners.", f(REG, 20), GREY),
                     ("Code examples use Python 3.13. Tools and versions change; the ideas don't.", f(REG, 20), GREY),
                     ("Latest version and the companion carousel: depriver.tech/blog/python-roadmap", f(SEMI, 22), NAVY)]:
    y = s.para(BM, y, ln, fnt, CW, 36, col) + 24
done(s)

# contents
s = new_page()
smallcaps(s, BM, 220, "Contents · Yaliyomo", 20, ORANGE)
s.text(BM - 4, 330, "What's inside.", f(BOLD, 76), NAVY)
y = 470
entries = [("Preface", "How I learned Python, and why I wrote this", 5)] + \
          [(f"{i + 1:02d}", c["title"], c["page"]) for i, c in enumerate(CH)] + [("", "About the author", LAST)]
for a, b, p in entries:
    s.text(BM, y, a, f(BOLD, 26), ORANGE)
    s.text(BM + 110, y, b, f(SEMI, 30), NAVY)
    s.text(W - BM, y, str(p), f(SEMI, 28), NAVY, anchor="rs")
    hairline(s, BM, W - BM, y + 26, RULE)
    y += 84
frame(s, 4, "Contents")
done(s)

# preface
s = new_page()
smallcaps(s, BM, 220, "Preface · Utangulizi", 20, ORANGE)
s.text(BM - 4, 330, "How I learned", f(BOLD, 72), NAVY)
s.text(BM - 4, 410, "Python.", f(BOLD, 72), ORANGE)
y = 520
for para in [
    "I learned Python at Mbeya University of Science and Technology (MUST), during my Diploma in Computer Science. Class gave me the basics. "
    "The rest I learned on my own: free online resources, a lot of small projects, and more error messages than I can count.",
    "Nobody handed me a map. I jumped between tutorials, got stuck, started again and slowly figured out what to learn next. Looking back, "
    "I could have saved months with a clear path: what to learn first, what to build at each step and where the language can take you.",
    "Then one of my students asked me for exactly that: a guide from the very beginning to working like a professional. This book is my "
    "answer. It's the roadmap I wish I'd had on my first day.",
    "Read it in order. Type every example. Build every project. Don't worry about being slow; worry only about stopping. "
    "Kidogo kidogo, utafika.",
]:
    y = s.para(BM, y, para, f(REG, 27), CW, 44, INK) + 30
s.text(BM, y + 60, AUTHOR, f(SIG, 56), NAVY)
s.text(BM, y + 110, "Mbeya, October 2026", f(MED, 22), GREY)
frame(s, 5, "Preface")
done(s)

# chapters
for ci, (c, body) in enumerate(layout):
    n = c["page"]
    s = new_page()
    navy_block(s, 980)
    outline_text(s, W - BM + 20, 760, f"{ci + 1:02d}", f(BOLD, 520), stroke=3, color=(60, 84, 128), anchor="rs")
    smallcaps(s, BM, 220, f"Chapter {ci + 1:02d}", 22, ORANGE)
    yy = 380
    words, line, lines = c["title"].split(), "", []
    for w in words:
        trial = (line + " " + w).strip()
        if s.width(trial, f(BOLD, 96)) > CW and line:
            lines.append(line)
            line = w
        else:
            line = trial
    lines.append(line)
    for ln in lines:
        s.text(BM - 6, yy, ln, f(BOLD, 96), WHITE_T)
        yy += 110
    s.text(BM, yy + 30, c["sw"], f(SIG, 62), ORANGE)
    swash(s, BM + 6, BM + min(s.width(c["sw"], f(SIG, 62)) * 0.9, 700), yy + 58, ORANGE, 6, seed=ci)
    s.para(BM, 1100, c["intro"], f(REG, 32), CW, 50, NAVY)
    smallcaps(s, BM, 1440, "In this chapter", 16, GREY)
    heads = [b[1] for b in c["blocks"] if b[0] == "h2"][:6] or [b[2] for b in c["blocks"] if b[0] == "area"][:6]
    chip_row(s, heads, BM, 1470, size=21, maxx=W - BM)
    s.text(W / 2, H - 66, str(n), f(SEMI, 20), NAVY, anchor="ms")
    done(s)
    for j, pg in enumerate(body):
        s = new_page()
        for b, y in pg:
            draw(s, b, y)
        frame(s, n + 1 + j, f"{ci + 1:02d} · {c['label']}")
        done(s)

# about the author
s = new_page()
smallcaps(s, BM, 220, "About the author", 20, ORANGE)
s.text(BM - 4, 330, AUTHOR, f(BOLD, 72), NAVY)
s.text(BM, 400, "Software Engineer & Digital Innovator", f(SEMI, 30), ORANGE)
y = 500
for para in [
    "Privatus Cosmas, known online as depriver, is from Kitwe village in Kyerwa District, Kagera, Tanzania. He studied a Diploma in Computer "
    "Science at Mbeya University of Science and Technology (MUST).",
    "He works as a Software Engineer and Digital Innovator at Rohi Company Limited, and shares practical tech lessons for students in "
    "Swahili and English at depriver.tech.",
]:
    y = s.para(BM, y, para, f(REG, 27), CW, 44, INK) + 30
smallcaps(s, BM, y + 40, "Say hello · Karibu", 16, ORANGE)
for i, (a, b) in enumerate([("Website", "depriver.tech"), ("Instagram & more", "@_depriver"),
                            ("This book online", "depriver.tech/blog/python-roadmap")]):
    s.text(BM, y + 100 + i * 60, a, f(MED, 24), GREY)
    s.text(BM + 300, y + 100 + i * 60, b, f(SEMI, 26), NAVY)
frame(s, LAST, "About the author")
done(s)

# back cover
s = new_page()
navy_block(s, H)
s.text(BM, 420, "Start today.", f(BOLD, 110), WHITE_T)
s.text(BM, 540, "Finish what you start.", f(BOLD, 64), ORANGE)
s.text(BM, 640, "Maliza unachoanza", f(SIG, 60), SOFT)
y = 760
for a, b, _, _ in LEVELS:
    pass
for lab, name, when, focus in LEVELS:
    s.text(BM, y, f"{lab} · {name}", f(SEMI, 30), WHITE_T)
    s.text(W - BM, y, when, f(MED, 26), SOFT, anchor="rs")
    hairline(s, BM, W - BM, y + 24, (38, 60, 100))
    y += 74
paste_print(s, print_art("python_light", k(300)), W - BM - 300, H - 520, opacity=0.3)
s.text(BM, H - 160, AUTHOR, f(BOLD, 34), WHITE_T)
s.text(BM, H - 112, "depriver.tech · @_depriver", f(MED, 24), SOFT)
done(s)

# export: page JPEGs (for checking) + one PDF at 150 dpi
for old in os.listdir(OUT):
    os.remove(os.path.join(OUT, old))
small = []
for i, im in enumerate(pages):
    im.save(f"{OUT}page-{i + 1:02d}.jpg", quality=92)
    small.append(im.resize((W, H), Image.LANCZOS).convert("RGB"))
pdf = f"{OUT}python-daily.pdf"
small[0].save(pdf, save_all=True, append_images=small[1:], resolution=150, quality=72)
print(f"ok {len(pages)} pages -> {pdf}")
