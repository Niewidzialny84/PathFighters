from .. import db

class Stats(db.Model):
    """ Stats Model for storing user statistics. """
    __tablename__ = "stats"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), db.ForeignKey("users.username", ondelete='CASCADE'), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    fails = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False)

    def __init__(self, username, total, fails, wins):
        self.username = username
        self.total = total
        self.fails = fails
        self.wins = wins

    def __repr__(self):
        return "<Stats for user: '{}'>".format(self.username)
    
