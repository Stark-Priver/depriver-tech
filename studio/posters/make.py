"""Feed posters (1080x1350) and statuses (1080x1920) for the post bank (Nov 2026 → Mar 2027), exported at 2x, each built
from its carousel cover (run the carousel first). One table instead of one folder per post.

    python3 studio/posters/make.py                 # every slug whose carousel export exists
    python3 studio/posters/make.py ussd-apps ...   # just these

Output: studio/posters/export/<slug>-poster.jpg and <slug>-status.jpg (picked up by scripts/post-kit.py)."""
import os
import sys
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())
exec(open(os.path.join(STUDIO, "kit.py")).read())
POST_URL = "depriver.tech/blog"
TOTAL = 1
exec(open(os.path.join(STUDIO, "editorial.py")).read())

POSTERS = {  # slug: (footer kicker, status header label)
    "freelance-like-a-pro": ("From zero to paid · 7 stages", "Beginners · Kazi huru"),
    "first-language-and-framework": ("Pick · learn · build · ship", "Beginners · Wanaoanza"),
    "uongo-au-kweli": ("Six tech myths · Hadithi sita", "Tech myths · Hadithi za tech"),
    "study-programming-for-exams": ("Trace tables · past papers · exam day", "Exam season · Msimu wa mitihani"),
    "ussd-apps": ("Jenga kwa Tanzania #01 · USSD", "Build for Tanzania"),
    "code-ya-wiki-01": ("Spot the bug · Python", "Code ya Wiki #01"),
    "your-first-hackathon": ("Prepare · build · pitch", "Hackathon season"),
    "njia-za-tech-backend": ("Njia za Tech #01 · Backend", "Tech careers, explained"),
    "how-mobile-money-works": ("Inavyofanya kazi #01 · Mobile money", "How it works"),
    "mobile-money-in-your-app": ("Jenga kwa Tanzania #02 · Payments", "Build for Tanzania"),
    "read-error-messages": ("Read · search · isolate · ask", "Skills uni skips"),
    "hiki-au-kile-01": ("Five match-ups · Learning", "Hiki au Kile #01"),
    "njia-za-tech-frontend": ("Njia za Tech #02 · Frontend", "Tech careers, explained"),
    "price-your-first-freelance-job": ("Hours × rate + costs + buffer", "Freelancing · Kazi huru"),
    "holiday-learning-plan": ("4 weeks · 1 hour a day", "December break · Likizo"),
    "what-happens-when-you-type-a-url": ("Inavyofanya kazi #02 · The web", "How it works"),
    "build-for-cheap-phones": ("Jenga kwa Tanzania #03 · Light apps", "Build for Tanzania"),
    "code-ya-wiki-02": ("Spot the bug · JavaScript", "Code ya Wiki #02"),
    "njia-za-tech-data-analyst": ("Njia za Tech #03 · Data", "Tech careers, explained"),
    "hii-ni-nini": ("Quiz · guess the file", "Chemsha bongo"),
    "sim-swap-scam": ("Inavyofanya kazi #03 · SIM swap", "Stay safe · Usalama"),
    "tech-roadmap-2027": ("Q1 · Q2 · Q3 · Q4", "New year · Mwaka mpya"),
    "kamusi-ya-tech-02": ("Maneno 8 ya darasa la kwanza", "Kamusi ya Tech · Toleo 02"),
    "terminal-in-10-commands": ("pwd · ls · cd · mkdir · and more", "Skills uni skips"),
    "njia-za-tech-cybersecurity": ("Njia za Tech #04 · Security", "Tech careers, explained"),
    "offline-first-apps": ("Jenga kwa Tanzania #04 · Offline", "Build for Tanzania"),
    "code-ya-wiki-03": ("Spot the bug · SQL", "Code ya Wiki #03"),
    "emails-that-get-replies": ("Recruiters · lecturers · clients", "Skills uni skips"),
    "how-whatsapp-keeps-messages-private": ("Inavyofanya kazi #04 · Encryption", "How it works"),
    "njia-za-tech-ui-ux": ("Njia za Tech #05 · Design", "Tech careers, explained"),
    "sms-still-wins": ("Jenga kwa Tanzania #05 · SMS", "Build for Tanzania"),
    "read-the-docs": ("Quickstart · reference · versions", "Skills uni skips"),
    "hiki-au-kile-02": ("Five match-ups · Career", "Hiki au Kile #02"),
    "njia-za-tech-mobile": ("Njia za Tech #06 · Mobile", "Tech careers, explained"),
    "how-ai-knows-things": ("Inavyofanya kazi #05 · AI", "How it works"),
    "estimate-your-time": ("Break down · buffer · speak early", "Skills uni skips"),
    "njia-za-tech-devops": ("Njia za Tech #07 · DevOps", "Tech careers, explained"),
    "njia-za-tech-it-support": ("Njia za Tech #08 · IT Support", "Tech careers, explained"),
    "njia-za-tech-product-manager": ("Njia za Tech #09 · Product", "Tech careers, explained"),
    "which-tech-path": ("Five questions · nine paths", "Njia za Tech · The finale"),
    "password-managers-and-2fa": ("Password manager · 2FA", "Stay safe · Usalama"),
    "code-ya-wiki-04": ("Spot the bug · Python", "Code ya Wiki #04"),
    "git-in-7-commands": ("init · add · commit · push", "Skills uni skips"),
    "kiswahili-in-your-app": ("Jenga kwa Tanzania #06 · Kiswahili", "Build for Tanzania"),
    "hiki-au-kile-03": ("Five match-ups · Tools", "Hiki au Kile #03"),
    "how-passwords-are-stored": ("Inavyofanya kazi #06 · Hashing", "How it works"),
    "ai-prompts-for-coding": ("Context · goal · constraints · format", "AI for students"),
    "kamusi-ya-tech-03": ("Maneno 8 ya internet", "Kamusi ya Tech · Toleo 03"),
    "plan-your-semester": ("15 weeks, one plan", "Semester 2 · Muhula wa pili"),
    "first-open-source-contribution": ("Fork · branch · pull request", "Skills uni skips"),
    "code-ya-wiki-05": ("Spot the bug · PHP security", "Code ya Wiki #05"),
    "sql-kwa-kiswahili": ("SELECT · WHERE · GROUP BY · JOIN", "Skills uni skips"),
    "apply-for-fpt-early": ("Documents · places · timeline", "FPT season · Msimu wa FPT"),
    "remote-work-real-vs-scam": ("Six red flags", "Stay safe · Usalama"),
}

slugs = sys.argv[1:] or list(POSTERS)
for slug in slugs:
    exp = os.path.join(STUDIO, slug, "export")
    if not os.path.exists(os.path.join(exp, "slide-1.jpg")):
        print("skip (no carousel yet):", slug)
        continue
    POST_URL = f"depriver.tech/blog/{slug}"
    kicker, label = POSTERS[slug]
    poster_from_cover(exp, slug, kicker, label)
    print("ok", slug)
