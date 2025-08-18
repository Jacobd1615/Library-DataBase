from app.extensions import ma
from app.models import Loan, db
from marshmallow import fields
from app.blueprints.member.schemas import MemberSchema
from app.blueprints.book.schemas import BookSchema


class LoanSchema(ma.SQLAlchemyAutoSchema):
    member_id = fields.Int(required=True, load_only=True)
    book_ids = fields.List(fields.Int(), required=True, load_only=True)
    member = fields.Nested(MemberSchema, dump_only=True)
    books = fields.Nested(BookSchema, many=True, dump_only=True)

    class Meta:
        model = Loan
        load_instance = False  # Set to False to avoid object creation issues
        sqla_session = db.session
        include_fk = True


class EditLoanSchema(ma.Schema):
    add_book_ids = fields.List(fields.Int())
    remove_book_ids = fields.List(fields.Int())


loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)
edit_loan_schema = EditLoanSchema()
