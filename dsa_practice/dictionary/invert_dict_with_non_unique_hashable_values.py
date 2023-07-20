"""
67. Write a Python program to invert a given dictionary with non-unique hashable values.

Sample Output: {8: ['Ora Mckinney', 'Mathew Gilbert'], 7: ['Theodore Hollandl', 'Mae Fleming', 'Ivan Little']}
"""

d = {
    'Ora Mckinney': 8,
    'Theodore Hollandl': 7,
    'Mae Fleming': 7,
    'Mathew Gilbert': 8,
    'Ivan Little': 7,
}

# Method 1
dd = {}
for k, v in d.items():
    if v not in dd.keys():
        dd[v] = [k]
    else:
        dd[v].append(k)
print(dd)


# Method 2
res = {}
for k, v in d.items():
    for i in v:
        if i not in res.keys():
            res[i] = k
        else:
            pass
print(res)
