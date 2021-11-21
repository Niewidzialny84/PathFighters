"""
Test User Model
"""
import unittest
from app.main.model.user_model import User
from app.test.base import BaseTestCase

class TestUserModel(BaseTestCase):

    def test_user_model_object_creation(self):
        """ Test checks if creation user object conducted properly. """
        #Given
        user = User(
            id = 1,
            username = "test",
            email = "example@test.com",
            password = "123"
        )
        
        #Then
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, "test")
        self.assertEqual(user.email, "example@test.com")
        self.assertEqual(user.password, "123")
        
if __name__ == '__main__':
    unittest.main()