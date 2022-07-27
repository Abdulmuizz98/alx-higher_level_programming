#!/usr/bin/python3

"""
Module contains the definition of "class_to_json" function


"""


def class_to_json(obj):
    """
    returns the dictionary description with simple
    data structure for json serialization
    """
    return obj.__dict__
