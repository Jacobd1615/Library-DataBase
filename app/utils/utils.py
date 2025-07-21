# JWT authentication utilities

from datetime import datetime, timedelta, timezone
from jose import jwt
import jose
from functools import wraps
from flask import request, jsonify, current_app
import os

SECRET_KEY = os.environ.get("SECRET_KEY") or "super secret secrets"


def token_required(f):
    """Decorator to protect routes with JWT token validation."""

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify({"messages": "Token is missing"}), 401

        try:
            data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            member_id = data["sub"]

        except jose.exceptions.ExpiredSignatureError:
            return jsonify({"messages": "Token has expired"}), 401
        except jose.exceptions.JWTError:
            return jsonify({"messages": "Token is invalid"}), 401

        return f(member_id, *args, **kwargs)

    return decorated


def encode_token(user_id):
    """Generate JWT token for user authentication."""
    payload = {
        "exp": datetime.now(timezone.utc) + timedelta(days=0, hours=1),
        "iat": datetime.now(timezone.utc),
        "sub": str(user_id),
    }

    token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
    return token
