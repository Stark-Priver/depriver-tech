"""Njia za Tech #08: it support specialist. Content only: layout is studio/njia-za-tech/template.py."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 8,
    'slug': 'njia-za-tech-it-support',
    'role': 'IT Support Specialist',
    'role_sw': 'Mtaalamu wa msaada wa IT',
    'initials': 'IT',
    'sw': 'Mlango wa kwanza wa tech',
    'cover_line': "They keep computers, networks and people working. It's one of the most common first jobs in tech.",
    'one_line': 'They keep people, computers and networks working.',
    'what': ("When the printer fails, the email won't open or the network is down, IT support fixes it, and teaches people how to avoid it "
 'next time.'),
    'duties': ['Fix computers, printers and accounts', 'Set up networks and new staff', 'Keep backups and antivirus up to date'],
    'analogy': 'The family doctor of an office: sees every problem first, fixes most, and knows when to call a specialist.',
    'day': [   ('08:00', 'Set up a laptop for a new staff member'),
    ('09:30', 'Fix Wi-Fi in the meeting room'),
    ('11:00', 'Reset passwords and email problems'),
    ('14:00', "Check that last night's backup worked"),
    ('15:30', 'Log every ticket and how it was solved')],
    'tools': [   ('Foundations', ['Windows & Linux', 'Networking basics', 'Hardware']),
    ('Tools', ['Microsoft 365 / Google Workspace', 'Active Directory', 'Ticket systems']),
    ('Skills', ['Patience', 'Explaining simply', 'Writing notes'])],
    'like': ['Helping people every day', 'Fixing hardware and networks', 'A job you can start soon after college'],
    'not_for': ["You don't enjoy talking to people", 'You want to only write code'],
    'steps': [   ('Learn PC hardware', 'Open one, name the parts, rebuild it.'),
    ('Learn networking basics', 'IP, DHCP, DNS, routers, cables.'),
    ('Practise on real problems', 'Help family, a school or a church office.'),
    ('Keep a fix log', "Problem, cause, fix. It's your portfolio.")],
    'first_project': 'Set up and document a small office network for a shop or school.',
    'where': ['Schools and universities', 'Hospitals', 'Banks and offices', 'Government offices', 'NGOs', 'IT service companies'],
    'where_note': 'Pay depends on employer and city. A good start that grows into networks or security.',
    'question': ('Is IT support', 'your path?'),
}

exec(open(os.path.join(STUDIO, "njia-za-tech", "template.py")).read())
