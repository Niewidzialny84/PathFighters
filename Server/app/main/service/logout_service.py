"""
Logout service file.
"""
from flask_jwt_extended import get_jwt
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from ..model.token_blacklist_model import TokenBlackList
from .. import db
import pytz

def handle_logout():
    jti = get_jwt()["jti"]
    exp_time = datetime.fromtimestamp(get_jwt()["exp"], pytz.utc)
    db.session.add(TokenBlackList(jti=jti, expiration_time=exp_time))
    db.session.commit()