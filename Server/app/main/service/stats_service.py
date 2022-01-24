"""
Stats service file.
"""
import requests
from app.main.model.stats_model import Stats
from app.main.service.enum.link_enum import LinkEnum

def api_get_all_stats():
    """ Method to get all stats list. """
    response = requests.get(LinkEnum.API_ALL_STATS.value)
    try:
        return response.status_code, response.json()
    except Exception as _:
        return response.status_code, None

def api_get_user_stats(userid):
    """ Method to get stats with specific userid. """
    response = requests.get(LinkEnum.API_STATS_BY_ID.value.format(userid))
    try:
        return response.status_code, Stats(**response.json())
    except Exception as _:
        return response.status_code, None

def api_stats_add_win(userid):
    """ Method to add win into stats with specific userid. """
    response = requests.patch(LinkEnum.API_STATS_ADD_WIN.value.format(userid))
    return response.status_code
    
def api_stats_add_fail(userid):
    """ Method to add fail into stats with specific userid. """
    response = requests.patch(LinkEnum.API_STATS_ADD_FAIL.value.format(userid))
    return response.status_code
