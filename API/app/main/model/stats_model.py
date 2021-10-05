from .. import db

class Stats(db.Model):
    """ Stats Model for storing user statistics. """
    __tablename__ = "stats"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    fails = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False)

    def __init__(self, userid, total, fails, wins):
        self.userid = userid
        self.total = total
        self.fails = fails
        self.wins = wins

    def __repr__(self):
        return "<Stats for user with id: '{}'>".format(self.userid)