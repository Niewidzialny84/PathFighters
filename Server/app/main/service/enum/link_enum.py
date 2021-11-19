from enum import Enum

class LinkEnum(Enum): # HERE WE SHOULD CHANGE LINKS TO APPROPRIET VERSION ON DEPLOY
    """ Enumerate class which store links information. """
    API_ALL_USERS = "http://127.0.0.1:5000/users" 
    API_USER_BY_USERNAME = "http://127.0.0.1:5000/users/{}"
    API_USER_BY_ID = "http://127.0.0.1:5000/users/id/{}"
    API_ALL_STATS= "http://127.0.0.1:5000/stats"
    API_STATS_BY_ID = API_ALL_STATS + "/{}"
    API_STATS_ADD_WIN = API_STATS_BY_ID + "/add-win"
    API_STATS_ADD_FAIL = API_STATS_BY_ID + "/add-fail"
    