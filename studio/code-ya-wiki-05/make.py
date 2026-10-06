"""Code ya Wiki #05: the login anyone can break. Content only: layout is studio/code-ya-wiki/template.py.
New episode: copy this folder to code-ya-wiki-NN, change EP, run `npm run carousel -- code-ya-wiki-NN`."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 5,
    'lang': 'PHP',
    'file': 'login.php',
    'question': 'Kwa nini hii ni hatari?',
    'goal': 'find a user by the phone number typed in the login form.',
    'code': [   '$phone = $_POST["phone"];',
    '',
    '$sql = "SELECT * FROM users',
    '        WHERE phone = \'$phone\'";',
    '$user = $db->query($sql);'],
    'bug_lines': [2, 3],
    'expected': "Only that user's row",
    'got': "Every user's row",
    'hint': 'Imagine someone types a quote mark and a bit of SQL into the phone box instead of a number.',
    'why': ("The input is pasted straight into the SQL. Typing ' OR '1'='1 changes the query itself. This is SQL injection, a top cause of "
 'data leaks.'),
    'fixed': [   '$phone = $_POST["phone"];',
    '',
    '$stmt = $db->prepare(',
    '    "SELECT * FROM users WHERE phone = ?");',
    '$stmt->execute([$phone]);'],
    'fix_lines': [2, 3, 4],
    'lesson': 'Never paste user input into SQL. Use prepared statements.',
    'avoid': [   ('Prepared statements, always', 'PDO prepare() + execute() in PHP, the same idea in every language.'),
    ('Validate input', 'A phone number should only contain digits.'),
    ("Use the framework's tools", "Laravel's Eloquent and query builder do this for you.")],
    'sw': 'Usimwamini mtumiaji',
}

exec(open(os.path.join(STUDIO, "code-ya-wiki", "template.py")).read())
