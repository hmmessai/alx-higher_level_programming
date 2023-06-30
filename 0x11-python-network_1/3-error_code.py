#!/usr/bin/python3
"""
Sends a request to the URL
and displays the body of the response
"""
import sys
import urllib.request
import urllib.error

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as res:
        try:
            res.read()
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
