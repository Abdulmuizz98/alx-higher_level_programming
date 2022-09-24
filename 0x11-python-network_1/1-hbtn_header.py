#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    req = argv[1]
    with urlopen(req) as response:
        header = response.getheader("X-Request-Id")

    print(header)
