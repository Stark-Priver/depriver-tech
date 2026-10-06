"""Swali la Wiki #01: can I learn to code with only a phone? Content only: layout is studio/swali-la-wiki/template.py.
New episode: copy this folder to swali-la-wiki-NN, change EP, run `npm run carousel -- swali-la-wiki-NN`."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    "num": 1,
    "question": "Naweza kujifunza coding kwa simu tu?",
    "question_en": "Can I learn to code with only a phone?",
    "source": "Swali linaloulizwa mara nyingi · A question students ask a lot",
    "short": "Ndiyo, lakini...",
    "short_en": "Yes, you can start on a phone. But plan to move to a computer for real projects.",
    "one_line": "Start on your phone today. Don't wait for a laptop.",
    "sw": "Simu inatosha kuanza",
    "how_title": ("Your phone", "is a classroom."),
    "steps": [("Learn the basics in the browser", "freeCodeCamp and W3Schools work on mobile."),
              ("Write real code on the phone", "Pydroid 3 for Python, Acode for HTML, CSS and JS."),
              ("Practise a little every day", "Sololearn-style lessons on the daladala count."),
              ("Use campus or cyber café computers", "For bigger projects, Git and your CV portfolio.")],
    "how_tip": "Save lessons on Wi-Fi so your bundle lasts longer.",
    "careful": [("Small screen, slow typing", "Fine for learning, hard for big projects."),
                ("Some tools need a computer", "Android Studio, Docker, most IDEs."),
                ("Jobs expect a laptop", "Save a little each month toward one.")],
    "next_step": "Install Pydroid 3 or Acode, write a program that prints your name and age, then post a screenshot.",
}
exec(open(os.path.join(STUDIO, "swali-la-wiki", "template.py")).read())
