"""
*** 71.
Write a Python program to retrieve the value of the nested key indicated by the given
selector list from a dictionary or list.


https://www.geeksforgeeks.org/python-extract-selective-keys-values-including-nested-keys/
"""

# Method 1
# Extract selective keys' values [ Including Nested Keys ] : Using recursion + loop + yield
def get_vals(test_dict, key_list):
    for i, j in test_dict.items():
        if i in key_list:
            yield (i, j)
        yield from [] if not isinstance(j, dict) else get_vals(j, key_list)


test_dict = {'gfg': {'is': {'best': 3}}, 'for': {'all': 4}, 'geeks': 5}
key_list = ['best', 'geeks']
res = dict(get_vals(test_dict, key_list))

print(res)


# Method 2-uses recursion and a helper function:
def get_vals(test_dict, key_list):
    def _get_vals_helper(sub_dict):
        result = {}
        for key, val in sub_dict.items():
            if key in key_list:
                result[key] = val
            elif isinstance(val, dict):
                nested_result = _get_vals_helper(val)
                if nested_result:
                    result[key] = nested_result
        return result

    return _get_vals_helper(test_dict)


# Method 3-Using recursion and a list comprehension.
def get_vals(test_dict, key_list):
    return [(k, v) for k, v in test_dict.items() if k in key_list] + \
           [item for sub_dict in test_dict.values() if isinstance(sub_dict, dict)
            for item in get_vals(sub_dict, key_list)]
