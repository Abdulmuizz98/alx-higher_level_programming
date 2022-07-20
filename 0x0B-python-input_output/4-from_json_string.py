#!/usr/bin/python3

"""
Module contains the definition of "from_json_string" function


"""
import json


def from_json_string(my_str):
    """
    decodes a json string into an object
    """
    return json.loads(my_str)
