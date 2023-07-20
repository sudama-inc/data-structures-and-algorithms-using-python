"""
***
179. Write a Python program to create the largest possible number
using the elements of a given list of positive integers.

Original list: [3, 40, 41, 43, 74, 9]
Largest possible number using the elements of the said list of positive integers:
9744341403

https://www.geeksforgeeks.org/python-largest-number-possible-from-list-of-given-numbers/


180. Write a Python program to create the smallest possible number
using the elements of a given list of positive integers.

Original list: [3, 40, 41, 43, 74, 9]
Smallest possible number using the elements of the said list of positive integers:
3404143749


"""

from functools import cmp_to_key


# Method 1
def create_largest_number(lst):
    if all(val == 0 for val in lst):
        return '0'
    result = ''.join(sorted((str(val) for val in lst), reverse=True,
                            key=lambda i: i*(len(str(max(lst))) * 2 // len(i))))
    return result


nums = [3, 40, 41, 43, 74, 9]

print(create_largest_number(nums))


# Method 2 : using sorted() + lambda
test_list = [23, 65, 98, 3, 4]

res = sorted(test_list, key=cmp_to_key(lambda i, j: -1
                                       if str(j) + str(i) < str(i) + str(j) else 1))

# printing result
print(''.join(map(str, res)))


# Method 3
test_list = [23, 65, 98, 3, 4]

# custom comparison function


def compare(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    if ab > ba:
        return -1
    elif ab < ba:
        return 1
    else:
        return 0


res = sorted(test_list, key=cmp_to_key(compare))
print(''.join(map(str, res)))


# Smallest possible number
def create_largest_number(lst):
    if all(val == 0 for val in lst):
        return '0'
    result = ''.join(sorted((str(val) for val in lst), reverse=False,
                            key=lambda i: i*(len(str(min(lst))) * 2 // len(i))))
    return result


nums = [3, 40, 41, 43, 74, 9]
print(create_largest_number(nums))
