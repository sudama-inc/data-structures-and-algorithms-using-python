"""
155. WAPP to add two given lists of different lengths, starting on the left.
156. WAPP to add two given lists of different lengths, starting on the right.
add two given lists of Same lengths.

Original lists:
[2, 4, 7, 0, 5, 8]
[3, 3, -1, 7]

Add said two lists from left: [5, 7, 6, 7, 5, 8]

194. Write a Python program to sum two or more lists. The lengths of the lists may be different.
Original list: [[1, 2, 4], [2, 4, 4], [1, 2]]
Sum said lists with different lengths: [4, 8, 8]

197. Write a Python program to compute the average of the n-th element in a
given list of lists with different lengths.
Original list:
[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
Average of n-th elements in the said list of lists with different lengths:
[4.8, 5.8, 6.8, 8.0, 11.0]

https://www.geeksforgeeks.org/python-sum-two-unequal-length-lists-in-cyclic-manner/
https://www.geeksforgeeks.org/python-adding-two-list-elements/
"""


from itertools import zip_longest
a = [0, 1, 3, 4]
b = [5, 6]

iter_len = len(a)-(len(b)-1)

for j in range(len(a), 0, -1):
    if j-iter_len < 0:
        break
    else:
        a[j-1] = a[j-1] + b[j-iter_len]
print(a)

# Method 2
list1 = [150, 177, 454, 126]
list2 = [9, 44, 2, 168, 66, 80, 123, 6, 180, 184]
# List comprehension
output = [list1[i % len(list1)]+list2[i] for i in range(len(list2))]

# Printing output
print(output)


# Method 3
list1 = [150, 177, 454, 126]
list2 = [9, 44, 2, 168, 66, 80, 123, 6, 180, 184]
output = []

longer_length = max(len(list1), len(list2))

for i in range(longer_length):
    sum = list1[i % len(list1)] + list2[i % len(list2)]
    output.append(sum)

print(output)


# Method 4
def sum_lists(*lists):
    return [sum(values) for values in zip_longest(*lists, fillvalue=0)]


lst = [[1, 2, 4], [2, 4, 4], [1, 2]]
result = sum_lists(*lst)

print(result)  # Output: [4, 8, 8]
