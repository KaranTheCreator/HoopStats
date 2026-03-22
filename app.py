from flask import Flask, render_template, request
from metrics import get_player_stats

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    return render_template("metrics.html")

@app.route("/calculator")
def calculator():
    return render_template("calculator.html")

@app.route("/calculate-per", methods=["POST"])
def calculate_per():
    result = None
    stats = []
    name = None

    # Player stats form
    if "player_name" in request.form:
        player_name = request.form["player_name"]
        name, stats = get_player_stats(player_name)
        if not name:
            name = "Player not found"
            stats = []

    # PER calculator form
    else:
        points = float(request.form["points"])
        rebounds = float(request.form["rebounds"])
        assists = float(request.form["assists"])
        steals = float(request.form["steals"])
        blocks = float(request.form["blocks"])
        fga = float(request.form["fga"])
        fgm = float(request.form["fgm"])
        fta = float(request.form["fta"])
        ftm = float(request.form["ftm"])
        turnovers = float(request.form["turnovers"])

        result = (points + rebounds + assists + steals + blocks) - ((fga - fgm) + (fta - ftm) + turnovers)

    return render_template("calculator.html", stats=stats, name=name, result=result)

if __name__ == "__main__":
    app.run(debug=True)
