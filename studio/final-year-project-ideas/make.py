"""Carousel: 10 final year project ideas that solve real Tanzanian problems (9 slides, 1080x1350, exported at 2x).
Same editorial / print direction as dont-get-hacked. Every idea is a card: Tatizo (the local problem, red strip),
Suluhisho (the build), who uses it, the stack, and a difficulty badge (Rahisi / Wastani / Ngumu)."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())       # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())        # paper, print art, editorial tools
TOTAL = 9
POST_URL = "depriver.tech/blog/final-year-project-ideas"
exec(open(os.path.join(STUDIO, "editorial.py")).read())  # page, horizon, notes, cards, closing

LEVEL = {"Rahisi": GREEN_OK, "Wastani": ORANGE, "Ngumu": RED_NO}
IDEAS = [
    ("VICOBA Digital", "Rekodi za VICOBA na SACCO",
     "Vikundi hutunza michango na mikopo kwenye daftari. Makosa na migogoro ni mingi.",
     "App ya michango, mikopo na riba, na risiti kwa SMS kwa kila mwanachama.",
     "Vikundi vya akiba", "Laravel · MySQL · SMS", "Wastani"),
    ("Bei ya Mazao", "Bei za sokoni kwa SMS / USSD",
     "Wakulima huuza kwa madalali bila kujua bei halisi sokoni.",
     "Piga *code# uone bei ya leo Mbeya, Kariakoo, Arusha. Inafanya kazi kwenye kitochi.",
     "Wakulima", "USSD · Django · PostgreSQL", "Wastani"),
    ("Foleni Zahanati", "Foleni na miadi ya zahanati",
     "Wagonjwa husubiri masaa mengi kwenye foleni bila kujua zamu yao.",
     "Namba ya foleni kwa SMS, muda wa kusubiri, na dashboard ya muuguzi.",
     "Zahanati na vituo vya afya", "React · Node.js · SMS", "Wastani"),
    ("Mzazi Portal", "Ada, matokeo na mahudhurio",
     "Wazazi hupata taarifa za ada na matokeo kwa kuchelewa, au kwa barua.",
     "SMS za salio la ada, matokeo na mahudhurio, na dashboard ya walimu.",
     "Shule za sekondari", "Laravel · MySQL · SMS", "Rahisi"),
    ("Daladala Finder", "Ruti za daladala na mwendokasi",
     "Wageni mjini hawajui daladala ipi inaenda wapi, wala nauli.",
     "Tafuta kwa vituo: ruti, nauli na mabadiliko. Inafanya kazi bila internet.",
     "Abiria Dar, Mbeya, Arusha", "Flutter · SQLite (offline)", "Wastani"),
    ("Hostel Bila Dalali", "Vyumba karibu na chuo",
     "Wanafunzi wa mwaka wa kwanza hutapeliwa na madalali wa vyumba.",
     "Vyumba vilivyothibitishwa: picha, bei, umbali na maoni ya wanafunzi.",
     "Wanafunzi wa vyuo", "Next.js · Firebase", "Rahisi"),
    ("Boda Salama", "Usalama wa abiria wa bodaboda",
     "Abiria hawajui dereva ni nani. Wizi na ajali hutokea bila kumbukumbu.",
     "Scan QR kwenye boda uone dereva aliyesajiliwa, kisha share safari kwa rafiki.",
     "Abiria na vikundi vya boda", "Flutter · Firebase · QR", "Wastani"),
    ("Duka Smart", "Mauzo na stoo ya duka dogo",
     "Maduka madogo hayajui faida halisi. Mauzo yako kwenye daftari.",
     "POS rahisi: mauzo, tahadhari ya stoo, faida ya siku. Offline, inasawazisha baadaye.",
     "Maduka na vibanda", "PWA · IndexedDB · Laravel", "Wastani"),
    ("Shamba Bot", "Ushauri wa kilimo kwa Kiswahili",
     "Ushauri wa wataalamu wa kilimo haupatikani kwa urahisi vijijini.",
     "Chatbot ya WhatsApp kwa Kiswahili: maswali ya kupanda, na picha ya jani kutambua ugonjwa.",
     "Wakulima vijijini", "Python · AI model · WhatsApp API", "Ngumu"),
    ("Maji Token", "Malipo ya vituo vya maji vya jamii",
     "Vituo vya maji vya jamii hukusanya pesa kwa mkono. Upotevu ni mkubwa.",
     "Malipo kabla (token), app ya mkusanyaji, na ripoti za mwezi kwa kamati ya maji.",
     "Kamati za maji vijijini", "Laravel · USSD · IoT (hiari)", "Ngumu"),
]


def idea_card(s, y0, i, idea, h=300):
    name, sub, tatizo, sulu, users, stack, level = idea
    x0, x1 = M, W - M - 8
    card(s, (x0, y0, x1, y0 + h))
    s.text(x0 + 26, y0 + 56, f"{i + 1:02d}", f(BOLD, 34), ORANGE)
    s.text(x0 + 90, y0 + 54, name, f(BOLD, 36), NAVY)
    s.text(x0 + 90, y0 + 90, sub, f(REG, 23), GREY)
    lw = s.width(level, f(BOLD, 19)) + 34
    s.d.rounded_rectangle([k(x1 - 24 - lw), k(y0 + 24), k(x1 - 24), k(y0 + 64)], radius=k(20), fill=LEVEL[level])
    s.text(x1 - 24 - lw / 2, y0 + 45, level, f(BOLD, 19), WHITE_T, anchor="mm")
    s.rect(x0 + 3, y0 + 110, x1 - 3, y0 + 112, RULE)
    smallcaps(s, x0 + 26, y0 + 156, "Tatizo", 14, RED_NO)
    yy = s.para(x0 + 150, y0 + 158, tatizo, f(REG, 26), x1 - x0 - 180, 36, NAVY)
    smallcaps(s, x0 + 26, yy + 18, "Suluhisho", 14, GREEN_OK)
    s.para(x0 + 150, yy + 20, sulu, f(MED, 26), x1 - x0 - 180, 36, NAVY)
    s.rect(x0 + 3, y0 + h - 58, x1 - 3, y0 + h - 56, RULE)
    smallcaps(s, x0 + 26, y0 + h - 22, "Watumiaji", 13, GREY)
    s.text(x0 + 150, y0 + h - 22, users, f(SEMI, 21), NAVY)
    s.text(x1 - 26, y0 + h - 22, stack, f(SEMI, 21), ORANGE, anchor="rs")


# ── 1 · cover ────────────────────────────────────────────────────────────────────────────────────
s = page(1, "For final year students · Tanzania")
s.text(M - 6, 250, "Stop building", f(BOLD, 96), NAVY)
s.text(M - 6, 352, "another library", f(BOLD, 96), NAVY)
s.text(M - 8, 466, "system.", f(BOLD, 120), ORANGE)
s.text(M, 560, "Tatua matatizo ya Tanzania", f(SIG, 60), NAVY)
swash(s, M + 8, M + 560, 586, ORANGE, 6)
s.para(M, 670, "10 final year project ideas that solve real problems here at home, with the stack and difficulty for each.",
       f(REG, 27), 520, 40, GREY)
names = [i[0] for i in IDEAS]
x, y = M, 820
for nm in names:
    ww = s.width(nm, f(SEMI, 21)) + 32
    if x + ww > W - M:
        x, y = M, y + 56
    s.d.rounded_rectangle([k(x), k(y), k(x + ww), k(y + 44)], radius=k(22), fill=(255, 255, 255), outline=NAVY, width=k(2.5))
    s.text(x + ww / 2, y + 23, nm, f(SEMI, 21), NAVY, anchor="mm")
    x += ww + 10
sticker(s, W - M - 170, 560, "Supervisors love these", angle=6, size=19, bg=NAVY)
horizon(s, 1)
cover_footer(s, "Swipe for 10 ideas")
finish(s)
s.save(1)

# ── 2 · what makes a good project ────────────────────────────────────────────────────────────────
s = page(2, "The rule · Kanuni")
title2(s, "A good project", "has real users.", y=230, size=84)
rules = [("A real problem", "Something you've seen in your street, school or village."),
         ("Real people use it", "Even 10 people. Not just your supervisor."),
         ("Works on their phones", "Many people use kitochi: think SMS and USSD."),
         ("You can finish it", "One thing done well beats ten features half-done."),
         ("You can demo it live", "Deployed, with real data, in under 5 minutes.")]
numbered(s, rules, 440, gap=110)
horizon(s, 2)
navy_note(s, "Remember", "The best projects start with a problem, not a technology.", "Anza na tatizo", seed=2)
finish(s)
s.save(2)

# ── 3–7 · ideas ──────────────────────────────────────────────────────────────────────────────────
notes = [("Pro tip", "Visit a real VICOBA group or market before you write code.", "Ongea na watumiaji"),
         ("Pro tip", "Ask a dispensary or school what wastes their time most.", "Uliza kwanza"),
         ("Pro tip", "Offline-first apps win where the network is weak.", "Mtandao si kila mahali"),
         ("Pro tip", "Start with one market or one route, then grow.", "Anza kidogo"),
         ("Pro tip", "Hard ones make great team projects. Split the work.", "Kazi ya timu")]
for p in range(5):
    n = p + 3
    s = page(n, f"Ideas {p * 2 + 1:02d}–{p * 2 + 2:02d} · Mawazo ya miradi")
    for j in range(2):
        i = p * 2 + j
        idea_card(s, 170 + j * 430, i, IDEAS[i], h=390)
    horizon(s, n)
    navy_note(s, *notes[p], seed=n)
    finish(s)
    s.save(n)

# ── 8 · make it real ─────────────────────────────────────────────────────────────────────────────
s = page(8, "Make it real · Ifanye halisi")
title2(s, "From idea to", "a project that wins.", y=220, size=80)
steps = [("Talk to 5 real users", "Ask what wastes their time or money. Write it down."),
         ("Build the smallest version", "One core feature that works end to end."),
         ("Test it with them", "Watch them use it. Fix what confuses them."),
         ("Deploy it", "Online, or on their phones, with real data."),
         ("Document and present with proof", "README, screenshots, and what users said.")]
numbered(s, steps, 430, gap=110)
horizon(s, 8)
navy_note(s, "Bonus", "A project real people use can become your first business.", "Mradi leo, kampuni kesho", seed=8)
finish(s)
s.save(8)

# ── 9 · closing ──────────────────────────────────────────────────────────────────────────────────
s = page(TOTAL, "The end · Mwisho")
closing(s, "Which problem will", "you solve?", [("Save", "for proposal season"), ("Share", "with your project group"),
                                              ("Comment", "a Tanzanian problem I missed")])
horizon(s, TOTAL)
closing_footer(s)
finish(s)
s.save(TOTAL)
print("ok")
