'''
Unit tests for task 6 of assignment 1.

Reminder, the method you are testing is:
    calculate_discount(age)
Data types and descriptions are provided in the assignment specification.

You can assume that the calculate_discount method is already imported into this python module,
so you can call "calculate_discount" directly.

Author:Claire Zhang
Student ID: 33111332
'''

import unittest


class TestDiscount(unittest.TestCase):
    def test_0_discount(self): #equivalence partitioning
        self.assertEqual(0, calculate_discount(25))

    def test_0_discount_boundary(self): #boundary value analysis and equivalence partitioning
        self.assertEqual(0, calculate_discount(50))
    
    def test_outside_0_discount_boundary(self): #boundary value analysis and equivalence partitioning
        self.assertEqual(10, calculate_discount(51))
    
    def test_10_discount(self): #equivalence partitioning
        self.assertEqual(10, calculate_discount(55))

    def test_10_discount_boundary(self): #boundary value analysis and equivalence partitioning
        self.assertEqual(10, calculate_discount(64))
    
    def test_outside_10_discount_boundary(self): #boundary value analysis and equivalence partitioning
        self.assertEqual(15, calculate_discount(65))

    def test_15_discount(self): #equivalence partitioning
        self.assertEqual(15, calculate_discount(70))

    def test_15_discount_boundary(self): #boundary value analysis and equivalence partitioning
        self.assertEqual(15, calculate_discount(89))

    def test_outside_15_discount_boundary(self): #boundary value analysis and equivalence partitioning
        self.assertEqual(100, calculate_discount(90))

    def test_100_discount(self): #equivalence partitioning
        self.assertEqual(100, calculate_discount(110))

    def test_error_boundary(self): #using logical reasoning, negative ages should give an error
        #boundary value analysis and equivalence partitioning
        self.assertEqual("ERROR", calculate_discount(-1))

    def test_error(self): #using logical reasoning, negative ages should give an error
        #equivalence partitioning
        self.assertEqual("ERROR", calculate_discount(-110))

    def test_outside_error_boundary(self): #boundary value analysis and equivalence partitioning
        self.assertEqual(0, calculate_discount(0))

    
    

    