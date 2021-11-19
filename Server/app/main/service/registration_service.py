"""
Registration service file.
"""
import requests
from app.main.service.enum.link_enum import LinkEnum

def api_add_user(request_json):
    """ Method to perform registraion process. """
    response = requests.post(LinkEnum.API_ALL_USERS.value, json = request_json)
    return response.status_code
