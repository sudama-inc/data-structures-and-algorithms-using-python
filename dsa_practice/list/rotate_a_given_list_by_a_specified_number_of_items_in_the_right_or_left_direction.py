
"""
109. Write a Python program to rotate a given list by a specified number of items
in the right or left direction.

***181. Write a Python program to iterate a given list cyclically at a specific index position.

original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Rotate the said list in Left direction by 4: [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
Rotate the said list in Right direction by 2: [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]


*** https://www.geeksforgeeks.org/python-ways-to-rotate-a-list/
https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
https://www.geeksforgeeks.org/python-index-specific-cyclic-iteration-in-list/

"""


# initializing list
import numpy as np
lst = [1, 4, 6, 7, 2]

# Method 1
# using list comprehension to left rotate by 2
res = [lst[(i + 2) % len(lst)] for i, x in enumerate(lst)]

# using list comprehension to right rotate by 2
lst = [lst[(i - 2) % len(lst)] for i, x in enumerate(lst)]


# Method 2

nums = [11, 4, 6, 7, 8, 33]
k = 2
x = np.roll(nums, k)


# Method 3
for i in range(2):
    # Remove the last element of the list and insert it at the beginning
    lst.insert(0, lst.pop())


# Method 4
# Python program to right rotate a list by n
def rightRotate(lists, num):
    output_list = []
    # Will add values from n to the new list
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

    # Will add the values before n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])

    return output_list


# Driver Code
rotate_num = 3
list_1 = [1, 2, 3, 4, 5, 6]

print(rightRotate(list_1, rotate_num))


# Method 5 : Using Recursion
def right_rotate(lst, n):
    if n == 0:
        return lst
    else:
        return right_rotate(lst[-1:] + lst[:-1], n-1)


# Driver Code
list_1 = [1, 2, 3, 4, 5, 6]
n = 2
print(right_rotate(list_1, n))

# Method 1
# Iterate a given list cyclically at a specific index position


def cyclically_iteration(lst, spec_index):
    result = []
    length = len(lst)
    for i in range(length):
        element_index = spec_index % length
        result.append(lst[element_index])
        spec_index += 1
    return result


chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
spec_index = 3
print(cyclically_iteration(chars, spec_index))


# Method 2
# Iterate a given list cyclically at a specific index position
test_list = [5, 4, 2, 3, 7]

# starting index
K = 3
res = []

for i in range(len(test_list)):
    res.append(test_list[K % len(test_list)])
    K += 1

print(res)
