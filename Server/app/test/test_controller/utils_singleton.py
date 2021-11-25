"""
Utils class for controller tests
"""
import json
from app.test.base import BaseTestCase
from app.test.test_controller.utils_singleton_meta import UtilsSingletonMeta

class ControllerTestsUtils(metaclass = UtilsSingletonMeta):
    def __init__(self): 
        self.test_client = BaseTestCase.create_app(self).test_client()
        self.test_username = "test"
        self.test_email =  "test@test.pl"
        self.test_password = "testPasswd"
        self.test_id = None
        self.test_stats_id = None
        self.test_wins = None
        self.test_fails = None
        self.test_jwt_token = ""
        self.create_test_user()
        self.perform_test_user_login()
        self.perform_get_test_user_stats()
    
    def get_test_username(self):
        return self.test_username
    
    def get_test_email(self):
        return self.test_email
    
    def get_test_password(self):
        return self.test_password
    
    def get_test_id(self):
        return self.test_id
    
    def get_test_stats_id(self):
        return self.test_stats_id
    
    def get_test_wins(self):
        return self.test_wins
    
    def get_test_fails(self):
        return self.test_fails

    def get_test_jwt_token(self):
        return self.test_jwt_token
    
    def set_test_username(self, username):
        self.test_username = username
    
    def set_test_password(self, passwd):
        self.test_password = passwd
    
    def create_test_user(self):
        """Method to create test user"""
        payload = {
            "username": self.test_username,
            "email": self.test_email,
            "password": self.test_password
        }

        response = self.test_client.post('/register',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        if response.status_code != 201:
            self.perform_test_user_logout()
            self.perform_test_user_login()
            self.perform_delete_test_user()

            response = self.test_client.post('/register',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))

        return response
    
    def perform_test_user_login(self):
        """Method to perform login"""
        payload = {
            "username": self.test_username,
            "password": self.test_password
        }

        response = self.test_client.post('/login',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        if response.status_code == 200:
            self.test_id = response.json['user']['id']
            self.test_jwt_token = response.json['jwt_token']
        
        return response
    
    def perform_login(self, username, password):
        """Method to perform login"""
        payload = {
            "username": username,
            "password": password
        }

        response = self.test_client.post('/login',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        if response.status_code == 200:
            self.test_id = response.json['user']['id']
            self.test_username = response.json['user']['username']
            self.test_password = response.json['user']['password']
            self.test_jwt_token = response.json['jwt_token']
        
        return response
    
    def perform_get_test_user_stats(self):
        """Method to perform get stats"""
        response = self.test_client.get('/stats/{}'.format(self.test_id),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        if response.status_code == 200:
            self.test_stats_id = response.json['id']
            self.test_wins = response.json['wins']
            self.test_fails = response.json['fails']
        
        return response
    
    def perform_delete_test_user(self):
        """Method to delete test user"""
        response = self.test_client.delete('/user/id/{}'.format(self.test_id),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        return response
    
    def perform_delete_user_by_username(self, username):
        """Method to delete test user"""
        response = self.test_client.delete('/user/{}'.format(username),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        return response
    
    def perform_delete_user_by_id(self, id):
        """Method to delete test user"""
        response = self.test_client.delete('/user/id/{}'.format(id),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})

        return response

    def perform_test_user_logout(self):
        """Method to perform get stats"""
        response = self.test_client.delete('/logout',
            headers = {"Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        return response
    
    def perform_refresh_token(self, username, password):
        """Method to perform refresh token action"""
        payload = {
            "username": username,
            "password": password
        }

        response = self.test_client.post('/refresh',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))
        
        if response.status_code == 200:
            self.test_jwt_token = response.json['jwt_token']
        
        return response
    
    def perform_registration(self, username, email, password):
        """Method to perform registration"""
        payload = {
            "username": username,
            "email": email,
            "password": password
        }

        response = self.test_client.post('/register',
            headers = {"Content-Type": "application/json"},
            data = json.dumps(payload))

        return response

    def perform_get_all_stats(self):
        """Method to perform get all stats"""
        response = self.test_client.get('/stats',
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        return response
    
    def perform_add_win_test_user_stats(self):
        """Method to perform add-win to stats"""
        response = self.test_client.patch('/stats/{}/add-win'.format(self.test_id),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        self.perform_get_test_user_stats()
        return response

    def perform_add_fail_test_user_stats(self):
        """Method to perform add-fail to stats"""
        response = self.test_client.patch('/stats/{}/add-fail'.format(self.test_id),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        self.perform_get_test_user_stats()
        return response
    
    def perform_add_win_stats_by_id(self, userid):
        """Method to perform add-win to stats with specific userid"""
        response = self.test_client.patch('/stats/{}/add-win'.format(userid),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        return response

    def perform_add_fail_stats_by_id(self, userid):
        """Method to perform add-fail to stats with specific userid"""
        response = self.test_client.patch('/stats/{}/add-fail'.format(userid),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        return response
    
    def perform_get_stats_by_id(self, userid):
        """Method to perform get stats with specific userid"""
        response = self.test_client.get('/stats/{}'.format(userid),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        return response
    
    def perform_get_all_users(self):
        """Method to get all users"""
        response = self.test_client.get('/user',
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        return response
    
    def perform_get_user_by_username(self, username):
        """Method to get user with specific username"""
        response = self.test_client.get('/user/{}'.format(username),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        return response
    
    def perform_get_user_by_id(self, id):
        """Method to get user with specific id"""
        response = self.test_client.get('/user/id/{}'.format(id),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})

        return response

    def perform_patch_user_by_id(self, id, payload):
        """Method to get user with specific id"""
        response = self.test_client.patch('/user/id/{}'.format(id),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)},
            data = json.dumps(payload))
        
        return response
            