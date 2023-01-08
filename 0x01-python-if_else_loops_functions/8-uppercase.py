#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str) - 1):
        if ord(str[i]) <= 122 and ord(str[i]) >= 97:
            print("{}".format(char(ord(str[i] + 32))))
        else:
            print("{}".format(str[i]), end="")
