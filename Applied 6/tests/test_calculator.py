import unittest

from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_initial_answer(self):
        self.assertEqual(0, self.calc.get_answer())

    def test_reset(self):
        self.calc._answer = 1
        self.calc.reset()
        self.assertEqual(0, self.calc._answer)
    
    def test_add(self):
        self.calc.add(1)
        self.assertEqual(1, self.calc._answer)

    def test_subtract(self):
        self.calc._answer = 1
        self.calc.subtract(1)
        self.assertEqual(0, self.calc._answer)

    def test_multiply(self):
        self.calc._answer = 1
        self.calc.multiply(2)
        self.assertEqual(2, self.calc._answer)

    def test_power(self):
        self.calc._answer = 2
        self.calc.power(2)
        self.assertEqual(4, self.calc._answer)
