#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers of a list. """
    for item in range(len(my_list)):
        print("{:d}".format(my_list[item]))
