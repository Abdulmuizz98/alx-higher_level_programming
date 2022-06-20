#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer """
    try:
        value /= 1;
        print("{:d}".format(value))
    except ValueError:
        return False
    else:
        return True
