"""Njia za Tech #06: mobile developer. Content only: layout is studio/njia-za-tech/template.py."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())  # palette, fonts, Slide helpers
exec(open(os.path.join(STUDIO, "kit.py")).read())   # paper, print art, editorial tools

EP = {
    'num': 6,
    'slug': 'njia-za-tech-mobile',
    'role': 'Mobile Developer',
    'role_sw': 'Mjenzi wa apps za simu',
    'initials': 'MB',
    'sw': 'Tanzania inaishi kwenye simu',
    'cover_line': 'They build the apps on your phone, and in Tanzania, the phone is where people bank, learn and shop.',
    'one_line': "They build apps that live in people's pockets.",
    'what': 'They build Android and iOS apps that must work on slow networks, small screens and cheap phones, and still feel fast.',
    'duties': ['Build app screens and features', 'Make it work offline and on slow networks', 'Publish updates to the Play Store'],
    'analogy': 'A tailor making clothes for many body sizes: one app, hundreds of phone sizes and versions, all must fit.',
    'day': [   ('08:30', 'Stand-up with the team'),
    ('09:00', 'Build the new offline orders screen'),
    ('11:30', 'Test on a 2 GB RAM Android phone'),
    ('14:00', 'Fix a crash reported in the Play Console'),
    ('16:00', 'Prepare the next release for review')],
    'tools': [   ('Pick one road', ['Kotlin (Android)', 'Flutter (Dart)', 'React Native', 'Swift (iOS)']),
    ('Tools', ['Android Studio', 'Firebase', 'Git']),
    ('Skills', ['APIs / JSON', 'Offline storage', 'App store publishing'])],
    'like': ['Building things people carry everywhere', 'Making things fast on weak phones', 'Seeing your app in the Play Store'],
    'not_for': ['Your laptop has very little RAM (Android Studio is heavy)', 'You dislike testing on many devices'],
    'steps': [   ('Choose Flutter or Kotlin', 'Flutter for Android + iOS, Kotlin for Android only.'),
    ('Build 3 small apps', 'Calculator, notes, a list from an API.'),
    ('Add offline storage', "Save data when there's no network."),
    ('Publish one app', 'A Play Store link is a strong CV item.')],
    'first_project': 'A notes or budget app that works fully offline and syncs later.',
    'where': ['Fintech and mobile money', 'Banks', 'Startups', 'Agencies', 'Telecoms', 'Freelance and remote'],
    'where_note': 'Pay depends on skill, company and city. Ask people who do the job.',
    'question': ('Is mobile', 'your path?'),
}

exec(open(os.path.join(STUDIO, "njia-za-tech", "template.py")).read())
