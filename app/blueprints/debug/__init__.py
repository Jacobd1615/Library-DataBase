# Debug Blueprint Initialization
# This module creates the Flask blueprint for debug and development utilities.
# Only available in development environment for testing and debugging purposes.

from flask import Blueprint

debug_bp = Blueprint("debug", __name__)

from . import routes
