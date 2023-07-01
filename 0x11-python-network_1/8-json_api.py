#!/usr/bin/python3
"""
A Script that takes in a letter
and sends a post request to the url
with the letter param
"""
import sys
import requests

if __name__ == '__main__':
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        response = r.json()
        if response = {}:
            print("No result")
        else:
            print("".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
