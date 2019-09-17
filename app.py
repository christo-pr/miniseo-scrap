from flask import Flask, jsonify, request
from flask_cors import CORS
from bs4 import BeautifulSoup as bs
import requests

import utils
import miniseo

app = Flask(__name__)
CORS(app)

@app.route('/seo', methods=['GET', 'POST'])
def scrap_site():
    try:
        url = request.args.get('url', '') if request.method == "GET" else request.get_json().get('url', '')
        valid_url = utils.validate_url(url)
        if not valid_url:
            return jsonify({ "status": 401, "data": "", "errors": ["Invalid URL"] })

        site = requests.get(url)
        soup = bs(site.text, 'html.parser')
        results = miniseo.collect(soup)

        return jsonify({ "status": 200, "data": results, "errors": [] })

    except Exception as e:
        print(e)
        return jsonify({ "status": 500, "data": "", "errors": ["Server error"] })
