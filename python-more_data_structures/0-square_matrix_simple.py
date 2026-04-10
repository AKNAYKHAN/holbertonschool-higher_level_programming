#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num * num)
        new_matrix.append(new_row)

    return new_matrix
