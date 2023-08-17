
"""
38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]

*** It can be Left / Right Rotation.

https://www.geeksforgeeks.org/python-program-right-rotate-list-n/


can apply slicing 

"""


import numpy as np


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


def right_rotate(lst, n):
    if n == 0:
        return lst
    else:
        return right_rotate(lst[-1:] + lst[:-1], n-1)


list_1 = [1, 2, 3, 4, 5, 6]
n = 2
print(right_rotate(list_1, n))


def right_rotate(lst, n):
    n = n % len(lst)
    lst.extend(lst[:n])
    del lst[:n]
    return lst


lst = [1, 2, 3, 4, 5, 6]
n = 3
print(right_rotate(lst, n))


def right_rotate(lst, n):
    arr = np.array(lst)     	# Convert the list to a numpy array
    # Use np.roll to shift the elements to the right
    arr = np.roll(arr, n)
    arr = arr.tolist()          # Convert the numpy array back to a list
    return arr.tolist()         # Return the rotated list


list_1 = [1, 2, 3, 4, 5, 6]
n1 = 2
print(right_rotate(list_1, n1))
