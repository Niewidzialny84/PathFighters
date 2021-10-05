"""
Test User Services class
"""
import unittest
from app.main.service.user_service import *
from app.test.base import BaseTestCase

class TestUserServices(BaseTestCase):

    """ Test check if creation user process conduct properly and return 201 status code. """
    def test_user_serivces_add_new_user_201(self):
        request_dict = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user_1"
        }
        status_code = add_new_user(request_dict)
       
        self.assertEquals(status_code, 201)

        delete_all_users()

    """ Test check if creation user process return 409 status code. """
    def test_user_serivces_add_new_user_409(self):
        request_dict = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user_1"
        }

        status_code = add_new_user(request_dict)
        status_code = add_new_user(request_dict)
       
        self.assertEquals(status_code, 409)

        delete_all_users()
   
    """ Test check if service return proper user list. """
    def test_user_services_get_all_users_proper(self):
        request_dict_1 = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user_1"
        }

        request_dict_2 = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user_2"
        }

        add_new_user(request_dict_1)
        add_new_user(request_dict_2)
        
        list_of_users = get_all_users()
        
        self.assertEquals(len(list_of_users), 2)
        self.assertEquals(list_of_users[0].email, "test@test.com")
        self.assertEquals(list_of_users[0].password, "test")
        self.assertEquals(list_of_users[0].username, "test_user_1")
        
        self.assertEquals(list_of_users[1].email, "test@test.com")
        self.assertEquals(list_of_users[1].password, "test")
        self.assertEquals(list_of_users[1].username, "test_user_2")

        delete_all_users()
    
    """ Test check if service return proper empty user list. """
    def test_user_services_get_all_users_empty(self):
        list_of_users = get_all_users()
        
        self.assertEquals(list_of_users, [])
        self.assertTrue(len(list_of_users) == 0)
    
        delete_all_users()
    
    """ Test check if get user by username process conduct properly. """
    def test_user_serivces_get_user_by_username(self):
        request_dict_1 = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user_1"
        }

        request_dict_2 = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user_2"
        }

        add_new_user(request_dict_1)
        add_new_user(request_dict_2)
       
        user_1 = get_user("test_user_1")
        user_2 = get_user("test_user_2")

        self.assertEquals(user_1.id, 1)
        self.assertEquals(user_1.email, "test@test.com")
        self.assertEquals(user_1.password, "test")
        self.assertEquals(user_1.username, "test_user_1")
        
        self.assertEquals(user_2.id, 2)
        self.assertEquals(user_2.email, "test@test.com")
        self.assertEquals(user_2.password, "test")
        self.assertEquals(user_2.username, "test_user_2")
        
        delete_all_users()
    
    """ Test check if get user by id process conduct properly. """
    def test_user_serivces_get_user_by_id(self):
        request_dict_1 = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user_1"
        }

        request_dict_2 = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user_2"
        }

        add_new_user(request_dict_1)
        add_new_user(request_dict_2)
       
        user_1 = get_user_by_id(1)
        user_2 = get_user_by_id(2)

        self.assertEquals(user_1.id, 1)
        self.assertEquals(user_1.email, "test@test.com")
        self.assertEquals(user_1.password, "test")
        self.assertEquals(user_1.username, "test_user_1")
        
        self.assertEquals(user_2.id, 2)
        self.assertEquals(user_2.email, "test@test.com")
        self.assertEquals(user_2.password, "test")
        self.assertEquals(user_2.username, "test_user_2")
        
        delete_all_users()
        
if __name__ == '__main__':
    unittest.main()