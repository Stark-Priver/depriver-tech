"""Ratiba ya posts: the posting timetable as designed calendars, six weeks per page (four pages, Oct 2026 – Mar 2027) (1080x1350 and a 1080x1920 phone version,
exported at 2x). Six weeks, Monday to Sunday; carousels on Tue/Thu/Sat at 19:00, Swali la Wiki on Sundays.
Planning image for me, not a carousel (no blog post). Copied into ~/Pictures/Priver/Ratiba by hand or post-kit."""
import os
import datetime as dt
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())
exec(open(os.path.join(STUDIO, "kit.py")).read())
POST_URL = "depriver.tech/blog"
TOTAL = 1
exec(open(os.path.join(STUDIO, "editorial.py")).read())

KINDS = {"post": ORANGE, "swali": NAVY, "todo": (150, 158, 175), "event": GREEN_OK, "draft": (176, 62, 30)}
PLAN = {  # date: (short label, kind)
    "2026-10-06": ("FPT count", "post"), "2026-10-07": ("MUST talk", "event"), "2026-10-08": ("Talk recap", "draft"),
    "2026-10-10": ("Free tools", "post"), "2026-10-11": ("Swali #01", "swali"), "2026-10-13": ("Kamusi", "post"),
    "2026-10-15": ("FYP ideas", "post"), "2026-10-17": ("Tech gigs", "post"), "2026-10-18": ("Swali #02", "todo"),
    "2026-10-20": ("Scams", "post"), "2026-10-22": ("Laptops", "post"), "2026-10-24": ("GitHub", "post"),
    "2026-10-25": ("Swali #03", "todo"), "2026-10-27": ("CV", "post"), "2026-10-29": ("LinkedIn", "post"),
    "2026-10-31": ("Interview", "post"), "2026-11-01": ("Swali #04", "todo"), "2026-11-03": ("AI tutor", "post"),
    "2026-11-05": ("Data", "post"), "2026-11-07": ("Portfolio", "post"), "2026-11-08": ("Swali #05", "todo"),
    "2026-11-10": ("Group work", "post"), "2026-11-12": ("Betting", "post"),
    # post bank, 14 Nov 2026 → 13 Mar 2027 (studio/BANK.md)
    "2026-11-14": ("Myths", "post"),
    "2026-11-17": ("Exams", "post"),
    "2026-11-19": ("USSD", "post"),
    "2026-11-21": ("Code #01", "post"),
    "2026-11-24": ("Hackathon", "post"),
    "2026-11-26": ("Backend", "post"),
    "2026-11-28": ("M-money", "post"),
    "2026-12-01": ("Payments", "post"),
    "2026-12-03": ("Errors", "post"),
    "2026-12-05": ("Hiki #01", "post"),
    "2026-12-08": ("Frontend", "post"),
    "2026-12-10": ("Pricing", "post"),
    "2026-12-12": ("Holiday", "post"),
    "2026-12-15": ("URL", "post"),
    "2026-12-17": ("Light apps", "post"),
    "2026-12-19": ("Code #02", "post"),
    "2026-12-22": ("Data", "post"),
    "2026-12-24": ("Quiz", "post"),
    "2026-12-26": ("SIM swap", "post"),
    "2026-12-29": ("2027 plan", "post"),
    "2026-12-31": ("Kamusi 02", "post"),
    "2027-01-02": ("Terminal", "post"),
    "2027-01-05": ("Security", "post"),
    "2027-01-07": ("Offline", "post"),
    "2027-01-09": ("Code #03", "post"),
    "2027-01-12": ("Emails", "post"),
    "2027-01-14": ("WhatsApp", "post"),
    "2027-01-16": ("UI/UX", "post"),
    "2027-01-19": ("SMS", "post"),
    "2027-01-21": ("Docs", "post"),
    "2027-01-23": ("Hiki #02", "post"),
    "2027-01-26": ("Mobile", "post"),
    "2027-01-28": ("How AI", "post"),
    "2027-01-30": ("Estimates", "post"),
    "2027-02-02": ("DevOps", "post"),
    "2027-02-04": ("IT support", "post"),
    "2027-02-06": ("Product", "post"),
    "2027-02-09": ("Path quiz", "post"),
    "2027-02-11": ("2FA", "post"),
    "2027-02-13": ("Code #04", "post"),
    "2027-02-16": ("Git", "post"),
    "2027-02-18": ("Kiswahili", "post"),
    "2027-02-20": ("Hiki #03", "post"),
    "2027-02-23": ("Hashing", "post"),
    "2027-02-25": ("Prompts", "post"),
    "2027-02-27": ("Kamusi 03", "post"),
    "2027-03-02": ("Semester", "post"),
    "2027-03-04": ("Open src", "post"),
    "2027-03-06": ("Code #05", "post"),
    "2027-03-09": ("SQL", "post"),
    "2027-03-11": ("FPT early", "post"),
    "2027-03-13": ("Job scams", "post"),
    "2026-11-15": ("Swali", "todo"),
    "2026-11-22": ("Swali", "todo"),
    "2026-11-29": ("Swali", "todo"),
    "2026-12-06": ("Swali", "todo"),
    "2026-12-13": ("Swali", "todo"),
    "2026-12-20": ("Swali", "todo"),
    "2026-12-27": ("Swali", "todo"),
    "2027-01-03": ("Swali", "todo"),
    "2027-01-10": ("Swali", "todo"),
    "2027-01-17": ("Swali", "todo"),
    "2027-01-24": ("Swali", "todo"),
    "2027-01-31": ("Swali", "todo"),
    "2027-02-07": ("Swali", "todo"),
    "2027-02-14": ("Swali", "todo"),
    "2027-02-21": ("Swali", "todo"),
    "2027-02-28": ("Swali", "todo"),
    "2027-03-07": ("Swali", "todo"),
    "2027-03-14": ("Swali", "todo"),
}
WEEKS = 6
PAGES = [(dt.date(2026, 10, 5), "Oct – Nov 2026", ""), (dt.date(2026, 11, 16), "Nov – Dec 2026", "-2"),
         (dt.date(2026, 12, 28), "Dec 2026 – Feb 2027", "-3"), (dt.date(2027, 2, 8), "Feb – Mar 2027", "-4")]


def render(name, height, top, ty, gy, cell_h, ly, blk, ts=140, START=None, span=""):
    s = poster_start(height, top, "Content calendar · " + span)
    s.text(M - 6, ty, "Ratiba", f(BOLD, ts), NAVY)
    s.text(M - 6, ty + ts * 0.83, "ya posts.", f(BOLD, ts * 0.79), ORANGE)
    s.text(M, ty + ts * 1.42, "Post moja kwa wakati wake", f(SIG, 50), NAVY)
    swash(s, M + 8, M + 500, ty + ts * 1.42 + 24, ORANGE, 6)
    cw = (W - 2 * M) / 7
    for i, d in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]):
        smallcaps(s, M + i * cw + 10, gy - 16, d, 15, ORANGE if d in ("Tue", "Thu", "Sat") else NAVY if d == "Sun" else GREY)
    for w in range(WEEKS):
        for i in range(7):
            day = START + dt.timedelta(days=w * 7 + i)
            x0, y0 = M + i * cw, gy + w * cell_h
            box = [k(x0 + 3), k(y0 + 3), k(x0 + cw - 3), k(y0 + cell_h - 3)]
            item = PLAN.get(day.isoformat())
            s.d.rounded_rectangle(box, radius=k(12), fill=(255, 255, 255) if item else (238, 241, 246),
                                  outline=NAVY if item else (214, 219, 230), width=k(2.5 if item else 1.5))
            s.text(x0 + 14, y0 + 36, str(day.day), f(BOLD if item else MED, 24), NAVY if item else (150, 158, 175))
            if day.day == 1 or (w == 0 and i == 0):
                s.text(x0 + cw - 14, y0 + 34, day.strftime("%b"), f(SEMI, 16), ORANGE, anchor="rs")
            if item:
                lab, kind = item
                col = KINDS[kind]
                s.d.rounded_rectangle([k(x0 + 10), k(y0 + cell_h - 52), k(x0 + cw - 10), k(y0 + cell_h - 14)], radius=k(10), fill=col)
                s.text(x0 + cw / 2, y0 + cell_h - 32, lab, f(BOLD, fit(s, lab, BOLD, 17, cw - 30)), WHITE_T, anchor="mm")
    x = M
    for lab, kind in [("Carousel · 19:00", "post"), ("Swali la Wiki", "swali"), ("To make", "todo"), ("Event", "event"), ("Needs photos", "draft")]:
        s.d.rounded_rectangle([k(x), k(ly - 18), k(x + 26), k(ly + 8)], radius=k(6), fill=KINDS[kind])
        s.text(x + 36, ly + 4, lab, f(SEMI, 19), NAVY)
        x += 36 + s.width(lab, f(SEMI, 19)) + 28
    global POST_URL
    poster_end(s, blk, "Tue · Thu · Sat carousels · Sunday Swali la Wiki", name)


for start, span, suf in PAGES:
    render("ratiba-ya-posts" + suf, 1350, top=96, ty=215, gy=440, cell_h=90, ly=1028, blk=1065, ts=112, START=start, span=span)
    render("ratiba-ya-posts-phone" + suf, 1920, top=210, ty=430, gy=700, cell_h=118, ly=1440, blk=1500, START=start, span=span)
print("ok")
