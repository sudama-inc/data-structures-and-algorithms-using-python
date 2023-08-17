"""

60. Write a Python program to find the shortest list of values for the keys in a given dictionary.
Original Dictionary: {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}

Shortest list of values with the keys of the said dictionary: ['VI', 'VIII', 'X']

"""

d = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40],
     'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}


min_value = min([len(d[ele]) for ele in d])

print("Min Value : ", min_value)

# min_value=1
res = [k for k, v in d.items() if len(v) == min_value]

print(res)
