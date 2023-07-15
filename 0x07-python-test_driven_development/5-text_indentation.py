#!/usr/bin/python3
"""
This module contains the definition of the
function ``text_indentation()``.

"""


def text_indentation(text):
    """ Prints a text with 2 new lines after each
    of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    res = text.replace(': ', ':\n\n').replace(':', ':\n\n')
    res = res.replace('. ', '.\n\n').replace('.', '.\n\n')
    res = res.replace('? ', '?\n\n').replace('?', '?\n\n')
    print(res, end="")
