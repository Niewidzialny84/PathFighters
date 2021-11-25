"""
Test Authorized User Model
"""
import unittest
from app.test.base import BaseTestCase
from app.test.test_controller.utils_singleton import ControllerTestsUtils as CTU

class TestLoginController(BaseTestCase):
    ctu = CTU()

    def test_login_controller_return_200(self):
        """ Test checks if login process conducted properly and return 200 status code. """
        
        self.assert200(self.ctu.perform_test_user_logout())
