#!/usr/bin/python3

"""
Module contains the definition of "to_json_string" function


"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of ann object
    """
    return json.dumps(my_obj)
