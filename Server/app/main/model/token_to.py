class Token(object):
    """ Token Model for storing user related details """
    def __init__(self, jwt_token):
        self.jwt_token = jwt_token