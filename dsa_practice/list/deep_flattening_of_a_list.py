"""
***
255. Write a Python program to perform a deep flattening of a list.

Sample Output:
Original list elements: [1, [2], [[3], [4], 5], 6]
Deep flatten the said list: [1, 2, 3, 4, 5, 6]


https://www.geeksforgeeks.org/python-program-to-flatten-a-list-without-using-recursion/
"""

from collections.abc import Iterable

# Method 1


def deep_flatten(lst):
    return ([a for i in lst for a in
            deep_flatten(i)] if isinstance(lst, Iterable) else [lst])


nums = [1, [2], [[3], [4], 5], 6]
print(deep_flatten(nums))


# Method 2 : using Recursion
def flatten(lst):
    result = []
    for x in lst:
        if isinstance(x, list):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result


l = [1, 2, [3, 4, [5, 6], 7], [[[8, 9], 10]], [11, [12, 13]]]
print(flatten(l))
