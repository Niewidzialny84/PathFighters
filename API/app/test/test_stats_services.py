"""
Test Stts Services class
"""
import unittest

from flask_sqlalchemy import get_state
from app.main.service.stats_service import *
from app.test.base import BaseTestCase

class TestStatsServices(BaseTestCase):

    def test_stats_serivces_create_new_stats(self):
        """ [ Test checks if creation stats process conducted properly. ] """

        stats = get_all_stats()
        self.assertEqual(len(stats), 0)

        create_new_stats(1)
        stats = get_all_stats()

        self.assertEqual(len(stats), 1)
        self.assertEqual(stats[0].userid, 1)
        self.assertEqual(stats[0].total, 0)
        self.assertEqual(stats[0].fails, 0)
        self.assertEqual(stats[0].wins, 0)

        delete_all_stats()
    
    def test_stats_serivces_get_all_stats(self):
        """ [ Test checks if get all stats process conducted properly. ] """

        stats = get_all_stats()
        self.assertEqual(len(stats), 0)

        create_new_stats(1)
        create_new_stats(2)
        
        stats = get_all_stats()
        self.assertEqual(len(stats), 2)
        
        delete_all_stats()

    def test_stats_serivces_get_stats_by_id(self):
        """ [ Test checks if get stats by id process conducted properly. ] """

        stats = get_all_stats()
        self.assertEqual(len(stats), 0)

        create_new_stats(1)
        create_new_stats(2)
        
        stats = get_user_stats(1)
        self.assertEqual(stats.userid, 1)
        self.assertEqual(stats.total, 0)
        self.assertEqual(stats.fails, 0)
        self.assertEqual(stats.wins, 0)

        stats = get_user_stats(2)
        self.assertEqual(stats.userid, 2)
        self.assertEqual(stats.total, 0)
        self.assertEqual(stats.fails, 0)
        self.assertEqual(stats.wins, 0)
        
        delete_all_stats()
    
    def test_stats_serivces_put_stats_by_id_200(self):
        """ [ Test checks if put stats by id process conducted properly and return 200 status code. ] """

        create_new_stats(1)

        request_dict = {
            "total" : 3,
            "wins" : 2,
            "fails" : 1
        }

        status_code = stats_put(1, request_dict)
        stats = get_user_stats(1)

        self.assertEqual(status_code, 200)
        self.assertEqual(stats.userid, 1)
        self.assertEqual(stats.total, 3)
        self.assertEqual(stats.wins, 2)
        self.assertEqual(stats.fails, 1)

        delete_all_stats()

    def test_stats_serivces_put_stats_by_id_400(self):
        """ [ Test checks if put stats by id process handle error and return 400 status code. ] """

        create_new_stats(1)

        request_dict = {
            "total" : 3,
            "wins" : 2
        }

        status_code = stats_put(1, request_dict)
        stats = get_user_stats(1)

        self.assertEqual(status_code, 400)
        self.assertEqual(stats.userid, 1)
        self.assertEqual(stats.total, 0)
        self.assertEqual(stats.wins, 0)
        self.assertEqual(stats.fails, 0)

        delete_all_stats()
    
    def test_stats_serivces_put_stats_by_id_404(self):
        """ [ Test checks if put stats by id process handle error and return 404 status code. ] """

        request_dict = {
            "total" : 3,
            "wins" : 2,
            "fails" : 1
        }

        status_code = stats_put(1, request_dict)
        stats = get_user_stats(1)

        self.assertEqual(status_code, 404)
        self.assertEqual(stats, None)

    def test_stats_serivces_delete_all_stats(self):
        """ [ Test checks if delete all stats process conducted properly. ] """

        create_new_stats(1)
        create_new_stats(2)
        create_new_stats(3)

        stats = get_all_stats()
        self.assertEqual(len(stats), 3)

        delete_all_stats()

        stats = get_all_stats()
        self.assertEqual(len(stats), 0)
    
    def test_stats_serivces_delete_stats_by_id_200(self):
        """ [ Test checks if delete stats by id process conducted properly and return 200 status code. ] """

        create_new_stats(1)
        create_new_stats(2)

        stats = get_all_stats()
        self.assertEqual(len(stats), 2)

        status_code = delete_stats(1)
        stats = get_all_stats()

        self.assertEqual(stats[0].userid, 2)
        self.assertEqual(status_code, 200)

        delete_all_stats()

    def test_stats_serivces_delete_stats_by_id_404(self):
        """ [ Test checks if delete stats by id process handle error and return 404 status code. ] """

        status_code = delete_stats(1)
        stats = get_all_stats()

        self.assertEqual(len(stats), 0)
        self.assertEqual(status_code, 404)

        delete_all_stats()

                        
if __name__ == '__main__':
    unittest.main()