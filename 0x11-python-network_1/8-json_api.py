#!/usr/bin/python3
"""A Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
- Using requests and sys packages.
"""
import requests
import sys

if __name__ == '__main__':
    # Define the URL
    url = 'http://0.0.0.0:5000/search_user'
    
    # Set the letter parameter
    q = sys.argv[1] if len(sys.argv) > 1 else ''
    
    # Send a POST request with the letter as a parameter
    response = requests.post(url, data={'q': q})
    
    try:
        # Try to parse the response as JSON
        data = response.json()
        
        # Check if the JSON is properly formatted and not empty
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        # Display error message if the JSON is not valid
        print("Not a valid JSON")

