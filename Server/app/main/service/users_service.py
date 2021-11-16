import requests, json
from app.main.model.user_model import User
from server import API_URL
from app.main.utils import users, stats

"""
Users service file.
"""
from app.main.model.login_model import Login # pragma: no cover
from app.main.utils import * # pragma: no cover

API_ALL_USERS = API_URL + "/users"

def api_get_users():
    response = requests.get(API_ALL_USERS)
    try:
        j = json.loads(response.json())
        users = list(User(**j))
    except Exception as _:
        users = None