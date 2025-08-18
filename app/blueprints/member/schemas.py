from app.extensions import ma
from app.models import Member, db
from marshmallow import fields, Schema


class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class MemberSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Member
        load_instance = True
        sqla_session = db.session


member_schema = MemberSchema()
members_schema = MemberSchema(many=True)
login_schema = LoginSchema()
