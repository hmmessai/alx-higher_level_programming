#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squareMatrix = matrix.copy()
    for i in range(len(matrix)):
        squareMatrix[i] = list(map(lambda x: x **2, matrix[i]))

    return squareMatrix
