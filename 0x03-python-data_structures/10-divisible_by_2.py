#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    truth_table = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            truth_table.append(True)
        else:
            truth_table.append(False)
    return truth_table
