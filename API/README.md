# API

## Running in Docker

To get app to running in Docker, you simply need to run docker-compose using the following:

```shell
docker-compose up -d
```

If neccesary `docker-compose.yml` file can be edited to change the port or volumes.

## Running in Terminal

### Terminal commands
Note: make sure you have `pip` and `virtualenv` installed.
Initial installation
> make install

To run tests
> make tests

To run application
> make run

To run all commands at once
> make all

Make sure to run the initial migration commands to update the database.

```shell
> python main_app.py db init
> python main_app.py db migrate --message 'initial database migration'
> python main_app.py db upgrade
```

Basic commands:
Run API
> python main_app.py run
Run tests
> python main_app.py test
Run tests with coverage
> python main_app.py cov
Run tests with coverage and generate html reports
> python main_app.py covhtml

### Viewing the app

Open the following url on your browser to view swagger documentation `http://127.0.0.1:5000/`
