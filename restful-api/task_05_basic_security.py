#!/usr/bin/python3

"""API Security and Authentication Techniques"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-me'

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
    user = users.get(username)
    if not user:
        return False
    return check_password_hash(user['password'], password)


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username, None)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Bad username or password"}), 401

    additional_claims = {"role": user["role"]}
    access_token = create_access_token(
        identity=username,
        additional_claims=additional_claims
    )
    return jsonify(access_token=access_token), 200


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    claims = get_jwt()
    role = claims.get("role", None)
    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify({"error": "Missing Authorization Header"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(callback):
    return jsonify({"error": "Invalid Token"}), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token expired"}), 401


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token revoked"}), 401


@jwt.needs_fresh_token_loader
def needs_fresh_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


@jwt.user_lookup_error_loader
def user_lookup_error_callback(jwt_header, jwt_payload):
    return jsonify({"error": "User not found"}), 401


if __name__ == "__main__":
    app.run(debug=True)
