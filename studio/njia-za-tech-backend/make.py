"""Njia za Tech #01: backend developer. Content only: layout is studio/njia-za-tech/template.py.
New episode: copy this folder to njia-za-tech-<role>, change EP, run `npm run carousel -- njia-za-tech-<role>`."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    "num": 1, "slug": "njia-za-tech-backend",
    "role": "Backend Developer", "role_sw": "Mjenzi wa mifumo ya nyuma", "initials": "BE",
    "sw": "Jikoni ndiko kazi ilipo",
    "cover_line": "They build the part of an app you never see: the logic, the data and the security behind every button.",
    "what": "When you tap “Lipa” in an app, the backend checks who you are, saves the order, talks to the payment provider and sends the answer back.",
    "one_line": "The engine behind the screen: logic, data and security.",
    "duties": ["Build APIs the app talks to", "Design and protect the database", "Keep the system fast and safe"],
    "analogy": "A restaurant: the frontend is the dining room and the menu. The backend is the kitchen, the store and the cashier's book.",
    "day": [("08:30", "Stand-up: 15 minutes with the team on today's tasks"), ("09:00", "Build a new API endpoint for a feature"),
            ("11:30", "Review a teammate's pull request"), ("14:00", "Fix a bug a user reported from the logs"),
            ("16:00", "Write tests, then deploy to staging")],
    "tools": [("Languages · pick one", ["Python", "PHP", "JavaScript (Node)", "Java", "Go"]),
              ("Frameworks", ["Django", "Laravel", "Express", "Spring"]),
              ("Every day", ["SQL & PostgreSQL", "Git", "APIs / JSON", "Linux terminal"])],
    "like": ["Solving puzzles and making logic work", "Data, rules and how things connect", "Building things that must never break"],
    "not_for": ["You only enjoy visual design", "You hate reading error messages"],
    "steps": [("Learn one language well", "Python or PHP, the basics until loops feel easy."),
              ("Learn SQL", "Tables, SELECT, JOIN. Every backend uses data."),
              ("Build a small API", "A to-do or a shop: create, read, update, delete."),
              ("Add login and deploy it", "Then put the link on your CV and GitHub.")],
    "first_project": "A shop stock API: products, sales and a daily total.",
    "where": ["Banks and mobile money", "Telecom companies", "Startups and software houses", "Government systems",
              "NGOs and health projects", "Freelance and remote"],
    "where_note": "Pay depends on skill, company and city. Ask people who do the job.",
    "question": ("Is backend", "your path?"),
}
exec(open(os.path.join(STUDIO, "njia-za-tech", "template.py")).read())
