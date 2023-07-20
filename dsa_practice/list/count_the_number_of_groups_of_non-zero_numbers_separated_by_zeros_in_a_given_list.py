"""
***
209. Write a Python program to count the number of groups of non-zero numbers
separated by zeros in a given list of numbers.

Original list: [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 
                5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
Number of groups of non-zero numbers separated by zeros of the said list: 4

210. Write a Python program to compute the sum of non-zero groups
(separated by zeros) of a given list of numbers.

Original list: [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 
                7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
Compute the sum of non-zero groups (separated by zeros) of the said list of numbers:
[15, 38, 15, 27]

https://www.geeksforgeeks.org/python-summation-of-non-zero-groups/
"""

# Method 1


def test(lst):
    previous_digit = 0
    ctr = 0
    for digit in lst:
        if previous_digit == 0 and digit != 0:
            ctr += 1
        previous_digit = digit
    return ctr


nums = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0,
        0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
print(test(nums))


# Method 2
# Compute Sum on non-zero group
res = []
val = 0
for ele in nums:
    if ele == 0:
        if val != 0:
            res.append(val)
            val = 0
    else:
        val += ele


# Method 3
# Compute Sum on non-zero group : using a Generator Function
def sum_non_zero_groups(lst):
    val = 0
    for ele in lst:
        if ele == 0:
            if val != 0:
                yield val
                val = 0
        else:
            val += ele
