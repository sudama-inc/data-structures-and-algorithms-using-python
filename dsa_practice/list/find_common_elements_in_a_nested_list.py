"""
122. Write a Python program to find common elements in a nested list.

Original lists: [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]

Common element(s) in nested lists: [18, 12]

https://www.geeksforgeeks.org/python-find-common-elements-in-list-of-lists/

https://stackoverflow.com/questions/10066642/how-to-find-common-elements-in-list-of-lists
"""


from functools import reduce
test_list = [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]

# Method 1
common_elements = []

for element in test_list[0]:
    if all(element in sublist for sublist in test_list[1:]):
        common_elements.append(element)

print(common_elements)

# Method 2
res = set.intersection(*[set(list) for list in test_list])

# Method 3
res = set.intersection(*map(set, test_list))

# Method 4
ip = iter(test_list)
s = set(next(ip))
res = s.intersection(*ip)

# Method 5
res = reduce(lambda x, y: x & y, (set(i) for i in test_list))
