#!/usr/bin/python3

"""Flask application."""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """A home method."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """A method to get datas."""
    username = list(users.keys())
    return jsonify(username)


@app.route('/status')
def new_status():
    """Checks if it works."""
    return "OK"


@app.route('/users/<username>')
def user(username):
    """Show the user if he exists"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})


@app.route('/add_user', methods=["POST"])
def add_user():
    """Add a user."""
     data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = {
        "username": username,
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
