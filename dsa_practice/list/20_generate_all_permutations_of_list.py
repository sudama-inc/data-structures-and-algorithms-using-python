
"""
***
https://stackoverflow.com/questions/104420/how-do-i-generate-all-permutations-of-a-list

Write a Python program to generate all permutations of a list.

Leet Code : 
Given an list of integers, return all the possible permutations.
can return the ans in any order.
Ex: I/P = [1,2,3]
O/P = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

"""
from itertools import permutations


# Method 1
l = list(permutations(range(1, 4)))
print(l)
