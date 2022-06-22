#!/usr/bin/python3
"""Square module

Contains the definition of a square class.

"""


class Square:
    """Definition of a square object.

    Defines a square object that abstacts a real
    world square

    """
    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): the size of the new square.
        """
        self.__size = size
