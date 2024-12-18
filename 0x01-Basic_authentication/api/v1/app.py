#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from typing import Literal

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# initialize the 'auth' variable
auth = None

# retrieve the AUTH_TYPE
auth_type = os.getenv("AUTH_TYPE")

# check the AUTH_TYPE
if auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()

# Define the list of paths that doesn't require authentication
excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized', '/api/v1/forbidden/']

@app.before_request
def before_request():
    """method to filter requests
    """
    if auth is None:
        pass

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def unauthorized(error) -> str:
    """_summary_

    Args:
        error (_type_): _description_

    Returns:
        str: _description_
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error) -> str:
    """ 
    forbidden error handling
    """
    return jsonify({"error": "Forbidden"}), 403

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
