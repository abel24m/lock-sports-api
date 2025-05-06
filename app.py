import json

from flask import Flask

app = Flask(__name__)

@app.route('/mlb_data')
def get_current_time():
    with open ("web_scrape/data_storage/covers_mlb_data_05-06-2025.json") as file:
        data = json.load(file)
    return data

@app.route('/test')
def get_nba_games():
    return "Testing this endpoint"