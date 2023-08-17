"""
88. Write a Python program to read a square matrix from the console and print the
sum of the matrix's primary diagonal. Accept the size of the square matrix and elements
for each column separated with a space (for every row) as input from the user.

Input the size of the matrix: 3
2 3 4
4 5 6
3 4 7

Sum of matrix primary diagonal: 14

"""

# Initialize matrix
matrix = []

# For user input
for i in range(3):          # A for loop for row entries
    a = []
    for j in range(3):      # A for loop for column entries
        a.append(j)
    matrix.append(a)

print(matrix)


sum_1 = 0
sum_2 = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            sum_1 += matrix[i][j]
        if ((i+j) == (len(matrix)-1)):
            sum_2 += matrix[i][j]

# # Second Logic
# for i in range(len(matrix)):
#     sum_1 += matrix[i][i]
#     sum_2 += matrix[i][len(matrix)-i-1]


print(sum_1, sum_2)
