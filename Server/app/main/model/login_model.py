import json

class Login(object):
    """ Login Model for storing login details. """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "{\"username\":\"'{}'\", \"password\":\"'{}'\"}".format(self.username, self.password)
    