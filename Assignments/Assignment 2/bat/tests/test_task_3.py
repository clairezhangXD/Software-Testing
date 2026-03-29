import unittest

from src.business_logic import can_use_makerspace


'''
Feasible paths:
1: 135->148->150->151->153->155->157->158->159->161->162->164
2: 135->148->150->151->153->154->161->164
3: 135->148->150->151->153->155->156->161->164
4: 135->148->150->151->153->155->157->158->159->161->164
'''

class TestCanUseMakerspace(unittest.TestCase):

# Test for 1: 135->148->150->151->153->155->157->158->159->161->162->164
    def test_adult_owing_trained(self):
        self.assertFalse(can_use_makerspace(60, 50, True))

# Test for 2: 135->148->150->151->153->154->161->164
    def test_error_not_owing_trained(self):
        self.assertFalse(can_use_makerspace(-5, 0, True))

# Test for 3: 135->148->150->151->153->155->156->161->164
    def test_elderly_not_owing_trained(self):
        self.assertFalse(can_use_makerspace(100, 0, True))

# 4: 135->148->150->151->153->155->157->158->159->161->164
    def test_adult_not_owing_trained(self):
        self.assertTrue(can_use_makerspace(60, 0, True))


