"""
Test Stats Model
"""
import unittest
from app.main.model.stats_model import Stats
from app.test.base import BaseTestCase

class TestStatsModel(BaseTestCase):

    def test_stats_model_object_creation(self):
        """ Test checks if creation stats object conducted properly. """
        stats = Stats(
            id = 1,
            userid = 1,
            total = 3,
            wins = 2,
            fails = 1
        )
        
        self.assertTrue(isinstance(stats, Stats))
        self.assertEqual(stats.id, 1)
        self.assertEqual(stats.userid, 1)
        self.assertEqual(stats.total, 3)
        self.assertEqual(stats.wins, 2)
        self.assertEqual(stats.fails, 1)
        
if __name__ == '__main__':
    unittest.main()