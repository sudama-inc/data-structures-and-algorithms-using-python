"""
160. Write a Python program to remove the first specified number of elements
from a given list satisfying a condition.

Remove the first 4 number of even numbers from the following list:
[3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
Output: [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]

https://stackoverflow.com/questions/39580063/remove-the-first-n-items-that-match-a-condition-in-a-python-list
https://www.geeksforgeeks.org/python-ways-to-remove-particular-list-element/
https://www.geeksforgeeks.org/python-remove-first-k-elements-matching-some-condition/
"""


def condition_match(x):
    return ((x % 2) == 0)


def remove_items_con(data, N):
    ctr = 1
    result = []
    for x in data:
        if ctr > N or not condition_match(x):
            result.append(x)
        else:
            ctr = ctr + 1
    return result


nums = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
N = 4
print(remove_items_con(nums, N))


# Method 2
def iter_drop_n(data, condition, drop):
    dropped = 0

    for item in data:
        if dropped >= drop:
            yield item
            continue

        if condition(item):
            dropped += 1
            continue

        yield item


data = [1, 10, 2, 9, 3, 8, 4, 7]
out = list(iter_drop_n(data, lambda x: x < 5, 3))

print(out)
