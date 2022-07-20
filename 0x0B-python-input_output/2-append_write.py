#!/usr/bin/python3

"""
Module contains the definition of "append_write" function


"""


def append_write(filename="", text=""):
    """
    appends a string to text file (UTF8) and returns number of chars
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
