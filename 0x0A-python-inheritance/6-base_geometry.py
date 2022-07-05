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
