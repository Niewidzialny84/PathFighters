"""
Test User Db
"""
import unittest
from app.main import db
from app.main.model.user_model import User
from app.test.base import BaseTestCase

class TestUserDb(BaseTestCase):

    """ Test checks if creation user process conducted properly. """
    def test_user_db_proper_creation(self):
        user = User(
            email='test@test.com',
            password='test',
            username = 'test_user_1'
        )
        db.session.add(user)
        db.session.commit()
        
        user = User.query.filter_by(username = "test_user_1").first()
        
        self.assertTrue(isinstance(user, User))
        self.assertTrue(user.id == 1)
        self.assertTrue(user.email == 'test@test.com')
        self.assertTrue(user.password == 'test')
        self.assertTrue(user.username == 'test_user_1')
       
        db.session.delete(user)
        db.session.commit()
    
    """ Test checks if delete user process conducted properly. """
    def test_user_db_proper_delete(self):
        user = User(
            email='test@test.com',
            password='test',
            username = 'test_user_1'
        )
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(username = "test_user_1").first()
       
        db.session.delete(user)
        db.session.commit()
        self.assertTrue(User.query.all() == [])
    
    """ Test checks if autoincrement function work properly. """
    def test_user_db_proper_id_autoincrement(self):
        user_1 = User(
            email='test@test.com',
            password='test',
            username = 'test_user_1'
        )

        user_2 = User(
            email='test@test.com',
            password='test',
            username = 'test_user_2'
        )

        db.session.add(user_1)
        db.session.add(user_2)
        db.session.commit()

        id_1 = User.query.filter_by(username = "test_user_1").first().id
        id_2 = User.query.filter_by(username = "test_user_2").first().id
        
        self.assertTrue(id_1 == 1)
        self.assertTrue(id_2 == 2)

        db.session.query(User).delete()
        db.session.commit()
    
    """ Test checks if it is possible to create 1000 users. """
    def test_user_db_proper_create_1000_users(self):
        for i in range(1000):
            user = User(
            email='test@test.com',
            password='test',
            username = 'test_user_' + str(i)) 

            db.session.add(user)
        
        db.session.commit()
        
        self.assertTrue(len(User.query.all()) == 1000)
        
        db.session.query(User).delete()
        db.session.commit()

    """ Test checks if delete 1000 users process conducted properly. """    
    def test_user_db_proper_delete_1000_users(self):
        for i in range(1000):
            user = User(
            email='test@test.com',
            password='test',
            username = 'test_user_' + str(i)) 

            db.session.add(user)
        
        db.session.commit()
        
        db.session.query(User).delete()
        db.session.commit()

        self.assertTrue(User.query.all() == [])
    
    """ Test checks if modification user process conducted properly. """
    def test_user_db_modification(self):
        user = User(
            email='test@test.com',
            password='test',
            username = 'test_user_1'
        )
        db.session.add(user)
        db.session.commit()
        
        user = User.query.filter_by(username = "test_user_1").first()

        self.assertTrue(isinstance(user, User))
        self.assertTrue(user.id == 1)
        self.assertTrue(user.email == 'test@test.com')
        self.assertTrue(user.password == 'test')
        self.assertTrue(user.username == 'test_user_1')

        user.email = 'test_2@test.com'
        user.password = 'test_2'
        user.username = 'test_user_2'

        db.session.commit()

        user = User.query.filter_by(username = "test_user_2").first()

        self.assertTrue(isinstance(user, User))
        self.assertTrue(user.id == 1)
        self.assertTrue(user.email == 'test_2@test.com')
        self.assertTrue(user.password == 'test_2')
        self.assertTrue(user.username == 'test_user_2')
       
        db.session.delete(user)
        db.session.commit()
        
if __name__ == '__main__':
    unittest.main()

