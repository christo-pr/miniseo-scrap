from flask import Flask, jsonify, request
from bs4 import BeautifulSoup as bs
import requests

import utils
import miniseo

app = Flask(__name__)

@app.route('/seo')
def scrap_site():
    try:
        url = request.args.get('url', None)
        valid_url = utils.validate_url(url)
        if not valid_url:
            return jsonify({ "status": 401, "data": "", "errors": ["Error on the url."] })

        site = requests.get(url)
        soup = bs(site.text, 'html.parser')
        results = miniseo.collect(soup)

        return jsonify({ "status": 200, "data": results, "errors": [] })

    except Exception as e:
        print(e)
        return jsonify({ "status": 500, "data": "", "errors": ["Server error"] })
