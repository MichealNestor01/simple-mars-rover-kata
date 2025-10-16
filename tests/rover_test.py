import unittest
from src.rover import execute

class TestExecute(unittest.TestCase):
    def test_forward_no_rotation(self):
        self.assertEqual(execute("M"), "0:1:N")

    def test_forward_twice_no_rotation(self):
        self.assertEqual(execute("MM"), "0:2:N")

    def test_forward_thrice_no_rotation(self):
        self.assertEqual(execute("MMM"), "0:3:N")