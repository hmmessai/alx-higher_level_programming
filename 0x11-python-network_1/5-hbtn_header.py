#!/usr/bin/python3
"""
Sends a request to the URL
and displays the value of the variable
'X-Requests-Id' in the response header
"""
import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(dict(r.headers).get('X-Request-Id'))
