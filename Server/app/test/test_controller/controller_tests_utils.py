"""
Utils class for controller tests
"""
import json
from app.test.base import BaseTestCase

class ControllerTestsUtils():
    def __init__(self): 
        self.test_client = BaseTestCase.create_app(self).test_client()
        self.test_username = "username"
        self.test_email =  "test@test.pl"
        self.test_password = "testPasswd"
        self.test_id = None
        self.test_stats_id = None
        self.test_wins = None
        self.test_fails = None
        self.test_jwt_token = ""
        self.create_test_user()
        self.perform_test_login()
        self.perform_get_test_stats()
    
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
        
        return response.status_code, response.json
    
    def perform_test_login(self):
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
        
        return response.status_code, response.json
    
    def perform_get_test_stats(self):
        """Method to perform get stats"""
        response = self.test_client.get('/stats/{}'.format(self.test_id),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        if response.status_code == 200:
            self.test_stats_id = response.json['id']
            self.test_wins = response.json['wins']
            self.test_fails = response.json['fails']
        
        return response.status_code, response.json
    
    def perform_delete_test_user(self):
        """Method to delete test user"""
        response = self.test_client.delete('/user/{}'.format(self.test_id),
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        return response.status_code, response.json
    
    def perform_logout(self):
        """Method to perform get stats"""
        response = self.self.test_client.delete('/logout',
            headers = {"Authorization": "Bearer {}".format(self.test_jwt_token)})
        
        return response.status_code, response.json
