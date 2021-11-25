"""
Test refresh token contoller
"""
from app.test.base import BaseTestCase
from app.test.test_controller.utils_singleton import ControllerTestsUtils as CTU

class TestRefreshTokenController(BaseTestCase):
    ctu = CTU()

    def test_refresh_token_controller_return_200(self):
        """ Test checks if refresh token process conducted properly and return 200 status code. """
        result = self.ctu.perform_refresh_token("test", "testPasswd")
        self.assert200(result)
    
    def test_refresh_token_controller_return_400(self):
        """ Test checks if refresh token process handle error properly and return 400 status code. """
        result = self.ctu.perform_refresh_token("test", "123")
        self.assert400(result)
    
    def test_refresh_token_controller_return_404(self):
        """ Test checks if refresh token process handle error properly and return 404 status code. """
        result = self.ctu.perform_refresh_token("test_test", "testPasswd")
        self.assert404(result)
