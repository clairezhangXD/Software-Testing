import unittest

from src.statistics import *

class TestStatistics(unittest.TestCase):
    data = [0, 1, 3, 5, -10, -5]

    def test_something(self):
        self.assertTrue(True)

    def test_mean(self):
        self.assertEqual(-1,mean(self.data))

    def test_minimum(self):
        self.assertEqual(-10,minimum(self.data))
