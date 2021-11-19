from .. import db
from app.main.model.token_blacklist_model import TokenBlackList
from .. import jwt
from app.main.schema.token_blacklist_schema import tokens_blacklist_schema
from datetime import datetime

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    """ Callback function to revoke tokens. """
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlackList.id).filter_by(jti=jti).scalar()
    return token is not None

def delete_expired_tokens():
    """ Method to delete expired tokens from blacklist. """
    jwt_tokens = TokenBlackList.query.all()
    jwt_tokens_list = tokens_blacklist_schema.dump(jwt_tokens)
    now_str = datetime.utcnow().isoformat(' ', 'seconds')
    now = datetime.strptime(now_str, '%Y-%m-%d %H:%M:%S')
    for jwt_token in jwt_tokens_list:
        if now > datetime.strptime(jwt_token['expiration_time'], '%Y-%m-%dT%H:%M:%S'):
            TokenBlackList.query.filter_by(id=jwt_token['id']).delete()
            db.session.commit()
