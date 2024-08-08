import numpy as np

# INITIALLY THOUGHT THAT I CAN'T USE NUMPY FUNCTIONS


def create_matrix(size: int) -> np.ndarray:
    return np.random.random((size, size))


def transpose_matrix(matrix: np.ndarray):
    em = []

    for i in range(matrix[0].size):
        em.append(matrix[:, i])

    return np.array(em)  # same as np.transpose(matrix)


def reshape_matrix(matrix: np.ndarray, shape: tuple):
    if len(shape) != 2:
        print('wrong shape format')

    if shape[0] * shape[1] != matrix.size:
        print('cannot reshape into this shape')

    res = []
    flat = matrix.ravel()
    for i in range(0, len(flat), shape[1]):
        res.append(flat[i:i+shape[1]])

    return np.array(res)  # same as matrix.reshape(shape)


def matrix_split(matrix: np.array, splits_num: int, axis=0):
    if matrix.shape[axis] % splits_num != 0:
        print("can't split this way")
        return

    res = []
    split_size = int(matrix.shape[axis] / splits_num)

    for i in range(0, matrix.shape[axis], split_size):
        if axis == 0:
            res.append(matrix[i:i+split_size, :])
        else:
            res.append(matrix[:, i:i + split_size])

    return np.array(res)  # same as np.split


def combine_matrix(arrays):
    combined = []
    for arr in arrays:
        combined.extend(arr)

    return np.array(combined)

# data = create_matrix(6)


data = np.arange(0, 16).reshape(8,2)

# print(data)
# print(transpose_matrix(data))
# print(reshape_matrix(data, (5,2)))

# print(matrix_split(data, 4, 0))
# print(np.split(data, 4, 0))

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
array3 = np.array([[9, 10], [11, 12]])
combine_matrix([array1,array2,array3])