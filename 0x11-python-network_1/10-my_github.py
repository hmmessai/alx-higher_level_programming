#!/usr/bin/python3
"""
Takes Github credentials (username and password)
and displays the id 
"""
import sys
import requests

if __name__ == "__main__":
    payload = {'Authorization': "{}".format(sys.argv[2])}
    r = requests.get('https://api.github.com/users/{}'.format(sys.argv[1]), headers=payload)
    json = r.json()

    print(json['id'])
