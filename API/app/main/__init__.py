from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

from .config import config_by_name
from flask.app import Flask

db = SQLAlchemy()
ma = Marshmallow()
flask_bcrypt = Bcrypt()

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    @app.before_request
    def before_request() -> None:
        """ Get server_name from http_host """
        
        http_host = request.environ.get('HTTP_HOST')
        app.config['SERVER_NAME'] = http_host

    return app
