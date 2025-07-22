# Configuration settings for different environments

import os


class DevelopmentConfig:
    """Configuration for development environment."""

    SECRET_KEY = "a super secret, secret key"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:240179@localhost/library_db"
    CACHE_TYPE = "SimpleCache"


class TestingConfig:
    """Configuration for testing environment."""

    SECRET_KEY = "test-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///testing.db"
    DEBUG = True
    CACHE_TYPE = "SimpleCache"
    TESTING = True


class ProductionConfig:
    """Configuration for production environment."""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "super secret secrets"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("SQLALCHEMY_DATABASE_URI")
        or "mysql+mysqlconnector://root:240179@localhost/library_db"
    )
    CACHE_TYPE = "SimpleCache"
