import unittest

from src.statistics import *

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.data = [-1,0,1,1,2]
        self.dataForMinMax = [1,-1,2,0] # for branch coverage, min and max cannot be at  
                                        # at i=0 (otherwise data[i] < min and data[i] > max 
                                        # won't be met)

    def default_test(self):
        self.assertTrue(True)

    def test_sum(self):
        self.assertEqual(3, sum(self.data))

    def test_mean(self):
        self.assertEqual(0.6, mean(self.data))

    def test_minimum1(self):
        self.assertEqual(-1, minimum(self.dataForMinMax))

    def test_maximum(self):
        self.assertEqual(2, maximum(self.dataForMinMax))