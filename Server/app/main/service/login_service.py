"""
Login service file.
"""
from app.main.model.authorized_user_model import AuthorizedUser # pragma: no cover
from app.main.model.login_model import Login # pragma: no cover
from app.main.service.users_service import api_get_user_by_username # pragma: no cover
from flask_jwt_extended import create_access_token # pragma: no cover

def handle_login_data(request_json):
    """ Method to process login details. """
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
    authorized_user = AuthorizedUser(user, access_token)

    return status_code, authorized_user
