import unittest
import backend.activities_commands
import backend.users_commands
import build

class TestIndex(unittest.TestCase):

    def setUp(self):
        self.id = 1
        self.activity = "Running"
        self.tracker = 2
        self.training_type = "Endurance"
        self.user_id = 1
        self.username = "testi"
        self.password = "12345"
        build.initialize_database()
        backend.users_commands.register(self.username, self.password)
        backend.activities_commands.add_activity(self.activity, self.tracker, self.training_type, self.user_id)

    def test_activities_table(self):
        build.initialize_database()
        result = backend.activities_commands.get_activities(self.user_id)
        self.assertEqual(result, [])

    def test_users_table(self):
        build.initialize_database()
        result = backend.users_commands.login(self.username, self.password)
        self.assertEqual(result, None)