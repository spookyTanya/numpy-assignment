import numpy as np


def print_arr(array: np.array, message=None):
    if message:
        print(message)

    print(array)
    print("~~~~~~~~~")


# 1
one_dim = np.arange(1, 11)
print_arr(one_dim, "Create a one-dimensional NumPy array with values ranging from 1 to 10:")

#
matrix = np.arange(1, 10).reshape((3, 3))
print_arr(matrix, "Create a two-dimensional NumPy array (matrix) with shape (3, 3) containing values from 1 to 9:")


# 2
print_arr(one_dim[2], "Third element of the one-dimensional array")

sliced = matrix[0:2, 0:2]
print_arr(sliced, "First two rows and columns of the two-dimensional array")

print_arr(one_dim + 5, "One-dimensional array + 5")

print_arr(matrix * 2, "Two-dimensional array * 2")
