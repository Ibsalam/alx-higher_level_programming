#!/usr/bin/python3
"""A python script that fetches https://alx-intranet-hbtn.io/status
- using urllib package
"""
if __name__ == '__main__':
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    content = response.read().decode('utf-8')

print("\t- type: {}".format(type(content)))
print("\t- content: {}".format(content))

