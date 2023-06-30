#!/usr/bin/python3
"""
Sends a POST request to the passed URL
with email as parameter and displays the body of
response
"""
from urllib.request import Request, urlopen
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as res:
        print(res.read().decode("utf-8"))

