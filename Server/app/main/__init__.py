from flask import Flask, request
from flask_marshmallow import Marshmallow

from .config import config_by_name
from flask.app import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

ma = Marshmallow()
db = SQLAlchemy()
jwt = JWTManager()   

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    app.config["JWT_SECRET_KEY"] = "jLfaiVjHUgFA/4+#Q$"  # Change this "super secret" with something else!
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    jwt.init_app(app)

    # @app.before_request
    # def before_request() -> None:
    #     """ Get server_name from http_host """
        
    #     http_host = request.environ.get('HTTP_HOST')
    #     app.config['SERVER_NAME'] = http_host

    return app
