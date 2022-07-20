#!/usr/bin/python3

"""
Module contains the definition of "save_to_json_file" function


"""
to_json_string = __import__('3-to_json_string').to_json_string


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        jsonString = to_json_string(my_obj)
        myFile.write(jsonString)
