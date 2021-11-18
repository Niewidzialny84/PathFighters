class AuthorizedUser(object):
    """ Authorized User Model for storing user related details """
    def __init__(self, user, jwt_token):
        self.user = user
        self.jwt_token = jwt_token