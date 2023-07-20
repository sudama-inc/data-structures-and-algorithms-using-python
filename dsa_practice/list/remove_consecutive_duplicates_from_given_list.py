"""
***
73. Write a Python program to remove consecutive (following each other continuously)
duplicates (elements) from a given list.

Original list: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

"""

from itertools import groupby

lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 1, 1, 1]

last_seen = None

# res = [v for i, v in enumerate(lst) if i == 0 or v != lst[i-1]]

res = []
for i in lst:
    if i != last_seen:
        res.append(i)
        last_seen = i
print(res)


print([i[0] for i in groupby(lst)])


# You have a list containing 0 and 1. Remove all consecutive 1 from the list.
# input: 0,0,1,1,1,0,1,0,1,1,0
# output: 0,0,1,0,1,0,1,0

# op = [0,0,1,0]


lst = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
# input: 0,0,1,1,1,0,1,0,1,1,0
# output: 0,0,1,0,1,0,1,0
# res = []
# for i in range(len(lst)-1):
#     if lst[i] == 0:
#         res.append(lst[i])
#     if lst[i] == 1:
#         if lst[i] == lst[i+1]:
#             res.append(lst[i])

# print(res)
res = []

for i in range(len(lst)-1):
    if lst[i] == 0:
        res.append(lst[i])

    else:
        if res[-1] != 1:
            res.append(lst[i])

if lst[-1] == 0:
    res.append(lst[-1])

else:
    if res[-1] != 1:
        res.append(lst[-1])


print(res)


# You have a list containing 0 and 1. Remove all consecutive 1 from the list.
# input: 0,0,1,1,1,0,1,0,1,1,0
# output: 0,0,1,0,1,0,1,0

lst = [1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
op = []
for i in lst:
    if not len(op):
        op.append(i)
    elif i != op[-1]:
        op.append(i)
    elif i == 0:
        op.append(i)

print(op)
