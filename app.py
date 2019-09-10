from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/seo')
def scrap_site():
    site = request.args.get('site', None)
    if (site is None):
        return jsonify({ "status": 401, "data": "", "errors": ["Please provide a site"] })

    return jsonify({ "status": 200, "data": site, "errors": [] })
