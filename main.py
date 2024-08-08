import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

# a = np.array([[1, 2, 3], [4,5,6]], dtype=float)
# print(a)

# a = np.ones((4,2))
# print(a)

# a = np.arange(0, 11, 2)
# print(a.reshape((2, 3)))

# a = np.array([[1,2,3]])
# a = np.repeat(a, 3, axis=0)
# print(a.reshape((1, 9)))

# b = np.full((2, 4), 9)
# print(b)
#
# test = np.ones((5,5), dtype='int8')
# zeros = np.zeros((3,3))
# zeros[1,1] = 9
#
# test[1:4, 1:4] = zeros
#
# b = np.copy(test)
# b[0,0] = -1
# print(b, test)


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,9],[1,2,3]])

c = np.vstack((a,b))
print(c[c < 5])

# p = np.genfromtxt('data.txt')