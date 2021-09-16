import unittest

import datetime

from app.main import db
from app.main.model.user_model import User
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_proper_user_creation(self):
        user = User(
            email='test@test.com',
            password='test',
            username = 'test_user_1'
        )
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(username = "test_user_1").first()
        self.assertTrue(isinstance(user, User))

if __name__ == '__main__':
    unittest.main()

