#!/usr/bin/python3
"""
A Python script that takes 2 arguments in order to solve this challenge.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    r = requests.get(url)
    response = r.json()
    for commit in response[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")
