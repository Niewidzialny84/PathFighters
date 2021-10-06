"""
Test Stats Db
"""
import unittest
from app.main import db
from app.main.model.stats_model import Stats
from app.test.base import BaseTestCase

class TestStatsDb(BaseTestCase):

    def test_stats_db_proper_creation(self):
        """ Test check if creation stats process conduct properly. """
        stats = Stats(
            userid = 1,
            total = 3,
            wins = 2,
            fails = 1
        )
        db.session.add(stats)
        db.session.commit()
        
        stats = Stats.query.filter_by(userid = 1).first()
        
        self.assertTrue(isinstance(stats, Stats))
        self.assertTrue(stats.id == 1)
        self.assertTrue(stats.userid == 1)
        self.assertTrue(stats.total == 3)
        self.assertTrue(stats.wins == 2)
        self.assertTrue(stats.fails == 1)
       
        db.session.delete(stats)
        db.session.commit()
    
    
    def test_stats_db_proper_delete(self):
        """ Test check if delete stat process conduct properly. """
        stats = Stats(
            userid = 1,
            total = 3,
            wins = 2,
            fails = 1
        )
        db.session.add(stats)
        db.session.commit()

        stats = Stats.query.filter_by(userid = 1).first()
       
        db.session.delete(stats)
        db.session.commit()
        self.assertTrue(Stats.query.all() == [])
    
    def test_stats_db_proper_id_autoincrement(self):
        """ Test check if autoincrement function work properly. """
        stats_1 = Stats(
            userid = 4,
            total = 3,
            wins = 2,
            fails = 1
        )

        stats_2 = Stats(
            userid = 5,
            total = 3,
            wins = 2,
            fails = 1
        )

        db.session.add(stats_1)
        db.session.add(stats_2)
        db.session.commit()

        id_1 = Stats.query.filter_by(userid = 4).first().id
        id_2 = Stats.query.filter_by(userid = 5).first().id
        
        self.assertTrue(id_1 == 1)
        self.assertTrue(id_2 == 2)

        db.session.query(Stats).delete()
        db.session.commit()
    
    def test_stats_db_proper_create_1000_stats(self):
        """ Test check if it is possible to create 1000 stats. """
        for i in range(1000):
            stats = Stats(
                userid = i,
                total = 3,
                wins = 2,
                fails = 1
            )

            db.session.add(stats)
        
        db.session.commit()
        
        self.assertTrue(len(Stats.query.all()) == 1000)
        
        db.session.query(Stats).delete()
        db.session.commit()
  
    def test_stats_db_proper_delete_1000_stats(self):
        """ Test check if delete 1000 stats process conduct properly. """  
        for i in range(1000):
            stats = Stats(
            userid = i,
            total = 3,
            wins = 2,
            fails = 1)

            db.session.add(stats)
        
        db.session.commit()
        
        db.session.query(Stats).delete()
        db.session.commit()

        self.assertTrue(Stats.query.all() == [])
    
    def test_stats_db_proper_modification(self):
        """ Test check if modification stats process conduct properly. """
        stats = Stats(
            userid = 5,
            total = 3,
            wins = 2,
            fails = 1
        )
        
        db.session.add(stats)
        db.session.commit()
        
        stats = Stats.query.filter_by(userid = 5).first()

        self.assertTrue(isinstance(stats, Stats))
        self.assertTrue(stats.id == 1)
        self.assertTrue(stats.userid == 5)
        self.assertTrue(stats.total == 3)
        self.assertTrue(stats.wins == 2)
        self.assertTrue(stats.fails == 1)

        stats.userid = 2
        stats.total = 6
        stats.wins = 3
        stats.fails = 3

        db.session.commit()

        stats = Stats.query.filter_by(userid = 2).first()

        self.assertTrue(isinstance(stats, Stats))
        self.assertTrue(stats.id == 1)
        self.assertTrue(stats.userid == 2)
        self.assertTrue(stats.total == 6)
        self.assertTrue(stats.wins == 3)
        self.assertTrue(stats.fails == 3)

        db.session.delete(stats)
        db.session.commit()
        
if __name__ == '__main__':
    unittest.main()