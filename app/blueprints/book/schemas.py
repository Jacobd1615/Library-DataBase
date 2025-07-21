# Book Data Schemas for Serialization and Validation
# This module defines Marshmallow schemas for validating and serializing book data.
# Ensures consistent JSON representation and data validation for book objects.

from app.extensions import ma
from app.models import Book


class BookSchema(ma.SQLAlchemyAutoSchema):
    """
    Auto-generated schema for Book model serialization and deserialization.
    Automatically creates fields based on the Book model's database columns.
    Handles conversion between Book objects and JSON representation.
    """

    class Meta:
        model = Book  # SQLAlchemy model to generate schema from
        load_instance = True  # Create model instances when deserializing
        include_fk = True  # Include foreign key fields in serialization


book_schema = BookSchema()
books_schema = BookSchema(many=True)
