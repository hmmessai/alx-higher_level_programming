#!/usr/bin/python3
"""
Sends a request to the URL
and displays the body of the response
"""
import sys
import urllib.request
import urllib.error

if __name__ == '__main__':
        try:
            with urllib.request.urlopen(sys.argv[1]) as res:
                print(res.read().decode('UTF-8'))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
