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

    temp = text.replace('.', '.\n\n<sep>').replace(
                    ':', ':\n\n<sep>').replace(
                    '?', '?\n\n<sep>')
    temp = temp.split('<sep>')
    res = ''.join([el.lstrip() for el in temp])
    print(res, end="")
