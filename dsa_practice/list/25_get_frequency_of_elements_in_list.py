
"""
30. Write a Python program to get the frequency of elements in a list.

"""


lst = [1, 3, 6, 2, 3, 4, 1, 2, 3, 4]

freq = {}

for i in lst[:5]:
    try:
        freq[i] += 1
    except KeyError:
        freq[i] = 1
print(freq)


res = {}
for i in lst:
    if i not in res.keys():
        res[i] = 1
    else:
        res[i] += 1
print(res)