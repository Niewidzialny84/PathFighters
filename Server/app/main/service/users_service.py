"""
Users service file.
"""
import requests
from app.main.model.user_model import User
from app.main.service.enum.link_enum import LinkEnum

def api_get_users():
    """ Method to get all users list. """
    response = requests.get(LinkEnum.API_ALL_USERS.value)
    try:
        return response.status_code, response.json()
    except Exception as _:
        return response.status_code, None

def api_get_user_by_username(username):
    """ Method to get user with specific username. """
    response = requests.get(LinkEnum.API_USER_BY_USERNAME.value.format(username))
    try:
        return response.status_code, User(**response.json())
    except Exception as _:
        return response.status_code, None

def api_get_user_by_id(id):
    """ Method to get user with specific id. """
    response = requests.get(LinkEnum.API_USER_BY_ID.value.format(id))
    try:
        return response.status_code, User(**response.json())
    except Exception as _:
        return response.status_code, None

def api_update_user_by_id(id, request_json):
    """ Method to get update user with specific id. """
    response = requests.patch(LinkEnum.API_USER_BY_ID.value.format(id),  json=request_json)
    return response.status_code
    
def api_delete_user_by_id(id):
    """ Method to get delete user with specific id. """
    response = requests.delete(LinkEnum.API_USER_BY_ID.value.format(id))
    return response.status_code
        