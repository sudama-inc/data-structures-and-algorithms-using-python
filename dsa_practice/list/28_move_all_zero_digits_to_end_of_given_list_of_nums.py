
"""
***
65. Write a Python program to move all zero digits to the end of a given list of numbers.

Original list:
[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
Move all zero digits to end of the said list of numbers:
[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

https://www.geeksforgeeks.org/move-zeroes-end-array/

"""


def pushZerosToEnd(arr, n):
    count = 0  # Count of non-zero elements

    # Traverse the array. If element encountered is non-zero, then
    # replace the element at index 'count' with this element
    for i in range(n):
        if arr[i] != 0:

            # here count is incremented
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to front and 'count' is set
    # as index of first 0. Make all elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1

    return arr


# Driver code
arr = [1, 9, 0, 0, 2, 0, 0, 7, 0, 6, 0, 9]
n = len(arr)
print(pushZerosToEnd(arr, n))


# Method 2
A = [1, 9, 0, 0, 2, 0, 0, 7, 0, 6, 0, 9]
n = len(A)
j = 0
for i in range(n):
    if A[i] != 0:
        A[j], A[i] = A[i], A[j]  # Partitioning the array
        j += 1
print(A)  # Print the array


# Method 3
arr = [5, 6, 0, 4, 6, 0, 9, 0, 8]
# Storing all non zero values
nonZeroValues = [x for x in arr if x != 0]
# Storing all zeroes
zeroes = [j for j in arr if j == 0]
# Updating the answer
nonZeroValues.extend(zeroes)

# Printing the answer
print(nonZeroValues)
