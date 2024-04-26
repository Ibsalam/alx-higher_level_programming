#!/usr/bin/python3
"""A Python script that takes GitHub credentials (username and personal access token) and uses the GitHub API to display your user id.
- Using requests and sys packages.
"""
import requests
import sys

if __name__ == '__main__':
    # Get GitHub username and personal access token from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Define the URL to fetch user information
    url = 'https://api.github.com/user'

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=(username, password))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        
        # Display user id
        print("User id:", data['id'])
    else:
        print("Error:", response.status_code)

