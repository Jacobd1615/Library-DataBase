# Backwards compatibility entrypoint expected by Render (gunicorn flask_app:app)
from app import create_app

app = create_app("ProductionConfig")
