#!/usr/bin/python3

"""
Module contains the definition of "read_file" function


"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """
    with open(filename) as myFile:
        doc = myFile.read()

    print(doc, end="")
