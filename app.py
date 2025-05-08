import json
from datetime import datetime, timedelta

import schedule
from flask import Flask
from pathlib import Path

# from web_scrape import web_scraper
app = Flask(__name__)

today_date = datetime.now().strftime("%m-%d-%Y")
yesterday_date = (datetime.now() - timedelta(days=1)).strftime("%m-%d-%Y")



# Every Monday task() is called at 20:00
# schedule.every().day.at('10:00').do(web_scraper.initiate_web_scrape())

@app.route('/mlb_data')
def get_current_time():
    # schedule.run_pending()
    today_path = f"web_scrape/data_storage/covers_mlb_data_{today_date}.json"
    yesterday_path = f"web_scrape/data_storage/covers_mlb_data_{yesterday_date}.json"
    file = Path(today_path)
    if file.is_file():
        opened_file = open(today_path)
    else :
        opened_file = open(yesterday_path)
    data = json.load(opened_file)
    return data

@app.route('/test')
def get_nba_games():
    return "Testing this endpoint"