#!/usr/bin/python3
if __name__ == "__main__":
    """Print the result of the sum of all arguments"""
    import sys
i = 1
sum = 0
while i < len(sys.argv):
    sum += int(sys.argv[i])
    i += 1
print("{}".format(sum))
