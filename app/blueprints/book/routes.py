# Book management routes

from .schemas import book_schema, books_schema
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from app.models import Book, db
from . import book_bp
from app.extensions import cache, limiter


@book_bp.route("/", methods=["POST"])
@limiter.limit("100/day;20/hour;5/minute")
def create_book():
    # Create a new book in the library collection
    json_data = request.get_json()
    if not json_data:
        return jsonify({"Error": "Request body must be JSON"}), 400

    try:
        new_book = book_schema.load(json_data)
    except ValidationError as e:
        return jsonify({"Error": e.messages}), 400

    db.session.add(new_book)
    db.session.commit()

    return book_schema.jsonify(new_book), 201


@book_bp.route("/", methods=["GET"])
@limiter.limit("100/day;20/hour;5/minute")
@cache.cached(timeout=60)
def get_books():
    # Retrieve all books with optional pagination
    try:
        page = int(request.args.get("page"))
        per_page = int(request.args.get("per_page"))
        query = select(Book)
        books = db.paginate(query, page=page, per_page=per_page)
        return books_schema.jsonify(books.items), 200
    except:
        query = select(Book)
        books = db.session.execute(query).scalars().all()
        return books_schema.jsonify(books), 200


@book_bp.route("/<int:book_id>", methods=["GET"])
@limiter.limit("100/day;20/hour;5/minute")
@cache.cached(timeout=60)
def get_book(book_id):
    # Retrieve a specific book by ID
    book = db.session.get(Book, book_id)
    if book:
        return book_schema.jsonify(book), 200
    return jsonify({"message": "Book not found"}), 404


@book_bp.route("/<int:book_id>", methods=["PUT"])
@limiter.limit("100/day;20/hour;5/minute")
def update_book(book_id):
    # Update an existing book's information
    query = select(Book).where(Book.id == book_id)
    book = db.session.execute(query).scalars().first()

    if book == None:
        return jsonify({"Error": "Book was not found"}), 404

    json_data = request.get_json()
    if not json_data:
        return jsonify({"Error": "Request body must be JSON"}), 400

    try:
        book_schema.load(json_data, partial=True)
    except ValidationError as e:
        return jsonify({"Error": e.messages}), 400

    for field, value in json_data.items():
        if hasattr(book, field):
            setattr(book, field, value)

    db.session.commit()
    return book_schema.jsonify(book), 200


@book_bp.route("/<int:book_id>", methods=["DELETE"])
@limiter.limit("100/day;20/hour;5/minute")
def delete_book(book_id):
    # Delete a book from the library collection
    query = select(Book).where(Book.id == book_id)
    book = db.session.execute(query).scalars().first()

    if book == None:
        return jsonify({"Error": "Book was not found"}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": f"Book with id: {book_id} deleted successfully"}), 200


@book_bp.route("/popular", methods=["GET"])
@limiter.limit("100/day;20/hour;5/minute")
def popluar_books():
    # Retrieve books sorted by popularity (number of loans)
    query = select(Book)
    books = list(db.session.execute(query).scalars().all())

    books.sort(key=lambda book: len(book.loans), reverse=True)

    return books_schema.jsonify(books)


@book_bp.route("/search", methods=["GET"])
def search_book():
    # Search for books by title
    title = request.args.get("title")

    query = select(Book).where(Book.title.like(f"%{title}%"))
    books = db.session.execute(query).scalars().all()

    return books_schema.jsonify(books)
