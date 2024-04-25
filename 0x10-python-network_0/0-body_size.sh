#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the URL and store the response body size
response=$(curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f2 | tr -d '\r\n')

# Display the size of the response body in bytes
echo "Size of the response body: $response bytes"

