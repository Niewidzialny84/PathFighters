"""
Test User Controller
"""
import unittest
import json
from app.test.base import BaseTestCase

class TestUserController(BaseTestCase):

    def test_user_controller_get_all_users_200(self):
        """ Test checks if get all users conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['username'], "multiKorzych")
        self.assertEqual(response_content[0]['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content[0]['password'], "123")

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_get_all_users_204(self):
        """ Test checks if get all users conducted properly and return 204 status code. """
        
        test = self.app.test_client()
        
        response = test.get("/users")
        self.assertEqual(response.status_code, 204)
    
    def test_user_controller_get_user_by_username_200(self):
        """ Test checks if get user by username conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users/multiKorzych")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content['id'], 1)
        self.assertEqual(response_content['username'], "multiKorzych")
        self.assertEqual(response_content['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content['password'], "123")

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)

    def test_user_controller_get_user_by_username_404(self):
        """ Test checks if get user by username handle error properly and return 404 status code. """
        
        test = self.app.test_client()
        
        response = test.get("/users/multiKorzych")
        self.assertEqual(response.status_code, 404)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_get_user_by_id_200(self):
        """ Test checks if get user by id conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users/id/1")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content['id'], 1)
        self.assertEqual(response_content['username'], "multiKorzych")
        self.assertEqual(response_content['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content['password'], "123")

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)

    def test_user_controller_get_user_by_id_404(self):
        """ Test checks if get user by id handle error properly and return 404 status code. """
        
        test = self.app.test_client()
        
        response = test.get("/users/id/1")
        self.assertEqual(response.status_code, 404)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_post_200(self):
        """ Test checks if get post user conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['username'], "multiKorzych")
        self.assertEqual(response_content[0]['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content[0]['password'], "123")

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_post_409(self):
        """ Test checks if get post user handle error properly and return 409 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 409)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_put_by_username_200(self):
        """ Test checks if get put user by username conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['username'], "multiKorzych")
        self.assertEqual(response_content[0]['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content[0]['password'], "123")

        payload = {
            "username": "multiKorzych2",
            "email": "multiKorzych2@interia.pl",
            "password": "1232"
        }

        response = test.put('/users/multiKorzych',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 200)
        
        response = test.get("/users/multiKorzych2")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content['id'], 1)
        self.assertEqual(response_content['username'], "multiKorzych2")
        self.assertEqual(response_content['email'], "multiKorzych2@interia.pl")
        self.assertEqual(response_content['password'], "1232")

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_put_by_username_400(self):
        """ Test checks if get put user by username handle error properly and return 400 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['username'], "multiKorzych")
        self.assertEqual(response_content[0]['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content[0]['password'], "123")

        payload = {
            "username": "multiKorzych2",
            "email": "multiKorzych2@interia.pl"
        }

        response = test.put('/users/multiKorzych',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 400)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_put_by_username_404(self):
        """ Test checks if get put user by username handle error properly and return 404 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych2",
            "email": "multiKorzych2@interia.pl"
        }

        response = test.put('/users/multiKorzych',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 404)
    
    def test_user_controller_put_by_id_200(self):
        """ Test checks if get put user by id conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['username'], "multiKorzych")
        self.assertEqual(response_content[0]['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content[0]['password'], "123")

        payload = {
            "username": "multiKorzych2",
            "email": "multiKorzych2@interia.pl",
            "password": "1232"
        }

        response = test.put('/users/id/1',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 200)
        
        response = test.get("/users/id/1")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content['id'], 1)
        self.assertEqual(response_content['username'], "multiKorzych2")
        self.assertEqual(response_content['email'], "multiKorzych2@interia.pl")
        self.assertEqual(response_content['password'], "1232")

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_put_by_id_400(self):
        """ Test checks if get put user by id handle error properly and return 400 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['username'], "multiKorzych")
        self.assertEqual(response_content[0]['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content[0]['password'], "123")

        payload = {
            "username": "multiKorzych2",
            "email": "multiKorzych2@interia.pl"
        }

        response = test.put('/users/id/1',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 400)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_put_by_id_404(self):
        """ Test checks if get put user by id handle error properly and return 404 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych2",
            "email": "multiKorzych2@interia.pl"
        }

        response = test.put('/users/id/1',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 404)
    
    def test_user_controller_patch_by_username_200(self):
        """ Test checks if get patch user by username conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['username'], "multiKorzych")
        self.assertEqual(response_content[0]['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content[0]['password'], "123")

        payload = {
            "username": "multiKorzych2",
        }

        response = test.patch('/users/multiKorzych',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 200)
        
        response = test.get("/users/multiKorzych2")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content['id'], 1)
        self.assertEqual(response_content['username'], "multiKorzych2")
        self.assertEqual(response_content['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content['password'], "123")

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_patch_by_username_400(self):
        """ Test checks if get patch user by username handle error properly and return 400 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['username'], "multiKorzych")
        self.assertEqual(response_content[0]['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content[0]['password'], "123")

        payload = {}

        response = test.patch('/users/multiKorzych',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 400)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_patch_by_username_404(self):
        """ Test checks if get patch user by username handle error properly and return 404 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych2",
            "email": "multiKorzych2@interia.pl"
        }

        response = test.put('/users/multiKorzych',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 404)
    
    def test_user_controller_patch_by_id_200(self):
        """ Test checks if get patch user by id conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['username'], "multiKorzych")
        self.assertEqual(response_content[0]['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content[0]['password'], "123")

        payload = {
            "username": "multiKorzych2",
        }

        response = test.patch('/users/id/1',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 200)
        
        response = test.get("/users/id/1")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content['id'], 1)
        self.assertEqual(response_content['username'], "multiKorzych2")
        self.assertEqual(response_content['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content['password'], "123")

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_patch_by_id_400(self):
        """ Test checks if get patch user by id handle error properly and return 400 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content[0]['id'], 1)
        self.assertEqual(response_content[0]['username'], "multiKorzych")
        self.assertEqual(response_content[0]['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content[0]['password'], "123")

        payload = {}

        response = test.patch('/users/id/1',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 400)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
    def test_user_controller_patch_by_id_404(self):
        """ Test checks if get patch user by id handle error properly and return 404 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych2",
            "email": "multiKorzych2@interia.pl"
        }

        response = test.put('/users/id/1',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 404)
    
    def test_user_controller_delete_all_users_200(self):
        """ Test checks if delete all users conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)

        payload = {
            "username": "multiKorzych2",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)

        response = test.get("/users")
        self.assertEqual(response.status_code, 204)
    
    def test_user_controller_delete_user_by_username_200(self):
        """ Test checks if delete user by username conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users/multiKorzych")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content['id'], 1)
        self.assertEqual(response_content['username'], "multiKorzych")
        self.assertEqual(response_content['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content['password'], "123")
    
        response = test.delete("/users/multiKorzych")
        self.assertEqual(response.status_code, 200)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)

        response = test.get("/users")
        self.assertEqual(response.status_code, 204)
    
    def test_user_controller_delete_user_by_username_404(self):
        """ Test checks if delete user by username handle error properly and return 404 status code. """
        
        test = self.app.test_client()

        response = test.delete("/users/multiKorzych")
        self.assertEqual(response.status_code, 404)
    
    def test_user_controller_delete_user_by_id_200(self):
        """ Test checks if delete user by id conducted properly and return 200 status code. """
        
        test = self.app.test_client()

        payload = {
            "username": "multiKorzych",
            "email": "multiKorzych@interia.pl",
            "password": "123"
        }

        response = test.post('/users',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        self.assertEqual(response.status_code, 201)
        
        response = test.get("/users/multiKorzych")
        response_content = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content['id'], 1)
        self.assertEqual(response_content['username'], "multiKorzych")
        self.assertEqual(response_content['email'], "multiKorzych@interia.pl")
        self.assertEqual(response_content['password'], "123")
    
        response = test.delete("/users/id/1")
        self.assertEqual(response.status_code, 200)

        response = test.delete("/users")
        self.assertEqual(response.status_code, 200)
    
        response = test.get("/users")
        self.assertEqual(response.status_code, 204)
    
    def test_user_controller_delete_user_by_id_404(self):
        """ Test checks if delete user by id handle error properly and return 404 status code. """
        
        test = self.app.test_client()

        response = test.delete("/users/id/1")
        self.assertEqual(response.status_code, 404)
    
    # def test_stats_controller_put_200(self):
    #     """ Test checks if put stats conducted properly and return 200 status code. """
        
    #     test = self.app.test_client()

    #     payload = {
    #         "username": "multiKorzych4",
    #         "email": "multiKorzych@interia.pl",
    #         "password": "123"
    #     }

    #     response = test.post('/users',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 201)

    #     payload = {
    #         "total": 2,
    #         "wins": 1,
    #         "fails": 1
    #     }

    #     response = test.put('/stats/1',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 200)
        
    #     response = test.get("/stats")
    #     response_content = response.json

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response_content[0]['id'], 1)
    #     self.assertEqual(response_content[0]['userid'], 1)
    #     self.assertEqual(response_content[0]['total'], 2)
    #     self.assertEqual(response_content[0]['wins'], 1)
    #     self.assertEqual(response_content[0]['fails'], 1)

    #     response = test.delete("/users")
    #     self.assertEqual(response.status_code, 200)
    
    # def test_stats_controller_put_400(self):
    #     """ Test checks if put stats handle error properly and return 400 status code. """
        
    #     test = self.app.test_client()

    #     payload = {
    #         "username": "multiKorzych4",
    #         "email": "multiKorzych@interia.pl",
    #         "password": "123"
    #     }

    #     response = test.post('/users',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 201)

    #     payload = {
    #         "userid": 2,
    #         "total": 2,
    #         "wins": 1
    #     }

    #     response = test.put('/stats/1',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 400)
        
    #     response = test.get("/stats")
    #     response_content = response.json

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response_content[0]['id'], 1)
    #     self.assertEqual(response_content[0]['userid'], 1)
    #     self.assertEqual(response_content[0]['total'], 0)
    #     self.assertEqual(response_content[0]['wins'], 0)
    #     self.assertEqual(response_content[0]['fails'], 0)

    #     response = test.delete("/users")
    #     self.assertEqual(response.status_code, 200)
    
    # def test_stats_controller_put_404(self):
    #     """ Test checks if put stats handle error properly and return 404 status code. """
        
    #     test = self.app.test_client()

    #     payload = {
    #         "username": "multiKorzych4_new",
    #         "email": "multiKorzych@interia.pl_new",
    #         "password": "123_new"
    #     }

    #     response = test.put('/users/1',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 404)
    
    # def test_stats_controller_patch_200(self):
    #     """ Test checks if patch stats conducted properly and return 200 status code. """
        
    #     test = self.app.test_client()

    #     payload = {
    #         "username": "multiKorzych4",
    #         "email": "multiKorzych@interia.pl",
    #         "password": "123"
    #     }

    #     response = test.post('/users',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 201)

    #     payload = {
    #         "total": 2,
    #         "wins": 1,
    #         "fails": 1
    #     }

    #     response = test.patch('/stats/1',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 200)
        
    #     response = test.get("/stats")
    #     response_content = response.json

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response_content[0]['id'], 1)
    #     self.assertEqual(response_content[0]['userid'], 1)
    #     self.assertEqual(response_content[0]['total'], 2)
    #     self.assertEqual(response_content[0]['wins'], 1)
    #     self.assertEqual(response_content[0]['fails'], 1)

    #     response = test.delete("/users")
    #     self.assertEqual(response.status_code, 200)
    
    # def test_stats_controller_patch_404(self):
    #     """ Test checks if patch stats handle error properly and return 404 status code. """
        
    #     test = self.app.test_client()

    #     payload = {
    #         "username": "multiKorzych4_new",
    #         "email": "multiKorzych@interia.pl_new",
    #         "password": "123_new"
    #     }

    #     response = test.patch('/stats/',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 404)
    
    # def test_stats_controller_add_win_200(self):
    #     """ Test checks if add-win conducted properly and return 200 status code. """
        
    #     test = self.app.test_client()

    #     payload = {
    #         "username": "multiKorzych4",
    #         "email": "multiKorzych@interia.pl",
    #         "password": "123"
    #     }

    #     response = test.post('/users',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 201)

    #     payload = {
    #         "total": 2,
    #         "wins": 1,
    #         "fails": 1
    #     }

    #     response = test.patch('/stats/1/add-win',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 200)
        
    #     response = test.get("/stats")
    #     response_content = response.json

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response_content[0]['id'], 1)
    #     self.assertEqual(response_content[0]['userid'], 1)
    #     self.assertEqual(response_content[0]['total'], 1)
    #     self.assertEqual(response_content[0]['wins'], 1)
    #     self.assertEqual(response_content[0]['fails'], 0)

    #     response = test.delete("/users")
    #     self.assertEqual(response.status_code, 200)
    
    # def test_stats_controller_add_win_404(self):
    #     """ Test checks if add-win handle error properly and return 404 status code. """
        
    #     test = self.app.test_client()

    #     payload = {
    #         "username": "multiKorzych4_new",
    #         "email": "multiKorzych@interia.pl_new",
    #         "password": "123_new"
    #     }

    #     response = test.patch('/stats/1/add-win',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 404)

    # def test_stats_controller_add_fail_200(self):
    #     """ Test checks if add-fail conducted properly and return 200 status code. """
        
    #     test = self.app.test_client()

    #     payload = {
    #         "username": "multiKorzych4",
    #         "email": "multiKorzych@interia.pl",
    #         "password": "123"
    #     }

    #     response = test.post('/users',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 201)

    #     payload = {
    #         "total": 2,
    #         "wins": 1,
    #         "fails": 1
    #     }

    #     response = test.patch('/stats/1/add-fail',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 200)
        
    #     response = test.get("/stats")
    #     response_content = response.json

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response_content[0]['id'], 1)
    #     self.assertEqual(response_content[0]['userid'], 1)
    #     self.assertEqual(response_content[0]['total'], 1)
    #     self.assertEqual(response_content[0]['wins'], 0)
    #     self.assertEqual(response_content[0]['fails'], 1)

    #     response = test.delete("/users")
    #     self.assertEqual(response.status_code, 200)
    
    # def test_stats_controller_add_fail_404(self):
    #     """ Test checks if add-fail handle error properly and return 404 status code. """
        
    #     test = self.app.test_client()

    #     payload = {
    #         "username": "multiKorzych4_new",
    #         "email": "multiKorzych@interia.pl_new",
    #         "password": "123_new"
    #     }

    #     response = test.patch('/stats/1/add-fail',
    #         headers = {"Content-Type": "application/json"},
    #         data = json.dumps(payload))
        
    #     self.assertEqual(response.status_code, 404)
        
if __name__ == '__main__':
    unittest.main()
