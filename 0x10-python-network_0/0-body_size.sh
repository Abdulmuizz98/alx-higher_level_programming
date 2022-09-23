#!/bin/bash
# A Bash script that takes in a URL, sends a requestto that URL, and displays the size of the body of the response
curl -sI "$1" | grep Content-Length | grep -Eo '[0-9]{1,}'
