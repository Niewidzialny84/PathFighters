class AuthorizedUser(object):
    """ Authorized User Model for storing user related details """
    def __init__(self, user, token):
        self.user = user
        self.token = token