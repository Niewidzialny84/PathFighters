"""
Registration service file.
"""
import requests

API_ALL_USERS = "http://127.0.0.1:5000/users"

def api_add_user(request_json):
    response = requests.post(API_ALL_USERS, json = request_json)
    return response.status_code