"""
54. Write a Python program to get the depth of a dictionary.

"""

# Method 1


def dict_depth(d):
    str_dict = str(d)
    counter = 0
    for i in str_dict:
        if i == '{':
            counter += 1
    return counter


dic = {1: 'Geek', 2: {3: {4: {}}}}
print(dict_depth(dic))


# Method 2
def depth(d):
    depth = 0
    q = [(i, depth+1) for i in d.values() if isinstance(i, dict)]
    max_depth = 0
    while (q):
        n, depth = q.pop()
        max_depth = max(max_depth, depth)
        q = q + [(i, depth+1) for i in n.values() if isinstance(i, dict)]

    return max_depth


# Method 3
def dict_depth(d, depth=0):
    if not isinstance(d, dict) or not d:
        return depth
    return max(dict_depth(v, depth+1) for k, v in d.iteritems())


# Method 4
def get_dict_depth(dictionary):
    if not isinstance(dictionary, dict):
        return 0
    max_depth = 1
    for key, value in dictionary.items():
        if isinstance(value, dict):
            depth = 1 + get_dict_depth(value)
            max_depth = max(max_depth, depth)

    return max_depth


my_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}}

depth = get_dict_depth(my_dict)
print(f"The depth of the dictionary is: {depth}")
