"""
Test Token Model
"""
import unittest
from app.main.model.token_model import Token
from app.test.base import BaseTestCase

class TestTokenModel(BaseTestCase):

    def test_token_model_object_creation(self):
        """ Test checks if creation token object conducted properly. """
        #Given
        token_to_test = '''eyJhbGciOiJIUzI1
           NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOi
           IxMjM0NTY3ODkwIiwibmFtZSI6Ikpva
           G4gRG9lIiwiaWF0IjoxNTE2MjM5MDIy
           fQ.SflKxwRJSMeKKF2QT4fwpMeJf36P
           Ok6yJV_adQssw5c'''

        token = Token(
           jwt_token = token_to_test
        )
        
        #Then
        self.assertTrue(isinstance(token, Token))
        self.assertEqual(token.jwt_token, token_to_test)
        
if __name__ == '__main__':
    unittest.main()
    