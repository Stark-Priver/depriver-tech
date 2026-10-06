"""Njia za Tech #09: product manager. Content only: layout is studio/njia-za-tech/template.py."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 9,
    'slug': 'njia-za-tech-product-manager',
    'role': 'Product Manager',
    'role_sw': 'Msimamizi wa bidhaa',
    'initials': 'PM',
    'sw': 'Kujenga kitu sahihi',
    'cover_line': 'They decide what to build next and why, so the team builds the right thing for real users.',
    'one_line': 'They decide what to build, for whom, and why.',
    'what': ('They listen to users and the business, choose the most important problem, write what to build and keep designers, developers '
 'and managers aligned.'),
    'duties': ['Talk to users and understand problems', 'Decide priorities and write specs', 'Keep the whole team aligned'],
    'analogy': "The captain of a football team: doesn't play every position, but makes sure everyone runs towards the same goal.",
    'day': [   ('09:00', 'Call two customers about a complaint'),
    ('10:30', 'Prioritise next sprint with the team'),
    ('12:00', 'Write the spec for a new feature'),
    ('14:30', 'Review the designs with the designer'),
    ('16:00', "Check last week's numbers: did it work?")],
    'tools': [   ('Tools', ['Notion / Docs', 'Jira / Trello', 'Figma (viewing)', 'Spreadsheets']),
    ('Skills', ['User interviews', 'Writing clearly', 'Prioritising', 'Basic data']),
    ('Helps a lot', ['Some coding or design experience'])],
    'like': ['Talking to people and solving their problems', 'Seeing the big picture', 'Writing and organising'],
    'not_for': ['You want to code all day', 'You avoid hard decisions'],
    'steps': [   ('Start in any tech role', 'Most PMs were developers, designers or support first.'),
    ('Learn to interview users', 'Ask about problems, not features.'),
    ('Write a spec for a real app', 'Problem, users, solution, how to measure.'),
    ('Run a small project', 'A student club app, start to finish.')],
    'first_project': "Pick a local app, interview 5 users, write the one feature you'd build and why.",
    'where': ['Fintech and banks', 'Telecoms', 'Startups', 'Software houses', 'NGO tech projects', 'Remote product teams'],
    'where_note': 'Usually not a first job. Pay depends on experience. Ask people who do it.',
    'question': ('Is product', 'your path?'),
}

exec(open(os.path.join(STUDIO, "njia-za-tech", "template.py")).read())
