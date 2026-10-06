"""Code ya Wiki #04: the if that is always true. Content only: layout is studio/code-ya-wiki/template.py.
New episode: copy this folder to code-ya-wiki-NN, change EP, run `npm run carousel -- code-ya-wiki-NN`."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 4,
    'lang': 'Python',
    'file': 'karibu.py',
    'question': 'Kwa nini kila mtu anakaribishwa?',
    'goal': 'welcome only Asha and Juma to the admin page.',
    'code': [   'name = input("Jina lako: ")',
    '',
    'if name == "Asha" or "Juma":',
    '    print("Karibu admin!")',
    'else:',
    '    print("Huna ruhusa.")'],
    'bug_lines': [2],
    'expected': 'Huna ruhusa. (for Neema)',
    'got': 'Karibu admin!',
    'hint': 'Read the if line the way Python reads it. What is “Juma” on its own?',
    'why': 'Python reads it as (name == "Asha") or ("Juma"). A non-empty string is always true, so everyone gets in.',
    'fixed': [   'name = input("Jina lako: ")',
    '',
    'if name in ("Asha", "Juma"):',
    '    print("Karibu admin!")',
    'else:',
    '    print("Huna ruhusa.")'],
    'fix_lines': [2],
    'lesson': 'Each side of “or” is its own test. Compare both, or use “in”.',
    'avoid': [   ('Write full comparisons', 'name == "Asha" or name == "Juma"'),
    ('Or use in', 'name in ("Asha", "Juma") is cleaner.'),
    ('Test the “no” case too', 'Always try a name that should be refused.')],
    'sw': 'Jaribu jibu la hapana pia',
}

exec(open(os.path.join(STUDIO, "code-ya-wiki", "template.py")).read())
