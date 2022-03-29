import unittest
from library import *


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        print("method setUp")

    def tearDown(self) -> None:
        print("method tearDown")

    def test_document_numbers(self):
        self.assertIsInstance(document_numbers(), list)

    def test_person_id(self):
        self.assertIsInstance(person_id("123"), str)

    def test_shelf_id(self):
        self.assertIsInstance(shelf_id('123'), str)

    def test_full_list(self):
        self.assertIsInstance(full_list(), list)

    def test_new_document(self):
        self.assertIsInstance(new_document('1', 'pass', '123', 'passport'), dict)

    def test_move_document(self):
        self.assertEqual(move_document('123', '1'), None)

    def test_delete_document(self):
        self.assertEqual(delete_document('123'), None)

    def test_new_shelf(self):
        self.assertIsInstance(new_shelf('shelf'), bool)
