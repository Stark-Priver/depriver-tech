"""Njia za Tech #07: devops engineer. Content only: layout is studio/njia-za-tech/template.py."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 7,
    'slug': 'njia-za-tech-devops',
    'role': 'DevOps Engineer',
    'role_sw': 'Mhandisi wa uendeshaji',
    'initials': 'DO',
    'sw': 'Mfumo usilale hata usiku',
    'cover_line': 'They keep systems online and help teams release new code safely, quickly and often.',
    'one_line': 'They keep apps online and releases smooth.',
    'what': 'They set up servers and cloud, automate testing and deployment, and get alerted first when the system goes down at 2 a.m.',
    'duties': ['Automate builds, tests and deploys', 'Manage servers and cloud', 'Monitor uptime and fix outages'],
    'analogy': 'The engineer of a bus company: keeps the buses serviced, the routes running, and fixes breakdowns fast.',
    'day': [   ('08:30', 'Check the overnight uptime and alerts'),
    ('09:30', 'Fix a failing deploy pipeline'),
    ('11:30', 'Move an app into Docker'),
    ('14:00', 'Set up backups and test a restore'),
    ('16:00', 'Write the runbook for the on-call team')],
    'tools': [   ('Foundations', ['Linux', 'Networking', 'Bash scripting']),
    ('Tools', ['Docker', 'GitHub Actions', 'Nginx', 'Kubernetes']),
    ('Cloud', ['AWS', 'Google Cloud', 'Azure', 'Monitoring'])],
    'like': ['Automating boring, repeated work', 'Understanding how all the parts connect', 'Solving problems under pressure'],
    'not_for': ['You hate the terminal', 'You never want to be woken by an alert'],
    'steps': [   ('Learn Linux properly', 'Files, permissions, services, SSH.'),
    ('Deploy an app by hand', 'A cheap VPS, Nginx, a domain.'),
    ('Then containerise it', 'Put the same app in Docker.'),
    ('Automate with CI/CD', 'GitHub Actions: test and deploy on push.')],
    'first_project': 'Deploy your portfolio with Docker and auto-deploy it on every git push.',
    'where': ['Banks and fintech', 'Telecoms', 'Software houses', 'Hosting and data centres', 'Startups', 'Remote teams'],
    'where_note': 'Pay depends on skill, certificates and company. Ask people who do the job.',
    'question': ('Is DevOps', 'your path?'),
}

exec(open(os.path.join(STUDIO, "njia-za-tech", "template.py")).read())
