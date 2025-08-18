class DevelopmentConfig:
    SECRET_KEY = "a super secret, secret key"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:240179@localhost/library_db"
    CACHE_TYPE = "SimpleCache"


class TestingConfig:
    SECRET_KEY = "test-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///testing.db"  # Fixed: was MYDATABASE_URL
    DEBUG = True
    CACHE_TYPE = "SimpleCache"  # Fixed: was SimpleCashe (typo)
    TESTING = True


class ProductionConfig:
    SECRET_KEY = "a super secret, secret key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///production.db"
    CACHE_TYPE = "SimpleCache"
