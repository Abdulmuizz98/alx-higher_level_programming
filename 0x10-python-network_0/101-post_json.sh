#!/bin/bash
# A Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -X POST -H "Content-Type: application/json" -d @my_json_0 "$1"
