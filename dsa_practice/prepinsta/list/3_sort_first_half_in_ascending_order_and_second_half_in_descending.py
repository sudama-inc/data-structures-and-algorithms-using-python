"""
Python program to Sort first half in ascending order and
second half in descending order in an array

Example --> Input : arr[6] = [1, 90, 34, 89, 7, 9]
Output : 1 7 9 90 89 34

"""


"""
Method 1 : Sort the entire array then, print first half in ascending
and second half in descending.

Sort using inbuilt sort function:
Sort the entire array using inbuilt sort function
Run a loop till first half and print the element.
Run a loop for second half and print the elements.

sort() function
The sort() method is a built-in Python method that, by default, sorts the list
in ascending order. However, you can modify the order from ascending to
descending by specifying the sorting criteria.
"""


def printOrder(arr, n):
    arr.sort()
    res = []

    # printing first half in ascending order
    i = 0
    while i < n / 2:
        res.append(arr[i])
        i = i + 1

    # printing second half in descending order
    j = n - 1
    while j >= n / 2:
        res.append(arr[j])
        j = j - 1

    return res

# Driver code
arr = [5, 4, 6, 2, 1, 3, 8, 9, 7]
n = len(arr)
printOrder(arr, n)


"""
Method 2 : Using alternative way of above method
Sort the first half of the array in ascending order just because only the
elements in the first half of the input array needs to be sorted in ascending
order (In this way the original elements in the first half of the array will
remain in the first half but in ascending order).
Sort the second half of the array in descending order just because only the
elements in the second half of the input array needs to be sorted in descending
order (In this way the original elements in the second half of the array will
remain in the first half but in descending order)

"""


def printOrder(arr, n):
    arr.sort()
    res = []

    # printing first half in ascending order
    for i in range(n / 2):
        res.append(arr[i])

    # printing second half in descending order
    for j in range(n - 1, n // 2 - 1, -1):
        res.append(arr[j])
    return res


# Driver code
arr = [5, 4, 6, 2, 1, 3, 8, -1]
n = len(arr)
printOrder(arr, n)
