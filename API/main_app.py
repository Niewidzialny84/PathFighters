"""
This is main app of API.
"""
import os
import unittest
import alembic
import coverage
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import blueprint
from app.main import create_app, db

app = create_app(os.getenv('ENGINEER_API') or 'dev')

app.register_blueprint(blueprint)

app.app_context().push()

main_app = Manager(app)

migrate = Migrate(app, db)

main_app.add_command('db', MigrateCommand)

@main_app.command
def run():
    """Runs main app."""
    app.run()

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

if __name__ == '__main__':
    try:
        main_app.run()
    except alembic.util.exc.CommandError as ex:
        print(ex)
