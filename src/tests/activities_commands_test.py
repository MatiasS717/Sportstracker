import unittest
import activities_commands

class TestIndex(unittest.TestCase):

    def setUp(self):
        self.id = 1
        self.activity = "Running"
        self.tracker = 2
        self.training_type = "Endurance"
        self.user_id = 1
        activities_commands.add_activity(self.activity, self.tracker, self.training_type, self.user_id)

    def test_get_activities(self):
        result = activities_commands.get_activities(self.user_id)
        self.assertEqual((self.id, self.activity, self.tracker, self.training_type, self.user_id), result[0])