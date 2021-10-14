"""
Test Stats Controller
"""
import unittest
import json
from app.test.base import BaseTestCase

class TestStatsController(BaseTestCase):

    def test_stats_controller_get_all_stats_200(self):
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
    
    def test_stats_controller_get_all_stats_204(self):
        """ Test checks if get all stats conducted properly and return 204 status code. """
        
        test = self.app.test_client()
        
        response = test.get("/stats")
        self.assertEqual(response.status_code, 204)
    
    def test_stats_controller_get_stats_by_id_200(self):
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
        
        response = test.get("/stats/1")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content['id'], 1)
        self.assertEqual(response_content['userid'], 1)
        self.assertEqual(response_content['total'], 0)
        self.assertEqual(response_content['wins'], 0)
        self.assertEqual(response_content['fails'], 0)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_stats_controller_get_stats_by_id_404(self):
        """ Test checks if get all stats handle error properly and return 404 status code. """
        
        test = self.app.test_client()
        
        response = test.get("/stats/1")
        self.assertEqual(response.status_code, 404)
    
    def test_stats_controller_put_200(self):
        """ Test checks if put stats conducted properly and return 200 status code. """
        
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

        payload = {
            "total": 2,
            "wins": 1,
            "fails": 1
        }

        response = test.put('/stats/1',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 200)
        
        response = test.get("/stats")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['userid'], 1)
        self.assertEqual(response_content[0]['total'], 2)
        self.assertEqual(response_content[0]['wins'], 1)
        self.assertEqual(response_content[0]['fails'], 1)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_stats_controller_put_400(self):
        """ Test checks if put stats handle error properly and return 400 status code. """
        
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

        payload = {
            "userid": 2,
            "total": 2,
            "wins": 1
        }

        response = test.put('/stats/1',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 400)
        
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
    
    def test_stats_controller_put_404(self):
        """ Test checks if put stats handle error properly and return 404 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych4_new",
            "email": "multiKorzych@interia.pl_new",
            "password": "123_new"
        }

        response = test.put('/users/1',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 404)
    
    def test_stats_controller_patch_200(self):
        """ Test checks if patch stats conducted properly and return 200 status code. """
        
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

        payload = {
            "total": 2,
            "wins": 1,
            "fails": 1
        }

        response = test.patch('/stats/1',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 200)
        
        response = test.get("/stats")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['userid'], 1)
        self.assertEqual(response_content[0]['total'], 2)
        self.assertEqual(response_content[0]['wins'], 1)
        self.assertEqual(response_content[0]['fails'], 1)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_stats_controller_patch_404(self):
        """ Test checks if patch stats handle error properly and return 404 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych4_new",
            "email": "multiKorzych@interia.pl_new",
            "password": "123_new"
        }

        response = test.patch('/stats/',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 404)
    
    def test_stats_controller_add_win_200(self):
        """ Test checks if add-win conducted properly and return 200 status code. """
        
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

        payload = {
            "total": 2,
            "wins": 1,
            "fails": 1
        }

        response = test.patch('/stats/1/add-win',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 200)
        
        response = test.get("/stats")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['userid'], 1)
        self.assertEqual(response_content[0]['total'], 1)
        self.assertEqual(response_content[0]['wins'], 1)
        self.assertEqual(response_content[0]['fails'], 0)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_stats_controller_add_win_404(self):
        """ Test checks if add-win handle error properly and return 404 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych4_new",
            "email": "multiKorzych@interia.pl_new",
            "password": "123_new"
        }

        response = test.patch('/stats/1/add-win',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 404)

    def test_stats_controller_add_fail_200(self):
        """ Test checks if add-fail conducted properly and return 200 status code. """
        
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

        payload = {
            "total": 2,
            "wins": 1,
            "fails": 1
        }

        response = test.patch('/stats/1/add-fail',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 200)
        
        response = test.get("/stats")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['userid'], 1)
        self.assertEqual(response_content[0]['total'], 1)
        self.assertEqual(response_content[0]['wins'], 0)
        self.assertEqual(response_content[0]['fails'], 1)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_stats_controller_add_fail_404(self):
        """ Test checks if add-fail handle error properly and return 404 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych4_new",
            "email": "multiKorzych@interia.pl_new",
            "password": "123_new"
        }

        response = test.patch('/stats/1/add-fail',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 404)
        
if __name__ == '__main__':
    unittest.main()
