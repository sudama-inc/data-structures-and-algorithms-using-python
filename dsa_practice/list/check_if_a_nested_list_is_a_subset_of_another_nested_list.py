"""
92. Write a Python program to check if a nested list is a subset of another nested list.

Original list:
[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
[[1, 3], [13, 15, 17]]

If the one of the said list is a subset of another.: True

https://www.geeksforgeeks.org/python-check-if-a-nested-list-is-a-subset-of-another-nested-list/
"""


import pandas as pd
from collections import Counter


def checkSubset(list1, list2):
    exist = True
    for i in list2:
        if i not in list1:
            exist = False
    return exist


# Driver Code
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[1, 3], [13, 15, 17]]
print(checkSubset(list1, list2))


"""
94. Write a Python program to count the number of unique sublists within a given list.
Original list: [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]

Number of unique lists of the said list: {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11)

https://www.geeksforgeeks.org/python-count-unique-sublists-within-list/
"""

# Importing

# Input list initialization
lst = [[1, 2, 3], [4, 5, 6], [3, 2, 1], [1, 2, 3]]

# Using counter
Output = Counter([tuple(i) for i in lst])

print(Output)

# # Second Approach to Show the Result Creating pandas dataframe
Output = pd.DataFrame(data={'list': list(dict.keys()),
                            'count': list(dict.values())})

# Printing output
print(Output)
