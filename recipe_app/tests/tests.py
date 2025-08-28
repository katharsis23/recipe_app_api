
from app.utils.password_manager import PasswordManager
from django.test import SimpleTestCase
import uuid

class UtilsManager(SimpleTestCase):


    def test_password_hash(self):
        init_password = "password123"
        response = PasswordManager.generate_password(init_password)
        self.assertTrue(PasswordManager.verify_password(response, init_password))





