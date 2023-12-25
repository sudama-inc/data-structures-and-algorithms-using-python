"""
***
73. Write a Python program to remove consecutive (following each other continuously)
duplicates (elements) from a given list.

Original list: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

"""

from itertools import groupby

lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 1, 1, 1]


def remove_consecutive_duplicates(lst):
	last_seen = None
	res = []
	for x in lst:
		if x != last_seen:
			res.append(x)
		last_seen = x
	return res

print(remove_consecutive_duplicates(lst))


def remove_consecutive_duplicates(lst):
    res = lst[:1]
    for i in lst:
        if res[-1] != i:
            res.append(i)
    print(res)
test_list = [1, 4, 4, 4, 5, 6, 7, 4, 3, 3, 9]
print(remove_consecutive_duplicates(test_list))



# res = [v for i, v in enumerate(lst) if i == 0 or v != lst[i-1]]

print([i[0] for i in groupby(lst)])


# You have a list containing 0 and 1. Remove all consecutive 1 from the list.
# input: 0,0,1,1,1,0,1,0,1,1,0
# output: 0,0,1,0,1,0,1,0

# op = [0,0,1,0]


"""
You have a list containing 0 and 1. Remove all consecutive 1 from the list.
input: 0,0,1,1,1,0,1,0,1,1,0
output: 0,0,1,0,1,0,1,0
"""

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
