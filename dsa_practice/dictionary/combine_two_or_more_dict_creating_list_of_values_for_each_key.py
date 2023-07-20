"""

68. Write a Python program to combine two or more dictionaries, creating a list of values for each key.

Original dictionaries:
{'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
{'x': 300, 'y': 'Red', 'z': 600}

Combined dictionaries, creating a list of values for each key:
{'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}

"""

d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
d2 = {'x': 300, 'y': 'Red', 'z': 600}

# Method 1
lst = []
lst.append(d1)
lst.append(d2)
dd = {}
for i in lst:
    for k, v in i.items():
        if k not in dd.keys():
            dd[k] = [v]
        else:
            dd[k].append(v)

print(dd)


# Method 2
res = {}
for i in (d1, d2):
    for k, v in i.items():
        if k not in res.keys():
            res[k] = [v]
        else:
            res[k].append(v)
print(res)


# Method 3
output = {}
# Merge the keys from both dictionaries
keys = set(d1.keys()).union(d2.keys())

# Iterate over the keys and populate the output dictionary
for key in keys:
    output[key] = [d1.get(key), d2.get(key)]

print(output)
