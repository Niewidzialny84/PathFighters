"""
Test Login Model
"""
import unittest
from app.main.model.login_model import Login
from app.test.base import BaseTestCase

class TestLoginModel(BaseTestCase):

    def test_login_model_object_creation(self):
        """ Test checks if creation login object conducted properly. """
        #Given
        login = Login(
           username = "test",
           password = "testPassword"
        )
        
        #Then
        self.assertTrue(isinstance(login, Login))
        self.assertEqual(login.username, "test")
        self.assertEqual(login.password, "testPassword")
        
if __name__ == '__main__':
    unittest.main()