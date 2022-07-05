#!/usr/bin/python3
"""
    This module defines a function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
       Checks if the objects is exactly an instance
       of the specified class.
    """
    return isinstance(obj, a_class)
