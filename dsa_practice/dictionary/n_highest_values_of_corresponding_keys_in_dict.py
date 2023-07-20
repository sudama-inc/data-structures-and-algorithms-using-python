
# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

from collections import Counter
from heapq import nlargest


# Method 1
def get_key(val):
    for key, value in d.items():
        if val == value:
            return key

    return "key doesn't exist"


d = {'a': 2, 'b': 5, 'c': 6, 'd': 3}
x = list(d.values())
x.sort(reverse=True)
x = x[:3]

new_dict = {}
for i in x:
    new_dict[get_key(i)] = i

print(new_dict)


# Method 2
my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}
result = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:3])
print(result)


# Method 3
k = Counter(my_dict)
high = k.most_common(3)    # Finding 3 highest values
print("Keys: Values")
for i in high:
    print(i[0], " :", i[1], " ")


# Method 4
ThreeHighest = nlargest(3, my_dict, key=my_dict.get)
print("Keys: Values")
for val in ThreeHighest:
    print(val, ":", my_dict.get(val))
