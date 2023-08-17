
"""
77. Write a Python program to decode a run-length message.

Original encoded list: [[2, 1], 2, 3, [2, 4], 5, 1]

Decode a run-length encoded said list:
[1, 1, 2, 3, 4, 4, 5, 1]

"""

lst = [[2, 1], 2, 3, [2, 4], 5, 1]
res = []
for i in lst:
    if type(i) == type(lst):
        for x in range(i[0]):
            res.append(i[1])
    else:
        res.append(i)
print(res)


def decode(alist):
    def aux(g):
        if isinstance(g, list):
            return [(g[1], range(g[0]))]
        else:
            return [(g, [0])]
    return [x for g in alist for x, R in aux(g) for i in R]


n_list = [[2, 1], 2, 3, [2, 4], 5, 1]

print(decode(n_list))
