import unittest
from yandex import create_folder

fixture = [201, 400, 401, 403, 404, 406, 409, 423, 503, 507]
class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        print("method setUp")

    def tearDown(self) -> None:
        print("method tearDown")

    def test_create_folder(self):
        with open(r'C:\Users\vital\Desktop\token.txt', encoding='utf-8') as file:
            token = file.readline()
            self.assertIn(create_folder('test_folder', token), fixture)
