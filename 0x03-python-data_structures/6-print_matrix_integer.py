#!/usr/bin/python3
def print_matrix_integer(martix=[[]]):
    for i in matrix:
        for j in martix[i]:
            print("{:d}".format(matrix[i][j]), end="")
        print("")
