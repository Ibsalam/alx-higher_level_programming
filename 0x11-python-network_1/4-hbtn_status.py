#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status
- Using requests package.
"""
import requests

if __name__ == '__main__':
    # URL to fetch
    url = 'https://alx-intranet.hbtn.io/status'
    
    # Send GET request to the URL
    response = requests.get(url)
    
    # Print the body of the response with specified format
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

