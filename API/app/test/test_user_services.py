"""
Test User Services class
"""
import unittest
from app.main.service.user_service import *
from app.test.base import BaseTestCase

class TestUserServices(BaseTestCase):

    def test_user_serivces_add_new_user_201(self):
        """ [ Test checks if creation user process conducted properly and return 201 status code. ] """

        request_dict = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user_1"
        }
        status_code = add_new_user(request_dict)
       
        self.assertEqual(status_code, 201)

        delete_all_users()

   
    def test_user_serivces_add_new_user_409(self):
        """ [ Test checks if creation user process return 409 status code. ] """

        request_dict = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user_1"
        }

        status_code = add_new_user(request_dict)
        status_code = add_new_user(request_dict)
       
        self.assertEqual(status_code, 409)

        delete_all_users()
   
    def test_user_services_get_all_users_proper(self):
        """ [ Test checks if service return proper user list. ] """

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
        
        self.assertEqual(len(list_of_users), 2)
        self.assertEqual(list_of_users[0].email, "test@test.com")
        self.assertEqual(list_of_users[0].password, "test")
        self.assertEqual(list_of_users[0].username, "test_user_1")
        
        self.assertEqual(list_of_users[1].email, "test@test.com")
        self.assertEqual(list_of_users[1].password, "test")
        self.assertEqual(list_of_users[1].username, "test_user_2")

        delete_all_users()
    
    def test_user_services_get_all_users_empty(self):
        """ [ Test checks if service return proper empty user list. ] """

        list_of_users = get_all_users()
        
        self.assertEqual(list_of_users, [])
        self.assertTrue(len(list_of_users) == 0)
    
        delete_all_users()
    
    def test_user_serivces_get_user_by_username(self):
        """ [ Test checks if get user by username process conducted properly. ] """

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

        self.assertEqual(user_1.id, 1)
        self.assertEqual(user_1.email, "test@test.com")
        self.assertEqual(user_1.password, "test")
        self.assertEqual(user_1.username, "test_user_1")
        
        self.assertEqual(user_2.id, 2)
        self.assertEqual(user_2.email, "test@test.com")
        self.assertEqual(user_2.password, "test")
        self.assertEqual(user_2.username, "test_user_2")
        
        delete_all_users()
    
    def test_user_serivces_get_user_by_id(self):
        """ [ Test checks if get user by id process conducted properly. ] """

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

        self.assertEqual(user_1.id, 1)
        self.assertEqual(user_1.email, "test@test.com")
        self.assertEqual(user_1.password, "test")
        self.assertEqual(user_1.username, "test_user_1")
        
        self.assertEqual(user_2.id, 2)
        self.assertEqual(user_2.email, "test@test.com")
        self.assertEqual(user_2.password, "test")
        self.assertEqual(user_2.username, "test_user_2")
        
        delete_all_users()
    
    def test_user_services_user_put_by_username_200(self):
        """ [ Test checks if put user process conducted properly and return 200 statse code. ] """
        
        request_dict = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user"
        }

        request_dict_new = {
            "email" : "test_new@test.com",
            "password" : "test_new",
            "username" : "test_user_new"
        }

        add_new_user(request_dict)

        status_code = user_put("test_user", request_dict_new)

        user = get_user_by_id(1)

        self.assertEqual(status_code, 200)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.email, "test_new@test.com")
        self.assertEqual(user.password, "test_new")
        self.assertEqual(user.username, "test_user_new")

        delete_all_users()
    
    def test_user_services_user_put_by_username_404(self):
        """ [ Test checks if put user process handle error and return 404 statse code. ] """

        request_dict_new = {
            "email" : "test_new@test.com",
            "password" : "test_new",
            "username" : "test_user_new"
        }

        status_code = user_put("test_user_new", request_dict_new)

        user = get_user_by_id(1)

        self.assertEqual(status_code, 404)
        self.assertEqual(user, None)
    
    def test_user_services_user_put_by_username_400(self):
        """ [ Test checks if put user process handle error and return 400 statse code. ] """

        request_dict = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user"
        }

        request_dict_new = {}

        add_new_user(request_dict)

        status_code = user_put("test_user", request_dict_new)

        user = get_user_by_id(1)

        self.assertEqual(status_code, 400)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.email, "test@test.com")
        self.assertEqual(user.password, "test")
        self.assertEqual(user.username, "test_user")

        delete_all_users()
    
    def test_user_services_user_put_by_id_200(self):
        """ [ Test checks if put user process conducted properly and return 200 statse code. ] """
        
        request_dict = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user"
        }

        request_dict_new = {
            "email" : "test_new@test.com",
            "password" : "test_new",
            "username" : "test_user_new"
        }

        add_new_user(request_dict)

        status_code = user_put_by_id(1, request_dict_new)

        user = get_user_by_id(1)

        self.assertEqual(status_code, 200)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.email, "test_new@test.com")
        self.assertEqual(user.password, "test_new")
        self.assertEqual(user.username, "test_user_new")

        delete_all_users()
    
    def test_user_services_user_put_by_id_404(self):
        """ [ Test checks if put user process handle error and return 404 statse code. ] """

        request_dict_new = {
            "email" : "test_new@test.com",
            "password" : "test_new",
            "username" : "test_user_new"
        }

        status_code = user_put_by_id(1, request_dict_new)

        user = get_user_by_id(1)

        self.assertEqual(status_code, 404)
        self.assertEqual(user, None)
    
    def test_user_services_user_put_by_id_400(self):
        """ [ Test checks if put user process handle error and return 400 statse code. ] """

        request_dict = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user"
        }

        request_dict_new = {}

        add_new_user(request_dict)

        status_code = user_put_by_id(1, request_dict_new)

        user = get_user_by_id(1)

        self.assertEqual(status_code, 400)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.email, "test@test.com")
        self.assertEqual(user.password, "test")
        self.assertEqual(user.username, "test_user")

        delete_all_users()
    
    def test_user_services_delete_all_users(self):
        """ [ Test checks if delete all users process conducted properly. ] """
        
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

        users = get_all_users()
        self.assertEqual(len(users), 2)

        delete_all_users()

        users = get_all_users()
        self.assertEqual(len(users), 0)
    
    def test_user_services_delete_user_by_username_200(self):
        """ [ Test checks if delete user by username process conducted properly and return 200 status code. ] """
        
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

        users = get_all_users()
        self.assertEqual(len(users), 2)

        status_code = delete_user("test_user_1")

        users = get_all_users()
        self.assertEqual(status_code, 200)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "test_user_2")

        delete_all_users()
    
    def test_user_services_delete_user_by_username_404(self):
        """ [ Test checks if delete user by username process properly handle error and return 404 status code. ] """
        
        status_code = delete_user("test_user")
        self.assertEqual(status_code, 404)

    def test_user_services_delete_user_by_id_200(self):
        """ [ Test checks if delete user by id process conducted properly and return 200 status code. ] """
        
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

        users = get_all_users()
        self.assertEqual(len(users), 2)

        status_code = delete_user_by_id(1)

        users = get_all_users()
        self.assertEqual(status_code, 200)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "test_user_2")

        delete_all_users()
    
    def test_user_services_delete_user_by_id_404(self):
        """ [ Test checks if delete user by id process properly handle error and return 404 status code. ] """
        
        status_code = delete_user_by_id(1)
        self.assertEqual(status_code, 404)

    def test_user_services_user_patch_by_username_200(self):
        """ [ Test checks if patch user by username process conducted properly and return 200 status code. ] """
        
        request_dict = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user"
        }

        request_dict_new = {
            "email" : "test_new@test.com",
            "password" : "test_new",
            "username" : "test_user_new"
        }

        add_new_user(request_dict)

        status_code = user_patch("test_user", request_dict_new)
        
        user = get_user("test_user_new")

        self.assertEqual(status_code, 200)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.email, "test_new@test.com")
        self.assertEqual(user.username, "test_user_new")

        delete_all_users()
    
    def test_user_services_user_patch_by_username_404(self):
        """ [ Test checks if patch user by username process handle error and return 404 statse code. ] """

        request_dict_new = {
            "email" : "test_new@test.com",
            "password" : "test_new",
            "username" : "test_user_new"
        }

        status_code = user_patch("test_user_new", request_dict_new)

        user = get_user("test_user_new")

        self.assertEqual(status_code, 404)
        self.assertEqual(user, None)
    
    def test_user_services_user_patch_by_username_400(self):
        """ [ Test checks if patch user by username process handle error and return 400 statse code. ] """

        request_dict = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user"
        }

        request_dict_new = {}

        add_new_user(request_dict)

        status_code = user_patch(None, request_dict_new)

        user = get_user("test_user")

        self.assertEqual(status_code, 400)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.email, "test@test.com")
        self.assertEqual(user.password, "test")
        self.assertEqual(user.username, "test_user")

        delete_all_users()
    
    def test_user_services_user_patch_by_id_200(self):
        """ [ Test checks if patch user by id process conducted properly and return 200 statse code. ] """
        
        request_dict = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user"
        }

        request_dict_new = {
            "email" : "test_new@test.com",
            "password" : "test_new",
            "username" : "test_user_new"
        }

        add_new_user(request_dict)

        status_code = user_patch_by_id(1, request_dict_new)
        
        user = get_user_by_id(1)

        self.assertEqual(status_code, 200)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.email, "test_new@test.com")
        self.assertEqual(user.username, "test_user_new")

        delete_all_users()
    
    def test_user_services_user_patch_by_id_404(self):
        """ [ Test checks if patch user by id process handle error and return 404 statse code. ] """

        request_dict_new = {
            "email" : "test_new@test.com",
            "password" : "test_new",
            "username" : "test_user_new"
        }

        status_code = user_patch_by_id(1, request_dict_new)

        user = get_user_by_id(1)

        self.assertEqual(status_code, 404)
        self.assertEqual(user, None)
    
    def test_user_services_user_patch_by_id_400(self):
        """ [ Test checks if patch user by id process handle error and return 400 statse code. ] """

        request_dict = {
            "email" : "test@test.com",
            "password" : "test",
            "username" : "test_user"
        }

        request_dict_new = {}

        add_new_user(request_dict)

        status_code = user_patch_by_id(None, request_dict_new)

        user = get_user_by_id(1)

        self.assertEqual(status_code, 400)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.email, "test@test.com")
        self.assertEqual(user.password, "test")
        self.assertEqual(user.username, "test_user")

        delete_all_users()
        
if __name__ == '__main__':
    unittest.main()