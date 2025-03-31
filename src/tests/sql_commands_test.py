import unittest
import sql_commands

class TestIndex(unittest.TestCase):

    def setUp(self):
        username = "matias"
        password = "12345"
        sql_commands.create_table()
        sql_commands.register(username, password)

    def test_query(self):
        username = "matias"
        password = "12345"
        result = sql_commands.login(username, password)
        self.assertEqual(username, result[0])