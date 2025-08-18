from .schemas import book_schema, books_schema
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from app.models import Book, db
from . import book_bp
from app.extensions import cache, limiter


# Route to create a new book
@book_bp.route("", methods=["POST"])
@limiter.limit("100/day;20/hour;5/minute")
def create_book():
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


# Route to get all books
@book_bp.route("", methods=["GET"])
@limiter.limit("100/day;20/hour;5/minute")
@cache.cached(timeout=60)  # Cache the response for 60 seconds
def get_books():
    try:
        page_raw = request.args.get("page", "1")
        per_page_raw = request.args.get("per_page", "10")
        page = int(page_raw)
        per_page = int(per_page_raw)
        if page < 1 or per_page < 1:
            raise ValueError
        query = select(Book)
        books = db.paginate(query, page=page, per_page=per_page)
        return books_schema.jsonify(books.items), 200
    except:
        query = select(Book)
        books = db.session.execute(query).scalars().all()
        return books_schema.jsonify(books), 200


# Route to get a specific book by ID
@book_bp.route("/<int:book_id>", methods=["GET"])
@limiter.limit("100/day;20/hour;5/minute")
@cache.cached(timeout=60)  # Cache the response for 60 seconds
def get_book(book_id):
    book = db.session.get(Book, book_id)
    if book:
        return book_schema.jsonify(book), 200
    return jsonify({"message": "Book not found"}), 404


# Route to update a book by ID
@book_bp.route("/<int:book_id>", methods=["PUT"])
@limiter.limit("100/day;20/hour;5/minute")
def update_book(book_id):
    query = select(Book).where(Book.id == book_id)
    book = db.session.execute(query).scalars().first()

    if book == None:
        return jsonify({"Error": "Book was not found"}), 404

    json_data = request.get_json()
    if not json_data:
        return jsonify({"Error": "Request body must be JSON"}), 400
    try:
        # Validate the data
        book_schema.load(json_data, partial=True)
    except ValidationError as e:
        return jsonify({"Error": e.messages}), 400

    for field, value in json_data.items():
        if hasattr(book, field):
            setattr(book, field, value)

    db.session.commit()
    return book_schema.jsonify(book), 200


# Route to delete a book by ID
@book_bp.route("/<int:book_id>", methods=["DELETE"])
@limiter.limit("100/day;20/hour;5/minute")
def delete_book(book_id):
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
    query = select(Book)
    books = list(db.session.execute(query).scalars().all())

    books.sort(key=lambda book: len(book.loans), reverse=True)

    return books_schema.jsonify(books)


@book_bp.route("/search", methods=["GET"])
def search_book():
    title = request.args.get("title")

    query = select(Book).where(Book.title.like(f"%{title}%"))
    books = db.session.execute(query).scalars().all()

    return books_schema.jsonify(books)
