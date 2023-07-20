"""
162. Write a Python program to find the last occurrence of a specified item in a given list.

Original list:
['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']

Last occurrence of f in the said list: 7

https://www.geeksforgeeks.org/python-last-occurrence-of-some-element-in-a-list/
https://stackoverflow.com/questions/6890170/how-to-find-the-last-occurrence-of-an-item-in-a-python-list
"""


lst = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f',
       'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']

res = []

for i in range(len(lst)):
    if 'f' == lst[i]:
        res.append(i)
print(max(res))

# Method 2
res = max((loc for loc, val in enumerate(lst) if val == 'f'), default=None)
