from datetime import datetime, timedelta, timezone
from jose import jwt
import jose
from functools import wraps
from flask import request, jsonify, current_app


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify({"messages": "Token is missing"}), 401
        try:
            # Decode the token to get the user information
            data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            member_id = data["sub"]  # Extract user ID from token

        except jose.exceptions.ExpiredSignatureError:
            return jsonify({"messages": "Token has expired"}), 401
        except jose.exceptions.JWTError:
            return jsonify({"messages": "Token is invalid"}), 401

        return f(member_id, *args, **kwargs)

    return decorated


def encode_token(user_id):  # Encode a JWT token with an expiration time
    payload = {
        "exp": datetime.now(timezone.utc)
        + timedelta(days=0, hours=1),  # Expiration time
        "iat": datetime.now(timezone.utc),  # Issued at time
        "sub": str(user_id),  # Subject (user ID)
    }

    token = jwt.encode(
        payload, current_app.config["SECRET_KEY"], algorithm="HS256"
    )  # Encode the payload into a JWT token
    return token
