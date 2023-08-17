"""
149. Write a Python program to get all possible combinations of the elements of a given list.

Original list: ['orange', 'red', 'green', 'blue']

All possible combinations of the said list's elements:
[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'],
['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'],
['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'],
['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

https://www.geeksforgeeks.org/python-program-to-find-all-the-combinations-in-the-list-with-the-given-condition/
https://www.geeksforgeeks.org/itertools-combinations-module-python-print-possible-combinations/
https://stackoverflow.com/questions/464864/get-all-possible-2n-combinations-of-a-list-s-elements-of-any-length

"""
from itertools import combinations


# Method 1
def generate_combinations(lst, n):
    return list(combinations(lst, n))


# Test the function
input_list = ['orange', 'red', 'green', 'blue']
n = 2
print(generate_combinations(input_list, n))


# Method 2
def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs


print(combs([1, 2, 3]))


# Approach 1: Straightforward recursion
def subsets(nums):
    result = []

    def powerset(alist, index, curr):
        if index == len(alist):
            result.append(curr)
            return

        powerset(alist, index + 1, curr + [alist[index]])
        powerset(alist, index + 1, curr)

    powerset(nums, 0, [])
    return result


print(subsets([1, 2, 3]))

# Approach 2: Backtracking


def subsets(nums):
    result = []

    def backtrack(index, curr, k):
        if len(curr) == k:
            result.append(list(curr))
            return
        for i in range(index, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, curr, k)
            curr.pop()

    for k in range(len(nums) + 1):
        backtrack(0, [], k)
    return result

# OR


def subsets(nums):
    result = []

    def dfs(nums, index, path, result):
        result.append(path)
        for i in range(index, len(nums)):
            dfs(nums, i + 1, path + [nums[i]], result)

    dfs(nums, 0, [], result)
    return result
