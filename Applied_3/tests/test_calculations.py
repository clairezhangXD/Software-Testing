import unittest

from src.calculations import Calculator 

class TestCalculations(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_basic_add(self):
        expected = 7
        actual = self.calc.add(3,4)
        self.assertEqual(expected, actual, "3+4 not adding to 7")

    def test_add_strings(self):
        expected = "Hello World"
        actual = self.calc.add("Hello ", "world")
        self.assertEqual(expected, actual)
