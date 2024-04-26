#!/usr/bin/python3
"""A Python script that lists 10 commits (from the most recent to oldest) of a repository by a specified owner using the GitHub API.
- Using requests and sys packages.
"""
import requests
import sys

if __name__ == '__main__':
    # Get repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Define the URL to fetch commits
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response JSON
        commits = response.json()

        # Print the 10 most recent commits
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)

