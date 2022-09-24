#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    letter_payload = argv[1] if len(argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data={'q': letter_payload})
    dic = response.json()

    if dic:
        print(f"[{dic['id']}] {dic['name']}")
    else:
        if type(dic) is not dict:
            print("Not a valide JSON")
        else:
            print("No result")
