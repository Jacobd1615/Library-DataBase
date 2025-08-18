from flask import Blueprint


book_bp = Blueprint("books", __name__)

from . import routes