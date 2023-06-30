#!/usr/bin/python3
"""Script that displays the 'X-Request-Id' variable in header"""


if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as res:
        print(dict(res.headers).get("X-Request-Id"))
