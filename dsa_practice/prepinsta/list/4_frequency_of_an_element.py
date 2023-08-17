"""
Finding the frequency of element Frequency of elements in an array using Python.

"""


"""
Method 1 : sort the array then, count the frequency of the elements.
Time Complexity : O(nlogn)
Space Complexity : O(1)
"""


def countDistinct(arr, n):
    arr.sort()

    # Traverse the sorted array
    i = 0
    while i < n:
        count = 1
        # Move the index ahead whenever you encounter  duplicates
        while i < n - 1 and arr[i] == arr[i + 1]:
            i += 1
            count += 1

        print("{0}: {1}".format(arr[i], count))
        i += 1


# Driver Code
arr = [5, 8, 5, 7, 8, 10]
n = len(arr)
countDistinct(arr, n)


"""
Method 2 : count use hash-map to count the frequency of each elements.

Declare a dictionary dict().
Start iterating over the entire array
If element is present in map, then increase the value of frequency by 1.
Otherwise, insert that element in map.
After complete iteration over array, start traversing map and print the key-value pair.

Time Complexity : O(n)
Space Complexity : O(n)
"""


def countFreq(arr, n):
    mp = dict()

    # Traverse through array elements and count frequencies
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    # Traverse through map and print frequencies
    for x in mp:
        print(x, " ", mp[x])


# Driver Code
arr = [10, 30, 10, 20, 10, 20, 30, 10]
n = len(arr)
countFreq(arr, n)
