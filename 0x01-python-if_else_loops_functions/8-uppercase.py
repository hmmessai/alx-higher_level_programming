#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(str[i]) <= 122 and ord(str[i]) >= 97:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
