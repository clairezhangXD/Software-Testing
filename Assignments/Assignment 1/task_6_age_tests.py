'''
Unit tests for task 6 of assignment 1.

Reminder, the method you are testing is:
    type_of_patron(age)
Data types and descriptions are provided in the assignment specification.

You can assume that the type_of_patron method is already imported into this python module,
so you can call "type_of_patron" directly.

Author: Claire Zhang
Student ID: 33111332
'''

import unittest


class TestAge(unittest.TestCase):
    def test_minor(self): #equivalence partitioning
        self.assertEqual("Minor", type_of_patron(14))

    def test_minor_boundary(self): #boundary value analysis and equivalence partitioning
        self.assertEqual("Minor", type_of_patron(17))

    def test_outside_minor_boundary(self): #boundary value analysis and equivalence partitioning
        self.assertEqual("Adult", type_of_patron(18))

    def test_adult(self): #equivalence partitioning
        self.assertEqual("Adult", type_of_patron(65))
    
    def test_adult_boundary(self): #boundary value analysis and equivalence partitioning
        self.assertEqual("Adult", type_of_patron(89))

    def test_outside_adult_boundary(self): #boundary value analysis and equivalence partitioning
        self.assertEqual("Elderly", type_of_patron(90))

    def test_elderly(self): #equivalence partitioning
        self.assertEqual("Elderly", type_of_patron(100))

    def test_error_boundary(self): #using logical reasoning, negative ages should give an error
        #boundary value analysis and equivalence partitioning
        self.assertEqual("ERROR", type_of_patron(-1))
    
    def test_error(self): #using logical reasoning, negative ages should give an error
        #equivalence partitioning
        self.assertEqual("ERROR", type_of_patron(-50))

    def test_outside_error_boundary(self): #boundary value analysis and equivalence partitioning
        self.assertEqual("Minor", type_of_patron(0))



