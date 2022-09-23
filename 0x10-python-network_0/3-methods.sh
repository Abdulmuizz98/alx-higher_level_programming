#!/bin/bash
# A Bash script that that takes in a URL and displays all HTTP methods the server will accept.
curl -sI -X OPTIONS "$1" | grep -i ^Allow: | sed -e "s/Allow: //"
