#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy = []
    for i in range(len(my_list)):
        cpy.append(my_list[i])
    if idx < 0 or idx >= len(my_list):
        return cpy
    cpy[idx] = element
    return cpy
