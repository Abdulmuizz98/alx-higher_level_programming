#!/usr/bin/python3
def multiple_returns(sentence):
    """Return tuple with the length of a string and its first char"""
    char = ""
    if len(sentence) == 0:
        char = None
    else:
        char = sentence[0:1]
    return len(sentence), char
