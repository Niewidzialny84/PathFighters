"""
Performance tests
"""
import unittest
import json
from app.test.base import BaseTestCase

class TestDbPerformance(BaseTestCase):

    def test_user_controller_create_250_users_and_stats(self):
        """ Test checks if create 250 users conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        for i in range (0, 250):
            payload['username'] = "multiKorzych" + str(i)
            response = test.post('/users',
                headers = {"Content-Type": "application/json"},
                data = json.dumps(payload))
            self.assertEqual(response.status_code, 201)
        
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_content), 250)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)

    def test_user_controller_put_250_users(self):
        """ Test checks if put 250 users conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        for i in range (0, 250):
            payload['username'] = "multiKorzych" + str(i)
            response = test.post('/users',
                headers = {"Content-Type": "application/json"},
                data = json.dumps(payload))
            self.assertEqual(response.status_code, 201)
       
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_content), 250)

        for i in range (0, 250):
            payload = {
                "username": "test" + str(i),
                "email": "multiKorzych@interia.pl",
                "password": "123"
            }
            response = test.put('/users/multiKorzych' + str(i),
                headers = {"Content-Type": "application/json"},
                data = json.dumps(payload))
            self.assertEqual(response.status_code, 200)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)        
    
    def test_user_controller_patch_250_users(self):
        """ Test checks if patch 250 users conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        for i in range (0, 250):
            payload['username'] = "multiKorzych" + str(i)
            response = test.post('/users',
                headers = {"Content-Type": "application/json"},
                data = json.dumps(payload))
            self.assertEqual(response.status_code, 201)
       
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_content), 250)

        for i in range (0, 250):
            payload = {"password": "123"}
            response = test.patch('/users/multiKorzych' + str(1),
                headers = {"Content-Type": "application/json"},
                data = json.dumps(payload))
            self.assertEqual(response.status_code, 200)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)        
        
if __name__ == '__main__':
    unittest.main()