from flask import Blueprint


loan_bp = Blueprint("loans", __name__)

from . import routes