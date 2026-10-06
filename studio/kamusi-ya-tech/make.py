"""Carousel: Kamusi ya Tech, toleo 01 (10 slides, 1080x1350, exported at 2x). Tech words explained in plain Swahili.
Every word is a dictionary page: huge headword, pronunciation, part of speech, maana (Swahili), the English line,
a daily-life mfano, and an alphabet thumb index on the right edge with the word's letter pulled out as a tab."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 10
POST_URL = "depriver.tech/blog/kamusi-ya-tech"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing

ART.update({
    "dictionary": svg(GROUND + f'''
      <path d="M300 80 C240 58 120 54 50 72 V360 C120 342 240 346 300 368z" fill="#fff" {ST}/>
      <path d="M300 80 C360 58 480 54 550 72 V360 C480 342 360 346 300 368z" fill="#fff" {ST}/>
      <path d="M300 80 V368" {ST} stroke-width="4"/>
      <text x="90" y="150" font-family="Poppins" font-weight="700" font-size="54" fill="#0b1e3f">API</text>
      <text x="90" y="182" font-family="Poppins" font-weight="500" font-size="18" fill="#e8603a">(nomino)</text>
      <path d="M90 214 h170 M90 242 h150 M90 270 h165 M90 298 h120" stroke="#c9d4ea" stroke-width="9" stroke-linecap="round"/>
      <text x="330" y="150" font-family="Poppins" font-weight="700" font-size="54" fill="#e8603a">Bug</text>
      <path d="M330 190 h170 M330 218 h140 M330 246 h160 M330 274 h110" stroke="#c9d4ea" stroke-width="9" stroke-linecap="round"/>
      <rect x="548" y="96" width="34" height="56" rx="6" fill="#e8603a" {ST} stroke-width="4"/>
      <text x="565" y="132" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="22" fill="#fff">A</text>
      <rect x="548" y="160" width="34" height="56" rx="6" fill="#0b1e3f" {ST} stroke-width="4"/>
      <text x="565" y="196" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="22" fill="#fff">B</text>'''),
})

WORDS = [
    ("API", "ei-pi-ai", "nomino", "Application Programming Interface",
     "Njia ambayo programu moja huongea na programu nyingine na kubadilishana taarifa.",
     "A set of rules that lets one program ask another program for data or actions.",
     "Mhudumu wa mgahawa: unaagiza chakula (request), jikoni wanapika, mhudumu anakuletea (response). Huoni jikoni, unapata chakula tu.",
     "“App yetu inachukua hali ya hewa ya Mbeya kupitia API.”"),
    ("Bug", "bag", "nomino", "Kosa kwenye code",
     "Hitilafu kwenye code inayofanya programu ifanye kitu ambacho hukutarajia.",
     "An error in code that makes a program behave in an unexpected way.",
     "Calculator inasema 2 + 2 = 22. Kutafuta na kurekebisha bug ndiyo debugging.",
     "“Nimekaa usiku mzima natafuta bug moja tu.”"),
    ("Git", "git", "nomino", "Version control",
     "Mfumo unaohifadhi historia ya kila mabadiliko kwenye code yako, hatua kwa hatua.",
     "A tool that records every change to your code, so you can go back or work in a team.",
     "Kama save points kwenye game. Hakuna tena final_FINAL2.zip. GitHub ni mahali project za Git zinakaa mtandaoni.",
     "“Usisahau ku-commit kwenye Git kabla hujafunga laptop.”"),
    ("Deploy", "di-ploi", "kitenzi", "Kuweka mtandaoni",
     "Kuhamisha programu yako kutoka kwenye kompyuta yako na kuiweka mtandaoni ili watu waitumie.",
     "To put your app on a server so real users can reach it.",
     "Kupika nyumbani dhidi ya kufungua mgahawa. “Inafanya kazi kwenye laptop yangu” haitoshi mpaka u-deploy.",
     "“Tume-deploy toleo jipya jana usiku.”"),
    ("Server", "sa-va", "nomino", "Kompyuta ya huduma",
     "Kompyuta inayohudumia tovuti au programu kwa watumiaji wengi, masaa 24.",
     "A computer that serves websites, apps or data to other computers over a network.",
     "Kama duka lisilofungwa kamwe: wateja (browsers) wanakuja wakati wowote, duka linawahudumia.",
     "“Server imezima, ndiyo maana tovuti haifunguki.”"),
    ("Cloud", "klaud", "nomino", "Wingu",
     "Kutumia server na huduma za kampuni nyingine kupitia internet badala ya kununua zako.",
     "Renting computing power, storage and services over the internet.",
     "Kupanga nyumba badala ya kujenga. Google Drive ni cloud: picha zako ziko kwenye server za mtu mwingine.",
     "“Tumehamisha mfumo wa shule kwenda cloud.”"),
    ("Database", "dei-ta-beis", "nomino", "Hifadhidata",
     "Mahali data huhifadhiwa kwa mpangilio ili itafutwe, ibadilishwe na ipatikane haraka.",
     "An organised store of data that apps read from and write to.",
     "Daftari la mauzo la duka, ila unaweza kutafuta mauzo ya mwaka mzima kwa sekunde moja.",
     "“Majina ya wanafunzi wote yako kwenye database.”"),
    ("Framework", "freim-wek", "nomino", "Kiunzi",
     "Msingi uliotengenezwa tayari, wenye sheria na zana, unaojengea programu haraka.",
     "Ready-made structure and tools you build your app on, like Laravel, React or Django.",
     "Kiunzi cha nyumba kilichosimamishwa tayari: wewe unajenga kuta na kupamba, hauanzi kuchimba msingi.",
     "“Tunajenga mfumo huu kwa framework ya Laravel.”"),
]
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def thumb_index(s, letter):
    """Alphabet strip on the right edge; the word's letter sticks out as an orange tab."""
    x0, top, step = W - 40, 150, 34
    s.rect(x0, top - 10, W, top + step * 26, (232, 235, 242))
    for i, ch in enumerate(LETTERS):
        y = top + i * step
        if ch == letter:
            s.d.rounded_rectangle([k(x0 - 30), k(y - 4), k(W + 10), k(y + step - 2)], radius=k(8), fill=ORANGE)
            s.text(x0 - 6, y + step / 2, ch, f(BOLD, 22), WHITE_T, anchor="mm")
        else:
            s.text(x0 + 20, y + step / 2, ch, f(SEMI, 15), (150, 158, 175), anchor="mm")


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "Toleo 01 · Episode 01")
s.text(M - 6, 270, "Kamusi", f(BOLD, 150), NAVY)
s.text(M - 6, 400, "ya Tech.", f(BOLD, 150), ORANGE)
s.text(M, 500, "Maneno 8 ambayo lecturer hakueleza", f(SIG, 54), NAVY)
swash(s, M + 8, M + 620, 526, ORANGE, 6)
s.para(M, 610, "Tech words explained in plain Swahili, with examples from daily life.", f(REG, 27), 420, 40, GREY)
paste_print(s, print_art("dictionary", k(500)), 520, 560)
x, y = M, 760
for w_ in [w[0] for w in WORDS]:
    ww = s.width(w_, f(SEMI, 22)) + 36
    if x + ww > 500:
        x, y = M, y + 60
    s.d.rounded_rectangle([k(x), k(y), k(x + ww), k(y + 46)], radius=k(23), fill=(255, 255, 255), outline=NAVY, width=k(2.5))
    s.text(x + ww / 2, y + 24, w_, f(SEMI, 22), NAVY, anchor="mm")
    x += ww + 10
horizon(s, 1)
cover_footer(s, "Swipe, jifunze neno kwa neno")
finish(s)
s.save(1)

# ── 2–9 · words ──────────────────────────────────────────────────────────────────────────────────
for i, (word, pron, pos, full, maana, eng, mfano, sentence) in enumerate(WORDS):
    n = i + 2
    s = page(n, f"Neno {i + 1:02d} / 08", "Kamusi ya Tech")
    thumb_index(s, word[0])
    outline_text(s, W - 70, 470, word[0], f(BOLD, 380), stroke=3, color=RULE, anchor="rs")
    hs = fit(s, word, BOLD, 128, W - 2 * M - 320)
    s.text(M - 6, 300, word, f(BOLD, hs), NAVY)
    hx = M + s.width(word, f(BOLD, hs)) + 24
    s.text(hx, 260, f"/{pron}/", f(REG, 26), GREY)
    s.text(hx, 300, f"({pos})", f(SEMI, 26), ORANGE)
    s.text(M, 356, full, f(SEMI, 27), GREY)
    hairline(s, M, W - 110, 386, RULE)
    smallcaps(s, M, 450, "Maana", 15, ORANGE)
    y = s.para(M, 500, maana, f(MED, 34), W - M - 130, 48, NAVY)
    smallcaps(s, M, y + 30, "In English", 15, GREY)
    y = s.para(M, y + 74, eng, f(REG, 26), W - M - 130, 38, GREY)
    my = y + 30
    box_h = 84 + wrap_lines(s, mfano, f(REG, 27), W - M - 180) * 40 + 10
    card(s, (M, my, W - 110, my + box_h), r=16)
    s.rect(M + 2, my + 2, M + 12, my + box_h - 2, ORANGE)
    smallcaps(s, M + 34, my + 46, "Mfano · Example", 14, ORANGE)
    s.para(M + 34, my + 94, mfano, f(REG, 27), W - M - 180, 40, NAVY)
    horizon(s, n)
    smallcaps(s, M, BASE + 74, "Kwenye sentensi · In a sentence", 16, ORANGE)
    s.text(M, BASE + 134, sentence, f(SEMI, fit(s, sentence, SEMI, 31, W - 2 * M)), WHITE_T)
    s.text(W - M, BASE + 224, f"{i + 1} / 8", f(SEMI, 21), SOFT, anchor="rs")
    finish(s)
    s.save(n)

# ── 10 · closing ─────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "Mwisho wa toleo 01")
closing(s, "Neno gani litoke", "Toleo 02?", [("Save", "kamusi yako ya mfukoni"), ("Share", "na mwanafunzi wa mwaka wa kwanza"),
                                           ("Comment", "neno unalotaka nieleze")])
paste_print(s, print_art("dictionary", k(380)), 640, 650)
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
