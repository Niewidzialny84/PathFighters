"""
Test registration contoller
"""
from app.test.base import BaseTestCase
from app.test.test_controller.utils_singleton import ControllerTestsUtils as CTU

class TestRegistrationController(BaseTestCase):
    ctu = CTU()

    def test_registration_controller_return_201(self):
        """ Test checks if registration process conducted properly and return 201 status code. """
        
        result = self.ctu.perform_registration("test_2", "test@email", "124")
        self.assertEqual(result.status_code, 201)
    
    def test_registration_controller_return_409(self):
        """ Test checks if registration process handle error properly and return 409 status code. """
        
        result = self.ctu.perform_registration("test_2", "test@email", "124")
        self.assertEqual(result.status_code, 409)
        self.ctu.perform_delete_user_by_username("test_2")
    