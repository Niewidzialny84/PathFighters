from flask import Flask
from flask_marshmallow import Marshmallow

from .config import config_by_name
from flask.app import Flask
from flask_jwt_extended import JWTManager

ma = Marshmallow()

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    app.config["JWT_SECRET_KEY"] = "jLfaiVjHUgFA/4+#Q$"  # Change this "super secret" with something else!
    jwt = JWTManager(app)   

    return app
