#!/usr/bin/python3
"""
    This module defines a class BaseGeometry
"""


class BaseGeometry():
    """
    Base Geometry class
    """
    def area(self):
        """
        Defines the area of the geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
