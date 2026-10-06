"""Njia za Tech #02: frontend developer. Content only: layout is studio/njia-za-tech/template.py."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 2,
    'slug': 'njia-za-tech-frontend',
    'role': 'Frontend Developer',
    'role_sw': 'Mjenzi wa sehemu unayoiona',
    'initials': 'FE',
    'sw': 'Unachokiona ni kazi yao',
    'cover_line': 'They build everything you see and touch in a website or web app: the screens, the buttons and how it feels.',
    'one_line': 'They turn designs into screens that work on every phone.',
    'what': ('A designer draws the screen. The frontend developer turns it into real code that loads fast, works on a cheap phone and talks '
 'to the backend.'),
    'duties': ['Turn designs into working pages', 'Make it work on every screen size', 'Connect the screens to the API'],
    'analogy': "A shop: the frontend is the shelves, the lights and the counter. If customers can't find things, they leave.",
    'day': [   ('08:30', 'Stand-up with the team'),
    ('09:00', 'Build the new checkout screen from the design'),
    ('12:00', 'Test it on a small Android phone and fix the layout'),
    ('14:30', 'Connect the form to the backend API'),
    ('16:30', 'Pull request, review, fix comments')],
    'tools': [   ('The base · learn first', ['HTML', 'CSS', 'JavaScript']),
    ('Frameworks', ['React', 'Vue', 'Tailwind CSS', 'Next.js']),
    ('Every day', ['Browser DevTools', 'Git', 'Figma (reading designs)', 'APIs / JSON'])],
    'like': [   'Seeing your work on the screen right away',
    'Details: spacing, colours, smooth clicks',
    'Thinking about how real people use things'],
    'not_for': ['You never want to touch design', 'Small visual details annoy you'],
    'steps': [   ('HTML and CSS first', 'Build three static pages from scratch.'),
    ('Then JavaScript', 'Make buttons, forms and lists react.'),
    ("Copy a real site's layout", 'A bank or school homepage, for practice only.'),
    ('Learn one framework', 'React or Vue, then deploy free.')],
    'first_project': 'A restaurant menu site that works perfectly on a TZS 150k phone.',
    'where': ['Software houses and agencies', 'Banks and fintech', 'Startups', 'Media and e-commerce', 'Freelance websites', 'Remote teams'],
    'where_note': 'Pay depends on skill, company and city. Ask people who do the job.',
    'question': ('Is frontend', 'your path?'),
}

exec(open(os.path.join(STUDIO, "njia-za-tech", "template.py")).read())
