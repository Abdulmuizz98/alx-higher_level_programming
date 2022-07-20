#!/usr/bin/python3

"""
Module contains the definition of "save_to_json_file" function


"""
from_json_string = __import__('4-from_json_string').from_json_string


def load_from_json_file(filename):
    """
    creates an Object from a json file
    """
    with open(filename, encoding="utf-8") as myFile:
        jsonString = myFile.read()
        return from_json_string(jsonString)
