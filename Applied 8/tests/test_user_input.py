import unittest
from unittest import mock

from src.user_input import *

class TestUserInput(unittest.TestCase):
    @mock.patch('src.user_input.read_string')
    def test_read_string(self, readstr): #readstr is the mock of read_string
        readstr.return_value = 'blah'
        self.assertEqual('blah', readstr('Enter a value: '))

    @mock.patch('src.user_input.read_string')
    def test_read_int(self, readstr):
        readstr.side_effect = ['hihi', 1]
        self.assertEqual(1, read_integer('Enter an integer: '))

    def new_read_string(self):
        return 2
    
    @mock.patch('src.user_input.read_string', side_effect=new_read_string)
    def test_blah(self, readstr):
        self.assertEqual(2, read_integer('Integer please: ')) #side effect means
        # that the readstr mock won't be used (overwritten by new_read_string). 
        # useful when the output of the mock needs to be computed or is complex
        # dynamic value --> use this func to call threads

    #ChatGPT example:
        #Dynamic Behavior Based on Input: You can define a custom function using side_effect
        #to return different results based on the input arguments passed to the mocked function.
        #This makes the mock behave more like the real function it is standing in for.

        # def mock_function_side_effect(arg):
        #     if arg == 'a':
        #         return 1
        #     elif arg == 'b':
        #         return 2
        #     raise ValueError("Invalid argument")

        # mock_function.side_effect = mock_function_side_effect

        #Now, calling mock_function('a') returns 1, and mock_function('b') returns 2.
        #If an invalid argument is passed, it raises a ValueError.


    @mock.patch('src.user_input.read_string')
    def test_read_float(self, readstr):
        readstr.side_effect = ['hihi', 1.05]
        self.assertEqual(1.05, read_float('Enter a float: '))

    @mock.patch('src.user_input.read_string')
    def test_read_integer_range(self, readstr, min, max):
        readstr.side_effect = ['hihi', 5]
        self.assertEqual()