"""
Find Second Smallest Element in an Array using Python.

"""

"""
Method 1 :
Take a variable say first and set it to integer maximum value.
Run a loop for range (0, len(arr))
Check if first > arr[i], set first = arr[i]
Now, declare a variable say second and set it to integer maximum value.
Run a loop for range (0, len(arr))
Check if ( arr[i] != first and arr[i]<second), set second = arr[i]
Print(second)

"""
import math
arr = [10, 13, 17, 11, 34, 21]
first = math.inf
second = math.inf

for i in range(0, len(arr)):
    if arr[i] < first:
        first = arr[i]

for i in range(0, len(arr)):
    if arr[i] != first and arr[i] < second:
        second = arr[i]

print(second)


"""
Method 2 :
Take two variable say first and second, set them to integer maximum value.
Run a loop for range (0, len(arr))
Check if first > arr[i], set second = first and first = arr[i]
Else Check if ( arr[i] != first and arr[i]<second), set second = arr[i]
Print(second)
"""
arr = [10, 13, 17, 11, 34, 21]
first = second = math.inf
for i in range(0, len(arr)):
    if arr[i] < first:
        second = first
        first = arr[i]

    elif (arr[i] < second and arr[i] != first):
        second = arr[i]

print(second)


"""
Method 3 :
Sort the array using inbuilt sort() function.
sort(), sort the array in ascending order.
So, to print the second smallest element of the array print arr[1].

"""
arr = [10, 13, 17, 11, 34, 21]
arr.sort()
print(arr[1])
