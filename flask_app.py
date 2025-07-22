# Main application entry point for Flask Library Management System

from app import create_app
from app.models import db
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create Flask app instance using production configuration
app = create_app("ProductionConfig")

# Initialize database tables
with app.app_context():
    # db.drop_all()  # Uncomment to reset database
    db.create_all()
