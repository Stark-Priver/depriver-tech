"""Kamusi ya Tech, toleo 03: the words of the internet. Layout: studio/kamusi/template.py."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {"num": 3, "words": [
    ("Domain", "do-mein", "nomino", "Jina la tovuti",
     "Anwani ya tovuti ambayo watu wanaandika kwenye browser, kama depriver.tech.",
     "The name people type to reach a website.",
     "Jina la duka kwenye bango. Watu wanakumbuka “Duka la Mama Asha”, si namba ya kiwanja.",
     "“Nimesajili domain ya .co.tz kwa ajili ya biashara.”"),
    ("Hosting", "hos-ting", "nomino", "Mwenyeji wa tovuti",
     "Huduma ya kukodisha nafasi kwenye server ili tovuti yako iwe mtandaoni.",
     "Renting space on a server so your website is online.",
     "Kukodi fremu ya duka. Domain ni jina la duka, hosting ni chumba chenyewe.",
     "“Tovuti iko chini kwa sababu hosting imeisha muda.”"),
    ("DNS", "di-en-es", "nomino", "Kitabu cha anwani cha internet",
     "Mfumo unaotafsiri jina la tovuti kuwa anwani ya namba (IP) ya server.",
     "The system that turns a website name into the server's number address.",
     "Phonebook ya simu: unatafuta “Juma”, simu inapata namba yake. Wewe hukumbuki namba.",
     "“Nimebadilisha DNS, tovuti itaonekana baada ya muda.”"),
    ("Cache", "kash", "nomino", "Hifadhi ya muda",
     "Nakala ya data iliyohifadhiwa karibu ili ipatikane haraka zaidi wakati ujao.",
     "A saved copy of data kept close so it loads faster next time.",
     "Unaweka sukari mezani badala ya kwenda stoo kila mara. Ukibadilisha sukari stoo, ya mezani bado ni ya zamani.",
     "“Futa cache ya browser uone mabadiliko mapya.”"),
    ("Cookie", "ku-ki", "nomino", "Kumbukumbu ndogo ya tovuti",
     "Taarifa ndogo ambayo tovuti inaihifadhi kwenye browser yako ili ikukumbuke.",
     "A small piece of data a website stores in your browser to remember you.",
     "Tiketi ya kuegesha gari: unaionyesha, wanajua wewe ni nani na umelipa nini.",
     "“Ukifuta cookies, utalazimika ku-login upya.”"),
    ("Encryption", "en-krip-shen", "nomino", "Usimbaji fiche",
     "Kubadilisha taarifa kuwa siri ambayo ni mwenye ufunguo tu anayeweza kuisoma.",
     "Scrambling data so only someone with the key can read it.",
     "Barua kwenye sanduku lenye kufuli: posta inalibeba, lakini ni mwenye ufunguo tu anayeweza kulifungua.",
     "“Kufuli kwenye browser inaonyesha muunganisho una encryption.”"),
    ("Token", "to-ken", "nomino", "Kibali cha kidijitali",
     "Kipande cha maandishi kinachothibitisha wewe ni nani, bila kutuma password kila mara.",
     "A piece of text that proves who you are without sending your password every time.",
     "Bangili ya harusi: umeonyesha kadi mlangoni mara moja, sasa bangili inakuruhusu kuingia na kutoka.",
     "“Token imeisha muda, app inakuomba u-login tena.”"),
    ("Webhook", "web-huk", "nomino", "Taarifa ya moja kwa moja",
     "Njia ambayo mfumo mmoja unautumia mwingine ujumbe papo hapo jambo linapotokea.",
     "One system automatically notifying another the moment something happens.",
     "Badala ya kupiga simu kila dakika “mzigo umefika?”, duka linakutumia SMS mzigo ukifika.",
     "“Malipo yakikamilika, mtoa huduma anatuma webhook kwa server yetu.”"),
]}
exec(open(os.path.join(STUDIO, "kamusi", "template.py")).read())
