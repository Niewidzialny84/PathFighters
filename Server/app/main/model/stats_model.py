class Stats(object):
    """ Stats Model for storing user statistics. """
    def __init__(self, id, userid, total, fails, wins):
        self.id = id
        self.userid = userid
        self.total = total
        self.fails = fails
        self.wins = wins
        