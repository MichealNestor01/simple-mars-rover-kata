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
        self.assertEqual(execute("L"), "0:0:W")

    def test_turn_left_twice(self):
        self.assertEqual(execute("LL"), "0:0:S")

    def test_turn_left_thrice(self):
        self.assertEqual(execute("LLL"), "0:0:E")

    def test_turn_left_frice(self):
        self.assertEqual(execute("LLLL"), "0:0:N")