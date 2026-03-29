import unittest

import src.business_logic as business_logic
from src.data_mgmt import DataManager
import src.search as search

class TestBusinessLogic(unittest.TestCase):

    def setUp(self):
        self.dataManager = DataManager()

    def test_type_of_patron_minor(self):
        self.assertEqual("Minor", business_logic.type_of_patron(17))

    def test_can_borrow_with_book(self):
        self.assertTrue(business_logic.can_borrow("Book", 50, 4, 0, False, False))

    def test_can_borrow_book_exceed_len_loan(self):
        self.assertFalse(business_logic.can_borrow_book(50, 60, 0))

    def test_can_borrow_book_with_fees(self):
        self.assertFalse(business_logic.can_borrow_book(50, 4, 100))

    def test_can_borrow_with_gardening(self):
        self.assertTrue(business_logic.can_borrow("Gardening tool", 50, 4, 0, True, False))

    def test_can_borrow_gardening_tool_with_fees(self):
        self.assertFalse(business_logic.can_borrow_gardening_tool(50, 4, 100, True))

    def test_can_borrow_gardening_tool_exceed_loan(self):
        self.assertFalse(business_logic.can_borrow_gardening_tool(50, 30, 0, True))

    def test_can_borrow_with_carpentry_exceed_loan(self):
        self.assertFalse(business_logic.can_borrow("Carpentry tool", 50, 20, 0, True, True))

    def test_can_borrow_with_invalid_item(self):
        self.assertFalse(business_logic.can_borrow("cactus", 50, 4, 0, True, True))

    def test_calculate_discount_error(self):
        self.assertEqual("ERROR", business_logic.calculate_discount(-5))

    def test_calculate_discount_15(self):
        self.assertEqual(15, business_logic.calculate_discount(70))

    def test_process_return_item_1(self):
        # retrieve patron
        patronData = self.dataManager._patron_data
        johnDoe = search.find_patron_by_name_and_age("John Doe", 95, patronData)
        # process return
        business_logic.process_return(johnDoe, 1)
        self.assertEqual(johnDoe.find_loan(1), None)

    def test_process_loan_item_1_valid(self):
        # retrieve patron
        patronData = self.dataManager._patron_data
        janeSmith = search.find_patron_by_name_and_age("Jane Smith", 23, patronData)
        # retrieve borrowable item
        itemData = self.dataManager._catalogue_data
        item1 = search.find_item_by_id(1, itemData)
        # process loan
        business_logic.process_loan(janeSmith, item1, 4)
        self.assertEqual(janeSmith.find_loan(1)._item, item1)

    def test_process_loan_item_1_invalid(self):
        # retrieve patron
        patronData = self.dataManager._patron_data
        aliceJohnson = search.find_patron_by_name_and_age("Alice Johnson", 8, patronData)
        # retrieve borrowable item
        itemData = self.dataManager._catalogue_data
        item1 = search.find_item_by_id(1, itemData)
        # attempt to process loan
        business_logic.process_loan(aliceJohnson, item1, 4)
        self.assertEqual(aliceJohnson.find_loan(1), None)