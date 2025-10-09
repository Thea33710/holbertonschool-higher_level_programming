#!/usr/bin/python3

"""Flask application."""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    """A home method."""
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def get_data():
    """A method to get datas."""
    data = users = {
        "jane": {
            "username": "jane",
            "name": "Jane",
            "age": 28,
            "city": "Los Angeles"
        },
        "john": {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
