#!/usr/bin/python3
"""
    This module defines a function inherits_from.
"""


def inherits_from(obj, a_class):
    """
       Checks if the objects is an instance
       of a class that inherited from the
       specified class.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
