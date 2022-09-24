#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a
request to the URL and displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]

    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
