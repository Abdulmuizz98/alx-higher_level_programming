#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Function that executes a function safely """
    try:
        a, b = args
        res = fct(a, b)
        return res
    except BaseException as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
