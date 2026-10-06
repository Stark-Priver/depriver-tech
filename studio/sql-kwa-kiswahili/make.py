"""Carousel: SQL kwa Kiswahili, talk to a database (8 slides, 1080x1350, exported at 2x). Ujuzi wa kazini. Every query
is read out in plain Kiswahili ("Nipe ... kutoka ... pale ambapo ...") above a code window and its result table."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 8
POST_URL = "depriver.tech/blog/sql-kwa-kiswahili"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing
exec(open(os.path.join(STUDIO, "devices.py")).read())    # phones, stamps, terminals, docs

STUDENTS = [["1", "Asha", "Mbeya", "78"], ["2", "Juma", "Dodoma", "64"], ["3", "Neema", "Mbeya", "91"], ["4", "Baraka", "Arusha", "55"]]
WID = [110, 300, 300, W - 2 * M - 8 - 710]


def said(s, y, text):
    """The query read out in Kiswahili, as an orange speech line."""
    s.text(M, y, "“" + text + "”", f(SEMI, fit(s, "“" + text + "”", SEMI, 32, W - 2 * M)), ORANGE)


def query_slide(n, label, t1, t2, sw_line, sql, cols, rows, widths, note, hl=()):
    s = page(n, label, "SQL kwa Kiswahili")
    title2(s, t1, t2, y=210, size=80)
    said(s, 400, sw_line)
    y = code_window(s, 430, sql, file="wanafunzi.sql", lang="SQL", size=25, lh=40)
    table(s, M, y + 40, cols, rows, widths, size=25, rh=60, hl_rows=hl)
    horizon(s, n)
    navy_note(s, *note, seed=n)
    finish(s)
    s.save(n)


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Skills uni skips · Ujuzi wa kazini")
s.text(M - 6, 260, "SQL kwa", f(BOLD, 120), NAVY)
s.text(M - 6, 380, "Kiswahili.", f(BOLD, 120), ORANGE)
s.text(M, 470, "Ongea na database", f(SIG, 60), NAVY)
swash(s, M + 8, M + 420, 496, ORANGE, 6)
said(s, 590, "Nipe majina ya wanafunzi wa Mbeya")
code_window(s, 620, ["SELECT jina FROM wanafunzi", "WHERE mkoa = 'Mbeya';"], file="wanafunzi.sql", lang="SQL", size=27, lh=44)
s.para(M, 900, "Six patterns that cover most of what you'll do at work, read out in plain Kiswahili.", f(REG, 27), W - 2 * M, 40, GREY)
horizon(s, 1)
cover_footer(s, "Swipe, jifunze SQL")
finish(s)
s.save(1)

# ── 2 · the table ────────────────────────────────────────────────────────────────────────────────
s = page(2, "The table · Jedwali", "SQL kwa Kiswahili")
title2(s, "A table is like", "a daftari.", y=220, size=86)
table(s, M, 420, ["id", "jina", "mkoa", "alama"], STUDENTS, WID, size=27, rh=78)
tick_list(s, [("Table (jedwali): wanafunzi", None), ("Row (mstari): one student", None), ("Column (safu): one detail, like mkoa", None)], 870, size=28)
horizon(s, 2)
navy_note(s, "Note", "Every example uses this same table. Follow along.", "Fuatilia jedwali hili", seed=2)
finish(s)
s.save(2)

query_slide(3, "SELECT · Nipe", "SELECT:", "nipe…", "Nipe jina na alama kutoka wanafunzi",
            ["SELECT jina, alama", "FROM wanafunzi;"], ["jina", "alama"], [r[1::2] for r in STUDENTS], [480, W - 2 * M - 8 - 480],
            ("Tip", "SELECT * means “nipe kila kitu”. Use it only while exploring.", "Nipe kila kitu"))
query_slide(4, "WHERE · Pale ambapo", "WHERE:", "pale ambapo…", "Nipe wanafunzi pale ambapo mkoa ni Mbeya",
            ["SELECT jina, alama FROM wanafunzi", "WHERE mkoa = 'Mbeya';"], ["jina", "alama"], [["Asha", "78"], ["Neema", "91"]], [480, W - 2 * M - 8 - 480],
            ("Remember", "Text goes in 'single quotes'. Numbers don't.", "Chuja kwa WHERE"))
query_slide(5, "ORDER BY · Panga", "ORDER BY:", "panga kwa…", "Nipe watatu bora, panga kwa alama kushuka",
            ["SELECT jina, alama FROM wanafunzi", "ORDER BY alama DESC", "LIMIT 3;"], ["jina", "alama"], [["Neema", "91"], ["Asha", "78"], ["Juma", "64"]],
            [480, W - 2 * M - 8 - 480], ("Words", "DESC = kushuka (big first). ASC = kupanda.", "Panga na chukua"))
query_slide(6, "GROUP BY · Kwa kila", "GROUP BY:", "kwa kila…", "Hesabu wanafunzi kwa kila mkoa",
            ["SELECT mkoa, COUNT(*) AS idadi", "FROM wanafunzi", "GROUP BY mkoa;"], ["mkoa", "idadi"], [["Mbeya", "2"], ["Dodoma", "1"], ["Arusha", "1"]],
            [480, W - 2 * M - 8 - 480], ("Also", "SUM, AVG, MAX work the same way. Sales per day = GROUP BY tarehe.", "Jumla kwa kila kundi"))

# ── 7 · JOIN ─────────────────────────────────────────────────────────────────────────────────────
s = page(7, "JOIN · Unganisha", "SQL kwa Kiswahili")
title2(s, "JOIN:", "unganisha majedwali.", y=210, size=80)
said(s, 400, "Nipe jina na ada iliyolipwa, ukiunganisha na jedwali la ada")
y = code_window(s, 430, ["SELECT w.jina, a.kiasi", "FROM wanafunzi w", "JOIN ada a ON a.mwanafunzi_id = w.id;"], file="wanafunzi.sql", lang="SQL", size=25, lh=40)
table(s, M, y + 40, ["jina", "kiasi (TZS)"], [["Asha", "450,000"], ["Juma", "300,000"], ["Neema", "450,000"]], [480, W - 2 * M - 8 - 480], size=25, rh=60)
horizon(s, 7)
navy_note(s, "Key idea", "Tables share an id. JOIN matches rows where the ids are equal.", "Kitambulisho kinaunganisha", seed=7)
finish(s)
s.save(7)

# ── 8 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Write a query", "in the comments.", [("Challenge", "wanafunzi wenye alama > 70"), ("Save", "your SQL cheat sheet"),
                                                ("Share", "with a classmate before the DB exam")])
code_window(s, 830, ["SELECT * FROM", "  furaha;"], file="?.sql", lang="SQL", size=22, lh=36, x0=640)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
