"""
Finding minimum scalar product of two vectors in Python
"""


arr1 = [1, 2, 6, 3, 7]
arr2 = [10, 7, 45, 3, 7]
n = len(arr1)

# Sort arr1 in ascending order
arr1.sort()

# Sort arr2 in descending order
arr2.sort(reverse=True)

product = 0
for i in range(n):
    product += arr1[i]*arr2[i]

print(product)
