"""
Test stats contoller
"""
from app.test.base import BaseTestCase
from app.test.test_controller.utils_singleton import ControllerTestsUtils as CTU

class TestStatsController(BaseTestCase):
    ctu = CTU()

    def test_get_all_stats_return_200(self):
        """ Test checks if get all stats process conducted properly and return 200 status code. """
        
        result = self.ctu.perform_get_all_stats()
        self.assert200(result)
        self.assertTrue(len(result.json) > 0)
    
    def test_get_stats_return_200(self):
        """ Test checks if get stats process conducted properly and return 200 status code. """
        
        result = self.ctu.perform_get_test_user_stats()
        self.assert200(result)
        self.assertEqual(self.ctu.get_test_wins(), 1)
        self.assertEqual(self.ctu.get_test_fails(), 1)
    
    def test_get_stats_return_404(self):
        """ Test checks if get stats process handle error properly and return 404 status code. """
        
        result = self.ctu.perform_get_stats_by_id(0)
        self.assert404(result)

    def test_add_fail_return_200(self):
        """ Test checks if add fail to stats process conducted properly and return 200 status code. """
        
        result = self.ctu.perform_add_fail_test_user_stats()
        self.assert200(result)
        self.assertEqual(self.ctu.get_test_wins(), 0)
        self.assertEqual(self.ctu.get_test_fails(), 1)
    
    def test_add_fail_return_404(self):
        """ Test checks if add fail to stats handle error properly and return 404 status code. """
        
        result = self.ctu.perform_add_fail_stats_by_id(0)
        self.assert404(result)
    
    def test_add_win_return_200(self):
        """ Test checks if add win to stats process conducted properly and return 200 status code. """
        
        result = self.ctu.perform_add_win_test_user_stats()
        self.assert200(result)
        self.assertEqual(self.ctu.get_test_wins(), 1)
        self.assertEqual(self.ctu.get_test_fails(), 1)
    
    def test_add_win_return_404(self):
        """ Test checks if add win to stats handle error properly and return 404 status code. """
        
        result = self.ctu.perform_add_win_stats_by_id(0)
        self.assert404(result)     
    