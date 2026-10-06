"""Kamusi ya Tech, toleo 02: the words of your first programming class. Layout: studio/kamusi/template.py."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {"num": 2, "words": [
    ("Algorithm", "al-go-ri-dhim", "nomino", "Mpangilio wa hatua",
     "Hatua kwa hatua, kwa mpangilio, za kutatua tatizo fulani.",
     "A step-by-step set of instructions to solve a problem.",
     "Mapishi ya chai: chemsha maji, weka majani, ongeza maziwa, weka sukari. Ukibadilisha mpangilio, chai inaharibika.",
     "“Kabla ya ku-code, andika algorithm kwenye karatasi.”"),
    ("Variable", "ve-ri-a-bo", "nomino", "Kibadilika",
     "Jina linalohifadhi thamani fulani ndani ya programu, na thamani hiyo inaweza kubadilika.",
     "A named box in a program that stores a value you can change.",
     "Sanduku lenye lebo “bei”. Leo lina 5000, kesho unaweza kuweka 6000. Lebo ni ile ile.",
     "“Weka jina la mteja kwenye variable inayoitwa jina.”"),
    ("Function", "fank-shen", "nomino", "Kazi / kitendakazi",
     "Kipande cha code chenye jina, kinachofanya kazi moja, na unaweza kukiita mara nyingi.",
     "A named block of code that does one job and can be reused.",
     "Mashine ya juisi: unaweka matunda (input), unabonyeza, unapata juisi (output). Hutengenezi mashine mpya kila siku.",
     "“Tengeneza function moja ya kukokotoa VAT.”"),
    ("Loop", "luup", "nomino", "Mzunguko",
     "Njia ya kurudia kazi ile ile mara nyingi bila kuandika code upya.",
     "Code that repeats an action many times.",
     "Mwalimu anaita majina ya wanafunzi 60 mmoja mmoja. Loop inafanya hivyo kwa kila jina kwenye orodha.",
     "“Tumia loop kutuma SMS kwa wateja wote.”"),
    ("Frontend", "front-end", "nomino", "Sehemu ya mbele",
     "Sehemu ya programu au tovuti ambayo mtumiaji anaiona na kuigusa.",
     "The part of an app users see and interact with.",
     "Ukumbi wa mgahawa: meza, menyu, mapambo. Mteja anaona hiki tu.",
     "“Frontend yetu imejengwa kwa React.”"),
    ("Backend", "bak-end", "nomino", "Sehemu ya nyuma",
     "Sehemu isiyoonekana inayoshughulikia mantiki, data na usalama wa programu.",
     "The hidden part of an app: logic, data and security.",
     "Jikoni kwa mgahawa: chakula kinapikwa, stoo, hesabu. Mteja haoni, lakini bila jikoni hakuna chakula.",
     "“Backend inahifadhi oda zote kwenye database.”"),
    ("Open source", "o-pen sos", "nomino", "Chanzo huria",
     "Programu ambayo code yake iko wazi: mtu yeyote anaweza kuisoma, kuitumia na kuchangia.",
     "Software whose code is public for anyone to read, use and improve.",
     "Mapishi ya bibi yaliyoandikwa kwenye ubao wa kijiji: kila mtu anaweza kupika, na kuongeza ujuzi wake.",
     "“Linux na Python ni open source.”"),
    ("Debugging", "di-ba-ging", "kitenzi", "Kutafuta na kurekebisha makosa",
     "Kazi ya kutafuta chanzo cha kosa kwenye code na kulirekebisha.",
     "Finding the cause of a bug and fixing it.",
     "Fundi wa gari anasikiliza mlio, anafungua, anajaribu sehemu moja moja mpaka apate tatizo.",
     "“Nimetumia saa mbili ku-debug, kumbe nilisahau koma.”"),
]}
exec(open(os.path.join(STUDIO, "kamusi", "template.py")).read())
