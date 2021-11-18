"""
This is main app of Server.
"""
import os
import unittest
import alembic
import coverage
import time
import threading
from flask_script import Manager
from app import blueprint
from app.main import create_app, db, jwt
from app.main.utils.token_utils import delete_expired_tokens

# from datetime import datetime
# from datetime import timedelta
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
# from flask_jwt_extended import JWTManager
# from flask_jwt_extended import get_jwt
# from flask_jwt_extended import set_access_cookies
# from flask_jwt_extended import unset_jwt_cookies
# from datetime import timezone


app = create_app(os.getenv('ENGINEER_Server') or 'dev')
app.app_context().push()
db.create_all()

app.register_blueprint(blueprint)

app.app_context().push()

main_app = Manager(app)

@main_app.command
def run():
    """Runs main app."""
    app.run(host='0.0.0.0', port=5001, use_reloader=False) #, ssl_context="adhoc"

@main_app.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@main_app.command
def covhtml():
    """Runs the unit tests with coverage."""
    
    cover = coverage.coverage(branch=True, include='app/main*')
    cover.start()

    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        cover.stop()
        cover.save()
        print('Coverage Summary:')
        cover.report(omit=['main_app.py', 'app/main/__init__.py', 'test/*', 'venv*/*'])
        # cov.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        cover.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        cover.erase()
        return 0
    return 1

@main_app.command
def cov():
    """Runs the unit tests with coverage."""
    
    cover = coverage.coverage(branch=True, include='app/main*')
    cover.start()

    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        cover.stop()
        cover.save()
        print('Coverage Summary:')
        cover.report(omit=['main_app.py', 'app/main/__init__.py', 'test/*', 'venv*/*'])
        cover.erase()
        return 0
    return 1

# @app.after_request
# def refresh_expiring_jwts(response):
#     try:
#         exp_timestamp = get_jwt()["exp"]
#         now = datetime.now(timezone.utc)
#         target_timestamp = datetime.timestamp(now + timedelta(minutes=1))
#         if target_timestamp > exp_timestamp:
#             access_token = create_access_token(identity=get_jwt_identity())
#             set(response, access_token)
#         return response
#     except (RuntimeError, KeyError):
#         # Case where there is not a valid JWT. Just return the original respone
#         return response

# from datetime import datetime

def schedule_tokens():
    while(True):
        # print(threading.active_count())
        with app.app_context():
            delete_expired_tokens()
        time.sleep(1)

if __name__ == '__main__':
    try:
        t2 = threading.Thread(target=schedule_tokens)
        t2.daemon = True
        t2.start()
       
        main_app.run(default_command="run")
    except alembic.util.exc.CommandError as ex:
        t2.join
        print(ex)
