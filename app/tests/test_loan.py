from app import create_app
from app.models import db, Loan, Member, Book
from datetime import datetime
import unittest


class TestLoan(unittest.TestCase):
    def setUp(self):
        self.app = create_app("TestingConfig")

        # Create test member
        self.member = Member(
            name="test_user",
            email="test@email.com",
            DOB=datetime.strptime("1900-01-01", "%Y-%m-%d").date(),
            password="test",
        )

        # Create test books
        self.book1 = Book(
            title="Test Book 1",
            author="Test Author 1",
            genre="Fiction",
            desc="First test book",
        )

        self.book2 = Book(
            title="Test Book 2",
            author="Test Author 2",
            genre="Mystery",
            desc="Second test book",
        )

        with self.app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(self.member)
            db.session.add(self.book1)
            db.session.add(self.book2)
            db.session.commit()

        self.client = self.app.test_client()

    def test_create_loan(self):
        loan_payload = {"member_id": 1, "book_ids": [1, 2], "loan_date": "2025-07-19"}

        response = self.client.post("/loans/", json=loan_payload)
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertEqual(len(response_data["books"]), 2)
        self.assertIn("loan_date", response_data)
        self.assertIn("member", response_data)

    def test_invalid_loan_creation(self):
        loan_payload = {
            "member_id": 1
            # Missing book_ids and loan_date
        }

        response = self.client.post("/loans/", json=loan_payload)
        self.assertEqual(response.status_code, 400)
        response_data = response.get_json()
        self.assertIn("Error", response_data)

    def test_get_all_loans(self):
        # First create a loan
        loan_payload = {"member_id": 1, "book_ids": [1], "loan_date": "2025-07-19"}
        self.client.post("/loans/", json=loan_payload)

        # Then get all loans
        response = self.client.get("/loans/")
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertIsInstance(response_data, list)
        self.assertEqual(len(response_data), 1)

    def test_get_loan_by_id(self):
        # First create a loan
        loan_payload = {"member_id": 1, "book_ids": [1], "loan_date": "2025-07-19"}
        self.client.post("/loans/", json=loan_payload)

        # Then get the loan by ID
        response = self.client.get("/loans/1")
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertIn("member", response_data)
        self.assertEqual(len(response_data["books"]), 1)

    def test_get_nonexistent_loan(self):
        response = self.client.get("/loans/999")
        self.assertEqual(response.status_code, 404)
        response_data = response.get_json()
        self.assertEqual(response_data["error"], "Loan not found")

    def test_update_loan(self):
        # First create a loan
        loan_payload = {"member_id": 1, "book_ids": [1], "loan_date": "2025-07-19"}
        self.client.post("/loans/", json=loan_payload)

        # Update the loan by adding another book
        update_payload = {"add_book_ids": [2]}

        response = self.client.put("/loans/1", json=update_payload)
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertEqual(len(response_data["books"]), 2)

    def test_delete_loan(self):
        # First create a loan
        loan_payload = {"member_id": 1, "book_ids": [1], "loan_date": "2025-07-19"}
        self.client.post("/loans/", json=loan_payload)

        # Delete the loan
        response = self.client.delete("/loans/1")
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertEqual(response_data["message"], "Loan id: 1 deleted successfully")

        # Verify loan is actually deleted
        get_response = self.client.get("/loans/1")
        self.assertEqual(get_response.status_code, 404)
