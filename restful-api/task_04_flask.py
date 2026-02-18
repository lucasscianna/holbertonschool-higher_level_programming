#!/usr/bin/python3
"""
Module that implements a simple Flask API.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Root endpoint.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """
    Return list of all usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    API status endpoint.
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Return full user object by username.
    """
    user = users.get(username)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the API.
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
