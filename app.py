# Import the create_app function from the app package, which serves as the application factory.
from app import create_app
from app.models import db


# Create an instance of the Flask application by calling the factory function.
app = create_app("ProductionConfig")


# This block ensures that the database tables are created before the app starts.
with app.app_context():
    # db.drop_all()
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
