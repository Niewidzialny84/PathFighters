"""
Test Authorized User Model
"""
import unittest
from app.main.model.authorized_user_model import AuthorizedUser
from app.main.model.user_model import User
from app.test.base import BaseTestCase

class TestAuthorizedUserModel(BaseTestCase):

    def test_authorized_user_model_object_creation(self):
        """ Test checks if creation AuthorizedUser object conducted properly. """
        #Given
        authorizedUser = AuthorizedUser(
           user = User(
                id = 1,
                username = "test",
                email = "example@test.com",
                password = "123"
            ),
           jwt_token = "testTOKEN"
        )
        
        #Then
        self.assertTrue(isinstance(authorizedUser, AuthorizedUser))
        self.assertTrue(isinstance(authorizedUser.user, User))
        self.assertEqual(authorizedUser.user.id, 1)
        self.assertEqual(authorizedUser.user.username, "test")
        self.assertEqual(authorizedUser.user.email, "example@test.com")
        self.assertEqual(authorizedUser.user.password, "123")
        self.assertEqual(authorizedUser.jwt_token, "testTOKEN")
        
if __name__ == '__main__':
    unittest.main()