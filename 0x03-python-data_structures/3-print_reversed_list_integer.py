#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order. """
    if not isinstance(my_list, list):
        return
    item = len(my_list) - 1
    while item >= 0:
        print("{:d}".format(my_list[item]))
        item -= 1
