"""
***
134. Write a Python program to find the difference between two lists including duplicate elements.

Original lists:
[1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
[1, 1, 2, 4, 5, 6]

Difference between two said list including duplicate elements): [3, 3, 4, 7]

https://stackoverflow.com/questions/8106227/difference-between-two-lists-with-duplicates-in-python
https://www.geeksforgeeks.org/python-difference-of-two-lists-including-duplicates/

"""

from collections import defaultdict
a = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
b = [1, 1, 2, 4, 5, 6]


def list_difference25(a, b):
    # count items in a
    count = defaultdict(int)  # item -> number of occurrences
    for x in a:
        count[x] += 1
    print("A: ", count)

    # subtract items that are in b
    for x in b:
        count[x] -= 1
    print("B: ", count)

    diff = []
    for x in a:
        if count[x] > 0:
            count[x] -= 1
            diff.append(x)
    return diff


print(list_difference25(a, b))


# Method 2
# Using map() + lambda + remove()
test_list1 = [1, 3, 4, 5, 1, 3, 3]
test_list2 = [1, 3, 5]
# Using map() + lambda + remove()
res = map(lambda x: test_list1.remove(x)
          if x in test_list1 else None, test_list2)

print(test_list1)
