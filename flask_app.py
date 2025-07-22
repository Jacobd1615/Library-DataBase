# Main application entry point for Flask Library Management System

from app import create_app
from app.models import db
from dotenv import load_dotenv
from sqlalchemy import inspect

# Load environment variables from .env file
load_dotenv()

# Create Flask app instance using production configuration
app = create_app("ProductionConfig")

# Initialize database tables only if they don't exist
with app.app_context():
    # Check if tables exist before creating
    inspector = inspect(db.engine)
    if not inspector.has_table("members"):
        # db.drop_all()
        db.create_all()
        print("✅ Database tables created successfully!")
    else:
        print("ℹ️ Database tables already exist - skipping creation")
