#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element of a list at
       a specific position without modifying
       the original list. """
    new_list = my_list.copy()
    if idx >= len(my_list) or idx < 0:
        return new_list
    new_list[idx] = element
    return new_list
