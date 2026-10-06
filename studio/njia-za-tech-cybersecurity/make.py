"""Njia za Tech #04: cybersecurity analyst. Content only: layout is studio/njia-za-tech/template.py."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 4,
    'slug': 'njia-za-tech-cybersecurity',
    'role': 'Cybersecurity Analyst',
    'role_sw': 'Mlinzi wa mifumo',
    'initials': 'CY',
    'sw': 'Walinzi wa ulimwengu wa kidijitali',
    'cover_line': "They protect systems, data and people from attacks. It's mostly defence, not movie-style hacking.",
    'one_line': 'They find weak spots and stop attacks before damage.',
    'what': ('They watch for strange activity, fix weak spots before criminals find them, and respond fast when something goes wrong. Most '
 'of the work is careful defence.'),
    'duties': ['Monitor systems for suspicious activity', 'Find and fix weaknesses', 'Train staff to avoid scams'],
    'analogy': 'The security guard of a bank: checks who comes in, watches the cameras, and knows exactly what to do in an emergency.',
    'day': [   ('08:00', 'Review overnight security alerts'),
    ('09:30', 'Investigate a suspicious login from abroad'),
    ('11:30', 'Check that servers have the latest updates'),
    ('14:00', 'Run a phishing awareness session for staff'),
    ('16:00', 'Write the incident report')],
    'tools': [   ('Foundations', ['Networking basics', 'Linux', 'How the web works']),
    ('Tools', ['Wireshark', 'Nmap', 'SIEM dashboards', 'Burp Suite']),
    ('Practice legally', ['TryHackMe', 'Hack The Box', 'CTF competitions'])],
    'like': ['Thinking like an attacker to defend better', 'Staying calm when things break', 'Learning new threats all the time'],
    'not_for': ["You want to “hack” people's accounts (that's a crime)", 'You dislike reading logs and rules'],
    'steps': [   ('Learn networking', 'IP, DNS, ports, HTTP. Everything starts here.'),
    ('Get comfortable with Linux', 'The terminal is your main tool.'),
    ('Practise on legal labs', 'TryHackMe beginner paths, never real systems.'),
    ('Join CTFs and write up', 'Your write-ups become your portfolio.')],
    'first_project': 'Secure your own home Wi-Fi and phone, then write what you changed and why.',
    'where': [   'Banks and mobile money',
    'Telecoms',
    'Government and regulators',
    'Audit and consulting firms',
    'Security companies',
    'Remote SOC teams'],
    'where_note': 'Pay depends on skill, certificates and sector. Ask people who do the job.',
    'question': ('Is security', 'your path?'),
}

exec(open(os.path.join(STUDIO, "njia-za-tech", "template.py")).read())
