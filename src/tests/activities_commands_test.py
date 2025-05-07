import unittest
import backend.activities_commands

class TestIndex(unittest.TestCase):

    def setUp(self):
        self.id = 1
        self.activity = "Running"
        self.tracker = 2
        self.training_type = "Endurance"
        self.user_id = 1
        backend.activities_commands.add_activity(self.activity, self.tracker, self.training_type, self.user_id)
    
    def test_edit_activity(self):
        tracker = 7
        backend.activities_commands.edit_activity(self.activity, tracker, self.training_type, self.user_id)
        result = backend.activities_commands.get_activities(self.user_id)
        self.assertEqual(result[0], (self.id, self.activity, tracker, self.training_type, self.user_id))

    def test_get_activities(self):
        result = backend.activities_commands.get_activities(self.user_id)
        self.assertEqual((self.id, self.activity, 7, self.training_type, self.user_id), result[0])

    def test_delete_activity(self):
        backend.activities_commands.delete_activity(self.activity, self.tracker, self.training_type, self.user_id)
        result = backend.activities_commands.get_activities(self.user_id)
        self.assertEqual(result, [])
