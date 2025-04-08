import unittest
import users_commands

class TestIndex(unittest.TestCase):

    def setUp(self):
        self.username = "testi"
        self.password = "12345"
        users_commands.register(self.username, self.password)

    def test_login(self):
        result = users_commands.login(self.username, self.password)
        users_commands.remove_user(self.username, self.password)
        self.assertEqual(self.username, result[0])

    def test_get_id(self):
        users = users_commands.get_all_users()
        result = users_commands.get_id(self.username, self.password)
        users_commands.remove_user(self.username, self.password)
        self.assertEqual(len(users), result[0])
