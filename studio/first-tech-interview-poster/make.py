"""Feed poster (1080x1350) and status (1080x1920) for first-tech-interview, exported at 2x, built from the carousel cover
(run the carousel first). Status keeps clear of the top/bottom app overlays."""
import os
STUDIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "export") + "/"
os.makedirs(OUT, exist_ok=True)
ART_STYLE = "print"
exec(open(os.path.join(STUDIO, "base.py")).read())
exec(open(os.path.join(STUDIO, "kit.py")).read())
POST_URL = "depriver.tech/blog/first-tech-interview"
TOTAL = 1
exec(open(os.path.join(STUDIO, "editorial.py")).read())
poster_from_cover(os.path.join(STUDIO, "first-tech-interview", "export"), "first-tech-interview", "5 questions · how to answer · follow-up", "For students & fresh graduates")
print("ok")
