from datetime import datetime
from .. import db
from datetime import datetime

class TokenBlackList(db.Model):
    """ Token Black List Model for storing basic information about jwt_token. """
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    expiration_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    