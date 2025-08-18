from app import create_app

# Entry point for WSGI servers like gunicorn
app = create_app("ProductionConfig")
