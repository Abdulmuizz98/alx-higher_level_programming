#!/usr/bin/python3
""" My student class module
"""


class Student:
    """ My Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)

    def to_json(self):
        """retrieves dictionary representation of a student """
        return self.__dict__
