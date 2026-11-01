from flask import Flask
from datetime import date

app = Flask(__name__)

BONETIDER = {
    1: ("04:50", "11:40", "13:24", "15:59", "18:04"),
    2: ("04:52", "11:40", "13:22", "15:56", "18:02"),
    3: ("04:54", "11:40", "13:20", "15:53", "17:59"),
    4: ("04:57", "11:40", "13:18", "15:50", "17:57"),
    5: ("04:59", "11:40", "13:17", "15:48", "17:55"),
    6: ("05:01", "11:40", "13:15", "15:45", "17:53"),
    7: ("05:03", "11:40", "13:13", "15:42", "17:51"),
    25: ("05:39", "11:44", "12:45", "15:01", "17:21"),
    26: ("05:41", "11:44", "12:44", "14:59", "17:20"),
    27: ("05:42", "11:44", "12:43", "14:57", "17:19"),
    28: ("05:44", "11:44", "12:42", "14:55", "17:18"),
    29: ("05:46", "11:45", "12:41", "14:54", "17:17"),
    30: ("05:47", "11:45", "12:41", "14:52", "17:16"),
}

@app.route("/")
def home():
    idag = date.today()
    tider = ""

    if idag.year == 2026 and idag.month == 11 and 1 <= idag.day <= 7:
        dagens = BONETIDER.get(idag.day)
    else:
        dagens = None

    namn = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

    if dagens:
        for namn_i, tid in zip(namn, dagens):
            tider += f"<div class='tid'><span>{namn_i}</span><strong>{tid}</strong></div>"
    else:
        tider = "<p>Kontrollera moskéns officiella bönetider.</p>"

    return f"""
<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Söderhamns moskén / Ibrahim</title>
<style>
* {{ box-sizing: border-box; }}
body {{
    margin: 0;
    background: #071b18;
    color: white;
    font-family: Arial, sans-serif;
}}
header {{
    text-align: center;
    padding: 55px 20px;
    background: linear-gradient(135deg, #064e3b, #092c27);
    border-bottom: 2px solid #c9a85b;
}}
header h1 {{ color: #f5d78e; font-size: 34px; }}
nav {{
    display: flex;
    justify-content: center;
    gap: 25px;
    padding: 18px;
    background: #10352d;
    flex-wrap: wrap;
}}
nav a {{ color: #f5d78e; text-decoration: none; }}
main {{ max-width: 750px; margin: 30px auto; padding: 20px; }}
.card {{
    background: #10352d;
    border: 1px solid #c9a85b;
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 20px;
}}
h2 {{ color: #f5d78e; }}
.tid {{
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #ffffff22;
    padding: 13px 5px;
    font-size: 18px;
}}
footer {{ text-align: center; padding: 25px; color: #b7c9c1; }}
</style>
</head>
<body>
<header>
    <h1>🕌 Söderhamns moskén / Ibrahim</h1>
    <p>Välkommen till vår moské</p>
    <p>{idag.strftime("%d-%m-%Y")}</p>
</header>

<nav>
    <a href="#bonetider">Bönetider</a>
    <a href="#om">Om moskén</a>
</nav>

<main>
    <section class="card" id="bonetider">
        <h2>Dagens bönetider</h2>
        {tider}
        <p><a style="color:#f5d78e"
        href="https://soderhamns-moske-kulturforening.azurewebsites.net/PrayerTimes"
        target="_blank">Öppna officiella bönetider</a></p>
    </section>

    <section class="card" id="om">
        <h2>Om moskén</h2>
        <p>En plats för gemenskap, bön och kunskap.</p>
    </section>
</main>

<footer>Söderhamns moskén / Ibrahim · Välkommen</footer>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=False)