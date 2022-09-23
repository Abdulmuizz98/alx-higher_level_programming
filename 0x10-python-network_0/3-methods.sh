#!/bin/bash
# A Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sI -X OPTIONS "$1" | grep -i ^Allow: | sed -e "s/Allow: //"
