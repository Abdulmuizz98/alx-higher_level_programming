#!/usr/bin/python3
"""
    This module defines an extended list called MyList
"""


class MyList(list):
    """List that inherists from list """
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the list sorted"""
        print(sorted(self))
