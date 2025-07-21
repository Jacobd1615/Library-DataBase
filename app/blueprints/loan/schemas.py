# Loan Data Schemas for Serialization and Validation
# This module defines Marshmallow schemas for validating and serializing loan data.
# Handles complex relationships between members, books, and loan transactions.

from app.extensions import ma
from app.models import Loan, db
from marshmallow import fields
from app.blueprints.member.schemas import MemberSchema
from app.blueprints.book.schemas import BookSchema


class LoanSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for Loan model serialization and deserialization.
    Handles the complex many-to-many relationship between loans and books,
    as well as the relationship with members.
    """

    member_id = fields.Int(required=True, load_only=True)  # Required for creating loans
    book_ids = fields.List(
        fields.Int(), required=True, load_only=True
    )  # List of book IDs to loan
    member = fields.Nested(MemberSchema, dump_only=True)  # Member details in response
    books = fields.Nested(
        BookSchema, many=True, dump_only=True
    )  # Book details in response

    class Meta:
        model = Loan
        load_instance = False  # Avoid object creation issues with complex relationships
        sqla_session = db.session
        include_fk = True


class EditLoanSchema(ma.Schema):
    """
    Schema for editing existing loans.
    Allows adding or removing books from an existing loan transaction.
    """

    add_book_ids = fields.List(fields.Int())  # Book IDs to add to the loan
    remove_book_ids = fields.List(fields.Int())  # Book IDs to remove from the loan


loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)
edit_loan_schema = EditLoanSchema()
