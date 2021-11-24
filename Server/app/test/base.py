
from flask_testing import TestCase
import app

from app.main import db
from server import app


class BaseTestCase(TestCase):
    """ Base Tests """
    def __init__(self):
        super().__init__()

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
