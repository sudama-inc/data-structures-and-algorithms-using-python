"""
***
74. Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

After packing consecutive duplicates of the said list elements into sublists:
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

"""


from itertools import groupby
data = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

res = []
for i, l in enumerate(data):
    if i == 0 or l != data[i-1]:
        res.append([l])
    else:
        res[-1].append(l)
print(res)


def pack(List):
    result = []
    for key, group in groupby(List):
        result.append(list(group))

    return result


l = [1, 1, 1, 2, 2, 3, 4, 4, 1]
print(pack(l))

# result = [list(group) for key,group in groupby(l)]


# Method 3
def pack_consecutive_duplicates(lst):
    packed_list = []
    current_group = []

    for item in lst:
        if not current_group or current_group[-1] == item:
            current_group.append(item)
        else:
            packed_list.append(current_group)
            current_group = [item]

    if current_group:
        packed_list.append(current_group)

    return packed_list


# Test the function
original_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
result = pack_consecutive_duplicates(original_list)
print(result)
