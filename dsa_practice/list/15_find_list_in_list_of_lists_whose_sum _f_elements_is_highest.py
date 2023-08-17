
"""
66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.

"""


arr = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

max_sum = sum(arr[0])
val = None
for k, v in enumerate(arr):
    if max_sum < sum(v):
        max_sum = sum(v)
        val = k
print(max_sum)
print(arr[val])
