
"""

26. Write a Python program to check whether two lists are circularly identical.

https://www.geeksforgeeks.org/python-check-whether-two-lists-circularly-identical/

"""


import numpy as np


def circularly_identical(list1, list2):

    list3 = list1 * 2			# doubling list

    for x in range(0, len(list1)):  # traversal in twice of list1
        z = 0

        for y in range(x, x + len(list1)):  # check if list2 == list1 circularly
            if list2[z] == list3[y]:
                z += 1
            else:
                break

        if z == len(list1):		# if all n elements are same circularly
            return True

    return False


def circularly_identical(list1, list2):

    list1.extend(list1)			# doubling list

    for i in range(len(list1)):		# traversal in twice of list1
        print("print : ", list1[i: i + len(list2)])

        # check if sliced list1 is equal to list2
        if list2 == list1[i: i + len(list2)]:
            return True
    return False


def is_dup(a, b):
    for i in range(len(a)):
        if a == list(np.roll(b, i)):  # shift b circularly by i
            return True
    return False


# driver code
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]


# check for list 1 and list 2
if(circularly_identical(list1, list2)):
    print("Yes")
else:
    print("No")

# check for list 2 and list 3
if(circularly_identical(list2, list3)):
    print("Yes")
else:
    print("No")
