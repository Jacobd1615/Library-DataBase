# Member management routes

from .schemas import (
    member_schema,
    members_schema,
    login_schema,
)
from flask import (
    request,
    jsonify,
)
from marshmallow import ValidationError
from sqlalchemy import select
from app.models import Member, db
from . import member_bp
from app.extensions import limiter
from app.extensions import cache
from app.utils.utils import encode_token, token_required


@member_bp.route("/login", methods=["POST"])
def login_member():
    # Authenticate a member and return a JWT token
    if not request.is_json:
        return jsonify({"messages": "Request body must be JSON"}), 400

    try:
        credentials = login_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"messages": e.messages}), 400

    query = select(Member).where(Member.email == credentials["email"])
    member = db.session.execute(query).scalar_one_or_none()

    if member and member.password == credentials["password"]:
        auth_token = encode_token(member.id)

        response = {
            "status": "success",
            "message": "Successfully logged in.",
            "auth_token": auth_token,
        }
        return jsonify(response), 200
    else:
        return jsonify({"messages": "Invalid email or password"}), 401


@member_bp.route("/", methods=["POST"])
@limiter.limit("10 per hour")
def create_member():
    # Create a new library member account
    if not request.is_json or request.json is None:
        return {"error": "Request body must be JSON"}, 400

    try:
        new_member = member_schema.load(request.json)
    except ValidationError as e:
        return {"errors": e.messages}, 400

    query = select(Member).where(Member.email == new_member.email)
    existing_member = db.session.execute(query).scalars().all()
    if existing_member:
        return {"error": "Email already exists"}, 400

    db.session.add(new_member)
    db.session.commit()
    return member_schema.jsonify(new_member), 201


@member_bp.route("/", methods=["GET"])
@limiter.limit("100/day;20/hour;5/minute")
@cache.cached(timeout=60)
def get_members():
    # Retrieve all library members
    query = select(Member)
    members = db.session.execute(query).scalars().all()
    return members_schema.jsonify(members), 200


@member_bp.route("/<int:member_id>", methods=["GET"])
@limiter.limit("100/day;20/hour;5/minute")
def get_member(member_id):
    # Retrieve a specific member by ID
    member = db.session.get(Member, member_id)

    if member:
        return member_schema.jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404


@member_bp.route("/", methods=["PUT"])
@limiter.limit("100/day;20/hour;5/minute")
@token_required
def update_member(token_member_id):
    # Update member information for the authenticated user
    member = db.session.get(Member, int(token_member_id))

    if not member:
        return jsonify({"error": "Member not found."}), 404

    if not request.json:
        return jsonify({"error": "Request body must be JSON"}), 400

    try:
        member_schema.load(request.json, partial=True)
    except ValidationError as e:
        return jsonify(e.messages), 400

    for key, value in request.json.items():
        if hasattr(member, key):
            setattr(member, key, value)

    db.session.commit()
    return member_schema.jsonify(member), 200


@member_bp.route("/", methods=["DELETE"])
@token_required
def delete_member(requester_id):
    # Delete the authenticated member's account
    member = db.session.get(Member, int(requester_id))
    if not member:
        return jsonify({"error": "Member not found"}), 404

    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted member {requester_id}"}), 200
