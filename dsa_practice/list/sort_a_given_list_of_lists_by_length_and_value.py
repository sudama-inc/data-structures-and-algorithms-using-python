"""
95. Write a Python program to sort each sublist of strings in a given list of lists.

Original list: [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value: [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]



96. Write a Python program to sort a given list of lists by length and value.

Original list: [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value: [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

https://www.geeksforgeeks.org/python-sort-list-of-lists-by-lexicographic-value-and-then-length/

"""


lst = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

lst.sort()  # sort by sublist contents
lst.sort(key=len)
print(lst)

res = sorted(lst, key=lambda i: (len(i), i))
print(res)