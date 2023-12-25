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


def first_second_element(arr):
    first = math.inf
    second = math.inf

    for i in range(0, len(arr)):
        if arr[i] < first:
            first = arr[i]
        if arr[i] != first and arr[i] < second:
            second = arr[i]

    return first, second

arr = [10, 13, 17, 11, 34, 21]
print(first_second_element(arr))


"""
Method 3 :
Sort the array using inbuilt sort() function.
sort(), sort the array in ascending order.
So, to print the second smallest element of the array print arr[1].

"""
arr = [10, 13, 17, 11, 34, 21]
arr.sort()
print(arr[1])
