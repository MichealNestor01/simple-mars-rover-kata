import unittest
from src.rover import execute

class TestExecute(unittest.TestCase):
    def test_forward_no_turn(self):
        self.assertEqual(execute("M"), "0:1:N")

    def test_forward_twice_no_turn(self):
        self.assertEqual(execute("MM"), "0:2:N")

    def test_forward_thrice_no_turn(self):
        self.assertEqual(execute("MMM"), "0:3:N")
    
    def test_turn_left(self):
        self.assertEqual(execute("M"), "0:0:W")