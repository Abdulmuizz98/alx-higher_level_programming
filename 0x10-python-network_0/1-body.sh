#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
[ "$(curl -Ls -o /dev/null  -w "%{http_code}" "$1")" -eq 200 ] && curl -sL "$1"
