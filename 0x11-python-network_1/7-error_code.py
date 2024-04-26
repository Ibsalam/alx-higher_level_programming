#!/usr/bin/python3
"""A Python script that takes in a URL
- sends a request to the URL, and displays the body of the response
- Using requests and sys packages.
"""
import requests
import sys

if __name__ == '__main__':
    # Get the URL from the command-line arguments
    url = sys.argv[1]
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Display the body of the response
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)

