"""
58.
Write a Python program to get all combinations of key-value pairs in a given dictionary.
Original Dictionary: {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

Combinations of key-value pairs of the said dictionary:
[{'V': [1, 4, 6, 10], 'VI': [1, 4, 12]}, {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]}, {'VI': [1, 4, 12], 'VII': [1, 3, 8]}]

"""


from itertools import combinations
d = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

lis = []
for i in range(1, len(d)):
    for x in combinations(d, i):
        dic = {z: d[z] for z in x}
        lis.append(dic)
print(lis)


def test(d):
    result = list(map(dict, combinations(d.items(), 2)))
    return result
