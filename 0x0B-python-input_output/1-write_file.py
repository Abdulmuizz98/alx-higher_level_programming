#!/usr/bin/python3

"""
Module contains the definition of "write_file" function


"""


def write_file(filename="", text=""):
    """
    writes a string to text file (UTF8) and returns number of chars
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
