#!/usr/bin/python3
"""
This module contains the definition of an
addition function.

"""


def add_integer(a, b=98):
    """Adds two integers together """

    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
