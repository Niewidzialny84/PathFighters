class User(object):
    """ User Model for storing user related details """
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return "{\"id\":\"'{}'\", \"username\":\"'{}'\", \"email\":\"'{}'\", \"password\":\"'{}'\"}".format(
            self.id,
            self.username,
            self.email,
            self.password)