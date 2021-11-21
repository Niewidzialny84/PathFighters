class Token(object):
    """ Token Model for storing content of jwt_token. """
    def __init__(self, jwt_token):
        self.jwt_token = jwt_token
        