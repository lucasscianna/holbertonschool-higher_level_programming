#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for i in row:
            count += 1

        idx = 0
        while idx < count:
            if idx != count - 1:
                print("{:d}".format(row[idx]), end=" ")
            else:
                print("{:d}".format(row[idx]))
            idx += 1
