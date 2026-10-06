"""Hiki au Kile #03: tools and tech. Content only: layout is studio/hiki-au-kile/template.py.
New episode: copy this folder to hiki-au-kile-NN, change EP, run `npm run carousel -- hiki-au-kile-NN`."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 3,
    'theme': 'Tools',
    'theme_sw': 'Mjadala wa zana',
    'rounds': [   {   'a': 'SQL',
        'a_pts': ['Tables, relations, rules', 'Banks, schools, shops'],
        'b': 'NoSQL',
        'b_pts': ['Flexible documents', 'Fast to start'],
        'note': 'MongoDB and Firebase are worth learning after.',
        'pick': 0,
        'reason': 'Learn SQL first. Most real business data lives in tables.',
        'sw': 'SQL kwanza'},
    {   'a': 'Flutter',
        'a_pts': ['One code for Android + iOS', 'Smooth by default'],
        'b': 'React Native',
        'b_pts': ['Uses JavaScript', 'Big web community'],
        'note': 'Your first app matters more than the framework.',
        'pick': None,
        'reason': 'Know JavaScript already? React Native. Starting fresh? Flutter is very friendly.',
        'sw': 'App ya kwanza ni muhimu'},
    {   'a': 'Laravel',
        'a_pts': ['PHP, very popular in TZ', 'Cheap shared hosting'],
        'b': 'Django',
        'b_pts': ['Python, batteries included', 'Great admin panel'],
        'note': 'Pick the one your local job ads ask for.',
        'pick': None,
        'reason': 'Laravel if you know PHP, Django if you know Python. Both power real products.',
        'sw': 'Angalia soko'},
    {   'a': 'Windows',
        'a_pts': ['Familiar, on most laptops', 'Office and games'],
        'b': 'Linux',
        'b_pts': ['What servers run', 'Light on old laptops'],
        'note': 'No need to delete Windows. Dual-boot or WSL.',
        'pick': 1,
        'reason': 'Learn Linux. Servers run it. WSL lets you try it inside Windows.',
        'sw': 'Jifunze terminal'},
    {   'a': 'Cloud (AWS…)',
        'a_pts': ['Scales to millions', 'Many managed services'],
        'b': 'A simple VPS',
        'b_pts': ['Cheap, predictable bill', 'You learn how servers work'],
        'note': 'Cloud free tiers can bill you. Set a budget alert.',
        'pick': 1,
        'reason': 'A simple VPS for your first projects. You learn more and pay less.',
        'sw': 'Anza kidogo'}],
}

exec(open(os.path.join(STUDIO, "hiki-au-kile", "template.py")).read())
