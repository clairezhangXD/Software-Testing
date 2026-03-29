import unittest
from unittest import mock

from src.bat_ui import BatUI
from src.data_mgmt import DataManager
import src.search as search

class TestBatUI(unittest.TestCase):
    
    def setUp(self):
        dataManager = DataManager()
        self.ui = BatUI(dataManager)

    @mock.patch('src.user_input.read_string')
    def test_loan_item_no_such_item_return_to_main_menu(self, mock_read_str):
        # initialise current screen to "LOAN ITEM"
        self.ui._current_screen = self.ui._loan_item

        # input answers using mocking:
        # item = 10
        mock_read_str.return_value = "10"
        
        #run current screen to check transition
        self.ui.run_current_screen()
        
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")
    
    @mock.patch('src.user_input.read_string')
    def test_loan_item_incorrect_item_return_to_main_menu(self, mock_read_str):
        # initialise current screen to "LOAN ITEM"
        self.ui._current_screen = self.ui._loan_item

        # input answers using mocking:
        # item = 3
        # choice = 'n'
        mock_read_str.side_effect = ["3", "n"]
        
        #run current screen to check transition
        self.ui.run_current_screen()
        
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch('src.user_input.read_string')
    def test_loan_item_no_such_patron_return_to_main_menu(self, mock_read_str):
        # initialise current screen to "LOAN ITEM"
        self.ui._current_screen = self.ui._loan_item

        # input answers using mocking:
        # item = 3
        # choice = 'y'
        # patron name and age = "Claire Zhang", 21
        mock_read_str.side_effect = ["3", "y", "Claire Zhang", "21"]
        
        #run current screen to check transition
        self.ui.run_current_screen()
        
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch('src.user_input.read_string')
    def test_loan_item_success(self, mock_read_str):
        # input answers using mocking:
        # item = 3
        # choice = 'y'
        # patron name and age = "Jane Smith", 23
        # length of loan = 4
        mock_read_str.side_effect = ["3", "y", "Jane Smith", "23", "4"]
        self.ui._loan_item()

        # retrieve patron from data_manager
        patronData = self.ui._data_manager._patron_data
        janeSmith = search.find_patron_by_name_and_age("Jane Smith", 23, patronData)
        self.assertEqual(janeSmith.find_loan(3)._item._id, 3)

    @mock.patch('src.user_input.read_string')
    def test_loan_item_no_success(self, mock_read_str):
        # input answers using mocking:
        # item = 3
        # choice = 'y'
        # patron name and age = "Jane Smith", 23
        # length of loan = 100
        mock_read_str.side_effect = ["3", "y", "Jane Smith", "23", "100"]
        self.ui._loan_item()

        # retrieve patron from data_manager
        patronData = self.ui._data_manager._patron_data
        janeSmith = search.find_patron_by_name_and_age("Jane Smith", 23, patronData)
        self.assertEqual(janeSmith.find_loan(3), None)
    
    @mock.patch('src.user_input.read_string')
    def test_return_item_id_invalid_then_valid(self, mock_read_str):
        # input answers using mocking:
        # name and age of patron = "John Doe", 95
        # item ID = 10, then item ID = 1
        mock_read_str.side_effect = ["John Doe", "95", "10", "1"]
        self.ui._return_item()
        
        # retrieve patron from data_manager
        patronData = self.ui._data_manager._patron_data
        johnDoe = search.find_patron_by_name_and_age("John Doe", 95, patronData)
        self.assertEqual(johnDoe.find_loan(1), None)

    @mock.patch('src.user_input.read_string')
    def test_return_item_no_such_patron_return_to_main_menu(self, mock_read_string):
        # initialise current screen to "RETURN ITEM"
        self.ui._current_screen = self.ui._return_item

        # input answers using mocking:
        # patron name and age = "Claire Zhang", 21
        mock_read_string.side_effect = ["Claire Zhang", "21"]
        
        #run current screen to check transition
        self.ui.run_current_screen()
        
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch('src.user_input.read_string')   
    def test_search_for_patron_by_name_found_continue_search_for_patron(self, mock_read_string):
        # initialise current screen to "SEARCH FOR PATRON"
        self.ui._current_screen = self.ui._search_for_patron

        # input answers using mocking:
        # choice = 1
        # name = "John Doe"
        mock_read_string.side_effect = ["1", "John Doe"]
        
        #run current screen to check transition
        self.ui.run_current_screen()
        
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @mock.patch('src.user_input.read_string')   
    def test_search_for_patron_by_age_not_found_continue_search_for_patron(self, mock_read_string):
        # initialise current screen to "SEARCH FOR PATRON"
        self.ui._current_screen = self.ui._search_for_patron

        # input answers using mocking:
        # choice = 2
        # name = 1000
        mock_read_string.side_effect = ["2", "1000"]
        
        #run current screen to check transition
        self.ui.run_current_screen()
        
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @mock.patch('src.user_input.read_integer_range')
    def test_search_for_patron_back_to_main_menu(self, mock_read_int_range):
        # initialise current screen to "SEARCH FOR PATRON"
        self.ui._current_screen = self.ui._search_for_patron

        # input answers using mocking:
        # choice = 3
        mock_read_int_range.return_value = 3
        
        #run current screen to check transition
        self.ui.run_current_screen()
        
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch('src.user_input.read_integer_range')
    def test_search_for_patron_invalid_choice(self, mock_read_int_range):
        # initialise current screen to "SEARCH FOR PATRON"
        self.ui._current_screen = self.ui._search_for_patron

        # input answers using mocking:
        # choice = random
        mock_read_int_range.return_value = "goose"
        
        #run current screen to check transition
        self.ui.run_current_screen()
        
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @mock.patch('src.user_input.read_string')
    def test_register_patron(self, mock_read_str):
        # input answers using mocking:
        # name and age of patron = "Claire Zhang", 21
        mock_read_str.side_effect = ["Claire Zhang", "21"]
        
        self.ui._register_patron()

        # retrieve new patron from data manager
        patronData = self.ui._data_manager._patron_data
        claireZhang = search.find_patron_by_name_and_age("Claire Zhang", 21, patronData)
        self.assertEqual(claireZhang._name, "Claire Zhang")


    @mock.patch('src.user_input.read_string')
    def test_access_makerspace_patron_allowed_return_to_menu(self, mock_read_str):
        # initialise current screen to "ACCESS MAKERSPACE"
        self.ui._current_screen = self.ui._access_makerspace

        mock_read_str.side_effect = ["Jane Smith", 23]

        #run current screen to check transition
        self.ui.run_current_screen()
        
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch('src.user_input.read_string')
    def test_access_makerspace_patron_not_allowed_return_to_menu(self, mock_read_str):
        # initialise current screen to "ACCESS MAKERSPACE"
        self.ui._current_screen = self.ui._access_makerspace

        mock_read_str.side_effect = ["John Doe", 95]

        #run current screen to check transition
        self.ui.run_current_screen()
        
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch('src.user_input.read_string')
    def test_access_makerspace_no_patron_return_to_menu(self, mock_read_str):
        # initialise current screen to "ACCESS MAKERSPACE"
        self.ui._current_screen = self.ui._access_makerspace

        mock_read_str.side_effect = ["Claire Zhang", 21]

        #run current screen to check transition
        self.ui.run_current_screen()
        
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    def test_quit_returns_quit(self):
        res = self.ui._quit()
        self.assertEqual(res, self.ui._quit)
        
    
