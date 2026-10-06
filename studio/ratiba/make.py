"""Ratiba ya posts: the posting timetable as one designed calendar (1080x1350 and a 1080x1920 phone version,
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
}
START = dt.date(2026, 10, 5)   # Monday
WEEKS = 6


def render(name, height, top, ty, gy, cell_h, ly, blk, ts=140):
    s = poster_start(height, top, "Content calendar · Oct – Nov 2026")
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


render("ratiba-ya-posts", 1350, top=96, ty=215, gy=440, cell_h=90, ly=1028, blk=1065, ts=112)
render("ratiba-ya-posts-phone", 1920, top=210, ty=430, gy=700, cell_h=118, ly=1440, blk=1500)
print("ok")
