from app import create_app
from app.models import db, Book
import unittest


class TestBook(unittest.TestCase):
    def setUp(self):
        self.app = create_app("TestingConfig")
        self.book = Book(
            title="Test Book",
            author="Test Author",
            genre="Fiction",
            desc="A test book for testing purposes",
        )
        with self.app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(self.book)
            db.session.commit()
        self.client = self.app.test_client()

    def test_get_all_books(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertIsInstance(response_data, list)
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]["title"], "Test Book")

    def test_get_book_by_id(self):
        response = self.client.get("/books/1")
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertEqual(response_data["title"], "Test Book")
        self.assertEqual(response_data["author"], "Test Author")

    def test_get_nonexistent_book(self):
        response = self.client.get("/books/999")
        self.assertEqual(response.status_code, 404)
        response_data = response.get_json()
        self.assertEqual(response_data["message"], "Book not found")

    def test_create_book(self):
        book_payload = {
            "title": "New Book",
            "author": "New Author",
            "genre": "Mystery",
            "desc": "A mysterious new book",
        }

        response = self.client.post("/books/", json=book_payload)
        self.assertEqual(response.status_code, 201)
        response_data = response.get_json()
        self.assertEqual(response_data["title"], "New Book")
        self.assertEqual(response_data["author"], "New Author")

    def test_invalid_book_creation(self):
        book_payload = {
            "title": "Incomplete Book",
            "genre": "Fiction",
            # Missing required fields: author, desc
        }

        response = self.client.post("/books/", json=book_payload)
        self.assertEqual(response.status_code, 400)
        response_data = response.get_json()
        self.assertIn("Error", response_data)

    def test_update_book(self):
        update_payload = {"title": "Updated Book Title", "desc": "Updated description"}

        response = self.client.put("/books/1", json=update_payload)
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertEqual(response_data["title"], "Updated Book Title")
        self.assertEqual(response_data["desc"], "Updated description")
        # Check that other fields remain unchanged
        self.assertEqual(response_data["author"], "Test Author")

    def test_update_nonexistent_book(self):
        update_payload = {"title": "Non-existent Book"}

        response = self.client.put("/books/999", json=update_payload)
        self.assertEqual(response.status_code, 404)
        response_data = response.get_json()
        self.assertEqual(response_data["Error"], "Book was not found")

    def test_delete_book(self):
        response = self.client.delete("/books/1")
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertEqual(
            response_data["message"], "Book with id: 1 deleted successfully"
        )

        # Verify book is actually deleted
        get_response = self.client.get("/books/1")
        self.assertEqual(get_response.status_code, 404)

    def test_delete_nonexistent_book(self):
        response = self.client.delete("/books/999")
        self.assertEqual(response.status_code, 404)
        response_data = response.get_json()
        self.assertEqual(response_data["Error"], "Book was not found")
