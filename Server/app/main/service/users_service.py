"""
Users service file.
"""
# from app.main.model.login_model import Login # pragma: no cover
import requests, json
from app.main.model.user_model import User

API_ALL_USERS = "http://127.0.0.1:5000/users"
API_USER_BY_USERNAME = "http://127.0.0.1:5000/users/{}"
API_USER_BY_ID = "http://127.0.0.1:5000/users/id/{}"

def api_get_users():
    response = requests.get(API_ALL_USERS)
    try:
        return response.status_code, response.json()
    except Exception as _:
        return response.status_code, None

def api_get_user_by_username(username):
    response = requests.get(API_USER_BY_USERNAME.format(username))
    try:
        return response.status_code, User(**response.json())
    except Exception as _:
        return response.status_code, None

def api_get_user_by_id(id):
    response = requests.get(API_USER_BY_ID.format(id))
    try:
        return response.status_code, User(**response.json())
    except Exception as _:
        return response.status_code, None

def api_update_user_by_id(id, request_json):
    response = requests.patch(API_USER_BY_ID.format(id),  json=request_json)
    return response.status_code
    
def api_delete_user_by_id(id):
    response = requests.delete(API_USER_BY_ID.format(id))
    return response.status_code
        