# Loan management routes

from .schemas import loan_schema, loans_schema, edit_loan_schema
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from app.models import Loan, db, Book
from . import loan_bp
from app.extensions import limiter


@loan_bp.route("/", methods=["POST"])
@limiter.limit("100/day;20/hour;5/minute")
def create_loan():
    # Create a new loan transaction
    json_data = request.get_json()
    if not json_data:
        return jsonify({"Error": "No JSON data provided"}), 400

    try:
        loan_data = loan_schema.load(json_data)
    except ValidationError as e:
        return jsonify({"Error": e.messages}), 400

    new_loan = Loan(loan_date=loan_data["loan_date"], member_id=loan_data["member_id"])

    if "book_ids" in loan_data:
        for book_id in loan_data["book_ids"]:
            query = select(Book).where(Book.id == book_id)
            book = db.session.execute(query).scalar()
            if book:
                new_loan.books.append(book)
            else:
                return jsonify({"message": f"Invalid book id: {book_id}"}), 400

    db.session.add(new_loan)
    db.session.commit()
    return loan_schema.jsonify(new_loan), 200


@loan_bp.route("/", methods=["GET"])
@limiter.limit("100/day;20/hour;5/minute")
def get_loans():
    # Retrieve all loan records
    query = select(Loan)
    loans = db.session.execute(query).scalars().all()
    return loans_schema.jsonify(loans), 200


@loan_bp.route("/<int:loan_id>", methods=["GET"])
@limiter.limit("100/day;20/hour;5/minute")
def get_loan(loan_id):
    # Retrieve a specific loan by ID
    loan = db.session.get(Loan, loan_id)
    if loan:
        return loan_schema.jsonify(loan), 200
    return jsonify({"error": "Loan not found"}), 404


@loan_bp.route("/<int:loan_id>", methods=["DELETE"])
@limiter.limit("100/day;20/hour;5/minute")
def delete_loan(loan_id):
    # Delete a loan record (return all books)
    loan = db.session.get(Loan, loan_id)
    if not loan:
        return jsonify({"error": "Loan not found"}), 404

    db.session.delete(loan)
    db.session.commit()
    return jsonify({"message": f"Loan id: {loan_id} deleted successfully"}), 200


@loan_bp.route("/<int:loan_id>", methods=["PUT"])
@limiter.limit("100/day;20/hour;5/minute")
def edit_loan(loan_id):
    # Modify existing loan by adding or removing books
    json_data = request.get_json()
    if not json_data:
        return jsonify({"error": "No JSON data provided"}), 400

    try:
        loan_edits = edit_loan_schema.load(json_data)
    except ValidationError as e:
        return jsonify(e.messages), 400

    loan = db.session.get(Loan, loan_id)
    if not loan:
        return jsonify({"error": "Loan not found"}), 404

    # Add new books to the loan
    if "add_book_ids" in json_data:
        for book_id in json_data["add_book_ids"]:
            book = db.session.get(Book, book_id)
            if book and book not in loan.books:
                loan.books.append(book)

    # Remove books from the loan
    if "remove_book_ids" in json_data:
        for book_id in json_data["remove_book_ids"]:
            book = db.session.get(Book, book_id)
            if book and book in loan.books:
                loan.books.remove(book)

    db.session.commit()
    return loan_schema.jsonify(loan), 200
