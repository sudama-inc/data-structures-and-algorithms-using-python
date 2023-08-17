
"""
87. Write a Python program to read a matrix from the console and print the sum for each column.
As input from the user, accept matrix rows, columns, and elements separated by a space (each row).


"""


import numpy as np
# a = np.arange(4).reshape(2, 2)
# b = a.sum(axis=0)
# c = np.sum(a, axis=0)

# print(b)
# print(c)


# Initialize matrix
matrix = []

# For user input
for i in range(2):          # A for loop for row entries
    a = []
    for j in range(2):      # A for loop for column entries
        a.append(int(input('Enter Inpute: ')))
    matrix.append(a)

matrix_arr = np.array(matrix)   # Convert a List into nD array

result = np.sum(matrix_arr, axis=0)
print(result)

print(type(result))
