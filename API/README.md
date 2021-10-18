#### API

### Terminal commands
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all

Make sure to run the initial migration commands to update the database.
    
    > python main_app.py db init

    > python main_app.py db migrate --message 'initial database migration'

    > python main_app.py db upgrade

Basic commands:

    > python main_app.py run -> to run API

    > python main_app.py test -> run tests

    > python main_app.py cov -> run tests with coverage

    > python main_app.py covhtml -> run tests with coverage and generate html reports

### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/