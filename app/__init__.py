# Application factory for Flask Library Management System

from flask import Flask
from .extensions import ma, limiter, cache
from .models import db
from .blueprints.member import member_bp
from .blueprints.book import book_bp
from .blueprints.loan import loan_bp
from .blueprints.debug import debug_bp
from flask_swagger_ui import get_swaggerui_blueprint

# Swagger configuration
SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.yaml"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "library_db"}
)


def create_app(config_name):
    """Create and configure Flask application instance."""
    app = Flask(__name__)
    app.config.from_object(f"config.{config_name}")

    # Initialize extensions
    ma.init_app(app)
    db.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    # Register blueprints
    app.register_blueprint(member_bp, url_prefix="/members")
    app.register_blueprint(book_bp, url_prefix="/books")
    app.register_blueprint(loan_bp, url_prefix="/loans")
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    if config_name == "DevelopmentConfig":
        app.register_blueprint(debug_bp, url_prefix="/debug")

    return app
