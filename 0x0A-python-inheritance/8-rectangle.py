#!/usr/bin/python3
"""
    This module defines a class rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A rectangle definition that inherits from
    Base Geometry class
    """
    def __init__(self, width, height):
        """
        Initialize the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
