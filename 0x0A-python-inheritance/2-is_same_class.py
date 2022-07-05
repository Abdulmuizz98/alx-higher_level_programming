#!/usr/bin/python3
"""
    This module defines a function is_same_class.
"""


def is_same_class(obj, a_class):
    """
       Checks if the objects is exactly an instance
       od the specified class.
    """
    return (type(obj) is a_class)
