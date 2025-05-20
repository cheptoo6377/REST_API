
from flask import Flask, jsonify
import requests

app = Flask(__name__)
API_URL = ' https://restfulcountries.com/api/v1'

@app.route('/countries',methods=['GET'])
def get_countries():
    response = requests.get(f"{API_URL}/countries")
    if response.status_code != 200:
        return jsonify({"error": "no countries found"}), 404
    country_data = response.json()
    return jsonify(country_data)


@app.route('/countries/<string:name>',methods=['GET'])
def get_country(name):
    response = requests.get(f"{API_URL}/name/{name}")
    if response.status_code != 200:
        return jsonify({"error": "no country name found"}), 404
    country_data = response.json()
    return jsonify(country_data)














if __name__ == '__main__':
    app.run(debug=True)