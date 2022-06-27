#!/usr/bin/python3
"""Module that defines  a rectangle class """


class Rectangle:

    """Defines a rectangle object """
    def __init__(self, width=0, height=0):
        """Initializes a rectangle object """
        self.width = width
        self.height = height

    def __str__(self):
        """string representation of the rectangle in # symbols """
        res = ""
        if self.area() == 0:
            return res
        for h in range(self.height):
            res += (self.width * "#") + "\n"
        return res[:-1]

    def __repr__(self):
        """str representation that can officially create the object """
        return "Rectangle({}, {})".format(str(self.width), str(self.height))

    def __del__(self):
        """Deletes the rectangle object """
        print("Bye rectangle...")

    @property
    def width(self):
        """Getter and setter to the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter and setter to the width attribute """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle """
        return self.height * self.width

    def perimeter(self):
        """Perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.height + 2 * self.width
