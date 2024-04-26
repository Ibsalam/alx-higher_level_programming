#!/usr/bin/python3
"""A Python script that takes GitHub credentials (username and personal access token) and uses the GitHub API to display your user id.
- Using requests and sys packages.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
