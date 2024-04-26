#!/usr/bin/python3
"""A Python script that takes in a URL and an email address
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response.
- Using requests and sys packages.
"""
import requests
import sys

if __name__ == '__main__':
    # Get the URL and email from the command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Send a POST request to the URL with the email as a parameter
    response = requests.post(url, data={'email': email})
    
    # Display the body of the response
    print(response.text)

