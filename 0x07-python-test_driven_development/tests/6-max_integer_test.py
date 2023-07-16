#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    """
    def test_list(self):
        """
        """
        list_1 = [1, 2, 3, 4]
        list_2 = [10, 20, 30, 40]

        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer(list_1), 4)
        self.assertEqual(max_integer(list_2), 40)
    
    def test_no_params(self):
        """
        """
        self.assertIsNone(max_integer())
        
