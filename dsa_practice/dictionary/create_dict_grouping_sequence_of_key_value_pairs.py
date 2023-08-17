"""
46.

Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

"""

lst = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

res = {}
for item in lst:
  if item[0] not in res:
    res[item[0]] = [item[1]]
  else:
    res[item[0]].append(item[1])
    
print(res)
