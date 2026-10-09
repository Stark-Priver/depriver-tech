"""Shared content for the Python roadmap carousel (studio/python-roadmap) and its PDF guide (studio/python-roadmap-guide)."""

# (area, what it's for, libraries, a first project)
AREAS = [
    ("Web backends", "Websites, APIs, admin panels and logins", "Django · FastAPI · Flask", "A school results API"),
    ("Data analysis", "Turn spreadsheets and records into answers", "pandas · NumPy · Jupyter", "Analyse a shop's sales CSV"),
    ("Machine learning", "Models that predict, sort and recommend", "scikit-learn · PyTorch · TensorFlow", "Predict house prices"),
    ("AI apps & LLMs", "Chatbots, assistants and AI features in apps", "LLM APIs · Hugging Face · LangChain", "A Swahili FAQ chatbot"),
    ("Automation", "Scripts that do boring work for you", "pathlib · openpyxl · schedule", "Auto-build a weekly Excel report"),
    ("Web scraping", "Collect data from websites", "requests · BeautifulSoup · Scrapy", "Track new job posts every day"),
    ("Data visualisation", "Charts, reports and dashboards", "Matplotlib · Plotly · Streamlit", "A live sales dashboard"),
    ("Computer vision", "Teach computers to see images and video", "OpenCV · Ultralytics YOLO", "Count cars at a junction"),
    ("NLP & language", "Understand text and speech", "spaCy · NLTK · Transformers", "Sort customer messages by topic"),
    ("Cybersecurity", "Security tools, testing and analysis", "Scapy · Impacket · pwntools", "A simple port scanner"),
    ("DevOps & cloud", "Automate servers, deploys and the cloud", "Ansible · boto3 · Fabric", "Auto-backup files to the cloud"),
    ("Testing & QA", "Check that software really works", "pytest · Selenium · Playwright", "Test a login page automatically"),
    ("Bots", "Telegram, Discord and chat bots", "python-telegram-bot · discord.py", "A class reminder bot"),
    ("Desktop apps", "Apps for Windows, Mac and Linux", "Tkinter · PyQt", "A shop stock manager"),
    ("Games", "2D games and quick prototypes", "Pygame · Arcade", "A Snake game"),
    ("IoT & hardware", "Raspberry Pi, sensors and robots", "MicroPython · GPIO Zero", "A temperature alarm"),
    ("Science & research", "Biology, physics, health and space", "SciPy · Biopython · Astropy", "Analyse lab results"),
    ("Finance & fintech", "Analysis, risk and reporting", "pandas · NumPy · QuantLib", "Track your M-Pesa spending"),
    ("GIS & maps", "Maps and location data", "GeoPandas · Folium", "Map clinics in your region"),
    ("Education", "The first language in many schools", "Jupyter · turtle", "Teach a friend to code"),
]

# (level, name, when, focus)
LEVELS = [
    ("Level 0", "Set up", "Day 1", "Install Python and VS Code, run your first file"),
    ("Level 1", "Basics", "Weeks 1–6", "Variables, conditions, loops, functions, data structures"),
    ("Level 2", "Intermediate", "Months 2–3", "Modules, pip, classes, files, APIs, Git"),
    ("Level 3", "Advanced", "Months 4–6", "Testing, typing, clean code, databases"),
    ("Level 4", "Specialise", "Months 6–9", "Pick one area and go deep"),
    ("Level 5", "Professional", "Month 9+", "Real projects, teamwork, deploys, interviews"),
]

# (path, learn in order, first serious project)
PATHS = [
    ("Backend", "Django or FastAPI, SQL, auth, deploy", "A booking API with logins"),
    ("Data analyst", "pandas, SQL, charts, storytelling", "A sales report with insights"),
    ("ML / AI", "NumPy, pandas, scikit-learn, PyTorch", "A model that predicts prices"),
    ("Automation", "files, Excel, web, scheduling", "A daily report robot"),
    ("Cybersecurity", "networking, sockets, Scapy, CTFs", "A network scanner"),
    ("DevOps", "Linux, scripts, Docker, CI/CD, cloud", "An auto-deploy pipeline"),
]

# (name, what it is)
RESOURCES = [
    ("CS50's Python course (CS50P)", "Harvard's free course, with problem sets"),
    ("The python.org tutorial", "The official, free tutorial"),
    ("Automate the Boring Stuff", "Free to read online; perfect for automation"),
    ("Exercism Python track", "Free exercises with mentor feedback"),
    ("Kaggle Learn", "Free short courses on pandas and ML"),
    ("Real Python", "Clear tutorials on almost every topic"),
]

# Python logo illustration (print style), used by both the carousel and the book; needs kit.py loaded first.
ART.update({
    "python": svg(GROUND + f'''
      <path d="M300 60 c-80 0 -100 30 -100 60 v40 h104 v14 H150 c-40 0 -70 30 -70 90 s26 92 66 92 h34 v-50 c0 -36 30 -66 66 -66 h104
               c30 0 54 -24 54 -54 V120 c0 -30 -30 -60 -108 -60z" fill="#0b1e3f" {ST}/>
      <path d="M300 370 c80 0 100 -30 100 -60 v-40 H296 v-14 h154 c40 0 70 -30 70 -90 s-26 -92 -66 -92 h-34 v50 c0 36 -30 66 -66 66
               H250 c-30 0 -54 24 -54 54 v66 c0 30 30 60 104 60z" fill="#e8603a" {ST}/>
      <circle cx="252" cy="104" r="12" fill="#fff"/><circle cx="348" cy="326" r="12" fill="#fff"/>'''),
})
ART["python_light"] = ART["python"].replace('fill="#0b1e3f" stroke="#0b1e3f"', 'fill="#a9c4f5" stroke="#0b1e3f"', 1)
