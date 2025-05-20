
from flask import Flask, jsonify
import requests

app = Flask(__name__)
API_URL = 'https://restcountries.com/v3.1'

@app.route('/countries', methods=['GET'])

def get_countries():
    response = requests.get(f"https://restcountries.com/v3.1/countries")
    if response.status_code != 200:
        return jsonify({"error": "no countries found"}), 404
    country_data = response.json()
    return jsonify(country_data)
    





@app.route('/countries/<country_name>', methods=['GET'])
def get_country_by_name(country_name):
    response = requests.get(f"https://restcountries.com/v3.1/countries/{country_name}")
    if response.status_code != 200:
        return jsonify({"error": "no country found"}), 404
    return jsonify(response.json())

    









if __name__ == '__main__':
    app.run(debug=True)