#!/usr/bin/python3

"""API Security and Authentication Techniques"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
import jwt
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify the password."""
    if username in users and check_password_hash(
        users[username]["password"], password
    ):
        return username
    return None


@auth.error_handler
def unauthorized_error():
    """Returns an error message."""
    return "Unauthorized access", 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Returns a success message."""
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def login():
    """Function to creat an account."""
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return "Missing username or password", 400

    username = data["username"]
    password = data["password"]

    if username not in users or not check_password_hash(
            users[username]["password"], password):
        return "Invalid credentials", 401

    access_token = create_access_token(
            identity={"username": username, "role": users[username]["role"]}
        )
    return {'access_token': access_token}, 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Returns a success message."""
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Verify if the user is an admin."""
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return "Admin access required", 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Missing or invalid token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Invalid token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Token has expired"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Token has been revoked"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Fresh token required"""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
