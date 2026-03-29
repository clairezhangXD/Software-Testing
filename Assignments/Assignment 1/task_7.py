'''
Unit tests for task 7 of assignment 1.

Reminder, the method you are testing is:
    can_borrow(item_type, patron_age, outstanding_fees, gardening_training, carpentry_training)
Data types and descriptions are provided in the assignment specification.

You can assume that the can_borrow method is already imported into this python module,
so you can call "can_borrow" directly.

Author:Claire Zhang
Student ID: 33111332
'''

import unittest


class TestBorrow(unittest.TestCase):
    '''
    Note the below naming conventions:
    carp = carpentry type of item
    gard = gardening type of item
    nfees = no fees
    fees = has fees
    ngardt = no gardening tool training
    gardt = gardening tool training complete
    ncarpt = no carpentry tool training
    carpt = carpentry tool training complete
    '''

    def test_carp_elderly_long_nfees_ngardt_ncarpt(self): 
        self.assertFalse(can_borrow("carpentry", 90, 14, 0, False, False))
    
    def test_gard_minor_med_fees_gardt_carpt(self): 
        self.assertFalse(can_borrow("gardening", 17, 7, 1.05, True, True))

    def test_carp_adult_short_nfees_gardt_carpt(self): 
        self.assertTrue(can_borrow("carpentry", 19, 2, 0, True, True))

    def test_book_adult_med_fees_ngardt_ncarpt(self): 
        self.assertFalse(can_borrow("book", 19, 7, 1.05, False, False))

    def test_book_minor_short_nfees_gardt_ncarpt(self): 
        self.assertTrue(can_borrow("book", 17, 2, 0, True, False))

    def test_gard_elderly_short_fees_ngardt_carpt(self): 
        self.assertFalse(can_borrow("gardening", 90, 2, 1.05, False, True))

    def test_gard_adult_long_fees_gardt_carpt(self): 
        self.assertFalse(can_borrow("gardening", 19, 14, 1.05, True, True))

    def test_gard_elderly_med_nfees_gardt_ncarpt(self): 
        self.assertTrue(can_borrow("gardening",	90, 7, 0, True, False))

    def test_carp_minor_med_fees_ngardt_ncarpt(self): 
        self.assertFalse(can_borrow("carpentry", 17, 7, 1.05, False, False))

    def test_book_minor_long_nfees_ngardt_carpt(self): 
        self.assertTrue(can_borrow("book", 17, 14, 0, False, True))

    def test_book_elderly_short_fees_gardt_carpt(self): 
        self.assertTrue(can_borrow("book", 90, 2, 1.05,	True, True))



