"""
Test Stats Model
"""
import unittest
from app.main import db
from app.main.model.stats_model import Stats
from app.test.base import BaseTestCase

class TestStatsModel(BaseTestCase):

    def test_stats_model_object_creation(self):
        """ Test checks if creation stats object conducted properly. """
        stats = Stats(
            userid = 1,
            total = 3,
            wins = 2,
            fails = 1
        )
        
        self.assertTrue(isinstance(stats, Stats))
        self.assertEqual(stats.userid, 1)
        self.assertEqual(stats.total, 3)
        self.assertEqual(stats.wins, 2)
        self.assertEqual(stats.fails, 1)
    
    def test_stats_model_to_string(self):
        """ Test checks if to string method work properly. """
        stats = Stats(
            userid = 1,
            total = 3,
            wins = 2,
            fails = 1
        )

        string_result = repr(stats)

        self.assertTrue(isinstance(stats, Stats))
        self.assertEqual(stats.userid, 1)
        self.assertEqual(stats.total, 3)
        self.assertEqual(stats.wins, 2)
        self.assertEqual(stats.fails, 1)
        self.assertEqual(string_result, "User: <userid: '1', total: '3', fails: '1', wins: '2'>")
        
        
if __name__ == '__main__':
    unittest.main()