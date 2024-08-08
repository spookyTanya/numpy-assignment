import numpy as np

DEFAULT_MATRIX_SIZE = 6


def print_arr(array: np.array, message=None):
    if message:
        print(message)

    print(array)
    print("~~~~~~~~~")


def create_matrix(size: int) -> np.ndarray:
    return np.random.randint(0, 100, (size, size), dtype=int)


def transpose_matrix(matrix: np.ndarray) -> np.ndarray:
    return matrix.T


def reshape_matrix(matrix: np.ndarray, shape: tuple):
    return matrix.reshape(shape)


def split_matrix(matrix: np.array, splits_num: int, axis=0):
    return np.split(matrix, splits_num, axis)


def combine_matrix(arrays, axis=0) -> np.ndarray:
    return np.concatenate(arrays, axis=axis)


# Start
data = create_matrix(DEFAULT_MATRIX_SIZE)
print_arr(data, "Initial matrix")
assert data.shape == (DEFAULT_MATRIX_SIZE, DEFAULT_MATRIX_SIZE)

transposed = transpose_matrix(data)
print_arr(transposed, "Transposed matrix")
assert transposed.shape == (DEFAULT_MATRIX_SIZE, DEFAULT_MATRIX_SIZE), "Should remain the same size"
assert transposed[0, 1] == data[1, 0], "Elements must be swapped"

reshaped = reshape_matrix(data, (9, 4))
print_arr(reshaped, "Reshaped matrix")
assert reshaped.shape == (9, 4), "Should have new shape"
assert np.array_equal(reshaped.flatten(), data.flatten()), "Should remain the same values"

split_result = split_matrix(data, 3)
print_arr(split_result, "Split matrix")
assert len(split_result) == 3, "Should have 3 splits"
all_same = all([len(i) == 2 for i in split_result])
assert all_same, "All splits must have two arrays"

split_by_rows_result = split_matrix(data, 2, 1)
print_arr(split_by_rows_result, "Split matrix by rows")
assert len(split_by_rows_result) == 2, "Should have 3 splits"
all_same = all([len(i) == 6 for i in split_by_rows_result])
assert all_same, "All splits must have 6 arrays"

combined = combine_matrix([data, transposed], 1)
print_arr(combined, "Combined by rows array")
assert combined.shape == (DEFAULT_MATRIX_SIZE, DEFAULT_MATRIX_SIZE * 2), "Should be combined by rows"
combined = combine_matrix([data, transposed], 0)
print_arr(combined, "Combined by column array")
assert combined.shape == (DEFAULT_MATRIX_SIZE * 2, DEFAULT_MATRIX_SIZE), "Should be combined by columns"