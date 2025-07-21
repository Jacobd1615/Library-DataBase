# Debug routes for development

from flask import jsonify
from . import debug_bp
from app.models import db, Member, Book, Loan
from faker import Faker
import random
from datetime import date


@debug_bp.route("/seed-database", methods=["POST"])
def seed_database():
    # Clear existing data and seed database with fake data for testing
    loan_book_table = db.metadata.tables["loan_book"]
    db.session.execute(loan_book_table.delete())

    db.session.query(Loan).delete()
    db.session.query(Member).delete()
    db.session.query(Book).delete()
    db.session.commit()

    faker = Faker()
    members = []
    books = []

    # Create 100 fake members
    for _ in range(100):
        member = Member(
            name=faker.name(),
            email=faker.unique.email(),
            DOB=faker.date_of_birth(minimum_age=18, maximum_age=70),
            password=faker.password(),
        )
        members.append(member)
        db.session.add(member)

    # Create 100 fake books
    for _ in range(100):
        book = Book(
            title=faker.catch_phrase(),
            author=faker.name(),
            genre=faker.word(
                ext_word_list=["Fiction", "Non-Fiction", "Sci-Fi", "Fantasy", "Mystery"]
            ),
            desc=faker.sentence(),
        )
        books.append(book)
        db.session.add(book)

    db.session.commit()

    # Create 100 fake loans
    for _ in range(100):
        loan = Loan(
            member_id=random.choice(members).id,
            loan_date=faker.date_between(start_date="-2y", end_date="today"),
        )
        num_books = random.randint(1, 3)
        loaned_books = random.sample(books, num_books)
        loan.books.extend(loaned_books)
        db.session.add(loan)

    db.session.commit()

    return (
        jsonify(
            {
                "message": "Database seeded successfully with 100 members, 100 books, and 100 loans."
            }
        ),
        200,
    )
