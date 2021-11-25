"""
Test login contoller
"""
from app.test.base import BaseTestCase
from app.test.test_controller.utils_singleton import ControllerTestsUtils as CTU

class TestLoginController(BaseTestCase):
    ctu = CTU()

    def test_login_controller_return_200(self):
        """ Test checks if login process conducted properly and return 200 status code. """
        
        self.assertNotEqual(self.ctu.get_test_jwt_token(), "")
        self.assertNotEqual(self.ctu.get_test_id(), None)
        self.assertNotEqual(self.ctu.get_test_stats_id(), None)
        self.assertEqual(self.ctu.get_test_wins(), 0)
        self.assertEqual(self.ctu.get_test_fails(), 0)
    
    def test_login_controller_return_400(self):
        """ Test checks if login process handle error properly and return 400 status code. """
        
        result = self.ctu.perform_login("test", "123")
        self.assert400(result)
    
    def test_login_controller_return_404(self):
        """ Test checks if login process handle error properly and return 404 status code. """
        
        result = self.ctu.perform_login("test_test", "123")
        self.assert404(result)
