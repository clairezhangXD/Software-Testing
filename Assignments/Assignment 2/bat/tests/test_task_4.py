import unittest
from unittest import mock

from src.bat_ui import BatUI

# testing _main_menu, mock read_integer_range

class TestMainMenu(unittest.TestCase):

    # Pass None for data_manager arg since not being
    def setUp(self):
        self.ui = BatUI(None)
    
    @mock.patch('src.user_input.read_integer_range')
    def test_main_menu_loan_item(self, mock_read_integer_range):
        mock_read_integer_range.return_value = 1

        # Run the main menu
        self.ui.run_current_screen()

        # Use the method “get_current_screen” to verify that the UI has moved to the correct screen
        self.assertEqual(self.ui.get_current_screen(), "LOAN ITEM")

    @mock.patch('src.user_input.read_integer_range')
    def test_main_menu_return_item(self, mock_read_integer_range):
        mock_read_integer_range.return_value = 2

        # Run the main menu
        self.ui.run_current_screen()

        # Use the method “get_current_screen” to verify that the UI has moved to the correct screen
        self.assertEqual(self.ui.get_current_screen(), "RETURN ITEM")

    @mock.patch('src.user_input.read_integer_range')
    def test_main_menu_search_for_patron(self, mock_read_integer_range):
        mock_read_integer_range.return_value = 3

        # Run the main menu
        self.ui.run_current_screen()

        # Use the method “get_current_screen” to verify that the UI has moved to the correct screen
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @mock.patch('src.user_input.read_integer_range')
    def test_main_menu_register_patron(self, mock_read_integer_range):
        mock_read_integer_range.return_value = 4

        # Run the main menu
        self.ui.run_current_screen()

        # Use the method “get_current_screen” to verify that the UI has moved to the correct screen
        self.assertEqual(self.ui.get_current_screen(), "REGISTER PATRON")

    @mock.patch('src.user_input.read_integer_range')
    def test_main_menu_access_makerspace(self, mock_read_integer_range):
        mock_read_integer_range.return_value = 5

        # Run the main menu
        self.ui.run_current_screen()

        # Use the method “get_current_screen” to verify that the UI has moved to the correct screen
        self.assertEqual(self.ui.get_current_screen(), "ACCESS MAKERSPACE")

    @mock.patch('src.user_input.read_integer_range')
    def test_main_menu_quit(self, mock_read_integer_range):
        mock_read_integer_range.return_value = 6

        # Run the main menu
        self.ui.run_current_screen()

        # Use the method “get_current_screen” to verify that the UI has moved to the correct screen
        self.assertEqual(self.ui.get_current_screen(), "QUIT")
    
    @mock.patch('src.user_input.read_integer_range')
    def test_main_menu_main_menu(self, mock_read_integer_range):
        mock_read_integer_range.return_value = "chicken"

        # Run the main menu
        self.ui.run_current_screen()

        # Use the method “get_current_screen” to verify that the UI has moved to the correct screen
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch('src.user_input.read_integer_range')
    def test_main_menu_repeatedly_ask_until_valid(self, mock_read_integer_range):
        mock_read_integer_range.side_effect = ["chicken", 10, -1, 1]

        # Run the current screen each time main menu input is changed
        for _ in range(4):
            self.ui.run_current_screen()

        # Use the method “get_current_screen” to verify that the UI has moved to the correct screen
        self.assertEqual(self.ui.get_current_screen(), "LOAN ITEM")
    
    
