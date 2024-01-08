from flask import Flask, render_template,requests
import requests

app = Flask(__name__)

RUNESCAPE_API_BASE_URL = "https://apps.runescape.com/runemetrics/profile/profile?user=Auxxk"

RUNESCAPE_API_BASE2_URL = "&activities=2""

full_url = {RUNESCAPE_API_BASE_URL} 
{RUNESCAPE_API_BASE2_URL}
API_KEY = ''

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_player_stats", methods=["POST"])
def get_player_stats():
    if requests.method == "POST":
        player_name = requests.form.get("player_name")
        if player_name: 
            api_url = f"{RUNESCAPE_API_BASE_URL}{player_name}
            {RUNESCAPE_API_BASE2_URL}/json"
            try:
                response = requests.get(api_url)
                if response.status._code == 200:
                    player_data = response.json()
                    return render_template("player_stats.html",player_data=player_data)
                else:
                    return render_template("error.html,", message="Failed to retrieve player data.")
            except requests.RequestException
        else:
            return render_template("error.html", message = "please enter a player name")
if __name__ == "__main__":
    app.run(debug=true)