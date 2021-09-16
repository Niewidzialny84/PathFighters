# from flask import Flask, request, jsonify, make_response
# from flask_sqlalchemy import SQLAlchemy 
# from flask_marshmallow import Marshmallow
# from flask_restful import Resource, Api
# from sqlalchemy.orm import validates, Session
# from marshmallow import fields, validate
# from datetime import datetime
# from sqlalchemy.sql import func

# app = Flask(__name__) 
# api = Api(app) 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ptDatabase.db' 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
# db = SQLAlchemy(app) 
# ma = Marshmallow(app)

# api.add_resource(UserManager, '/api/users')

# api.add_resource(HistoryManager, '/api/history-manager')  

# if __name__ == '__main__':
#     app.run(debug=True)


import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db, ma
from app.main.model.user_model import User

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
