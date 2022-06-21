#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string. """
    new_str = [i for i in my_string if i != 'c' and i != 'C']
    return "".join(new_str)
