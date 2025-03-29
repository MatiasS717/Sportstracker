import unittest
from index import testing

class TestIndex(unittest.TestCase):

    def test_startup(self):
        testing()
        title = self.ui_view.winfo_toplevel().title()
        self.ui_view.destroy()
        expected = "Sportstracker"
        self.assertEqual(title, expected)