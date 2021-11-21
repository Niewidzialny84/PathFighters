"""
Test Token Blacklist Model
"""
import unittest
from app.main.model.token_blacklist_model import TokenBlackList
from app.test.base import BaseTestCase
from datetime import datetime

class TestTokenBlacklistModel(BaseTestCase):

    def test_token_blacklist_model_object_creation(self):
        """ Test checks if creation TokenBlacklist object conducted properly. """
        #Given
        test_date = datetime.utcnow

        token_blacklist = TokenBlackList(
           id = 1,
           jti = "22",
           expiration_time = test_date
        )
        
        #Then
        self.assertTrue(isinstance(token_blacklist, TokenBlackList))
        self.assertEqual(token_blacklist.id, 1)
        self.assertEqual(token_blacklist.jti, "22")
        self.assertEqual(token_blacklist.expiration_time, test_date)
        
if __name__ == '__main__':
    unittest.main()
