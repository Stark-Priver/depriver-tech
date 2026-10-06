"""Code ya Wiki #01: the average that skips a student. Content only: layout is studio/code-ya-wiki/template.py.
New episode: copy this folder to code-ya-wiki-NN, change EP, run `npm run carousel -- code-ya-wiki-NN`."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 1,
    'lang': 'Python',
    'file': 'wastani.py',
    'question': 'Kwa nini wastani si sahihi?',
    'goal': 'find the average mark of the class.',
    'code': [   'marks = [80, 60, 70]',
    '',
    'total = 0',
    'for i in range(1, len(marks)):',
    '    total = total + marks[i]',
    '',
    'average = total / len(marks)',
    'print(average)'],
    'bug_lines': [3],
    'expected': '70.0',
    'got': '43.33...',
    'hint': 'Count how many marks the loop actually adds. Is the first student included?',
    'why': 'range(1, len(marks)) starts at index 1, so marks[0] (the 80) is never added. Python lists start counting at 0.',
    'fixed': [   'marks = [80, 60, 70]',
    '',
    'total = 0',
    'for mark in marks:',
    '    total = total + mark',
    '',
    'average = total / len(marks)',
    'print(average)'],
    'fix_lines': [3, 4],
    'lesson': 'Lists start at index 0. Loop over the items, not the numbers.',
    'avoid': [   ('Loop over items directly', 'for mark in marks: no index, no off-by-one.'),
    ('Use built-ins', 'sum(marks) / len(marks) does it in one line.'),
    ('Test with tiny data', 'Three numbers you can add in your head.')],
    'sw': 'Hesabu kuanzia sifuri',
}

exec(open(os.path.join(STUDIO, "code-ya-wiki", "template.py")).read())
