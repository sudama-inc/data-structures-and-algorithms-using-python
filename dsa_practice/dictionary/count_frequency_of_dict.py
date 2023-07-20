
"""
61. Write a Python program to count the frequency of a dictionary.
Original Dictionary: {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

Count the frequency of the said dictionary:
Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})

"""


d = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20,
     'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

# Method 1
dd = {}
for i in list(d.values()):
    if i in dd:
        dd[i] += 1
    else:
        dd[i] = 1
print(dd)


# Method 2
res = {}
for k, v in d.items():
    if v not in res.keys():
        res[v] = 1
    else:
        res[v] += 1
print(res)
