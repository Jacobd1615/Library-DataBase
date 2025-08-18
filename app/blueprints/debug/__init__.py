from flask import Blueprint

debug_bp = Blueprint("debug", __name__)

from . import routes
