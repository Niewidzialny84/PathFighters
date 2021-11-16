"""
Login service file.
"""
import requests, json
from app.main.model.user_model import User
from app.main.utils import users, stats
from app.main.model.login_model import Login # pragma: no cover
from app.main.utils import * # pragma: no cover
from ..utils import API_URL

API_SPECIFIC_USER = API_URL + "/users/{}"

def handle_login_data(request_json):
    try:
        login = Login(**request_json)
    except Exception as _:
        login = None
    
    if login is None or None in [login.username, login.password]:
        return 400, None
    
    user = api_get_user(login.username)

    if stats is None:
        return 404, None

    return user

def api_get_user(username):
    response = requests.get("http://127.0.0.1:5000/users/" + username)
    try:
        j = response.json()
        user = User(**j)
    except Exception as _:
        user = None

    return user
