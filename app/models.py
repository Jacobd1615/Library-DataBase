# Import necessary components from Flask-SQLAlchemy, SQLAlchemy ORM, and Python's standard libraries.
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import date
from typing import List


# Defines a base class for all SQLAlchemy models.
class Base(DeclarativeBase):
    pass


# Initializes the SQLAlchemy extension.
db = SQLAlchemy(model_class=Base)

loan_book = db.Table(
    "loan_book",
    Base.metadata,
    db.Column("loan_id", db.ForeignKey("loans.id")),
    db.Column("book_id", db.ForeignKey("books.id"))
)

class Member(Base):
    __tablename__ = "members"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    email: Mapped[str] = mapped_column(db.String(150), unique=True, nullable=False)
    DOB: Mapped[date] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(db.String(100), nullable=False)

    loans: Mapped[List["Loan"]] = relationship("Loan", back_populates="member", cascade="all, delete")

class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True)
    loan_date: Mapped[date]
    member_id: Mapped[int] = mapped_column(db.ForeignKey("members.id"), nullable=False)

    member: Mapped["Member"] = db.relationship(back_populates="loans")
    books: Mapped[List["Book"]] = db.relationship(secondary=loan_book, back_populates="loans")

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(db.String(100), nullable=False)
    genre: Mapped[str] = mapped_column(db.String(50), nullable=False)
    desc: Mapped[str] = mapped_column(db.String(255), nullable=False)
    title: Mapped[str] = mapped_column(db.String(100), nullable=False)

    loans: Mapped[List["Loan"]] = db.relationship(secondary=loan_book, back_populates="books")