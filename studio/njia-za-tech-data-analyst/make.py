"""Njia za Tech #03: data analyst. Content only: layout is studio/njia-za-tech/template.py."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 3,
    'slug': 'njia-za-tech-data-analyst',
    'role': 'Data Analyst',
    'role_sw': 'Mchambuzi wa data',
    'initials': 'DA',
    'sw': 'Namba zinasema ukweli',
    'cover_line': "They turn messy numbers into clear answers: what's selling, who's leaving, and what to do next.",
    'one_line': 'They answer business questions with data and charts.',
    'what': ('A manager asks “why did sales drop in Mwanza?”. The data analyst pulls the data, cleans it, finds the pattern and explains it '
 'in a simple chart.'),
    'duties': ['Clean and organise messy data', 'Find patterns and answer questions', 'Present results in charts and reports'],
    'analogy': 'A doctor reading test results: the numbers are there, the analyst explains what they mean and what to do.',
    'day': [   ('08:30', 'Check the daily sales dashboard'),
    ('09:30', "Write SQL to pull last month's numbers"),
    ('11:30', 'Clean the data in Excel or Python'),
    ('14:00', "Build charts that answer the manager's question"),
    ('16:00', 'Present the findings in five slides')],
    'tools': [   ('Start here', ['Excel / Google Sheets', 'SQL']),
    ('Next', ['Power BI', 'Python (pandas)', 'Looker Studio']),
    ('Skills', ['Statistics basics', 'Clear charts', 'Explaining simply'])],
    'like': ['Asking “why?” about everything', 'Puzzles hidden in numbers', 'Explaining things to non-tech people'],
    'not_for': ['You hate spreadsheets', "You don't enjoy presenting your findings"],
    'steps': [   ('Master Excel', 'Formulas, pivot tables, charts.'),
    ('Learn SQL', 'SELECT, WHERE, GROUP BY, JOIN.'),
    ('Learn one dashboard tool', 'Power BI or Looker Studio, both have free versions.'),
    ('Analyse public data', 'NBS or open datasets, then write what you found.')],
    'first_project': "Analyse a shop's sales sheet and show the best day, product and month.",
    'where': [   'Banks and microfinance',
    'Telecoms',
    'NGOs and research projects',
    'Health programmes',
    'Government and statistics',
    'Retail and FMCG'],
    'where_note': 'Pay depends on skill, sector and city. Ask people who do the job.',
    'question': ('Is data', 'your path?'),
}

exec(open(os.path.join(STUDIO, "njia-za-tech", "template.py")).read())
