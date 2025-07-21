# Book Blueprint Initialization
# This module creates and configures the Flask blueprint for book-related routes.
# Handles all book management functionality including CRUD operations and search.

from flask import Blueprint

book_bp = Blueprint("books", __name__)

from . import routes
