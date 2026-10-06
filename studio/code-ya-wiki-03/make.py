"""Code ya Wiki #03: the update that changed everyone. Content only: layout is studio/code-ya-wiki/template.py.
New episode: copy this folder to code-ya-wiki-NN, change EP, run `npm run carousel -- code-ya-wiki-NN`."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 3,
    'lang': 'SQL',
    'file': 'ada.sql',
    'question': 'Kwa nini wote wamelipa?',
    'goal': 'mark that student 1042 has paid school fees.',
    'code': ['-- Asha (id 1042) has paid her fees', 'UPDATE students', 'SET fee_paid = 1;'],
    'bug_lines': [1, 2],
    'expected': '1 row updated',
    'got': '2,318 rows updated',
    'hint': 'The query says what to change. Does it say which student?',
    'why': "There's no WHERE. Without it, UPDATE changes every row in the table: the whole school is now marked as paid.",
    'fixed': ['-- Asha (id 1042) has paid her fees', 'UPDATE students', 'SET fee_paid = 1', 'WHERE id = 1042;'],
    'fix_lines': [3],
    'lesson': 'UPDATE and DELETE without WHERE touch every row.',
    'avoid': [   ('SELECT first', 'Run SELECT * FROM students WHERE id = 1042 and check the result.'),
    ('Use a transaction', 'BEGIN, run it, check, then COMMIT or ROLLBACK.'),
    ('Back up before big changes', 'And never practise on the live database.')],
    'sw': 'Chagua kwanza, badilisha baadaye',
}

exec(open(os.path.join(STUDIO, "code-ya-wiki", "template.py")).read())
