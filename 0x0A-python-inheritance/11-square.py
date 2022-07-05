#!/usr/bin/python3
"""
    This module defines a class square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A square definition that inherits from
    Rectangle class
    """
    def __init__(self, size):
        """
        Initialize the rectangle
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Initialize the rectangle
        """
        return "[{}] {}/{}".format(self.__class__.__name__, self.__size, self.__size)
