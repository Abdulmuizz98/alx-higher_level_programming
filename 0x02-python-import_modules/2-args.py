#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of and the list of its arguments """
    import sys

    length = len(sys.argv) - 1
    print("{} ".format(length), end="argument"
          if length == 1 else "arguments")
    print("", end=".\n" if length == 0 else ":\n")
    i = 1
    while i <= length:
        print("{}: {}".format(i, sys.argv[i]), end="\n")
        i = i + 1
