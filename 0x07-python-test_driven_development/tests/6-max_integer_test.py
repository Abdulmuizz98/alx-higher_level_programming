#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    """
    def test_output(self):
        """Test Output of max integer
        """
        # No list provided
        self.assertIsNone(max_integer())
        # No element list
        self.assertIsNone(max_integer([]))
        # One element list
        self.assertEqual(max_integer([1]), 1)
        # Negative integers
        self.assertEqual(max_integer([-1, -10, -5]), -1)
        # Max at the begining
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        # Max at the middle
        self.assertEqual(max_integer([3, 4, 2, 1]), 4)
        # Max at the end
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
