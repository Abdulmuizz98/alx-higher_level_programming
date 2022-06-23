#!/usr/bin/python3
"""Square module

Contains the definition of a square class.

"""


class Square:
    """Definition of a square object.

    Defines a square object that abstacts a real
    world square

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): the size of the new square.
            position (tuple): the tuple for position
        """
        self.size = size
        self.position = position

    def __str__(self):
        """string representation of the square """
        if self.size == 0:
            return "\n"
        res = ""
        lastIndex = len(range(self.size)) - 1
        for i in range(self.position[1]):
            res += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                res += " "
            for k in range(self.size):
                res += "#"
            if i == range(self.size)[lastIndex]:
                res += ""
            else:
                res += "\n"
        return res

    @property
    def size(self):
        """Getter and setter for the size attribute. """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter and setter for the position attribute. """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of the square. """
        return self.__size ** 2

    def my_print(self):
        """Prints the square rep in " " & # symbols. """
        if self.size == 0:
            print("")
            return

        [print("") for i in range(self.position[1])]
        for i in range(self.size):
            [print(" ", end="") for j in range(self.position[0])]
            [print("#", end="") for k in range(self.size)]
            print("")
