from app import create_app
from app.models import db, Member
from datetime import datetime
from app.utils import encode_token
import unittest


class TestMember(unittest.TestCase):
    def setUp(self):
        self.app = create_app("TestingConfig")
        self.member = Member(
            name="test_user",
            email="test@email.com",
            DOB=datetime.strptime("1900-01-01", "%Y-%m-%d").date(),
            password="test",
        )
        with self.app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(self.member)
            db.session.commit()
            self.token = encode_token(1)
        self.client = self.app.test_client()

    def test_login_member(self):
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
        update_payload = {
            "name": "Peter"
        }

        token = self.test_login_member()
        headers = {"Authorization": "Bearer " + token}

        response = self.client.put("/members/", json=update_payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertEqual(response_data["name"], "Peter")
        self.assertEqual(response_data["email"], "test@email.com")
