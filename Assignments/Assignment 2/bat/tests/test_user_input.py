import unittest
from unittest import mock

import src.user_input as user_input

class TestUserInput(unittest.TestCase):
    
    def test_is_int_with_int(self):
        self.assertTrue(user_input.is_int('1'))

    def test_is_int_with_str(self):
        self.assertFalse(user_input.is_int('chicken'))

    def test_is_float_with_float(self):
        self.assertTrue(user_input.is_float('1.23'))
    
    def test_is_float_with_str(self):
        self.assertFalse(user_input.is_float('potato'))
    
    @mock.patch('src.user_input.read_string')
    def test_read_integer_with_int(self, readstr):
        readstr.return_value = '1'
        self.assertEqual(user_input.read_integer(''), 1)

    @mock.patch('src.user_input.read_string')
    def test_read_integer_with_str_first(self, readstr):
        readstr.side_effect = ['pickle','1']
        self.assertEqual(1, user_input.read_integer(''))

    @mock.patch('src.user_input.read_string')
    def test_read_float_with_float(self, readstr):
        readstr.return_value = '1.23'
        self.assertEqual(user_input.read_float(''), 1.23)
    
    @mock.patch('src.user_input.read_string')
    def test_read_float_with_str_first(self, readstr):
        readstr.side_effect = ['pickle','1.23']
        self.assertEqual(1.23, user_input.read_float(''))
    
    @mock.patch('src.user_input.read_string')
    def test_read_integer_range_in_range(self, readstr):
        readstr.return_value = '1'
        self.assertEqual(1, user_input.read_integer_range('', 0, 10))

    @mock.patch('src.user_input.read_string')
    def test_read_integer_range_out_of_range_first(self, readstr):
        readstr.side_effect = ['11', '1']
        self.assertEqual(1, user_input.read_integer_range('', 0, 10))

    @mock.patch('src.user_input.read_string')
    def test_read_float_range_in_range(self, readstr):
        readstr.return_value = '1.23'
        self.assertEqual(1.23, user_input.read_float_range('', 0, 10))

    @mock.patch('src.user_input.read_string')
    def test_read_float_range_out_of_range_first(self, readstr):
        readstr.side_effect = ['11', '1.23']
        self.assertEqual(1.23, user_input.read_float_range('', 0, 10))

    @mock.patch('src.user_input.read_string')
    def test_read_bool_with_not_bool_first(self, readstr):
        readstr.side_effect = ['stallion', 'n']
        self.assertEqual('n', user_input.read_bool(''))