"""
Refresh token service file.
"""
from app.main.model.login_model import Login # pragma: no cover
from app.main.service.users_service import api_get_user_by_username
from flask_jwt_extended import create_access_token
from ..model.token_model import Token

def refresh_token(request_json):
    """ Method to refresh jwt_token. """
    try:
        login = Login(**request_json)
    except Exception as _:
        login = None
    
    if login is None or None in [login.username, login.password]:
        return 400, None
    
    status_code, user = api_get_user_by_username(login.username)

    if user is None:
        return 404, None
    elif user.password != login.password:
        return 400, None

    access_token = create_access_token(identity=user.password)
    return status_code, Token(access_token)
