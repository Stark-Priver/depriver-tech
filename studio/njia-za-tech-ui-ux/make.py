"""Njia za Tech #05: ui/ux designer. Content only: layout is studio/njia-za-tech/template.py."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 5,
    'slug': 'njia-za-tech-ui-ux',
    'role': 'UI/UX Designer',
    'role_sw': 'Msanifu wa matumizi',
    'initials': 'UX',
    'sw': 'Rahisi kutumia ndiyo nzuri',
    'cover_line': 'They decide how an app looks and how easy it is to use, before anyone writes code.',
    'one_line': 'They make apps easy, clear and pleasant to use.',
    'what': ('They talk to users, find what confuses them, sketch the screens and test the flow. UX is how it works for people, UI is how it '
 'looks.'),
    'duties': ['Research what users need', 'Design screens and user flows', 'Test designs with real people'],
    'analogy': 'An architect: plans where the doors and stairs go so people move easily, long before the builders arrive.',
    'day': [   ('09:00', 'Interview two users about the payment flow'),
    ('10:30', 'Sketch three ideas on paper'),
    ('12:00', 'Build the best one in Figma'),
    ('14:30', 'Test the prototype with a user'),
    ('16:00', 'Hand the design to the developers')],
    'tools': [   ('Design', ['Figma', 'Paper and pen', 'FigJam']),
    ('Skills', ['User research', 'Wireframes', 'Prototyping', 'Typography']),
    ('Good to know', ['HTML & CSS basics', 'Accessibility', 'Design systems'])],
    'like': ['Watching how people really use things', 'Visual design and clear layouts', 'Taking feedback without getting hurt'],
    'not_for': ['You want to design only for yourself', 'You hate changing your work after feedback'],
    'steps': [   ('Learn the basics', 'Layout, spacing, colour and type.'),
    ('Learn Figma (free)', 'Copy three good apps screen by screen.'),
    ('Redesign a local app', 'Pick a confusing one, fix the flow, explain why.'),
    ('Show the process', 'Case studies on Behance or your site.')],
    'first_project': 'Redesign a confusing form (e.g. a school registration form) and test it with 3 friends.',
    'where': ['Software houses and agencies', 'Banks and fintech', 'Startups', 'Telecoms', 'Freelance clients', 'Remote product teams'],
    'where_note': 'Pay depends on portfolio and company. Ask people who do the job.',
    'question': ('Is design', 'your path?'),
}

exec(open(os.path.join(STUDIO, "njia-za-tech", "template.py")).read())
