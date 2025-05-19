from flask import Flask, jsonify
import requests

app = Flask(__name__)
API_URL = 'https://jsonplaceholder.typicode.com'
@app.route('/')
def home():
    return "welcome to api"


@app.route('/posts')
def get_posts():
    response = requests.get(f'{API_URL}/posts')
    if response.status_code != 200:
        return jsonify({"error": "no posts found"}), 404
    return jsonify(response.json())
@app.route('/users')
def get_users():
    response = requests.get(f'{API_URL}/users')
    if response.status_code != 200:
        return jsonify({"error": "no users found"}), 404
    return jsonify(response.json())

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    response = requests.get(f'{API_URL}/users/{user_id}')
    if response.status_code != 200:
        return jsonify({"error": "user not found"}), 404
    user_data = response.json()
    return jsonify(user_data)

@app.route('/users/<int:user_id>/posts', methods=['GET'])
def user_posts(user_id):
    response = requests.get(f'{API_URL}/users/{user_id}/posts')
    if response.status_code != 200:
        return jsonify({'error': 'no posts for this user'}), 404
    user_data = response.json()
    return jsonify(user_data)
        


if __name__ == '__main__':
    app.run(debug=True)
    