#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    width = len(my_list) -1
    for i in range(width + 1):
        num = my_list[width - i] 
        print("{:d}".format(num))
