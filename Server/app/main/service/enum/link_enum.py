from enum import Enum

class LinkEnum(Enum): # HERE WE SHOULD CHANGE LINKS TO APPROPRIET VERSION ON DEPLOY
    """ Enumerate class which store links information. """
    API_URL = "http://127.0.0.1:5000"
    API_ALL_USERS = API_URL + "/users" 
    API_USER_BY_USERNAME = API_URL + "/users/{}"
    API_USER_BY_ID = API_URL + "/users/id/{}"
    API_ALL_STATS= API_URL + "/stats"
    API_STATS_BY_ID = API_ALL_STATS + "/{}"
    API_STATS_ADD_WIN = API_STATS_BY_ID + "/add-win"
    API_STATS_ADD_FAIL = API_STATS_BY_ID + "/add-fail"
    