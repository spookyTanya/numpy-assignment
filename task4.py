import numpy as np
from os.path import exists

INITIAL_SIZE = 10
TXT_PATH = "matrix.txt"
csv_path = "matrix.csv"
npy_path = "matrix.npy"


def print_arr(array: np.array, message=None):
    if message:
        print(message)

    print(array)
    print("~~~~~~~~~")


def create_matrix(size: int) -> np.ndarray:
    return np.random.randint(0, 100, (size, size), dtype=int)


def save_matrix(matrix: np.ndarray):
    np.savetxt(TXT_PATH, matrix, fmt='%2d')
    np.savetxt(csv_path, matrix, fmt='%2d')
    np.save(npy_path, matrix)


def load_matrix_from_text_file(filename: str) -> np.ndarray:
    return np.loadtxt(filename, dtype=int)


def load_matrix_from_binary(filename: str) -> np.ndarray:
    return np.load(filename)


def get_sum(data: np.ndarray, axis=None) -> np.ndarray:
    return data.sum(axis, dtype=int)


def get_mean(data: np.ndarray, axis=None) -> np.ndarray:
    return data.mean(axis, dtype=int)


def get_median(data: np.ndarray, axis=None) -> np.ndarray:
    return np.median(data, axis)


def get_std(data: np.ndarray, axis=None) -> np.ndarray:
    return np.std(data, axis)


# 1
matrix = create_matrix(INITIAL_SIZE)
print_arr(matrix, "Initial matrix")

# 2
save_matrix(matrix)
assert exists(TXT_PATH), "File must exist after saving"
assert exists(csv_path), "File must exist after saving"
assert exists(npy_path), "File must exist after saving"


loaded_matrix_npy = load_matrix_from_binary(npy_path)
loaded_matrix_csv = load_matrix_from_text_file(csv_path)
print_arr(loaded_matrix_npy, "Array loaded from npy file")
print_arr(loaded_matrix_csv, "Array loaded from csv file")
assert np.array_equal(loaded_matrix_npy, loaded_matrix_csv), "Arrays should be the same"
assert np.array_equal(loaded_matrix_npy, matrix), "Arrays should be the same"
assert loaded_matrix_npy.shape == (INITIAL_SIZE, INITIAL_SIZE), "Size should remain the same"

# 3 - Sum
total_sum = get_sum(matrix)
sum_columns = get_sum(matrix, 0)
sum_rows = get_sum(matrix, 1)

print("Total sum of matrix = ", total_sum)
print_arr(sum_columns, "Total sum of matrix columns", )
print_arr(sum_rows, "Total sum of matrix rows")

assert np.isscalar(total_sum), "Total sum should be a scalar"
assert sum_columns.shape == (10,), "Must have 10 sums"

all_integers = all([isinstance(x, np.integer) for x in sum_rows])
assert all_integers, "All sums must have int type"


# Mean
total_mean = get_mean(matrix)
mean_columns = get_mean(matrix, 0)
mean_rows = get_mean(matrix, 1)

print("Mean of matrix = ", total_mean)
print_arr(mean_columns, "Mean by matrix columns")
print_arr(mean_rows, "Mean by matrix rows")

assert np.isscalar(total_mean), "Total mean should be a scalar"
assert mean_columns.shape == (10,), "Must have 10 mean values"

all_integers = all([isinstance(x, np.integer) for x in mean_rows])
assert all_integers, "All means must have int type"


# Median
total_median = get_median(matrix)
median_columns = get_median(matrix, 0)
median_rows = get_median(matrix, 1)

print("Median of matrix = ", total_median)
print_arr(median_columns, "Median by matrix columns")
print_arr(mean_rows, "Median by matrix rows")

assert np.isscalar(total_median), "Total median should be a scalar"
assert median_columns.shape == (10,), "Must have 10 mean values"

all_integers = all([isinstance(x, (np.integer, np.float64)) for x in median_rows])
assert all_integers, "All medians must have int or float type"


# Standard Deviation
total_std = get_std(matrix)
std_columns = get_std(matrix, 0)
std_rows = get_std(matrix, 1)

print("STD of matrix = ", total_std)
print_arr(std_columns, "STD by matrix columns")
print_arr(std_rows, "STD by matrix rows")

assert np.isscalar(total_std), "Total STD should be a scalar"
assert std_columns.shape == (10,), "Must have 10 mean values"

all_integers = all([isinstance(x, np.float64) for x in std_rows])
assert all_integers, "All STD must have float type"
