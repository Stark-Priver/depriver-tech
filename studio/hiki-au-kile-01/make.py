"""Hiki au Kile #01: learning to code. Content only: layout is studio/hiki-au-kile/template.py.
New episode: copy this folder to hiki-au-kile-NN, change EP, run `npm run carousel -- hiki-au-kile-NN`."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 1,
    'theme': 'Learning',
    'theme_sw': 'Mjadala wa kujifunza',
    'rounds': [   {   'a': 'Python',
        'a_pts': ['Reads almost like English', 'Data, AI and automation'],
        'b': 'JavaScript',
        'b_pts': ['Runs in every browser', 'Websites, front to back'],
        'note': 'Switching later is easy. Not starting is the real mistake.',
        'pick': None,
        'reason': 'Both are great first languages. Websites? JavaScript. Data or automation? Python.',
        'sw': 'Chagua moja, anza leo'},
    {   'a': 'Laptop',
        'a_pts': ['Real projects, Git, IDEs', 'What jobs expect'],
        'b': 'Phone',
        'b_pts': ['You already have it', 'Learn basics anywhere'],
        'note': 'Campus labs and cyber cafés count as a laptop.',
        'pick': 0,
        'reason': "A laptop for real work. But don't wait for one: start on the phone today.",
        'sw': 'Usisubiri, anza'},
    {   'a': 'YouTube',
        'a_pts': ['Easy to follow', 'Great for first steps'],
        'b': 'Docs',
        'b_pts': ['Always up to date', 'Where real answers live'],
        'note': 'Video eats your bundle. Docs are almost free.',
        'pick': 1,
        'reason': 'Start with videos, grow with docs. Reading docs is a job skill.',
        'sw': 'Soma docs'},
    {   'a': 'Tutorials',
        'a_pts': ['Clear steps, quick wins', 'Good for basics'],
        'b': 'Projects',
        'b_pts': ['You learn to solve problems', 'Something to show'],
        'note': 'Stuck in “tutorial hell”? Build something small and ugly.',
        'pick': 1,
        'reason': 'Build projects. Tutorials only teach you to copy.',
        'sw': 'Jenga, usinakili tu'},
    {   'a': 'Certificate',
        'a_pts': ['Looks good on paper', 'Some HR filters ask'],
        'b': 'Portfolio',
        'b_pts': ['Proof you can build', 'Recruiters click the link'],
        'note': 'Free certificates are a bonus, not the main course.',
        'pick': 1,
        'reason': 'Portfolio. A link to working projects beats a certificate.',
        'sw': 'Onyesha, usiseme tu'}],
}

exec(open(os.path.join(STUDIO, "hiki-au-kile", "template.py")).read())
