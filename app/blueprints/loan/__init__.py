# Loan Blueprint Initialization
# This module creates and configures the Flask blueprint for loan-related routes.
# Handles all loan management functionality including borrowing and returning books.

from flask import Blueprint

loan_bp = Blueprint("loans", __name__)

from . import routes
