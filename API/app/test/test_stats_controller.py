"""
Test Stats Controller
"""
import unittest
import json
from app.test.base import BaseTestCase

class TestStatsController(BaseTestCase):

    def test_controller_get_all_stats_200(self):
        """ Test checks if get all stats conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych4",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/stats")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['userid'], 1)
        self.assertEqual(response_content[0]['total'], 0)
        self.assertEqual(response_content[0]['wins'], 0)
        self.assertEqual(response_content[0]['fails'], 0)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_controller_get_all_stats_204(self):
        """ Test checks if get all stats conducted properly and return 204 status code. """
        
        test = self.app.test_client()
        
        response = test.get("/stats")
        self.assertEqual(response.status_code, 204)
        
        
if __name__ == '__main__':
    unittest.main()