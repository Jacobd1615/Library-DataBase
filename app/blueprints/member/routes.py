from .schemas import member_schema, members_schema, login_schema
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from app.models import Member, db
from . import member_bp
from app.extensions import limiter
from app.extensions import cache
from app.utils.utils import encode_token, token_required


# create a login token for a member
@member_bp.route("/login", methods=["POST"])
def login_member():
    if not request.is_json:
        return jsonify({"messages": "Request body must be JSON"}), 400
    try:
        # Validate the incoming JSON data against the LoginSchema
        credentials = login_schema.load(request.json)
    except ValidationError as e:
        # Return validation errors if the data is invalid
        return jsonify({"messages": e.messages}), 400

    # Query the database for a member with the provided email
    query = select(Member).where(Member.email == credentials["email"])
    member = db.session.execute(query).scalar_one_or_none()

    # Check if the member exists and the password is correct
    if member and member.password == credentials["password"]:
    
        auth_token = encode_token(member.id)

        response = {
            "status": "success",
            "message": "Successfully logged in.",
            "auth_token": auth_token,
        }
        return jsonify(response), 200
    else:
        # Return an error message if the email or password is not valid
        return jsonify({"messages": "Invalid email or password"}), 401


# Define the route for creating a new member via POST request
@member_bp.route("/", methods=["POST"])
@limiter.limit("10 per hour")  # Limit to 3 requests per hour per IP address
def create_member():
    # Ensure the request contains JSON data
    if not request.is_json or request.json is None:
        return {"error": "Request body must be JSON"}, 400
    try:
        # Validate and deserialize the incoming JSON data using the schema
        new_member = member_schema.load(request.json)
    except ValidationError as e:
        # Return validation errors if the data is invalid
        return {"errors": e.messages}, 400

    # Check if a member with the same email already exists in the database
    query = select(Member).where(Member.email == new_member.email)
    existing_member = db.session.execute(query).scalars().all()
    if existing_member:
        return {"error": "Email already exists"}, 400

    # Add the new member to the database session
    db.session.add(new_member)
    # Commit the transaction to save the member to the database
    db.session.commit()
    # Return the newly created member as a JSON response with a 201 status code
    return member_schema.jsonify(new_member), 201


# Get all members
@member_bp.route("/", methods=["GET"])
@limiter.limit("100/day;20/hour;5/minute")
@cache.cached(timeout=60)  # Cache the response for 60 seconds
def get_members():
    # Query all members from the database
    query = select(Member)
    members = db.session.execute(query).scalars().all()
    # return the list of members as a JSON response
    return members_schema.jsonify(members), 200


# Get a specific member
@member_bp.route("/<int:member_id>", methods=["GET"])
@limiter.limit("100/day;20/hour;5/minute")
def get_member(member_id):
    member = db.session.get(Member, member_id)

    if member:
        return member_schema.jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404


# Update a member using their ID from token
@member_bp.route("/", methods=["PUT"])
@limiter.limit("100/day;20/hour;5/minute")
@token_required
def update_member(token_member_id):
    member = db.session.get(Member, int(token_member_id))

    if not member:
        return jsonify({"error": "Member not found."}), 404

    if not request.json:
        return jsonify({"error": "Request body must be JSON"}), 400

    try:
        # Validate the incoming data
        member_schema.load(request.json, partial=True)
    except ValidationError as e:
        return jsonify(e.messages), 400

    # Update the member with the new data
    for key, value in request.json.items():
        if hasattr(member, key):
            setattr(member, key, value)

    db.session.commit()
    return member_schema.jsonify(member), 200


# Delete a member using their ID from token
@member_bp.route("/", methods=["DELETE"])
@token_required
def delete_member(requester_id):
    member = db.session.get(Member, int(requester_id))
    if not member:
        return jsonify({"error": "Member not found"}), 404

    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted member {requester_id}"}), 200
