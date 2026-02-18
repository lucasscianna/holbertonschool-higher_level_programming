#!/usr/bin/python3
"""
Task 05 - API Security and Authentication Techniques

This module implements:
- Basic HTTP Authentication using Flask-HTTPAuth
- JWT Authentication using Flask-JWT-Extended
- Role-based access control
- Proper 401 handling for authentication errors
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
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
    """
    Verify user credentials for Basic Authentication.

    Args:
        username (str): Username provided.
        password (str): Password provided.

    Returns:
        str or None: Username if valid, otherwise None.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def basic_auth_error():
    """
    Handle Basic Authentication errors.

    Returns:
        tuple: JSON error message with 401 status.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Basic Auth protected route.

    Returns:
        str: Success message.
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate user and return JWT token.

    Expects JSON:
        {
            "username": "...",
            "password": "..."
        }

    Returns:
        JSON: Access token or error.
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 401

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    JWT protected route.

    Returns:
        str: Success message if token is valid.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Admin-only protected route.

    Returns:
        str or JSON: Success message or 403 error.
    """
    username = get_jwt_identity()
    user = users.get(username)

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_missing_token(error):
    """
    Handle missing JWT token.

    Returns:
        tuple: JSON error with 401.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(error):
    """
    Handle invalid JWT token.

    Returns:
        tuple: JSON error with 401.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    """
    Handle expired JWT token.

    Returns:
        tuple: JSON error with 401.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    """
    Handle revoked JWT token.

    Returns:
        tuple: JSON error with 401.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_fresh_token_required(jwt_header, jwt_payload):
    """
    Handle fresh token required error.

    Returns:
        tuple: JSON error with 401.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
