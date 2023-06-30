#!/usr/bin/python3
"""
Sends a POST requesnt to the passed URL
with the email as parameter
and finally display the body of the response
"""
import requests
import sys

if __name__ == '__main__':
    data = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data)
    print(r.text)
