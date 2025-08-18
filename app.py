from app import create_app

# Default to DevelopmentConfig when run directly; deployment will use wsgi:app
app = create_app("ProductionConfig")

if __name__ == "__main__":
    app.run(debug=True)
