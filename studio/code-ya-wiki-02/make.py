"""Code ya Wiki #02: the price that became a string. Content only: layout is studio/code-ya-wiki/template.py.
New episode: copy this folder to code-ya-wiki-NN, change EP, run `npm run carousel -- code-ya-wiki-NN`."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 2,
    'lang': 'JavaScript',
    'file': 'checkout.js',
    'question': 'Kwa nini jumla ni kubwa hivi?',
    'goal': 'add the delivery fee (TZS 2,000) to the price typed in a form.',
    'code': [   'const input = document.querySelector("#price");',
                'const price = input.value;',
    'const delivery = 2000;',
    '',
    'const total = price + delivery;',
    'console.log("Jumla:", total);'],
    'bug_lines': [1],
    'expected': 'Jumla: 7000',
    'got': 'Jumla: 50002000',
    'hint': 'The user typed 5000. What type of value does a form input give you?',
    'why': 'Form inputs always give text (a string). "5000" + 2000 joins the text instead of adding: "50002000".',
    'fixed': [   'const input = document.querySelector("#price");',
                 'const price = Number(input.value);',
    'const delivery = 2000;',
    '',
    'const total = price + delivery;',
    'console.log("Jumla:", total);'],
    'fix_lines': [1],
    'lesson': 'Form values are strings. Convert them before you do maths.',
    'avoid': [   ('Convert input to numbers', 'Number(value) or parseInt(value, 10).'),
    ('Check for NaN', 'If the user types letters, show an error.'),
    ('Log the type', 'console.log(typeof price) shows "string" right away.')],
    'sw': 'Maandishi si namba',
}

exec(open(os.path.join(STUDIO, "code-ya-wiki", "template.py")).read())
