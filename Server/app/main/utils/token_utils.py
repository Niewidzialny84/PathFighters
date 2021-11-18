from .. import db
from app.main.model.token_blacklist_model import TokenBlackList
from .. import jwt
from app.main.schema.token_blacklist_schema import TokenBlacklistSchema, tokens_blacklist_schema
from datetime import datetime
from datetime import timedelta
from datetime import timezone

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlackList.id).filter_by(jti=jti).scalar()
    return token is not None

def delete_expired_tokens():
    tokens = TokenBlackList.query.all()
    data = tokens_blacklist_schema.dump(tokens)
    now_str = datetime.utcnow().isoformat(' ', 'seconds')
    now = datetime.strptime(now_str, '%Y-%m-%d %H:%M:%S')
    # print(now)
    # print(data)
    for token in data:
        # print(now_str)
        # print(datetime.strptime(token['expiration_time'], '%Y-%m-%dT%H:%M:%S'))
        if now > datetime.strptime(token['expiration_time'], '%Y-%m-%dT%H:%M:%S'):
            TokenBlackList.query.filter_by(id=token['id']).delete()
            db.session.commit()
    # datetime.strptime(