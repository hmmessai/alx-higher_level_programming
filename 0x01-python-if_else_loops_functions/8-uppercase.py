#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if i == len(str):
            if ord(str[i]) <= 122 and ord(str[i]) >= 97:
                c = chr(ord(str[i]) - 32)
                print("{}".format(c), end="")
            else:
                print("{}".format(str[i]), end="")
        else:
            if i == len(str):
            if ord(str[i]) <= 122 and ord(str[i]) >= 97:
                c = chr(ord(str[i]) - 32)
                print("{}".format(c))
            else:
                print("{}".format(str[i]))
