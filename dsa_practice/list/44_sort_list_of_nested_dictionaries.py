
"""
50. Write a Python program to sort a list of nested dictionaries.

"""

# Using sorted() + generator expression + lambda

test_dict = {'Nikhil': {'English': 5, 'Maths': 2, 'Science': 14},
             'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
             'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}}

res = {key: dict(sorted(val.items(), key=lambda ele: ele[1]))
       for key, val in test_dict.items()}

# printing result
print(res)



my_list = [{'key': {'subkey': 1}}, {
    'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print(my_list)