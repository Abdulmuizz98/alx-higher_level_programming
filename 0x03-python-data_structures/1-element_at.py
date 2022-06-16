#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list. """
    if idx >= len(my_list) or idx < 0:
        return None
    return my_list[idx]
