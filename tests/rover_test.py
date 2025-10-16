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

    def test_turn_right(self):
        self.assertEqual(execute("R"), "0:0:E")

    def test_turn_right_twice(self):
        self.assertEqual(execute("RR"), "0:0:S")

    def test_turn_right_thrice(self):
        self.assertEqual(execute("RRR"), "0:0:W")

    def test_turn_right_frice(self):
        self.assertEqual(execute("RRRR"), "0:0:N")
    
    def test_move_forward_turn_left(self):
        self.assertEqual(execute("ML"), "0:1:W")

    def test_ove_forward_turn_right(self):
        self.assertEqual(execute("MR"), "0:1:E")
    
    def test_turn_right_move_forward(self):
        self.assertEqual(execute("RM"), "1:0:E")