import unittest
from src.rover import execute

class TestExecute(unittest.TestCase):
    def test_forward_no_rotation(self):
        self.assertEqual(execute("M"), "0:1:N")