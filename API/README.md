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


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/