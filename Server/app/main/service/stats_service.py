"""
Users service file.
"""
# from app.main.model.login_model import Login # pragma: no cover
import requests, json
from app.main.model.stats_model import Stats

API_ALL_STATS= "http://127.0.0.1:5000/stats"
API_STATS_BY_ID = API_ALL_STATS + "/{}"
API_STATS_ADD_WIN = API_STATS_BY_ID + "/add-win"
API_STATS_ADD_FAIL = API_STATS_BY_ID + "/add-fail"

def api_get_all_stats():
    response = requests.get(API_ALL_STATS)
    try:
        return response.status_code, response.json()
    except Exception as _:
        return response.status_code, None

def api_get_user_stats(id):
    response = requests.get(API_STATS_BY_ID.format(id))
    try:
        return response.status_code, Stats(**response.json())
    except Exception as _:
        return response.status_code, None

def api_stats_add_win(id):
    response = requests.patch(API_STATS_ADD_WIN.format(id))
    return response.status_code
    
def api_stats_add_fail(id):
    response = requests.patch(API_STATS_ADD_FAIL.format(id))
    return response.status_code