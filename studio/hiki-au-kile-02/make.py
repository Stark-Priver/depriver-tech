"""Hiki au Kile #02: first career moves. Content only: layout is studio/hiki-au-kile/template.py.
New episode: copy this folder to hiki-au-kile-NN, change EP, run `npm run carousel -- hiki-au-kile-NN`."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 2,
    'theme': 'Career',
    'theme_sw': 'Mjadala wa kazi',
    'rounds': [   {   'a': 'Freelance',
        'a_pts': ['Choose your clients', 'Fast real experience'],
        'b': 'First job',
        'b_pts': ['Mentors and code review', 'Steady pay, structure'],
        'note': 'Freelance on the side is a great way to start too.',
        'pick': 1,
        'reason': 'First job, if you can get one. You learn faster with seniors around you.',
        'sw': 'Jifunze kwa wakubwa'},
    {   'a': 'Startup',
        'a_pts': ['You do a bit of everything', 'Fast growth'],
        'b': 'Big company',
        'b_pts': ['Clear process and training', 'Stable and structured'],
        'note': 'Choose the team and the mentor, not the logo.',
        'pick': None,
        'reason': 'Startups teach you speed. Big companies teach you process. Both are good first homes.',
        'sw': 'Timu ni muhimu'},
    {   'a': 'Frontend',
        'a_pts': ['See your work right away', 'Design meets code'],
        'b': 'Backend',
        'b_pts': ['Logic, data, security', 'Powers every app'],
        'note': 'Full-stack starts with being good at one side.',
        'pick': None,
        'reason': 'Try both for a month. Most people feel which one is theirs.',
        'sw': 'Jaribu zote mbili'},
    {   'a': 'Remote',
        'a_pts': ['Earn from anywhere', 'No daladala every day'],
        'b': 'Office',
        'b_pts': ['Learn by sitting near seniors', 'Easier to ask quick questions'],
        'note': 'Remote job offers that ask you to pay are scams.',
        'pick': 1,
        'reason': "Office first, at least for your first year. Remote is easier once you're independent.",
        'sw': 'Ofisi kwanza'},
    {   'a': 'Specialist',
        'a_pts': ['Deep in one thing', 'Known for it'],
        'b': 'Generalist',
        'b_pts': ['Many skills, flexible', 'Great for small teams'],
        'note': 'Early on, go wide. Then pick your depth.',
        'pick': None,
        'reason': 'Be T-shaped: deep in one skill, comfortable with the rest.',
        'sw': 'Kina kimoja, upana mwingi'}],
}

exec(open(os.path.join(STUDIO, "hiki-au-kile", "template.py")).read())
