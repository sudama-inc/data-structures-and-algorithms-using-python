"""
281. Write a Python program that takes a list of integers and finds
all pairs of integers that differ by three. Return all pairs of integers in a list.

Sample Data:
([0, 3, 4, 7, 9]) -> [[0, 3], [4, 7]]
[0, -3, -5, -7, -8] -> [[-3, 0], [-8, -5]]

https://stackoverflow.com/questions/61062583/return-all-pairs-of-integers-from-a-given-list-of-integers-that-have-a-differenc
https://www.geeksforgeeks.org/python-program-to-find-all-possible-pairs-with-given-sum/
"""

# Method 1


def test(nums):
    result = []
    for i, x in enumerate(sorted(nums)):
        for y in nums[i+1:]:
            if y == x + 3:
                result.append([x, y])
    return result


nums = [0, 3, 4, 7, 9]
print(test(nums))


# Method 2
initial_list = [1, 2, 3, 4]
s = set(initial_list)

res = [(n, n+2) for n in initial_list if n + 2 in s]
print(res)


# Method 3
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def findIntsWithDif(data, dif):
    res = []
    for val1 in data:
        for val2 in data:
            if abs(val2 - val1) == dif and (val2, val1) not in res:
                res.append((val1, val2))
    return res


print(findIntsWithDif(arr, 2))


# Method 1
# all pairs in a list of integers with given sum
def findPairs(lst, K):
    res = []
    while lst:
        num = lst.pop()
        diff = K - num
        if diff in lst:
            res.append((diff, num))

    res.reverse()
    return res


# Driver code
lst = [1, 5, 3, 7, 9]
K = 12
print(findPairs(lst, K))


# Method 2
def find_pairs(lst, K):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == K:
                result.append((lst[i], lst[j]))
    return result


lst = [1, 5, 3, 7, 9]
K = 12
print(find_pairs(lst, K))
