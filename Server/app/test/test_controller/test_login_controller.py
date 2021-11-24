"""
Test Authorized User Model
"""
import unittest
from app.test.base import BaseTestCase
from app.test.test_controller.controller_tests_utils import ControllerTestsUtils as CTU

class TestLoginController(BaseTestCase):
    ctu = CTU()

    def test_login_controller_return_200(self):
        """ Test checks if login process conducted properly and return 200 status code. """
        
        self.assertNotEqual(self.ctu.get_test_jwt_token(), "")
        self.assertNotEqual(self.ctu.test_id, None)
        self.assertNotEqual(self.ctu.test_stats_id, None)
        self.assertEqual(self.ctu.test_wins, 0)
        self.assertEqual(self.ctu.test_fails, 0)
