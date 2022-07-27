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

    def to_json(self, attrs=None):
        """retrieves dictionary representation of a student """
        dic = self.__dict__
        if attrs is not None:
            dic = {k: v for (k, v) in self.__dict__.items()
                   if k in attrs and isinstance(k, str)}
        return dic

    def reload_from_json(self, json):
        """
        creates a student from a json file
        """
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
