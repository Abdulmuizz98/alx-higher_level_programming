#!/usr/bin/python3
"""
    This module defines a function lookup.
"""


def lookup(obj):
    """
       Returns the list of available attributes
       and methods of an object.
    """
    return dir(obj)
