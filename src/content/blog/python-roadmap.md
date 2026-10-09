---
title: "Python from beginner to professional: the full roadmap (+ free book, Python Daily)"
description: "Six levels from setup to professional, with real code at each step, every area where Python is used, specialisation paths, projects per level, free resources, and a free 43-page book to download."
date: 2026-10-14T19:00:00+03:00
status: live
tags: ["python", "beginners", "roadmap", "kiswahili"]
carousel: python-roadmap
slides:
  - "Python: beginner to professional. Six levels, real code, every area Python is used in, and a free book. Ramani kamili, hatua kwa hatua."
  - "Why start with Python? It reads almost like English, one language opens many careers, and the community is huge and free."
  - "Six levels, one at a time: set up (day 1), basics (weeks 1–6), intermediate (months 2–3), advanced (months 4–6), specialise (months 6–9), professional (month 9+)."
  - "Level 0 · Set up in one evening: install Python from python.org (tick Add to PATH on Windows), VS Code with the Python extension, run your first file. Phone only? Start on Colab or Replit."
  - "Level 1 · The basics, logic: variables, types, input and print, if/elif/else, loops, functions."
  - "Level 1 · The basics, data structures: lists, dicts, tuples and sets. Then errors with try/except, and files."
  - "Level 2 · Use other people's code: modules, pip, virtual environments, classes, JSON and CSV, APIs, Git and GitHub."
  - "Level 3 · Write code others can trust: type hints, pytest, PEP 8 and ruff, decorators, generators, SQL with sqlite3, async basics."
  - "Where Python is used (1/2): web backends, data analysis, machine learning, AI apps, automation, web scraping, data visualisation, computer vision, NLP, cybersecurity."
  - "Where Python is used (2/2): DevOps and cloud, testing and QA, bots, desktop apps, games, IoT and hardware, science, finance, GIS and maps, education."
  - "Level 4 · Pick one path and go deep: backend, data analyst, ML/AI, automation, cybersecurity or DevOps."
  - "Level 5 · Work like a professional: Git every day, tests and reviews, Docker and deploys, docs, interview practice, real users."
  - "One project per level: grade calculator, weather app, expense tracker with tests, a serious project in your path, then something real people use."
  - "Learn it for free: CS50P, the python.org tutorial, Automate the Boring Stuff, Exercism, Kaggle Learn, Real Python."
  - "Habits that get you there: code daily, read the error, build before you feel ready, use AI as a tutor, learn in public."
  - "Your turn: which level are you on right now? Download the free book, Python Daily."
---

One of my students asked me for a guide to Python "from the very beginning to working like a professional". So I made two things: this roadmap, and a free book that goes much deeper. *Ramani kamili, hatua kwa hatua.*

## 📘 Free book: Python Daily

**[Download Python Daily (PDF, 43 pages)](/guides/python-daily.pdf)**: every level in detail, with explanations, real code, practice exercises and a project per level, all 20 areas where Python is used, a 12-month plan, free resources and a glossary. Free to read, print and share. Please don't sell it.

## Why Python?

Python reads almost like English, so you spend your energy on logic, not symbols. One language opens many careers, and its community is huge: almost every error you meet, someone has already solved online.

## The six levels

| Level | Name | Rough time | Focus |
|---|---|---|---|
| 0 | Set up | Day 1 | Install Python and VS Code, run your first file |
| 1 | Basics | Weeks 1–6 | Variables, conditions, loops, functions, data structures |
| 2 | Intermediate | Months 2–3 | Modules, pip, classes, files, APIs, Git |
| 3 | Advanced | Months 4–6 | Testing, typing, clean code, databases |
| 4 | Specialise | Months 6–9 | One area, in depth |
| 5 | Professional | Month 9+ | Real projects, teamwork, deploys, interviews |

The times assume one to two hours a day. Slower is fine; stopping isn't. *Polepole ndio mwendo.*

### Level 0: Set up

Install Python from python.org (on Windows, tick **"Add python.exe to PATH"**), then VS Code with the Python extension. Run your first file with `python hello.py`. Only have a phone? Start in the browser with Google Colab or Replit.

### Level 1: The basics

Variables and types, `input()` and `print()`, `if / elif / else`, `for` and `while` loops, functions, then lists, dictionaries, tuples and sets, errors with `try / except`, and reading and writing files.

```python
marks = [78, 45, 90, 62]
for m in marks:
    if m >= 50:
        print(m, "Pass")
    else:
        print(m, "Fail")
```

**Build:** a grade calculator.

### Level 2: Intermediate

Modules and the standard library, `pip` and virtual environments, classes, comprehensions, JSON and CSV, calling APIs with `requests`, and Git and GitHub from now on, every day.

**Build:** a weather app using a free API.

### Level 3: Advanced

Type hints, testing with `pytest`, clean code (PEP 8, `ruff`), decorators and generators, SQL with `sqlite3`, and a first look at `async`.

```python
def average(marks: list[float]) -> float:
    return sum(marks) / len(marks)

def test_average():
    assert average([50, 100]) == 75
```

**Build:** an expense tracker with SQLite and tests.

## Where Python is used

1. **Web backends:** Django, FastAPI, Flask
2. **Data analysis:** pandas, NumPy, Jupyter
3. **Machine learning:** scikit-learn, PyTorch, TensorFlow
4. **AI apps and LLMs:** LLM APIs, Hugging Face, LangChain
5. **Automation:** pathlib, openpyxl, schedule
6. **Web scraping:** requests, BeautifulSoup, Scrapy
7. **Data visualisation:** Matplotlib, Plotly, Streamlit
8. **Computer vision:** OpenCV, Ultralytics YOLO
9. **NLP and language:** spaCy, NLTK, Transformers
10. **Cybersecurity:** Scapy, Impacket, pwntools
11. **DevOps and cloud:** Ansible, boto3, Fabric
12. **Testing and QA:** pytest, Selenium, Playwright
13. **Bots:** python-telegram-bot, discord.py
14. **Desktop apps:** Tkinter, PyQt
15. **Games:** Pygame, Arcade
16. **IoT and hardware:** MicroPython, GPIO Zero
17. **Science and research:** SciPy, Biopython, Astropy
18. **Finance and fintech:** pandas, NumPy, QuantLib
19. **GIS and maps:** GeoPandas, Folium
20. **Education:** Jupyter, turtle

Python Daily gives each area a short explanation and a first project.

## Level 4: Specialise

Pick one path and go deep. One path for six months beats six paths for one month.

- **Backend:** Django or FastAPI, SQL, authentication, deploys.
- **Data analyst:** pandas, SQL, charts, storytelling with data.
- **ML / AI:** NumPy, pandas, scikit-learn, PyTorch.
- **Automation:** files, Excel, the web, scheduling.
- **Cybersecurity:** networking, sockets, Scapy, CTFs.
- **DevOps:** Linux, scripting, Docker, CI/CD, the cloud.

## Level 5: Professional

Git every day, tests and code reviews, Docker and deploys, documentation, problem-solving practice for interviews, and real users through freelancing, open source or a team project. Professional means reliable, not knowing everything.

## Free resources

CS50's Python course (CS50P), the official python.org tutorial, *Automate the Boring Stuff with Python* (free online), Exercism's Python track, Kaggle Learn and Real Python.

## Habits that get you there

Code a little every day. Read the error message, bottom line first. Build before you feel ready. Use AI as a tutor, not a copy machine. Learn in public. And don't jump to Django or AI before the basics. *Usiruke hatua.*

**Which level are you on right now, and which area excites you most?** Tell me in the comments. And share Python Daily with someone who's starting.
