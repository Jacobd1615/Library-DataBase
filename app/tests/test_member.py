# Unit Tests for Member Management Functionality
# This module contains comprehensive test cases for member-related operations
# including authentication, CRUD operations, and API endpoint validation.

from app import create_app
from app.models import db, Member
from datetime import datetime
from app.utils import encode_token
import unittest


class TestMember(unittest.TestCase):
    """
    Test suite for Member model and API endpoints.
    Tests member registration, authentication, profile management, and data validation.
    """

    def setUp(self):
        """
        Set up test environment before each test case.
        Creates a test application, initializes a clean database,
        and creates a test member for authentication testing.
        """
        # Create test application with testing configuration
        self.app = create_app("TestingConfig")

        # Create a test member for use in test cases
        self.member = Member(
            name="test_user",
            email="test@email.com",
            DOB=datetime.strptime("1900-01-01", "%Y-%m-%d").date(),
            password="test",
        )

        # Set up clean database and add test member
        with self.app.app_context():
            db.drop_all()  # Remove all existing tables
            db.create_all()  # Create fresh database schema
            db.session.add(self.member)
            db.session.commit()
            # Generate authentication token for protected endpoint testing
            self.token = encode_token(1)

        # Create test client for making HTTP requests
        self.client = self.app.test_client()

    def test_login_member(self):
        """
        Test member authentication with valid credentials.
        Verifies that login endpoint returns success response and auth token.
        """
        credentials = {"email": "test@email.com", "password": "test"}

        response = self.client.post("/members/login", json=credentials)
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertEqual(response_data["status"], "success")
        self.assertIn("auth_token", response_data)
        # Return the token for other tests to use
        return response_data["auth_token"]

    def test_invaild_login(self):
        credentials = {"email": "bad_email@email.com", "password": "bad_pw"}

        response = self.client.post("/members/login", json=credentials)
        self.assertEqual(response.status_code, 401)
        response_data = response.get_json()
        self.assertEqual(response_data["messages"], "Invalid email or password")

    def test_create_member(self):
        member_payload = {
            "name": "John Doe",
            "email": "jd@example.com",
            "DOB": "1900-01-01",
            "password": "123",
        }

        response = self.client.post("/members/", json=member_payload)
        self.assertEqual(response.status_code, 201)
        response_data = response.get_json()
        self.assertEqual(response_data["name"], "John Doe")

    def test_invalid_creation(self):
        member_payload = {
            "name": "John Doe",
            "phone": "123-456-7890",
            "password": "123",
        }

        response = self.client.post("/members/", json=member_payload)
        self.assertEqual(response.status_code, 400)
        response_data = response.get_json()
        self.assertEqual(
            response_data["errors"]["email"], ["Missing data for required field."]
        )

    def test_update_member(self):
        update_payload = {"name": "Peter"}

        token = self.test_login_member()
        headers = {"Authorization": "Bearer " + token}

        response = self.client.put("/members/", json=update_payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertEqual(response_data["name"], "Peter")
        self.assertEqual(response_data["email"], "test@email.com")
