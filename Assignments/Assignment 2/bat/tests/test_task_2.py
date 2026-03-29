import unittest

from src.business_logic import can_borrow_carpentry_tool

'''
A = (fees_owed > 0)
B = (patron_age <= 18)
C = (patron_age >= 90)

Possible tests:
1: A=F, B=F, C=F, Outcome=T
2: A=F, B=F, C=T, Outcome=F
3: A=F, B=T, C=F, Outcome=F
4: A=F, B=T, C=T, Outcome=F
5: A=T, B=F, C=F, Outcome=F
6: A=T, B=F, C=T, Outcome=F
7: A=T, B=T, C=F, Outcome=F
8: A=T, B=T, C=T, Outcome=F

Independence pairs:
A: {1,5}
B: {1,3}
C: {1,2}

Possible optimal sets of tests using MC/DC:
- 1, 2, 3, 5

Set chosen: (1, 2, 3, 5)
'''

class TestCanBorrowCarpentryTool(unittest.TestCase):
    # Test for 1: A=F, B=F, C=F, Outcome=T
    def test_f_f_f(self):
        self.assertTrue(can_borrow_carpentry_tool(55, 2, 0, True))

    # Test for 2: A=F, B=F, C=T, Outcome=F
    def test_f_f_t(self):
        self.assertFalse(can_borrow_carpentry_tool(95, 2, 0, True))

    # Test for 3: A=F, B=T, C=F, Outcome=F
    def test_f_t_f(self):
        self.assertFalse(can_borrow_carpentry_tool(15, 2, 0, True))

    # Test for 5: A=T, B=F, C=F, Outcome=F
    def test_t_f_f(self):
        self.assertFalse(can_borrow_carpentry_tool(55, 2, 100, True))