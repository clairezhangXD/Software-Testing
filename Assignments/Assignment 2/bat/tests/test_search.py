import unittest

import src.search as search
from src.data_mgmt import DataManager

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.dataManager = DataManager()

    def test_find_patron_by_age(self):
        patronData = self.dataManager._patron_data
        patronList = search.find_patron_by_age(10, patronData)
        paulaBrooks = patronList[0]
        self.assertEqual(paulaBrooks._age, 10)
