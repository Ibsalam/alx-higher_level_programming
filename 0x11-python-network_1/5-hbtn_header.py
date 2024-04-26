#!/usr/bin/python3
"""A Python script that takes in a URL
- sends a request to the URL
- displays the value of the variable X-Request-Id in the response header.
- Using requests and sys packages.
"""
import requests
import sys

if __name__ == '__main__':
    # Get the URL from the command-line arguments
    url = sys.argv[1]
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Display the value of the X-Request-Id variable in the response header
    print(response.headers.get('X-Request-Id'))

