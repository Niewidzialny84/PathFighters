"""
Test user contoller
"""
from app.test.base import BaseTestCase
from app.test.test_controller.utils_singleton import ControllerTestsUtils as CTU

class TestUserController(BaseTestCase):
    ctu = CTU()

    def test_get_all_users_return_200(self):
        """ Test checks if get all users process conducted properly and return 200 status code. """
        
        result = self.ctu.perform_get_all_stats()
        self.assert200(result)
        self.assertTrue(len(result.json) > 0)
    
    def test_get_user_by_username_return_200(self):
        """ Test checks if get user by username process conducted properly and return 200 status code. """
        
        result = self.ctu.perform_get_user_by_username("test")
        self.assert200(result)
    
    def test_get_user_by_username_return_404(self):
        """ Test checks if get user by username process handle error properly and return 404 status code. """
        
        result = self.ctu.perform_get_user_by_username("test_10000")
        self.assert404(result)
    
    def test_get_user_by_id_return_200(self):
        """ Test checks if get user by id process conducted properly and return 200 status code. """
        
        result = self.ctu.perform_get_user_by_id(self.ctu.get_test_id())
        self.assert200(result)
    
    def test_get_user_by_id_return_404(self):
        """ Test checks if get user by id process handle error properly and return 404 status code. """
        
        result = self.ctu.perform_get_user_by_id(0)
        self.assert404(result)
    
    def test_delete_user_by_username_return_200(self):
        """ Test checks if delete user by username process conducted properly and return 200 status code. """
        
        self.ctu.perform_registration("test_1", "test@email", "124")
        result = self.ctu.perform_delete_user_by_username("test_1")
        self.assert200(result)
    
    def test_delete_user_by_username_return_404(self):
        """ Test checks if delete user by username process handle error properly and return 404 status code. """

        result = self.ctu.perform_delete_user_by_username("test_1")
        self.assert404(result)
    
    def test_delete_user_by_id_return_200(self):
        """ Test checks if delete user by id process conducted properly and return 200 status code. """
        
        self.ctu.perform_registration("test_1", "test@email", "124")
        test_user = self.ctu.perform_get_user_by_username("test_1").json
        result = self.ctu.perform_delete_user_by_id(test_user['id'])
        self.assert200(result)
    
    def test_delete_user_by_id_return_404(self):
        """ Test checks if delete user by id process handle error properly and return 404 status code. """

        result = self.ctu.perform_delete_user_by_id("test_1")
        self.assert404(result)
    
    def test_patch_user_by_id_return_200(self):
        """ Test checks if patch user by id process conducted properly and return 200 status code. """
        
        self.ctu.perform_registration("test_1", "test@email", "124")
        payload = {
            "email": "test_patch@email",
            "password": "124_patch"
        }
        test_user = self.ctu.perform_get_user_by_username("test_1").json
        result = self.ctu.perform_patch_user_by_id(test_user['id'], payload)
        self.assert200(result)
    
    def test_patch_user_by_id_return_400(self):
        """ Test checks if patch user by id process handle error properly and return 400 status code. """
        
        payload = {}
        test_user = self.ctu.perform_get_user_by_username("test_1").json
        result = self.ctu.perform_patch_user_by_id(test_user['id'], payload)
        self.assert400(result)
    
    def test_patch_user_by_id_return_404(self):
        """ Test checks if patch user by id process handle error properly and return 404 status code. """
        
        payload = {
            "email": "test_patch@email",
            "password": "124_patch"
        }
        result = self.ctu.perform_patch_user_by_id(0, payload)
        self.assert404(result)
        test_user = self.ctu.perform_get_user_by_username("test_1").json
        self.ctu.perform_delete_user_by_id("test_1")
