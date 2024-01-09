from flask import Flask, jsonify, request
import requests
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route('/')
def get_data():
    response = requests.get('https://secure.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=1042')

    home = response.json()

    return home
if __name__ == '__main__':
    app.run(debug=True)
